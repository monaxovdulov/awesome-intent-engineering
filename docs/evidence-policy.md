# Evidence Policy

The repository is designed to survive rapid terminology changes. Entries are accepted based on inspectable mechanisms and primary sources.

## Source priority

1. official project documentation or repository;
2. original paper or preprint;
3. original author announcement or design note;
4. independent technical analysis;
5. secondary reporting only when no primary source is available.

More than one source may be required when an entry combines product status, technical mechanism, and historical claims.

## Required evidence for a resource

Each item in `data/resources.yml` must include:

- a stable `id`;
- canonical `url`;
- category and lifecycle tags;
- a neutral description of an inspectable mechanism;
- availability and maturity;
- at least one primary-source evidence link;
- `last_verified` in `YYYY-MM-DD` form;
- a limitation or boundary when a reader could otherwise overgeneralize the claim.

## Shipped, planned, and inferred capabilities

Descriptions must distinguish:

- **shipped** — available in a released product or repository;
- **demonstrated** — publicly shown with enough detail to inspect;
- **planned** — listed on a roadmap or announcement;
- **inferred** — interpretation by this repository’s maintainers.

A planned feature cannot be written as a current capability.

## Authorship and provenance

When a system derives intent with a model, the entry should state whether the resulting artifact is:

- human-authored;
- human-approved;
- model-derived;
- agent-observed;
- system-inferred;
- runtime evidence.

A model-derived requirement can be useful. It should not be represented as a human decision without approval evidence.

## Historical claims

Use “prominent public signal” unless a source is sufficient to establish first use. Coinage claims require a dated primary source and a search for earlier use.

## Product claims

Metrics, customer results, security statements, and roadmap items reported by a vendor must be attributed to that vendor. The catalog does not independently validate them unless it links to an external audit or study.

## Freshness

- active products: review at least every 90 days;
- fast-moving roadmap entries: review at least every 30 days;
- papers and archived artifacts: review when a revision or contradiction appears.

A stale item is not automatically removed. Its verification date and status should make staleness visible.

## Removal criteria

An entry may be removed when:

- the canonical source disappears and no archive remains;
- the description cannot be supported by the cited source;
- the resource is a duplicate wrapper without a distinct mechanism;
- the project is generic agent infrastructure with no concrete intent surface;
- repeated promotional submissions provide no inspectable artifact.
