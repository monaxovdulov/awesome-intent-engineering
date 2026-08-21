# Awesome Intent Engineering [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

An evidence-first map of tools, formats, research, and operating practices for preserving human goals, rationale, constraints, authority, and success criteria across AI-agent workflows.

[![Status](https://img.shields.io/badge/status-emerging%20field-f59e0b)](#status) [![Resources](https://img.shields.io/badge/resources-21-2563eb)](data/resources.yml) [![Terms](https://img.shields.io/badge/terms-11-7c3aed)](data/terms.yml) [![Predictions](https://img.shields.io/badge/predictions-6-0891b2)](data/predictions.yml)

AI agents can shorten implementation cycles. Intent engineering keeps the intended outcome, decision history, boundaries, and proof available across that execution.

> [!IMPORTANT]
> **Intent Engineering is an emerging label, not a settled standard.** This repository tracks independently developed mechanisms. Every factual catalog entry points to a primary source, records current availability, and states a material limitation.

## Contents

- [Start here](#start-here)
- [Working definition](#working-definition)
- [Field model](#field-model)
- [Featured landscape](#featured-landscape)
- [Strongest current findings](#strongest-current-findings)
- [Relationship to neighboring disciplines](#relationship-to-neighboring-disciplines)
- [Experimental reference artifacts](#experimental-reference-artifacts)
- [Prediction ledger](#prediction-ledger)
- [Repository map](#repository-map)
- [Status](#status)

## Start here

| If you want to… | Start with… |
| --- | --- |
| Understand the field in five minutes | the [working definition](#working-definition) and [field model](docs/field-model.md) |
| Compare tools, formats, and research | the [featured landscape](#featured-landscape) or full [`resources.yml`](data/resources.yml) catalog |
| Try a durable intent artifact | the [example intent record](examples/intent-record.yml), [JSON Schema](schemas/intent-record.v0.1.schema.json), and [reference model](docs/reference-model.md) |
| Evaluate a new project or claim | the [evidence policy](docs/evidence-policy.md) and [evaluation rubric](docs/evaluation-rubric.md) |
| Contribute a resource, term, or correction | the [contribution guide](CONTRIBUTING.md) and [issue forms](https://github.com/monaxovdulov/awesome-intent-engineering/issues/new/choose) |

**Current snapshot:** 21 resources, 11 engineering terms, and 6 dated predictions. Catalog entries were last reviewed on **2026-08-21**; see the [changelog](CHANGELOG.md) for release history.

## Working definition

**Intent engineering** is the practice of designing and maintaining artifacts and mechanisms that carry human goals, constraints, trade-offs, rationale, authority, and success criteria from evidence and decisions into agent execution and verification.

A useful system keeps intent answerable across six operations:

```text
EVIDENCE / DECISIONS
        │
        ▼
     CAPTURE ──► REPRESENT ──► PROPAGATE ──► ENFORCE ──► VERIFY
        ▲                                                       │
        └────────────── EVOLVE / FINDINGS / CHANGES ────────────┘

Cross-cutting: provenance · ownership · authority · traceability
```

| Operation | Question | Typical artifact or mechanism |
| --- | --- | --- |
| **Capture** | What did a person, team, or organization decide? | interviews, prompts, tickets, product evidence, decision records |
| **Represent** | How is the decision stored without discarding important structure? | intent record, tree, atomic requirement, living spec, event log |
| **Propagate** | Which slice reaches the current agent, task, or reviewer? | selectors, inheritance, links, context packages, issue contracts |
| **Enforce** | Which boundaries must hold during execution? | policies, permissions, tests, linters, invariants, approval gates |
| **Verify** | Which evidence establishes that the outcome occurred? | acceptance checks, scenario coverage, independent review, runtime signals |
| **Evolve** | How do findings and changed decisions update intent while retaining history? | intent diff, supersession, merge, retraction, rejected-path memory |

See the full [taxonomy](docs/taxonomy.md), [field notes](docs/field-notes.md), and [evidence policy](docs/evidence-policy.md).

## Field model

The repository adapts a useful piece of prior art from [RFC 9315](https://www.rfc-editor.org/rfc/rfc9315.html), an informational IRTF document on intent-based networking. That RFC defines intent as declarative goals and outcomes without implementation instructions, then describes ingestion, refinement, translation, orchestration, monitoring, compliance assessment, corrective action, drift, and lifecycle changes.

Applied to coding agents, the control flow becomes:

```text
human evidence and decisions
        │
        ▼
 ingest → normalize → compile/propagate → fulfill/enforce
   ▲                                           │
   │                                           ▼
 evolve ← correct/escalate ← assess ← observe/collect
```

The model contains two loops:

- an **inner loop** can observe, verify, retry, and repair inside delegated authority;
- an **outer loop** lets a person or authorized process change the intent, constraints, trade-offs, or authority envelope.

The detailed adaptation, drift taxonomy, and three-record model are in [`docs/field-model.md`](docs/field-model.md). RFC 9315 remains networking-domain prior art; this repository does not present it as a software-engineering standard.

## Featured landscape

Projects are grouped by the mechanism they expose, not ranked or endorsed. Inclusion follows the [evaluation rubric](docs/evaluation-rubric.md), and every catalog record includes primary evidence, current availability, and a material limitation.

### Core systems and formats

| Project | Primary surface | Durable representation | Trace / verification | Availability |
| --- | --- | --- | --- | --- |
| **[CodeSpeak](https://codespeak.dev/)** | continuous capture from coding-agent chats | interconnected atomic requirements grounded in human prompts and accepted code | code mapping, planning, and drift verification; intent diffs and coverage are announced roadmap items | waitlist; recovery web tool available |
| **[IntentSpec](https://intentspec.org/)** | evidence-backed per-feature intent | Markdown + YAML frontmatter + JSON Schema | evidence anchors, explicit checks, CI schema validation | open format |
| **[Pathmode](https://pathmode.io/)** | product evidence and judgment | executable intent specs with objectives, outcomes, constraints, edge cases, and checks | agent handoff, verification, and findings write-back | commercial product |
| **[Intent-System](https://github.com/J-Tech-Japan/intent-system)** | operational Intent-Driven Development | intent tree + child issue contracts + GitHub metadata | deterministic design, implementation, review, recovery, and escalation workflow | open source |
| **[Linked-Intent Development](https://github.com/jszmajda/lid)** | durable design-before-code method | HLD → LLD → EARS → tests → code, linked by stable identifiers | trace navigation, attestation, consistency maintenance, and downstream cascade | open source |
| **[Intent Integrity Kit](https://github.com/intent-integrity-chain/kit)** | integrity-preserving specification workflow | intent → spec → Gherkin → step definitions → code | hash-locked feature steps, coverage and test-quality checks, requirement-change restart | open source |
| **[Intent](https://github.com/matthewsinclair/intent)** | project rationale and feature work | versioned Steel Threads containing why, what, design, and tasks | work packages, status, and close-gates | open source |
| **[Intent File Specification](https://github.com/IntentFile/intent-specification)** | declarative application intent | versioned vendor-neutral `*.intent` YAML | deterministic handoff to platform model generators; public proposal process | open format |
| **[Intent Engineering / INTENT.md](https://github.com/roboco-io/intent-engineering)** | minimal project-level intent | `INTENT.md`: Why, What, Not, Learnings | lifecycle from seed through clarification, build, or rejection | open source |
| **[SpecLeft](https://github.com/SpecLeft/specleft)** | behavioral intent | feature/scenario Markdown with stable IDs | pytest traceability, gap analysis, and intent coverage | open source; Python/pytest today |

> [!NOTE]
> **Featured case study: [CodeSpeak](docs/code-speak-case-study.md).** Its public design provides a concrete model for continuous capture, atomic intent evolution, living requirements, and intent diff. The case study separates the current product surface from the upcoming release and later roadmap.

### Provenance and decision memory

- **[Selvedge](https://github.com/masondelan/selvedge)** — local MCP server that records change events, rationale, constraints, supersession, and rejected paths while the original agent context still exists. Agent-authored rationale remains execution provenance until it is linked to an approved human or organizational decision.

### Adjacent specification and harness systems

- **[GitHub Spec Kit](https://github.com/github/spec-kit)** — governing principles, specification, plan, tasks, implementation, convergence, and consistency checks.
- **[OpenSpec](https://github.com/Fission-AI/OpenSpec)** — proposal, specs, design, tasks, application, verification, archival, and shared stores.
- **[OpenAI Harness Engineering](https://openai.com/index/harness-engineering/)** — repository structure, legibility, tools, feedback loops, and enforceable constraints around coding agents.

These projects enter the catalog when they transport or enforce explicit intent. Generic agent frameworks remain outside scope until they expose an inspectable intent artifact, trace, or verification mechanism.

### Prior art and research

- **[RFC 9315: Intent-Based Networking](https://www.rfc-editor.org/rfc/rfc9315.html)** — full intent lifecycle, fulfillment and assurance planes, drift, and inner/outer control loops.
- **[From Technical Debt to Cognitive and Intent Debt](https://arxiv.org/abs/2603.22106)** — intent debt as absent or eroded externalized rationale, goals, and constraints.
- **[From Code Review to Code Critique](https://arxiv.org/abs/2607.29516)** — intent prediction, drift detection, and code spotlight for AI-generated diffs.
- **[Beyond the Diff: Addressing Agentic Entropy](https://arxiv.org/abs/2604.16323)** — divergence between agent actions and architectural intent across time and tool calls.
- **[Towards Assurance Closure](https://arxiv.org/abs/2608.07317)** — required truths, evidence credibility, residual uncertainty, and bounded agent authority.
- **[Context Engineering: From Prompts to Corporate Multi-Agent Architecture](https://arxiv.org/abs/2603.09619)** — organizational goals, values, policies, and trade-off hierarchies as an intent layer.
- **[From Code-Centric to Intent-Centric Software Engineering](https://arxiv.org/abs/2605.11027)** — accountability and intent-centered work in generative and agentic development.

### Learning resources

- **[Intent Engineering for Coding Agents](https://intent-engineering-for-coding-agents.github.io/book/)** — open book on source-controlled decisions, repository foundations, specifications, ADRs, and test traceability.

The complete machine-readable catalog, including lifecycle tags, limitations, source evidence, and verification dates, lives in [`data/resources.yml`](data/resources.yml).

## Strongest current findings

1. **Provenance is part of the data model.** Human-authored decisions, human-approved model output, model-derived interpretations, agent observations, and runtime evidence need distinct labels.
2. **Intent has a lifecycle.** Ingestion, refinement, fulfillment, assurance, correction, and retraction existed as an intent-systems problem before the current coding-agent wave; RFC 9315 supplies a reusable control model.
3. **Artifact lifetime matters.** A change spec coordinates a bounded delivery event. Living intent remains attached to behavior after the original task closes.
4. **Structured representations support selective retrieval.** Current systems use atomic requirements, schemas, trees, stable scenario IDs, linked design layers, and append-only events. These structures let an agent receive a relevant slice and let reviewers trace it later.
5. **Evidence belongs beside the claim it supports.** IntentSpec and Pathmode attach observations to outcomes and edge cases. Intent Integrity Kit and Linked-Intent Development extend the chain into executable checks.
6. **Verification needs an independence model.** A system should record whether completion was asserted by the implementing agent, a separate reviewer, a mechanical check, a human, or runtime observation.
7. **Intent diff, coverage, and drift are forming a review vocabulary.** CodeSpeak announces intent diffs and coverage; SpecLeft reports behavioral coverage; current research evaluates intent drift and architecture-level divergence.
8. **Rejected paths remain operationally useful.** Recording why an approach was abandoned prevents later agents from repeating it under the same conditions.
9. **Authority can depend on assurance.** Evidence quality, uncertainty, and risk can determine whether an agent may retry, deploy, spend, delete, or must escalate.

Detailed sources and caveats are in [`docs/field-notes.md`](docs/field-notes.md). The catalog’s inclusion and scoring mechanics are in [`docs/evaluation-rubric.md`](docs/evaluation-rubric.md).

## Relationship to neighboring disciplines

```text
INTENT      outcome · rationale · constraints · trade-offs · authority · evidence
   │
   ▼
SPEC        buildable behavioral and technical contract
   │
   ▼
CONTEXT     relevant slice assembled for this decision
   │
   ▼
HARNESS     tools · repository · permissions · checks · feedback
   │
   ▼
LOOP/GRAPH  execution topology · state · continuation rules
   │
   ▼
ASSURANCE   evidence · credibility · uncertainty · escalation
   │
   └──────────── findings update the durable intent record
```

The layers compose. A specification can carry intent. A harness can enforce it. A graph can encode authority and escalation. Classification follows the artifact or control surface each project makes explicit.

## Experimental reference artifacts

The repository includes a small comparison format for testing the taxonomy across tools:

- [`schemas/intent-record.v0.1.schema.json`](schemas/intent-record.v0.1.schema.json) — JSON Schema Draft 2020-12;
- [`examples/intent-record.yml`](examples/intent-record.yml) — validated example with provenance, stable outcomes and constraints, authority, independent verification, stop conditions, and rejected paths;
- [`docs/reference-model.md`](docs/reference-model.md) — design goals, trace model, and open questions.

These files are discussion artifacts. They do not replace IntentSpec, Intent File, or another project’s schema.

Run the offline checks:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
```

The validator checks the resource catalog, term registry, prediction ledger, JSON Schema, stable identifiers, and semantic trace references in the example.

## Prediction ledger

Predictions are timestamped and include resolution and falsification conditions in [`data/predictions.yml`](data/predictions.yml).

| ID | Prediction | Window | Confidence |
| --- | --- | --- | ---: |
| P001 | **Intent diff** becomes a standard review surface for AI-assisted changes. | by 2027-12-31 | 0.78 |
| P002 | **Intent coverage** appears as a maintained metric in multiple tools or benchmarks. | by 2027-12-31 | 0.72 |
| P003 | Bidirectional **intent ↔ code/test traceability** becomes a recognizable product category. | by 2027-12-31 | 0.70 |
| P004 | Larger systems move from one monolithic `INTENT.md` toward trees, graphs, or atomic requirement stores. | by 2027-12-31 | 0.66 |
| P005 | Evidence quality and uncertainty become explicit inputs to **agent authority** and escalation. | by 2028-06-30 | 0.75 |
| P006 | **Intent Engineering** becomes a recognizable umbrella term across tools, research, and job descriptions. | by 2027-06-30 | 0.64 |

## Repository map

```text
.
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── CHANGELOG.md
├── data/
│   ├── resources.yml          # machine-readable evidence-first catalog
│   ├── terms.yml              # terms, status, definitions, source signals
│   └── predictions.yml        # timestamped, falsifiable forecasts
├── docs/
│   ├── thesis.md
│   ├── field-model.md         # adapted fulfillment/assurance lifecycle
│   ├── taxonomy.md
│   ├── landscape.md
│   ├── field-notes.md
│   ├── code-speak-case-study.md
│   ├── evaluation-rubric.md
│   ├── timeline.md
│   ├── glossary.md
│   ├── evidence-policy.md
│   └── reference-model.md
├── schemas/
│   └── intent-record.v0.1.schema.json
├── examples/
│   └── intent-record.yml
└── scripts/
    └── validate_catalog.py
```

## Contributing

Found a missing tool, a stale availability claim, or a better primary source? [Open a structured issue](https://github.com/monaxovdulov/awesome-intent-engineering/issues/new/choose) or [start a discussion](https://github.com/monaxovdulov/awesome-intent-engineering/discussions). Corrections are as valuable as additions.

A resource qualifies when it exposes at least one concrete intent mechanism:

- durable goals, rationale, constraints, trade-offs, or non-goals;
- an intent document, tree, graph, requirement store, scenario map, or event log;
- traceability from intent to code, tests, decisions, or runtime evidence;
- intent coverage, drift, fidelity, or assurance measurement;
- ownership, approval, authority, or escalation tied to intent;
- substantive research, specification, benchmark, or teaching material.

Every entry must link to a primary source, state current availability, record a limitation, distinguish authorship classes where relevant, and include `last_verified`.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), the [evidence policy](docs/evidence-policy.md), and the [evaluation rubric](docs/evaluation-rubric.md) before opening a pull request.

If this map saves you research time, star the repository to follow new tools, terminology, and prediction updates.

## Status

This repository is a field map, comparison framework, and public prediction ledger. It does not claim ownership of the term, endorse every included project, or declare a final standard. Definitions and classifications change when implementation evidence changes. The public seed is open for corrections while the maintainer completes the manual editorial review required before any submission to the canonical Awesome index.
