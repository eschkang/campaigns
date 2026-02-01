# NRCore Bundle (Templates + Runtime State)

## Read this first
Open `manifest.json` first. It declares which files are authoritative.

## Premise
Nova Roma begins as an established settlement (~2000 people) with new leadership aiming to look outward and make the world better through trade, diplomacy, and infrastructure.

## Authoritative files
- `state.json` (authoritative starting state in this bundle)
- `event_log.jsonl` (authoritative event log; empty on first boot)

## Templates (non-authoritative)
These are copy-only starters. They are deliberately named to avoid confusion:
- `state.template.json`
- `event_log.template.jsonl`

Workflow:
1) Copy templates into your runtime folder if you want a fresh run:
   - state.template.json -> state/state.json
   - event_log.template.jsonl -> state/event_log.jsonl
2) Edit only the copied runtime files, never the templates.

## Canon Impact (CI) convention
CI middle segment must use human-readable labels, not internal JSON paths.

Example:
CI: v2.7 | RStart Conditions: colony→settlement; RStarting Population: unspecified→2000; RNarrative Framing: neutral→outward-focused | MAJOR

## Bundle naming
Going forward, bundles follow: NRCore_v<major>_<minor>_<patch>.zip

## Technology registry
Tech registry: 50 canonical domains with tags, era gating, and full prerequisites are defined in novaroma_canon.json.

## Hard-spec
NR_SPEC.json contains non-skippable invariants plus proof-of-load and self-check protocol.
