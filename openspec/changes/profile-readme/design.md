# Design

## Context

See proposal.md - Why. The README is plain GitHub-flavoured Markdown; GitHub renders it on the
profile page with its own styles in light and dark theme, so a README without images and without
HTML layout cannot break by theme or width. Facts come from `~/projects/freelance_leads/cv/`:
numbers only from `ai-experience.md` (its section «Честно» says how not to overstate them), wording
of roles from `cv-en.md`.

## Goals / Non-Goals

**Goals:** a visitor reads who this is, what he shipped and where to go next in one screen.

**Non-Goals:** the CV site (`cv-site`, repo `axinvd.github.io`); pinning repositories (the owner's
hands); any badge, counter or image.

## Decisions

- D1. Plain Markdown, no images, no HTML. Ground: the step forbids third-party counters and images
  from foreign domains; with no images there is nothing to break in dark theme or at 390 px.
- D2. Positioning line «AI product & frontend engineer», the same words as the CV site's title
  (`axinvd.github.io` description). Ground: step Goal; one title across profile and site.
- D3. Five bullets, numbers from `ai-experience.md` only: caro.md commits and merged PRs (§1),
  infodreamhome.com commits (§1), the harness and its 121 steps, called «my own» (§2, «Честно»),
  tg-flow's MCP server, lines and tests (§3, §6), 8+ years and teams up to 5 (§1). Not taken: the
  dreamHome 73 → 96 score (two different tools, §5 caveat), the $ cost figures (not comparable,
  «Честно»), GraphQL and LangGraph (no fact).
- D4. The React Native core fix is called «merged» and linked: the PR shows «closed», but
  facebook-github-bot wrote «@javache merged this pull request in facebook/react-native@265af22»
  (checked 2026-11-18 via the GitHub API).
- D5. Private repos (tg-flow, the harness in ~/.claude, fathom) are named without links: a link
  would 404 for a visitor.
- D6. Links: site, caro.md, infodreamhome.com, LinkedIn, email — the step's list. Phone and Telegram
  are left out (not in the list; the CV site and LinkedIn carry them).
- D7. Pinned repositories proposed from the public list (`gh repo list axinvd`): the CV site,
  `recall`, the `react-native` fork that carries the merged fix, `icomoon-helper`,
  `react-native-scrollview-maintain`. Ground: they are the owner's own public work; forks without
  his commits and `test` are left out.

## Decided without the user

- Positioning wording «AI product & frontend engineer» — default: the CV site's title; ground: step
  Goal and the site's repo description.
- Which five facts go in the bullets — default: D3; ground: `ai-experience.md` §1–3, §6 and its
  «Честно» section.
- React Native fix called «merged» — default: yes, with the PR link; ground: the bot's merge comment
  on PR 39893.
- Phone and Telegram not on the profile — default: left out; ground: the step's link list.
- Pinned repositories proposal — default: D7; ground: the public repo list.

## Risks / Trade-offs

- [Numbers age: commit counts are a 2026-11-12 cut] → they are stated as counts, not «latest»; a
  later CV refresh updates both files.
- [LinkedIn answers 999 to curl] → it is LinkedIn's bot wall; the URL is the one in `cv-en.md` and
  the old README.

## ADR

none
