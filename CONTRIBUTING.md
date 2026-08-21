# Contributing

Contributions are welcome when they improve the evidence, taxonomy, or coverage of the field.

## Before submitting a resource

Confirm that the resource exposes at least one concrete intent mechanism:

- durable goals, rationale, constraints, trade-offs, or non-goals;
- an intent document, tree, graph, requirement store, scenario map, or event log;
- traceability from intent to code, tests, decisions, or runtime evidence;
- intent coverage, drift, fidelity, or assurance measurement;
- ownership, approval, authority, or escalation tied to intent;
- a substantive paper, benchmark, or teaching resource.

A generic agent framework, prompt collection, or marketing page without an inspectable mechanism will not be accepted.

## Resource pull request

1. Add one entry to `data/resources.yml`.
2. Use a primary canonical URL.
3. Include lifecycle tags, availability, maturity, a neutral description, a limitation, evidence links, and `last_verified`.
4. Update `README.md` or `docs/landscape.md` only when the resource belongs in a featured section.
5. Run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
```

## Description format

Use:

> **Project** — concrete mechanism, representation, and trace or verification behavior. Material limitation or current status.

Avoid:

- “revolutionary,” “best,” “leading,” or similar promotional claims;
- unqualified vendor metrics;
- presenting planned features as released;
- calling generated requirements human-authored;
- duplicate links to thin wrappers around the same project.

## New term proposal

A new term should have:

- a dated source;
- a concrete control surface;
- at least one implementation, method, or research definition;
- an explanation of overlap with existing terms;
- evidence of independent use when claiming broader traction.

One social post or joke can be tracked in an issue. It should not enter the glossary as an emerging field term until another substantive signal appears.

## Prediction updates

Existing prediction claims, deadlines, and confidence values are immutable. Submit one of:

- new resolution evidence;
- status change with supporting sources;
- calibration note explaining what the evidence means;
- a new prediction with a new ID and creation date.

## Conduct

Be direct about evidence and uncertainty. Critique mechanisms and claims, not contributors or project authors.
