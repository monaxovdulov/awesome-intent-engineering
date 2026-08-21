# Taxonomy

This taxonomy classifies resources by the concrete surface they expose. It does not require a project to use the phrase “Intent Engineering.”

## Lifecycle tags

### `capture`

Obtains intent from a person, team, evidence source, or decision process.

Examples: agent prompts, product interviews, customer evidence, explicit decisions, non-goals.

### `represent`

Stores intent as an inspectable artifact or data structure.

Examples: Markdown record, YAML schema, intent tree, atomic requirements, scenario graph.

### `propagate`

Moves the relevant subset of intent into a task, model context, agent, reviewer, or repository.

Examples: inheritance, issue contracts, context injection, links, selectors.

### `enforce`

Constrains execution mechanically.

Examples: permissions, policies, tests, linters, architecture checks, budgets, approval gates.

### `verify`

Collects evidence that outcomes occurred and constraints held.

Examples: scenario coverage, runtime checks, production metrics, review verdicts.

### `evolve`

Updates intent after learning while preserving history.

Examples: intent diffs, findings, status transitions, supersession, rejected paths.

### `provenance`

Records who or what produced a decision, requirement, explanation, change, or observation.

### `governance`

Defines ownership, authority, escalation, conflict resolution, and organizational inheritance.

## Catalog categories

| Category | Inclusion rule |
| --- | --- |
| `core` | Intent is a first-class artifact or mechanism. |
| `provenance` | The resource preserves rationale or decision history that helps reconstruct or audit intent. |
| `adjacent` | The resource transports, enforces, or verifies intent through specifications, harnesses, or workflows. |
| `research` | The resource introduces a substantive concept, method, benchmark, or empirical result. |
| `learning` | The resource teaches a coherent, inspectable practice. |
| `experimental` | The resource proposes a high-risk or early implementation such as executable natural-language intent. |

## Representation patterns

| Pattern | Strength | Constraint |
| --- | --- | --- |
| **Single document** | easy to inspect, diff, and adopt | becomes coarse and stale at larger scale |
| **Per-feature record** | clear scope and definition of done | cross-feature constraints need separate linkage |
| **Tree** | supports inheritance from organization/product/system to task | conflicts and shared descendants require explicit rules |
| **Graph** | represents many-to-many dependencies and provenance | harder to edit and review without strong tooling |
| **Atomic requirement store** | enables intent diff, selective context, and code links | extraction and merge semantics become central risks |
| **Scenario/test map** | creates mechanical traceability and coverage | may miss rationale and product evidence |
| **Event log** | preserves evolution, supersession, and rejected paths | needs compaction and a current-state projection |

## Authorship labels

Cataloged systems should distinguish:

- `human-authored`
- `human-approved`
- `model-derived`
- `agent-observed`
- `system-inferred`
- `runtime-evidence`

A project does not need these exact field names. It needs enough provenance that a reviewer can tell a decision from an inference.

## Maturity labels

| Label | Meaning |
| --- | --- |
| `operational` | released and usable for its stated scope |
| `emerging` | implemented or publicly demonstrated, with important limitations |
| `planned` | publicly described roadmap item, not treated as shipped |
| `research` | paper or prototype evaluated in a research setting |
| `discussion-draft` | proposed vocabulary or schema without adoption claims |
