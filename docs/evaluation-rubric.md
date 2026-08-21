# Resource Evaluation Rubric

The catalog evaluates inspectable mechanisms. It does not rank companies, models, or marketing claims.

## Eligibility gate

A resource enters the catalog only when all three conditions hold:

1. **Concrete surface** — it exposes an artifact, data structure, protocol, trace, check, workflow, or research definition related to intent.
2. **Primary evidence** — an official repository, specification, paper, or product document supports the description.
3. **Status clarity** — shipped, demonstrated, planned, inferred, and unavailable capabilities are separated.

A generic agent that accepts a natural-language goal does not pass this gate by itself.

## Mechanism coverage

Score each dimension from 0 to 3. The score describes visible mechanism coverage, not product quality.

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| **Provenance** | authorship absent | source mentioned | human/model/system classes distinguished | approval and derivation are traceable events |
| **Structure** | free-form prompt only | durable prose | stable sections or identifiers | typed/validated graph, tree, schema, or event model |
| **Propagation** | manual copy | full artifact handed over | relevant subset selected | inheritance, conflict, and freshness rules are explicit |
| **Enforcement** | advisory only | agent instruction | mechanical checks or permissions | multiple independent gates with failure behavior |
| **Verification** | self-reported completion | checklist or review | linked tests/observations | evidence credibility, independence, and residual uncertainty recorded |
| **Evolution** | overwrite only | version control history | diff or supersession semantics | merge, rejection, retraction, and findings write-back supported |
| **Authority** | implicit | role named | allowed and approval-required actions separated | authority changes with risk or assurance state |
| **Inspectability** | claim only | demo or prose | public format/repository or usable product | reproducible examples, validation, and documented limitations |

Maximum score: **24**.

Suggested use:

- **0–7** — terminology signal or weakly related mechanism;
- **8–13** — adjacent infrastructure;
- **14–18** — substantive intent-engineering system;
- **19–24** — broad lifecycle coverage worth detailed case study.

These ranges guide editorial discussion. They are not automatic acceptance or endorsement thresholds.

## Maturity is separate

Mechanism coverage and maturity answer different questions.

| Maturity | Meaning |
| --- | --- |
| `discussion-draft` | proposal, format, or early implementation with limited operating evidence |
| `emerging` | usable or publicly demonstrated, with significant lifecycle gaps or roadmap dependence |
| `operational` | released workflow used as an ongoing system, with inspectable artifacts and maintenance activity |
| `research` | paper, benchmark, conceptual model, or prototype evaluated in a research setting |
| `planned` | announced mechanism that is not yet available |

A narrow operational tool may score lower than a broad research architecture. Both can belong in the catalog when their status and limitations are explicit.

## Review questions

Before featuring a project, answer:

- Who authored the source intent?
- Which artifact is canonical?
- What survives after the original chat or issue closes?
- How does a task receive only the relevant intent?
- Which constraints are mechanically enforced?
- Can the same agent change both the requirement and the test that claims to verify it?
- How are conflicts, removals, and supersession represented?
- What evidence returns after execution?
- Which actions require human or organizational approval?
- Which listed capabilities are currently available?

## Catalog policy

The machine-readable catalog records category, lifecycle operations, availability, maturity, evidence, limitation, and verification date. Detailed rubric scores may be added later after maintainers can apply them consistently across the full catalog.
