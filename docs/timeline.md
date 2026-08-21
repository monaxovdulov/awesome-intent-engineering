# Selected Timeline

This is a timeline of **prominent public signals**, not a claim of first-ever coinage. A practice often predates the label attached to it.

| Date | Signal | Engineering unit emphasized |
| --- | --- | --- |
| 2021-02-15 | [Prompt Programming for Large Language Models](https://arxiv.org/abs/2102.07350) | instructions, examples, and metaprompts inside a model call |
| 2023-06-30 | [The Rise of the AI Engineer](https://www.latent.space/p/ai-engineer) expands the role beyond prompting | application integration around foundation models |
| 2024-01-16 | [AlphaCodium: From Prompt Engineering to Flow Engineering](https://arxiv.org/abs/2401.08500) | iterative multi-step solution flow |
| 2024-02-18 | [The Shift from Models to Compound AI Systems](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) | multiple interacting model calls, retrievers, tools, and code |
| 2025-06-23 | [The rise of context engineering](https://www.langchain.com/blog/the-rise-of-context-engineering) | dynamic delivery of the right information and tools |
| 2026-02-05 | [Engineer the Harness](https://mitchellh.com/writing/my-ai-adoption-journey) | repository instructions, programmed tools, and feedback that prevent repeated errors |
| 2026-02-11 | [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/) | agent-legible repositories, structured knowledge, mechanical constraints, and long feedback loops |
| 2026-03-03 | [Beyond the Diff](https://arxiv.org/abs/2604.16323) submitted | drift between agent actions and architectural intent |
| 2026-03-23 | [From Technical Debt to Cognitive and Intent Debt](https://arxiv.org/abs/2603.22106) submitted | externalized rationale, goals, and constraints as a software-health asset |
| 2026-06-07 | [Loop Engineering](https://addyosmani.com/blog/loop-engineering/) | systems that repeatedly prompt, allocate, check, and continue agent work |
| 2026-07-13 | [CodeSpeak: Structured Approach to Specs](https://codespeak.dev/blog/spindle-20260713) | atomic structured requirements, intent evolution, and planned intent diffs/coverage |
| 2026-07-22 | [3 Years of Graph Engineering with LangGraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph) | explicit nodes, edges, state, and constrained paths |
| 2026-07-31 | [From Code Review to Code Critique](https://arxiv.org/abs/2607.29516) submitted | intent prediction, drift detection, and review prioritization |
| 2026-08-07 | [Towards Assurance Closure](https://arxiv.org/abs/2608.07317) submitted | evidence credibility, uncertainty, and bounded agent authority |
| 2026-08-21 | Initial snapshot of this repository | intent lifecycle: capture, representation, propagation, enforcement, verification, evolution |

## Interpretation

The labels track a widening control surface:

```text
prompt → context → system/flow → harness → loop → graph
                                  │
                                  └─ durable intent and assurance cut across all of them
```

Intent is not only a layer after graph topology. It supplies goals, constraints, and decision criteria to prompts, contexts, harnesses, loops, and graphs. Assurance checks whether those mechanisms produced sufficient evidence.
