# Field Model: Intent Fulfillment and Assurance

This field model adapts prior work on intent-based systems to AI-native software engineering. Its closest formal precedent is [RFC 9315](https://www.rfc-editor.org/rfc/rfc9315.html), an informational IRTF document published in 2022 for intent-based networking.

RFC 9315 defines intent as declarative operational goals and outcomes without prescribing implementation. It then separates **fulfillment** from **assurance**:

- ingestion and refinement with the user;
- translation into actionable lower-level requests;
- orchestration of those requests;
- monitoring and observation;
- compliance assessment;
- corrective action or escalation;
- lifecycle changes, including refinement and retraction.

The networking domain differs from software-agent work. The control problem is still useful: an autonomous system receives desired outcomes, translates them into actions, changes a real environment, observes the result, and reports enough information for a person to revise the original intent.

## Adapted lifecycle for coding agents

```text
                           OUTER LOOP
       human evidence, decisions, approval, revision, retraction
                │                                  ▲
                ▼                                  │
┌─────────┐  ┌───────────┐  ┌───────────┐  ┌─────┴─────┐
│ INGEST  │→ │ NORMALIZE │→ │ COMPILE & │→ │  FULFILL  │
│         │  │ / REFINE  │  │ PROPAGATE │  │ / ENFORCE │
└─────────┘  └───────────┘  └───────────┘  └─────┬─────┘
                                                  │
                                                  ▼
                                            implementation
                                            tests / config
                                            deployment
                                                  │
                                                  ▼
┌─────────┐  ┌───────────┐  ┌───────────┐  ┌─────┴─────┐
│ EVOLVE  │← │ CORRECT / │← │  ASSESS   │← │  OBSERVE  │
│         │  │ ESCALATE  │  │ COMPLIANCE│  │ / COLLECT │
└─────────┘  └───────────┘  └───────────┘  └───────────┘
                ▲                                  │
                └────────── INNER LOOP ────────────┘

Cross-cutting: provenance · ownership · authority · traceability
```

### 1. Ingest

Collect candidate intent from prompts, interviews, tickets, strategy, product evidence, policies, and explicit decisions.

Required distinction: evidence, proposed interpretation, approved decision, and runtime observation are different provenance classes.

### 2. Normalize and refine

Resolve ambiguity, name outcomes and constraints, preserve trade-offs, assign ownership, record non-goals, and establish approval state.

An agent may assist with this step. Model-derived wording should remain identifiable until a person or authorized process approves it.

### 3. Compile and propagate

Translate durable intent into the relevant slice for a feature, issue, agent, reviewer, or deployment gate.

Typical outputs:

- task or change specification;
- context package;
- issue contract;
- testable scenarios;
- policy and permission rules;
- implementation plan.

The durable record and the compiled execution artifact can have different lifetimes.

### 4. Fulfill and enforce

Execute the work and apply hard boundaries through repository rules, permissions, tests, policy checks, budgets, and approval gates.

This is where intent composes with harness, loop, and graph engineering.

### 5. Observe and collect

Collect evidence from tests, static checks, reviews, runtime telemetry, user behavior, incidents, and implementation findings.

Evidence should identify its source, collection method, time, and the outcome or constraint it supports.

### 6. Assess compliance

Compare observed behavior with the approved intent record. A completion claim should state:

- which outcomes were checked;
- which constraints were checked;
- what evidence was obtained;
- how independent the check was;
- what uncertainty remains.

### 7. Correct or escalate

A system can retry or repair inside its delegated authority. It should escalate when evidence is insufficient, constraints conflict, or the required action exceeds its authority.

### 8. Evolve

Refine, supersede, merge, split, reject, or retract intent. Preserve the reason for the change and any rejected paths that remain relevant.

## Inner and outer loops

RFC 9315 separates two loops. The same distinction is useful here.

### Inner loop

The agentic system observes execution, checks compliance, and takes bounded corrective action without changing the approved objective or authority envelope.

Examples:

- rerun a failed deterministic test;
- repair a local implementation defect;
- regenerate a derived plan after a source file changes;
- request an additional mechanical check.

### Outer loop

A person or authorized organizational process changes the intent itself.

Examples:

- accept a trade-off that changes a success criterion;
- relax or strengthen a constraint;
- approve deployment or spending;
- resolve conflicting stakeholder goals;
- retract the feature.

Systems should make the boundary visible. An inner-loop repair must not silently become an outer-loop policy change.

## Drift types

| Drift | Observable mismatch | Typical detection |
| --- | --- | --- |
| **Semantic drift** | current requirement meaning differs from the approved decision | intent diff, approval history, requirement comparison |
| **Artifact drift** | specs, tests, code, or docs no longer agree | trace validation, coverage, consistency checks |
| **Execution drift** | agent actions diverge from the permitted plan or constraints | tool-call telemetry, policy checks, budget limits |
| **Behavior drift** | deployed behavior stops satisfying intended outcomes | runtime telemetry, user observation, incident signals |
| **Evidence drift** | a previously valid completion claim loses support after change | evidence freshness, dependency invalidation, assurance review |
| **Authority drift** | the system acts beyond its current delegation | permission audit, approval gates, signed policy checks |

## Three records

A practical implementation can separate three records while linking them with stable identifiers:

1. **Intent record** — goals, rationale, outcomes, constraints, trade-offs, authority, approval.
2. **Execution record** — plans, tasks, tool calls, code changes, decisions made during fulfillment.
3. **Evidence record** — tests, observations, runtime signals, reviewer verdicts, residual uncertainty.

This separation prevents an execution narrative from being mistaken for human intent and prevents a generated completion summary from being mistaken for independent evidence.

## Boundary

This document is an editorial synthesis. RFC 9315 is prior art from network management, not a software-engineering standard. The schema and terminology in this repository remain experimental until implementations test their merge, approval, trace, and assurance semantics.
