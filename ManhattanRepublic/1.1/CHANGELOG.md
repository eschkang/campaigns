# Nova Roma Core Changelog

Numbering is global and monotonic across all releases.

## v1.1.0
1. [CANON] Added canonical 50-domain technology registry, governance rules, prerequisites, and seeded baseline tiers for 500‑person Nova Roma.
2. [PLAYABILITY] Added domain metadata (category/tags/era), full prerequisite graph, era gating rules, and MSR tech-delta snapshot policy.
3. [BUGFIX] Corrected canon starting_population and premise to ~500-person isolated settlement; removed stale 2000-person defaults.

## v1.1.2 (2026-01-29)
5. [REFACTOR] Centralized starting_population in manifest.json. Removed all hardcoded population values from state, template, playability, and documentation files. All systems and users must now reference manifest.json for the authoritative starting population.

## v1.1.1
4. [BUGFIX] Restored NR_SPEC.json hard-spec and reattached proof-of-load/self-check protocol hooks after v1.1.1 regen dropped the file.
