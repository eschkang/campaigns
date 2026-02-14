#!/usr/bin/env python3
"""Fix and canonicalize ManhattanRepublic/State/commodities.json

This script:
- reads the file, replaces non-printable control characters (except \t,\n,\r)
- extracts top-level JSON objects by brace matching
- attempts to json.load each object; if parsing fails, it attempts to fix
  missing commas between object members and retries
- selects the best parsed object (largest) and writes it back
"""
import json
import sys
from pathlib import Path


P = Path(__file__).resolve().parents[1] / "ManhattanRepublic" / "State" / "commodities.json"


def sanitize_text(text: str) -> str:
    return ''.join(ch if (ord(ch) >= 32 or ch in '\t\n\r') else ' ' for ch in text)


def extract_top_level_objects(text: str):
    objs = []
    in_str = False
    esc = False
    depth = 0
    start_idx = None
    for i, ch in enumerate(text):
        if ch == '\\' and not esc:
            esc = True
            continue
        if ch == '"' and not esc:
            in_str = not in_str
        if not in_str:
            if ch == '{':
                if depth == 0:
                    start_idx = i
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0 and start_idx is not None:
                    objs.append(text[start_idx:i+1])
                    start_idx = None
        if esc:
            esc = False
    return objs


def extract_section_by_key(text: str, key: str):
    idx = text.find('"' + key + '"')
    if idx == -1:
        return None
    # find first '{' after the key
    brace_idx = text.find('{', idx)
    if brace_idx == -1:
        return None
    in_str = False
    esc = False
    depth = 0
    start = brace_idx
    for i, ch in enumerate(text[brace_idx:], brace_idx):
        if ch == '\\' and not esc:
            esc = True
            continue
        if ch == '"' and not esc:
            in_str = not in_str
        if not in_str:
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    return text[start:i+1]
        if esc:
            esc = False
    return None


def fix_missing_commas(obj_text: str) -> str:
    # Insert commas between a closing '}' of a nested object and the next key " when
    # both are at the same object depth (i.e., depth==1). Works by scanning and
    # inserting a comma when appropriate.
    out = []
    in_str = False
    esc = False
    depth = 0
    prev_non_ws = None
    for ch in obj_text:
        if ch == '\\' and not esc:
            esc = True
            out.append(ch)
            continue
        if ch == '"' and not esc:
            in_str = not in_str
        if not in_str:
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
        # if we are about to add a '"' that starts a key at depth==1 and the
        # previous significant char was '}', insert a comma
        if ch == '"' and not in_str and depth == 1 and prev_non_ws == '}':
            # ensure last appended significant char isn't already a comma
            # find last non-whitespace in out
            j = len(out)-1
            while j >= 0 and out[j].isspace():
                j -= 1
            if j >= 0 and out[j] != ',':
                out.append(',')
        out.append(ch)
        if not ch.isspace():
            prev_non_ws = ch
        if esc:
            esc = False
    return ''.join(out)


def try_parse_variants(objs):
    parsed = []
    for o in objs:
        try:
            parsed.append(json.loads(o))
            continue
        except Exception:
            # try fixing missing commas inside this object and parse again
            fixed = fix_missing_commas(o)
            try:
                parsed.append(json.loads(fixed))
                continue
            except Exception:
                # skip this object
                continue
    return parsed


def main():
    if not P.exists():
        print('ERROR: file not found:', P)
        sys.exit(2)
    text = P.read_text(encoding='utf-8', errors='replace')
    text = sanitize_text(text)
    objs = extract_top_level_objects(text)
    parsed = try_parse_variants(objs) if objs else []

    # Also try to extract well-known sections directly (in case full objects
    # were corrupted but sections remain). We prefer explicit sections when found.
    keys_to_try = [
        'raw_materials', 'processed_goods', 'commodity_cost_template',
        'commodity_master_ledger', 'fuel_heat_table', 'saline_products',
        'ferrous_products', 'resource_dependencies'
    ]
    for k in keys_to_try:
        sec = extract_section_by_key(text, k)
        if sec:
            try:
                parsed.append(json.loads(sec))
            except Exception:
                fixed = fix_missing_commas(sec)
                try:
                    parsed.append(json.loads(fixed))
                except Exception:
                    pass

    if not parsed:
        print('ERROR: no valid JSON object could be parsed after attempted repairs')
        sys.exit(4)
    # Merge parsed objects into a single canonical document.
    merged = {}
    def merge_dict(a, b):
        for k, v in b.items():
            if k in a and isinstance(a[k], dict) and isinstance(v, dict):
                merge_dict(a[k], v)
            else:
                a[k] = v

    for obj in parsed:
        if not isinstance(obj, dict):
            continue
        # If obj looks like a commodity map (keys are commodity ids and values
        # are dicts with 'commodity'), normalize by wrapping as 'raw_materials'
        top_keys = set(obj.keys())
        expected_sections = {'raw_materials','processed_goods','commodity_cost_template','commodity_master_ledger','fuel_heat_table','saline_products','ferrous_products','resource_dependencies'}
        has_expected = bool(top_keys & expected_sections)
        if not has_expected:
            # heuristic: if many entries contain 'commodity' field, treat as raw_materials
            cnt = sum(1 for v in obj.values() if isinstance(v, dict) and 'commodity' in v)
            if cnt >= max(1, len(obj)//2):
                obj = { 'raw_materials': obj }
        merge_dict(merged, obj)

    if not merged:
        print('ERROR: merge resulted in empty document')
        sys.exit(6)

    # Ensure top-level has expected containers; if raw_materials/processed_goods were
    # provided as the top-level themselves (e.g., file previously had just raw_materials),
    # normalize by wrapping if necessary.
    # If merged already contains commodity entries (keys look like commodity ids),
    # detect and wrap into 'raw_materials' if needed.
    sample_keys = list(merged.keys())[:10]
    # crude heuristic: if first keys look like commodity ids (no '_' or spaces),
    # and 'raw_materials' not present, wrap merged as full raw_materials map
    if 'raw_materials' not in merged and 'processed_goods' not in merged:
        # check if many values are dicts containing 'commodity' field
        cnt = 0
        for v in merged.values():
            if isinstance(v, dict) and 'commodity' in v:
                cnt += 1
        if cnt >= max(1, len(merged)//2):
            merged = { 'raw_materials': merged }

    # Move any commodity-like top-level entries under raw_materials if present
    expected_sections = {'raw_materials','processed_goods','commodity_cost_template','commodity_master_ledger','fuel_heat_table','saline_products','ferrous_products','resource_dependencies'}
    for k in list(merged.keys()):
        if k in expected_sections:
            continue
        v = merged[k]
        if isinstance(v, dict) and 'commodity' in v:
            merged.setdefault('raw_materials', {})[k] = v
            del merged[k]

    # write canonicalized JSON
    P.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
    # validate
    try:
        json.loads(P.read_text(encoding='utf-8'))
    except Exception as e:
        print('ERROR: validation failed after write:', e)
        sys.exit(5)
    print('OK: commodities.json fixed and validated')


if __name__ == '__main__':
    main()
