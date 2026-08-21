# CodeSpeak Case Study

Status reviewed: **2026-08-21**.

CodeSpeak is a strong current signal for Intent Engineering because it treats the prompts already exchanged with coding agents as provenance-bearing input, extracts atomic requirements, preserves their evolution, maps them to code, and plans to expose intent changes as a review surface.

## Availability map

### Available now

- Public product description and waitlist.
- Open Intent Studio, a web tool for recovering intent from existing agent chats.
- Public description of planning, verification, and collaboration around structured requirements.

### Announced for the upcoming release

- plugins for Claude and Codex;
- automatic intent extraction into structured specifications;
- aggregation of intent from multiple teammates;
- intent diffs for review and merge conflicts.

### Listed for future releases

- editing requirements and generating code from those edits;
- bidirectional links between requirements and code;
- intent-informed test generation and intent coverage;
- modularity and architectural guardrails.

The catalog does not describe upcoming or future items as shipped capabilities.

## Mechanism

CodeSpeak’s July 2026 design note separates two artifact lifetimes:

- a **change spec** coordinates one change and stops evolving after completion;
- a **living spec** remains attached to the functionality and changes with the system.

The proposed representation is a set of interconnected atomic requirements. The system tracks requirements added, dropped, or refined through agent prompts. Each requirement is grounded in the human’s words and accepted code rather than presented as an unqualified model-authored summary.

```text
agent conversations
        │
        ▼
provenance-bearing prompts
        │
        ▼
atomic structured requirements
        │
        ├────────► relevant requirement selection for planning
        ├────────► mapping to implementation
        ├────────► verification against later changes
        └────────► intent diff and history
```

## Why it matters

### Continuous capture

Teams already state goals, corrections, constraints, and trade-offs in agent conversations. Capturing those events reduces reliance on a separate specification-writing ritual.

### Authorship separation

The design explicitly classifies model-generated specifications as derivative artifacts. This creates a requirement for provenance and approval metadata in any shared intent store.

### Atomic evolution

Add, drop, and refine operations can be reviewed at requirement granularity. They provide a plausible basis for merge semantics, selective retrieval, and intent diff.

### Living retrieval

Relevant requirements can enter later agent contexts after the original feature task closes. This addresses continuity across sessions and changes.

### Review surface

An intent diff can show which expected behavior or constraint changed before a reviewer inspects implementation details.

## Open questions

The public materials leave several engineering questions open:

1. **Extraction fidelity** — how does the system preserve ambiguity instead of converting every prompt sentence into a requirement?
2. **Approval** — when does a model-extracted requirement become an approved team decision?
3. **Conflicts** — how are contradictory prompts from one person or several teammates resolved?
4. **Deletion and supersession** — how are dropped requirements distinguished from accidental omission?
5. **Accepted code as evidence** — code acceptance may confirm implementation while still failing to prove that a requirement reflects intended product behavior.
6. **Independent verification** — can the agent responsible for fulfillment also change the requirement or check that certifies completion?
7. **Privacy** — agent conversations can contain customer data, credentials, or internal decisions; capture and retention need explicit controls.
8. **Portability** — the public materials do not yet define an interoperable export or merge format for the requirement store.

## Evaluation snapshot

This is an editorial estimate using the repository’s [evaluation rubric](evaluation-rubric.md). It evaluates the publicly described mechanism, including current and announced components, and should be revised after the upcoming release becomes inspectable.

| Dimension | Score | Basis |
| --- | ---: | --- |
| Provenance | 2 | human prompts and accepted code are identified as grounding; approval semantics remain open |
| Structure | 3 | interconnected atomic requirements with explicit add/drop/refine operations |
| Propagation | 2 | relevant requirements are selected for planning and agent context; inheritance semantics are not public |
| Enforcement | 2 | product states that requirements are enforced on changes; implementation details are not yet public |
| Verification | 2 | drift verification is central; evidence independence and residual uncertainty are not described |
| Evolution | 3 | living history and intent diffs are explicit design goals |
| Authority | 0 | permissions and approval gates are not described in the public materials |
| Inspectability | 1 | public design and recovery tool; upcoming core product remains on waitlist |
| **Total** | **15/24** | substantive emerging system; reevaluate after release |

## Primary sources

- [CodeSpeak product page](https://codespeak.dev/)
- [What’s next for CodeSpeak: Structured Approach to Specs](https://codespeak.dev/blog/spindle-20260713)
