# Landscape

Last reviewed: **2026-08-21**.

The tables summarize primary-source claims. Availability and roadmaps can change; verify the linked source before adopting a tool.

## Core projects

| Project | Intent source | Representation | Execution handoff | Verification / evolution | Current constraint |
| --- | --- | --- | --- | --- | --- |
| [CodeSpeak](https://codespeak.dev/) | prompts in coding-agent conversations | structured, interconnected requirements grounded in human words and accepted code | relevant requirements are intended to enter agent context | planning and drift verification; intent diffs, bidirectional links, tests, and coverage are roadmap items | upcoming product on waitlist; older CLI is being retired |
| [IntentSpec](https://intentspec.org/) | human judgment plus product evidence | per-feature `intent.md`, YAML frontmatter, JSON Schema | any agent that can read the file | evidence anchors, explicit verification, CI schema validation | format validates structure; evidence quality remains a human/product judgment concern |
| [Pathmode](https://pathmode.io/) | customer evidence, strategy, decisions, codebase context | executable intent spec | exports/handoffs to agents and work trackers | findings write back into the spec | commercial product; product claims are vendor-reported |
| [Intent-System](https://github.com/J-Tech-Japan/intent-system) | human design and product decisions | intent tree and child issue contracts | GitHub issues and supervised worker/reviewer threads | deterministic workflow, review, recovery, and escalation | operational model is more involved than a single-repo document |
| [Intent](https://github.com/matthewsinclair/intent) | project and feature rationale | Steel Threads: why, what, design, tasks | CLI and agent-facing repository artifacts | work packages, status, and close-gates | opinionated project method and repository structure |
| [roboco Intent Engineering](https://github.com/roboco-io/intent-engineering) | manually maintained project intent | one `INTENT.md`: Why, What, Not, Learnings | handoff to an AI implementation workflow | lifecycle: seed, exploring, clarified, build, dropped | minimal artifact; large-project inheritance and traceability are not its focus |
| [SpecLeft](https://github.com/SpecLeft/specleft) | explicit behavioral specifications or PRD | feature/scenario Markdown with stable identifiers | agent-readable specs and generated test skeletons | pytest traceability, gap analysis, coverage reports | Python and pytest are the current supported path |

## Provenance and memory

| Project | Captures | Representation | Value to intent engineering | Boundary |
| --- | --- | --- | --- | --- |
| [Selvedge](https://github.com/masondelan/selvedge) | agent-authored change rationale, constraints, supersession, rejected paths | local SQLite event store plus exports | preserves why and failed approaches across sessions | agent rationale is evidence about execution, not automatic proof of human intent |

## Adjacent systems

| Project | Primary concern | Intent-relevant mechanism |
| --- | --- | --- |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | spec-driven development | governing principles, what/why specification, planning, tasks, implementation, convergence, and consistency checks |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | artifact-guided spec workflow | proposal, requirements/scenarios, design, tasks, verification, archive, and shared stores |
| [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/) | agent-legible engineering environment | versioned repository knowledge, execution plans, mechanical checks, structured feedback, and progressive disclosure |

## Research map

| Work | Concept | Operational implication |
| --- | --- | --- |
| [From Technical Debt to Cognitive and Intent Debt](https://arxiv.org/abs/2603.22106) | intent debt | missing rationale, goals, and constraints become a software-health liability |
| [From Code Review to Code Critique](https://arxiv.org/abs/2607.29516) | intent prediction and drift detection | review can rank divergence from inferred developer intent, not only inspect local style |
| [Beyond the Diff](https://arxiv.org/abs/2604.16323) | agentic entropy | oversight needs process and architecture-level telemetry across time and tool calls |
| [Towards Assurance Closure](https://arxiv.org/abs/2608.07317) | assurance closure | evidence credibility and uncertainty should bound agent authority |
| [Context Engineering: From Prompts to Corporate Multi-Agent Architecture](https://arxiv.org/abs/2603.09619) | organizational intent engineering | agents need access to goals, values, policies, and trade-off hierarchies |
| [From Code-Centric to Intent-Centric Software Engineering](https://arxiv.org/abs/2605.11027) | intent-centric accountability | engineering work shifts toward decisions, oversight, and responsibility for generated systems |

## Areas still thin

The catalog currently has fewer strong implementations for:

- resolving conflicts between organization, product, repository, and task intent;
- cryptographic or signed human approval of intent changes;
- standard merge semantics for atomic intent requirements;
- measuring intent fidelity without reconstructing intent post hoc;
- connecting product evidence to production outcomes over long periods;
- authority policies that automatically adapt to assurance confidence;
- interoperable exchange formats between product, specification, agent, and verification tools.
