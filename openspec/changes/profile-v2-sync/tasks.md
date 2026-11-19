# Tasks

## Context

- `README.md`: the profile README. Its bullets are edited and one bullet is added.
- `openspec/changes/profile-v2-sync/design.md`: D1–D8 say what changes, what is not taken and why.
- `~/projects/freelance_leads/cv/ai-experience.md`: v2. Read the records D1–D6 cite and «Limits».
- `openspec/changes/archive/2026-11-18-profile-readme/design.md`: D1, D3 and D5 are the rules of the page.
- No specs (`skip_specs: true`), no ADRs in force, no tests.

## 1. README

- [x] 1.1 Edit `README.md` per D1–D6. Verify: `grep -c 'agent tooling I make them with' README.md`
  and `grep -c 'never as me' README.md` printed `1` and `1` on today's tree, expected `0` and `0`;
  `grep -c 'lead-research tool' README.md` expected `1`; `grep -cE '<img|!\[' README.md` printed `0`,
  expected `0`; `grep -nE '[0-9]{2,}' README.md | grep -v http` printed nothing, expected nothing;
  `git diff --check` exit 0 today, expected exit 0.
- [x] 1.2 Every link answers: `curl -sL -o /dev/null -w '%{http_code}'` on each URL of README.md. On
  2026-11-19, axinvd.github.io, caro.md, infodreamhome.com, recall and the three upstream PRs gave 200
  each, and LinkedIn gave 999 (its bot wall). Expected the same after the edit, since no link changes.
- [x] 1.3 Render check on GitHub after the push: the branch's README at 1280 and 390 px, light and
  dark, screenshots opened. Expected: no image, no horizontal scroll at 390, the links clickable.

## Workflow follow-up

- The PR body carries «Сверка с v2» (design.md, Reconciliation).
- Archive after the owner's Approve, in the step's branch (roadmap-run).
