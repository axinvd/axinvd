# Roadmap

The todo list of future OpenSpec changes: each step is the input of a later run. A step is `### <change>` — the name of the change it will become — then one field
per line: `Depends:` (change names or —; a step needs another's code or decision, including
writing into an entity or feed it creates; `<change>@<repo>` for a step of another roadmap —
`<repo>` is a folder of `~/projects`, `.claude` is `~/.claude` — done when archived there), `Read:` (only what an agent would not find in
openspec/specs/ or adr/), `Goal:` (one sentence), `Scope:` (what is included; the model and
rules are decided by the step's explore), `Out:`, `Done when:`, `Decide:` (the user's
decisions the step leaves open — no ground in specs, ADRs or research, not technical —
written as cases, or `—` when there are none), `Hands:` (what only the owner can do: a key,
an account, a purchase), `Waits:` (an external event that is not a step of any roadmap, e.g. a
request; both optional, `—` or absent when none), optionally `Effort:` (the
architect's effort: `xhigh` for a step that opens a new capability or carried a
`Decide:`, `high` without the field; the owner may set any). About eight lines per step.
A mechanical step has `Decide: —` and no `Hands:` or `Waits:` (a step without `Decide:` is not
one). A step lives in the roadmap of the repo whose code it changes; a step that creates a repo
lives in `~/.claude` until the repo exists, then moves there.
A step is for work that waits — later in this session or in another one: session findings
to keep, a task large enough for its own explore. Every piece of work is a step: work that
waits stays here, and work the user takes now is a step too, built by a run of that one step
(`roadmap-run` with `only`); a session explores and writes steps and builds none itself. The step
is all its later reader gets: what the session found is written first into the doc that
owns the topic (a new file under `docs/research/` only when none does) and `Read:` names
that file.
State lives in OpenSpec: an active change of that name — in progress; archived — done, and
the block is deleted. What is free: `python3 openspec/roadmap-ready.py`; only the free
mechanical steps (defined above): `--mechanical`. Taking a step is a `roadmap-run`: of the
step the user names, or of every free mechanical step after its «Before the run» has shown the
blockers by what they unblock.

## Steps

### profile-v2-sync
Depends: —
Read: `~/projects/freelance_leads/cv/ai-experience.md` (v2 — подходы); README.md
Goal: README профиля сходится с ресёрчем подходов v2 — сильное не упущено, ничего не противоречит.
Scope: сверить пункты README («Things I've built», «In the open») с записями v2; добавить то, что сильнее нынешних формулировок, поправить расхождения; подача прежняя — подходы, без счётчиков активности, коротко. Список «добавлено / не взято и почему» — в PR.
Out: сайт (`axinvd.github.io`), закреплённые репозитории (владелец закрепил).
Done when: в PR список сверки с v2; README отрисован на github.com/axinvd без битых ссылок, в светлой и тёмной теме, на телефоне (390).
Decide: —


## Follow-ups

- The CV files name one upstream contribution as «contributed a fix»; the owner has three merged: react/react-native#39893 (GitHub shows it closed, facebook-github-bot merged it in facebook/react-native@265af222), wix/react-native-navigation#7801 (Android 14), webraptor/react-native-deck-swiper#116. Say «merged» and name all three in `cv/cv-en.md`, `cv/linkedin.md`, `cv/ai-experience.md` §1 — from profile-readme — repo `freelance_leads` (`~/projects/freelance_leads/cv/`).
- Pinned repositories of the profile are set by the owner by hand: `axinvd.github.io`, `recall`, the `react-native` fork, the `react-native-navigation` fork (optional fifth: `react-native-deck-swiper`); `icomoon-helper`, `react-native-scrollview-maintain`, `icomoon-cli` are archived and stay out; making private tg-flow public and pinning it is the owner's option — from profile-readme (PR #1, «Waiting for you»).
- The profile README keeps no counts that need upkeep (commits, PRs, lines, tests); the `cv-site` step should follow the same rule on the site — from profile-readme — repo `axinvd.github.io`.
- «Tests, CI and error monitoring behind the code» in `cv/cv-en.md` (line 14) and `cv/linkedin.md` (lines 37, 47) may not hold for fathom: v2 R1.2 says «no CI yet»; the `cv-ai-refresh` step there should check the line against v2 — from profile-v2-sync — repo `freelance_leads` (`~/projects/freelance_leads/cv/`).
- The profile README states approaches, no measurements; the measured figures live on the CV site («What I measured»); a later profile edit keeps that split — from profile-v2-sync (design D7).

## Candidates (user decides)
