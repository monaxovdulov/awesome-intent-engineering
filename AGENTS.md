# AGENTS.md

## Mission

Maintain an evidence-first map of Intent Engineering. Prefer primary sources, inspectable mechanisms, and explicit limitations.

## Non-negotiable rules

1. Do not convert a roadmap item into a shipped capability.
2. Do not call model-derived text “human intent” without approval provenance.
3. Do not claim first coinage without searching for earlier dated uses.
4. Do not add generic agent frameworks that only accept a natural-language goal.
5. Every catalog entry must have a primary source, limitation, and `last_verified` date.
6. Keep product descriptions neutral. Vendor metrics and security claims remain attributed to the vendor.
7. Preserve prediction text after creation. Update only status, resolution evidence, and explicit calibration notes.

## Taxonomy

Lifecycle tags:

- `capture`
- `represent`
- `propagate`
- `enforce`
- `verify`
- `evolve`
- `provenance`
- `governance`

Categories:

- `core`
- `provenance`
- `adjacent`
- `research`
- `learning`
- `experimental`

## Workflow

1. Read the canonical source.
2. Record the precise mechanism and current availability.
3. Identify human-authored, model-derived, inferred, and observed artifacts.
4. Add or update `data/resources.yml`.
5. Update the relevant Markdown view only when the catalog change affects it.
6. Run:

```bash
python scripts/validate_catalog.py
```

7. Keep one logical resource addition or correction per pull request when practical.

## Writing style

- Prefer concrete verbs: captures, stores, maps, validates, checks, infers, exports.
- State who authored an artifact and where it is stored.
- State shipped, demonstrated, planned, or inferred status.
- End descriptions with a material limitation when readers could overgeneralize.
- Avoid promotional adjectives and unsupported category claims.
