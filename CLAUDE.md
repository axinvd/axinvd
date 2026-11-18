# axinvd

README профиля GitHub (`https://github.com/axinvd`): репо с именем аккаунта, GitHub показывает его
`README.md` на странице профиля. Сайт-резюме — соседний репо `~/projects/axinvd.github.io`; факты —
`~/projects/freelance_leads/cv/`.

Полная проверка — `git diff --check`. `setup` — ничего. `RUN_SLOT` ничего не меняет. Превью PR —
отрисовка README на странице PR в GitHub.

<!-- openspec-kit -->
## OpenSpec

- `openspec/ROADMAP.md` — todo of future changes; its header holds the step format and how
  to take a step. A session with no named task starts here.
- `openspec/specs/` — what the system does now; `openspec/changes/archive/` — each change's
  proposal and design, the why behind the specs.
- `adr/` — durable decisions in force; format and rules in `adr/README.md`.
- `docs/research/` — research and the decisions it led to, when the project keeps it.
- Step chain: a session explores (`/opsx:explore`) and writes steps into the roadmap; each
  step is built by `roadmap-run`: the step's orchestrator, a session of its own, leads the
  step's roles as its subagents from the first exploring to the merge of its pull request.
  Work the user takes now is a step too, built by a run of that one step; the session does not
  run `/opsx:propose` for a step. A session's explore ends in roadmap steps (the rule is in
  `openspec/config.yaml`).
- A step that comes back with variants (one draft PR of the step, its preview switches them
  by `?variant=<letter>`): the user chooses a variant, and the choice is written into the
  step (`Decide: —`, the answer with its letter at the end of `Scope:`) by the chat agent
  from the topic or by the session; the step's orchestrator keeps the chosen variant in the
  step's branch and has the others removed in a commit of it, then the step goes on in the
  same PR as any step with screens (contract tests, apply, publication as a draft PR,
  review, persona pass, verifier). The session does not build it.
- A step the run ended with a PR: its orchestrator keeps the step until the merge. The PR
  opens as a draft and is marked ready for review only after the verifier's ok. The
  consent is an Approve in GitHub: the owner's in his own repos, two different people's of
  the team in shared ones; a word in the chat or a comment in the PR is not consent. Then a
  role of the step archives the change in the step's branch and pushes, and the step's
  orchestrator merges the pull request into the work branch itself; after the consent nobody
  does anything.
- Approval: an Approve in GitHub as is, or at once a text of what the user disagrees with
  (a remark, a review requesting changes); that text goes back to the step's role that built
  it, as a fix within the same change, and the approval is asked again after it. There is no
  separate reject.
- Each link is its own skill call or agent; `/opsx:verify` is a manual command, not a
  link. Between links, propose the next one in one line and wait.
<!-- /openspec-kit -->
