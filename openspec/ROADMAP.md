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

### profile-readme
Depends: —
Read: `~/projects/freelance_leads/cv/cv-en.md`, `~/projects/freelance_leads/cv/ai-experience.md`
Goal: страница профиля github.com/axinvd за десять секунд говорит, кто это и куда смотреть: AI product + фронтенд-инженер, сайт-резюме, живые проекты.
Scope: `README.md` профиля, собранный когда-то генератором (danielcranney/readme-generator): гифка, «a kind person», ссылка на Google Doc как портфолио, иконки навыков, которых в работе нет (Swift, Rust, Kotlin, Bootstrap…), соцсети с устаревшими (CodePen, CodeSandbox, Facebook, Instagram), сторонние счётчики (github-readme-stats на vercel, streak на herokuapp — падают). Новый — короткий: строка позиционирования, 3–5 пунктов о работе с цифрами из `cv/ai-experience.md`, стек текстом, ссылки на сайт `https://axinvd.github.io`, caro.md, infodreamhome.com, LinkedIn и почту; без сторонних счётчиков и картинок с чужих доменов. По-английски. Закреплённые репозитории профиля (pinned) меняет владелец руками — шаг предлагает какие.
Out: сайт-резюме (`cv-site`, соседний репо `axinvd.github.io`).
Done when: README профиля отрисован на github.com/axinvd без битых картинок, в светлой и тёмной теме, на телефоне (390); ссылка на сайт ведёт на `https://axinvd.github.io`.
Decide: —

## Follow-ups

- CV files say «contributed a fix» for react/react-native#39893, which GitHub shows as closed but facebook-github-bot merged into facebook/react-native@265af222: write «merged fix» in `cv/cv-en.md` and `cv/ai-experience.md` §1 — from profile-readme — repo `freelance_leads` (`~/projects/freelance_leads/cv/`).
- Pinned repositories of the profile are changed by the owner by hand: `axinvd.github.io`, `recall`, the `react-native` fork, `icomoon-helper`, `react-native-scrollview-maintain`; the README names tg-flow, fathom and the harness (private) without links, and making tg-flow public and pinning it is the owner's option — from profile-readme (PR #1, «Waiting for you»).

## Candidates (user decides)
