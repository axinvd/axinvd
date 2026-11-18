# Tasks

## Context

- `README.md` — the profile README, replaced whole.
- `openspec/changes/profile-readme/design.md` — the research paragraph and D1–D9: what goes in and
  what stays out.
- `~/projects/freelance_leads/cv/cv-en.md`, `linkedin.md`, `ai-experience.md` («Честно») — the
  stories and how not to overstate them.
- No specs (`skip_specs: true`), no ADRs in force, no tests.

## 1. README

- [x] 1.1 Rewrite `README.md` per design D1–D9. Verify: `grep -cE '<img|!\[|vercel\.app|herokuapp' README.md`
  on the original tree printed `12`, expected `0`; `grep -cE '[0-9]{2,}' README.md` (counts that go
  stale) expected `0` outside link URLs; `grep -c 'https://axinvd.github.io' README.md` expected `1`;
  `git diff --check` exit 0.
- [x] 1.2 Check every link answers: `curl -sL -o /dev/null -w '%{http_code}'` on axinvd.github.io,
  caro.md, infodreamhome.com, `recall` and the three upstream PRs — 200 each on 2026-11-18 (LinkedIn
  999 is its bot wall).
- [x] 1.3 Render check on GitHub after the push: the branch's README at 1280 and 390 px, light and
  dark (`colorScheme`), screenshots opened; no image, no horizontal scroll at 390, the site link goes
  to `https://axinvd.github.io`.
