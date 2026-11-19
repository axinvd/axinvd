# Proposal

## Why

The profile README (change `profile-readme`) was written before `~/projects/freelance_leads/cv/ai-experience.md`
was rewritten as v2, records of approaches («principle → task → approach → why → what broke»). Two
README lines now say more than v2 allows, and several of v2's strongest approaches, the ones that
show how the owner works with models, are not on the profile.

## What Changes

- Two corrections against v2. The intro says the client products are made with the agent tooling,
  but v2 «Limits» says caro.md and infodreamhome.com were built before the harness existed. tg-flow
  says the bot acts on GitHub «never as me», but v2 R4.2 says that holds only where its GitHub App is
  installed: there a failed App token is a refusal, never a fallback to the owner.
- Approaches added from v2, one sentence each, inside the existing bullets: infodreamhome.com keeps
  search engines out unless the build is production (R1.3); the harness keeps every agent from
  checking its own work and sends an answer back to the agent that asked (R2.1, Q3.3, R2.2); tg-flow's
  chat agent has no shell, only a few allowed tools, writes steps through his MCP server, and
  reaches only its project
  (R3.1, R4.4); fathom derives balances on every read and parses fiscal receipts by code (R1.1, Q2.3).
- One new bullet: the private lead-research tool, where the model only reads and points and code
  computes, and its model was chosen by measuring against hand-checked answers (Q2.1, Q2.2, Q4.1, R7.2).
- Same shape as before: «Things I've built», «In the open», career line, stack, links; no figures, no
  images.

## Capabilities

### New Capabilities

None. A profile README is content, not behaviour (`skip_specs: true`).

### Modified Capabilities

None.

## Impact

`README.md` only. The profile page shows the new text after the merge into `main`. The
reconciliation list («added / not taken, and why») goes into the pull request body (design.md,
«Reconciliation»).
