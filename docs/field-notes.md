# Field Notes: Strongest Signals as of 2026-08-21

These notes separate observed mechanisms from forecasts.

## 1. Human intent is becoming a provenance class

CodeSpeak’s July 13, 2026 design note states that model-generated specifications are derivative artifacts and should remain separate from human intent. Its proposed system extracts atomic requirements from the prompts people already give coding agents, then tracks additions, removals, and refinements.

Observed consequence: an intent system needs authorship and approval metadata. A generated summary cannot silently become the canonical decision.

Sources:

- https://codespeak.dev/blog/spindle-20260713
- https://codespeak.dev/

## 2. The market is splitting change specs from living intent

CodeSpeak describes two lifetimes:

- **change spec** — coordinates one change and stops updating when the work ends;
- **living spec** — remains attached to the behavior and changes with the system.

GitHub Spec Kit and OpenSpec provide mature change-oriented workflows. CodeSpeak’s structured requirements, Intent-System’s tree, Intent’s Steel Threads, and Selvedge’s event history address longer continuity in different ways.

Observed consequence: catalog entries should state the expected lifetime of their intent artifact.

Sources:

- https://codespeak.dev/blog/spindle-20260713
- https://github.com/github/spec-kit
- https://github.com/Fission-AI/OpenSpec

## 3. Structured intent is replacing the giant prose blob in several implementations

Current representations include:

- atomic interconnected requirements — CodeSpeak;
- schema-validated feature records — IntentSpec;
- intent trees — Intent-System;
- feature/scenario identifiers — SpecLeft;
- versioned Steel Threads — Intent;
- append-only rationale events — Selvedge.

OpenAI’s harness-engineering report independently documents why one large instruction file failed: context pressure, stale rules, weak mechanical verification, and poor navigability. Their repository uses a short map plus structured deeper sources of truth.

Observed consequence: a scalable intent system needs progressive disclosure, ownership, and selective retrieval.

Sources:

- https://openai.com/index/harness-engineering/
- https://codespeak.dev/blog/spindle-20260713
- https://intentspec.org/
- https://www.intent-driven-development.com/

## 4. Product evidence is entering the same artifact as definition of done

IntentSpec attaches quotes, friction, and observations to specific outcomes and edge cases. Pathmode describes a loop from raw evidence to objective, constraints, edge cases, agent handoff, verification, and findings write-back.

Observed consequence: the “why” can be inspectable at the same granularity as the expected behavior.

Sources:

- https://intentspec.org/
- https://pathmode.io/

## 5. Intent diff is a likely review primitive

A code diff shows implementation changes. It does not directly show which outcome, constraint, or trade-off changed.

CodeSpeak lists intent diffs and merge conflicts among its upcoming capabilities. Its current design also proposes tracking which requirements were added, dropped, or refined with each prompt.

Forecast: review systems will show an intent change before or beside the code diff.

Source: https://codespeak.dev/blog/spindle-20260713

## 6. Coverage and drift are turning intent into an observable control surface

SpecLeft reports whether declared feature scenarios map to implementation tests. CodeSpeak lists intent coverage on its roadmap. ARCTIC reports an evaluated intent-prediction and drift-detection system for generated diffs.

Observed consequence: intent can participate in CI and review when it has stable identifiers and links to checks.

Sources:

- https://specleft.dev/
- https://codespeak.dev/blog/spindle-20260713
- https://arxiv.org/abs/2607.29516

## 7. Rejected paths are part of durable intent history

A team can preserve the reason current code exists and still repeat an abandoned approach. Selvedge treats tried, reverted, and reopened paths as queryable history captured by the original agent at change time.

Observed consequence: an intent store needs negative decisions, supersession, and “do not retry until condition X changes.”

Source: https://github.com/masondelan/selvedge

## 8. Intent debt now has a research definition

Margaret-Anne Storey defines intent debt as absent or eroded explicit rationale, goals, and constraints in externalized knowledge. This distinguishes it from technical debt in code and cognitive debt in people.

Observed consequence: documentation volume is a poor proxy. The relevant question is whether future humans and agents can recover the rationale and boundaries required to change the system safely.

Source: https://arxiv.org/abs/2603.22106

## 9. Intent-level telemetry is moving into review and architecture oversight

ARCTIC uses conversation logs and metadata to infer intent and measure drift. “Beyond the Diff” describes agentic entropy as divergence between agent actions and architectural intent across time and tool calls.

Observed consequence: local code correctness can coexist with system-level misalignment. Review tools need task, process, and architecture context.

Sources:

- https://arxiv.org/abs/2607.29516
- https://arxiv.org/abs/2604.16323

## 10. Evidence quality may determine autonomy

Assurance closure requires a system to establish what must be true, gather evidence, judge credibility, preserve validity through change, and bound agent authority using remaining uncertainty.

Forecast: mature agent platforms will connect intent and verification records directly to permissions, deployment, spending, and escalation.

Source: https://arxiv.org/abs/2608.07317

## Working synthesis

The strongest common shape is:

```text
human decision / product evidence
        ↓
versioned intent with provenance
        ↓
selective handoff to task and agent
        ↓
mechanical constraints and checks
        ↓
trace from intent to code and tests
        ↓
execution evidence and findings
        ↓
intent diff, supersession, or escalation
```

No current project covers every stage equally. That gap is useful: it gives the repository a stable taxonomy even while product names and engineering labels change.
