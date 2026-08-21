# Intent Record Reference Model — Discussion Draft 0.1

This document is a synthesis for comparison and experimentation. It is **not a standard** and does not replace IntentSpec, Intent-System, OpenSpec, or any project-specific schema.

## Design goals

A record should let a future human or agent answer:

- What must become true?
- Why was this chosen?
- Which evidence supports the choice?
- What is explicitly outside scope?
- Which constraints and trade-offs apply?
- Who may approve, execute, deploy, spend, or delete?
- What evidence proves completion?
- What changed, and which prior paths were rejected?

## Minimal fields

| Field | Purpose |
| --- | --- |
| `id` | stable trace key |
| `status` | draft, approved, active, superseded, rejected, verified |
| `objective` | concise intended outcome |
| `rationale` | why the outcome matters |
| `evidence` | observations anchored to claims |
| `outcomes` | observable success conditions |
| `constraints` | boundaries that must hold |
| `non_goals` | explicit exclusions |
| `tradeoffs` | preferences under named conditions |
| `authority` | allowed actions and approval gates |
| `verification` | required checks and production signals |
| `provenance` | authorship, approval, and derivation |
| `evolution` | supersession, findings, rejected paths |

See [`examples/intent-record.yml`](../examples/intent-record.yml).

## Lifecycle

```text
draft → approved → active → verified
   │         │         │
   ├─────────┴─────────┴──► superseded
   └──────────────────────► rejected
```

A finding may move a verified record back to active or create a successor record.

## Trace model

```text
evidence ──supports──► outcome / constraint
intent   ──implemented-by──► code / configuration
intent   ──verified-by──► test / review / runtime signal
finding  ──challenges──► assumption / outcome / evidence
intent   ──supersedes──► prior intent
rejection──blocks-until──► reconsideration condition
```

## Open questions

- How should two intent records merge when both change the same requirement?
- How should an organization-level constraint override a local preference?
- Which fields require a human signature or approval event?
- How should confidence and evidence decay affect agent authority?
- What is the correct denominator for intent coverage?
- How should private product evidence be referenced without exposing it to every agent?
