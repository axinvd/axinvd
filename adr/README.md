# Architecture Decision Records

A record here is a durable decision: it commits the project long term (a pattern, a
technology, a boundary, a contract), affects changes beyond the one that made it, and has a
real trade-off. A tactical detail is not a record; when nothing meets the bar, none is written.

## In force

A record is in force while no later record's Status says `supersedes` it; a record superseded
for one clause stays in force for the rest. Only in-force records constrain a design; superseded
ones are history.

## Immutable

An accepted record is never edited — not its status, body or date. Revising a decision is a
new record whose Status says `accepted, supersedes ADR-NNNN` and whose Context says why the
old decision is revisited. A revision of one clause says `accepted, supersedes ADR-NNNN for
<the clause>` and leaves the rest of the old record in force. A design that needs to revisit a
record says so under Open Questions.

## File

`adr/NNNN-kebab-title.md`; `NNNN` is one above the highest number in use, never reused.

```
# ADR-NNNN: <Decision as a sentence>

- Status: accepted | accepted, supersedes ADR-NNNN | accepted, supersedes ADR-NNNN for <clause>
- Date: YYYY-MM-DD
- Source: change `<change>` (design D<n>)

## Context
<Why the decision was needed; for a revision, why the old one no longer holds.>

## Decision
<What is decided.>

## Consequences
<What follows, good and bad.>
```
