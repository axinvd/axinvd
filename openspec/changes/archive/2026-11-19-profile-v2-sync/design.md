# Design

## Context

See proposal.md, Why. The README's shape and rules come from the archived change `profile-readme`
(`openspec/changes/archive/2026-11-18-profile-readme/design.md`): plain Markdown with no images (D1),
no figure that rots (D3), one story per project (D4), private repos named without links (D5). v2 is
`~/projects/freelance_leads/cv/ai-experience.md`, a 2026-11-18 snapshot. Its «Limits» section is the
guard on wording, as «Честно» was for the first README. The CV site (`axinvd.github.io`, cv-site
design D7) already shows the lead-ranking finding and says both client sites predate the harness.
Today's links all answer 200, and LinkedIn answers 999 (its bot wall, same as at profile-readme).

## Goals / Non-Goals

**Goals:** nothing on the profile contradicts v2. Each project carries its strongest approach from
v2, as a sentence about what the approach does and why. The page stays about as short as it is now.

**Non-Goals:** measurements and their numbers; the CV site; pinned repositories; the CV files in
`freelance_leads` (contradictions found there go to Findings).

## Decisions

- D1. Intro: «I build web products in React and Next.js for clients, and my own agent tooling for
  Claude Code». Ground: v2 «Limits» («production client sites … were built with Claude Code before
  the harness existed») and the CV site's p-note. The old «the agent tooling I make them with» says
  the client products are made with it.
- D2. infodreamhome.com gets one sentence on the safe default: only a production build lets search
  engines in, so a forgotten setting hides a test copy instead of exposing it. Ground: v2 R1.3, its
  principle and its «Broke» (the dev stand went live open to crawlers). The quote-form wording stays
  as it is; it agrees with R6.2.
- D3. Harness: «each in a context of its own», «no agent checks its own work» (the blind tester
  stays, plus the fresh verifier that checks by running commands), and «an answer goes back to the
  agent that asked instead of restarting the step». Ground: v2 R2.1, Q3.3, R2.2. The merge on my
  Approve stays (R8.2).
- D4. tg-flow: the chat agent has no shell, only a few allowed tools (R4.4: the four tools of my MCP
  server, WebSearch, WebFetch and a read-only researcher subagent), and it writes a request as a
  step through my MCP server only after a second agent's check passes (R3.1, R7.1). The GitHub line is
  corrected: «acts as its own app, so I can approve its work, and it never falls back to my account»,
  in v2's own words (R4.2: a failed App token «never falls back to the owner»; where the App is not
  installed it does run as the owner, so «never as me» overstated it). The prompt-injection line gets
  its reason and its guard: the chat agent reads pages people send, so it reaches only its project
  (R4.4, R7.1).
- D5. fathom: «balance to zero» stays. Added: balances and shares are computed from the ledger on
  every read and never stored, so no edit can make them drift (R1.1, where a stored balance did
  drift). The scan line: a receipt with a fiscal QR code is parsed by code, and only a photo goes to a
  model whose answer is validated like untrusted input (Q2.3, Q4.3).
- D6. New bullet, «A lead-research tool» (private): it ranks the freelance leads and job posts that
  reach me and finds the real vacancy behind a thin post. The model only reads and points: it copies
  facts and numbers as written and returns addresses. Code downloads the pages, converts pay and
  scores, so the same post always scores the same. Its model was chosen by measuring candidates
  against answers checked by hand. Ground: v2 Q4 calls the research agent the hardest AI product, the
  principle «model copies, code computes» (FL ADR 0001) is behind Q2.1, Q2.2, Q4.1 and R7.4, and the
  CV site already publishes the lead-ranking finding (cv-site D7, m3). Repo `freelance_leads` is
  private, so the bullet has no link (profile-readme D5).
- D7. No measurements on the profile. v2 numbers are measurements, not activity counts, so they don't
  rot, but the step asks for a short page, and profile-readme D3 keeps facts as words. The figures
  live on the CV site («What I measured») and in the interview kit. Ground: step Scope («коротко»),
  profile-readme D3.
- D8. Not taken, by length or by fit (each is listed in the PR's reconciliation): R1.2 generated API
  client, R1.4 second-user access tests, R6.1 database constraints, R3.4 personal token (fathom
  internals, a step below the project story); R2.3 design variants as blind forks, R2.4 parallel
  worktrees, R5.4 solo sizing, R8.1 reactions, R4.1/R8.2 consent details (harness internals; the
  bullet keeps the Approve); R3.2/R3.3 skills over APIs instead of MCP servers, Q1.4 trimmed agent,
  Q2.4 code graph against grep, R7.3 with/without-skill evals (measure-before-trust is carried by
  D6's model choice); R5.2 persona readers on the specs; R5.3 the bounty channel (a closed business
  trial, not a product); R6.2 quote form (already in the README in words); Q3.4 flaky ordering bug
  (a debugging story for an interview); R6/R9 «no entries» (GraphQL, LangGraph, spoken English): v2
  says there is no record behind them, and the README claims none.

## Reconciliation

Goes into the PR body as «Сверка с v2», under three headings: corrected, added, not taken and
why. It is D1–D8 in a reader's words.

## Decided without the user

- Intro reworded so client sites are not said to be built with the harness. Default: D1. Ground: v2
  «Limits», CV site p-note.
- «never as me» corrected to «never falls back to my account». Default: D4. Ground: v2 R4.2.
- Which v2 approach each project gets. Default: D2–D5, one or two sentences each. Ground: v2 records
  and their principles; step Scope.
- The lead-research tool added as a private project. Default: D6. Ground: v2 Q4, FL ADR 0001; the CV
  site already shows lead ranking publicly.
- No measurements on the profile. Default: D7. Ground: step Scope «коротко», profile-readme D3.
- What is not taken. Default: D8. Ground: length, and v2's own «no entries».

## Risks / Trade-offs

- [The page grows by one bullet and about five sentences, from 391 to 569 words by `wc -w`] → each
  project still holds one short paragraph, and the shape is unchanged; the owner can strike a
  sentence in review.
- [The lead-research tool names a job search on a public profile] → the CV site already shows lead
  ranking publicly, and the site says he is open to roles. If the owner objects, the bullet comes out
  as a fix in the same PR.
- [v2 is a snapshot of 2026-11-18] → the README states approaches, not states; nothing in it needs a
  sync when v2 grows.

## ADR

none
