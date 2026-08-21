# Thesis

## Claim

As agents take on more implementation work, a team needs durable mechanisms for preserving what the work is meant to achieve, why it matters, which boundaries apply, who may authorize actions, and what evidence closes the task.

This repository uses **Intent Engineering** as a working name for that set of mechanisms.

## The intent lifecycle

```text
capture → represent → propagate → enforce → verify → evolve
```

Each stage has an observable artifact:

1. **Capture** leaves a prompt, quote, decision, observation, metric, interview note, or signed-off requirement.
2. **Represent** leaves a document, tree, graph, atomic requirement, scenario, decision record, or structured store.
3. **Propagate** leaves a context selection rule, inheritance edge, issue contract, link, or trace.
4. **Enforce** leaves a policy, permission, test, linter, invariant, budget, stop rule, or approval gate.
5. **Verify** leaves test output, runtime observation, artifact, review verdict, confidence estimate, or production signal.
6. **Evolve** leaves an intent diff, finding, supersession record, rejected-path record, or changed status.

## Human intent and derivative artifacts

A reliable system preserves provenance among three classes:

| Class | Example | Risk when unlabeled |
| --- | --- | --- |
| **Human-authored intent** | product decision, constraint, explicit non-goal, approved trade-off | a model rewrite can silently change meaning |
| **Model-derived artifact** | generated spec, implementation plan, inferred requirement | readers may treat a plausible synthesis as a decision |
| **Observed evidence** | user quote, metric, test result, runtime trace | evidence can be detached from the claim it supports |

CodeSpeak’s July 2026 design note makes this separation explicit: model-generated material is derivative, while the product aims to ground structured requirements in human prompts and accepted code. IntentSpec makes evidence anchors part of the same artifact as outcomes and edge cases.

Sources:

- https://codespeak.dev/blog/spindle-20260713
- https://intentspec.org/

## Change specs and living intent

A change spec coordinates a bounded change. Its useful lifetime usually ends when the change ships. A living intent record remains attached to the behavior or subsystem and must be updated when decisions or implementation change.

CodeSpeak describes this split as **Change Specs** and **Living Specs**. GitHub Spec Kit and OpenSpec provide strong change-oriented workflows. CodeSpeak, Intent-System, Intent, and Selvedge attempt different forms of durable continuity.

Sources:

- https://codespeak.dev/blog/spindle-20260713
- https://github.com/github/spec-kit
- https://github.com/Fission-AI/OpenSpec

## The representation is likely to become structured

A single `INTENT.md` is useful for small projects because it is inspectable and easy to version. It becomes harder to maintain when:

- many teams own different parts of the system;
- one decision constrains several repositories;
- requirements are added, removed, refined, or superseded independently;
- the current agent needs only a small relevant slice;
- reviewers need coverage, freshness, ownership, and traceability checks.

Current systems respond with several structures:

- atomic interconnected requirements — CodeSpeak;
- evidence-anchored feature records — IntentSpec;
- intent trees — Intent-System;
- Steel Threads — Intent;
- feature/scenario identifiers — SpecLeft;
- append-only event and rejected-path history — Selvedge.

The repository therefore treats the file, tree, graph, requirement store, and event log as alternative representations of the same lifecycle concern.

## Evidence belongs near the claim

Intent can be explicit and still be weak. A requirement backed only by authority or recollection can survive technically while losing the reason it was chosen.

IntentSpec and Pathmode attach quotes, friction, observations, and metrics to the outcomes and edge cases they justify. This allows an agent or reviewer to inspect the basis of the decision and update the record when the evidence changes.

Sources:

- https://intentspec.org/
- https://pathmode.io/

## Traceability creates operational leverage

The most useful emerging primitives are:

- **intent diff** — what decision or requirement changed;
- **intent-to-code trace** — where a requirement is implemented;
- **intent-to-test trace** — which check verifies a scenario;
- **intent coverage** — which declared behaviors have verification;
- **intent drift** — how far execution diverged from the intended result;
- **finding write-back** — what implementation or production revealed about the original assumption.

Signals:

- CodeSpeak lists intent diffs, bidirectional code links, test generation, and intent coverage on its roadmap.
- SpecLeft reports declared behavioral coverage and missing implementation.
- ARCTIC evaluates intent prediction and drift detection for generated diffs.
- Pathmode describes findings that return from execution into the spec.

Sources:

- https://codespeak.dev/blog/spindle-20260713
- https://specleft.dev/
- https://arxiv.org/abs/2607.29516
- https://pathmode.io/

## Provenance is required, but provenance is not intent

A record of what an agent reasoned when it changed code can explain implementation history. It does not by itself prove that the reasoning reflects the human decision.

Selvedge is included because it captures rationale, constraints, supersession, and rejected paths while the original agent context exists. Its data should be classified as agent-authored testimony unless a human approves or links it to a decision artifact.

Source: https://github.com/masondelan/selvedge

## Verification changes autonomy

The task is not closed merely because an agent says it is done. Assurance closure frames a stronger sequence:

1. establish what must be true;
2. determine appropriate evidence;
3. obtain that evidence;
4. judge its credibility;
5. preserve validity as the system changes;
6. use remaining uncertainty to bound agent authority.

This connects intent records with permissions, escalation, deployment, and long-running loops.

Source: https://arxiv.org/abs/2608.07317

## Relationship to neighboring layers

| Layer | Primary control surface |
| --- | --- |
| Prompt engineering | wording and examples in a model call |
| Context engineering | dynamic assembly of information and tools |
| Specification engineering / SDD | buildable and reviewable contracts |
| Harness engineering | repository, tools, checks, and environment |
| Loop engineering | repeated autonomous execution and stop conditions |
| Graph engineering | explicit topology, state, and transitions |
| Intent engineering | durable goals, rationale, constraints, trade-offs, authority, and definitions of done |
| Assurance engineering | evidence credibility, uncertainty, escalation, and bounded authority |

These layers compose. The same artifact may participate in more than one layer.
