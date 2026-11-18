# Design

## Context

See proposal.md - Why. The README is plain GitHub-flavoured Markdown; GitHub renders it on the
profile page with its own styles in light and dark theme, so a README without images and without
HTML layout cannot break by theme or width. The stories come from `~/projects/freelance_leads/cv/`
(`cv-en.md`, `linkedin.md`, `ai-experience.md` and its «Честно» section on how not to overstate).

The first draft (bullets of per-project commit, PR, line and test counts) was returned by the owner:
the counts go stale and nobody syncs them, nobody cares how many commits he made, the private
projects should say what is interesting about them, and the archived repos are not current work.

Research (2026-11-18). Real profiles of engineers known for AI and product work keep to a voice
and a few sentences, not widgets: Hamel Husain opens «Hi, I'm Hamel», says what he does and a
«What I'm working on» paragraph; Jason Liu says the role, the one project and why it mattered
(«OpenAI cited it as inspiration»), then «Previously»; Simon Willison is one «Currently working
on» line plus generated lists; Karpathy is one sentence. A recruiter-facing guide (techinterview.org)
gives the same shape: a 2–3 sentence intro, a short project list with context, an optional stack
line; no gifs, counters or long technology lists; pin fewer, stronger repos («3 polished beat 6
mixed»), substantive forks are fine, trivial ones are not. What makes them not boring is the voice
and the «what it is / what I did / why it is interesting» of each project, not numbers. The shape
chosen: first-person intro, «Things I've built» as one story per project, «In the open» for the
public work, one line on the earlier career, stack, links. A «Now» section is left out: it needs
upkeep, which the owner ruled out. Sources:
https://raw.githubusercontent.com/hamelsmu/hamelsmu/HEAD/README.md,
https://raw.githubusercontent.com/jxnl/jxnl/HEAD/README.md,
https://raw.githubusercontent.com/simonw/simonw/HEAD/README.md,
https://raw.githubusercontent.com/karpathy/karpathy/HEAD/README.md,
https://www.techinterview.org/post/3233474626/github-profile-engineers/,
https://app.unilink.us/blog/github-readme-templates-2026 (widget stacking reads as noise).

## Goals / Non-Goals

**Goals:** a visitor reads who this is, what he built and why it is interesting, and where to go
next, in about thirty seconds; nothing on the page needs updating as time passes.

**Non-Goals:** the CV site (`cv-site`, repo `axinvd.github.io`); pinning repositories (the owner's
hands); any badge, counter or image.

## Decisions

- D1. Plain Markdown, no images, no HTML. Ground: the step forbids third-party counters and images
  from foreign domains; with no images there is nothing to break in dark theme or at 390 px.
- D2. Positioning «AI product & frontend engineer», the CV site's title. Ground: step Goal.
- D3. No figure that rots: no commit, PR, line, test, page or year counts, no catalog size. Durable
  facts stay as words («I built most of it», «main developer»). Ground: the owner's remark.
- D4. Each project is a story of what it is, what he did and what is interesting: caro.md (live
  catalog through proxies with a cached fallback, the turnkey price calculator), infodreamhome.com
  (prerendered, fast on a phone, quote form, structured data), the harness (orchestrator and roles,
  tests written blind from the spec, merge only on his Approve), tg-flow (a team works with the
  agents from Telegram through his MCP server, a checker agent, its own GitHub App identity,
  prompt-injection tests), fathom (balances to zero, model output validated as untrusted). Wording
  keeps to «Честно»: the harness and tools are «my own», fathom is «in progress», nothing is
  «sandboxed».
- D5. Private repos are named without links. Ground: a link would 404 for a visitor.
- D6. Open source is told as what each piece does: `recall`, and the three upstream fixes linked to
  their merged PRs — React Native core #39893 (the PR reads «closed»; facebook-github-bot: «merged
  this pull request in facebook/react-native@265af22»), wix/react-native-navigation #7801 (Android
  14 support, merged 2023-11-06), webraptor/react-native-deck-swiper #116 (merged 2023-08-30).
  Checked 2026-11-18 via the GitHub API.
- D7. Archived repos (`icomoon-helper`, `react-native-scrollview-maintain`, `icomoon-cli`) are not on
  the page and not proposed for pinning.
- D8. Pinned repositories proposed from public, non-archived repos (`gh repo list axinvd`): the CV
  site, `recall`, and the `react-native` and `react-native-navigation` forks that hold the merged
  fixes; `react-native-deck-swiper` as an optional fifth. Left out: `figma-api` and
  `fastlane-plugin-file_manager` (no merged upstream work found), `test`, the profile repo. The
  profile shows «Popular repositories» today, so no pins are set.
- D9. Links: site, caro.md, infodreamhome.com, LinkedIn, email — the step's list. Phone and Telegram
  are left out (the CV site and LinkedIn carry them).

## Decided without the user

- Shape of the page — default: first-person intro, project stories, «In the open», one career line,
  stack, links; no «Now» section; ground: the research above and the owner's remark.
- No numbers that go stale — default: none on the page; ground: the owner's remark.
- What is told about each project — default: D4; ground: `cv-en.md`, `linkedin.md`,
  `ai-experience.md` and its «Честно» section.
- Upstream fixes called «merged» and linked — default: D6; ground: the merge state of each PR.
- Pinned repositories proposal — default: D8; ground: the public, non-archived repo list.
- Phone and Telegram not on the profile — default: left out; ground: the step's link list.

## Risks / Trade-offs

- [A story can still go stale — fathom «in progress», tg-flow private] → they are statements of
  state the owner would change anyway when the project changes; no figure needs a sync.
- [LinkedIn answers 999 to curl] → it is LinkedIn's bot wall; the URL is the one in `cv-en.md` and
  the old README.

## ADR

none
