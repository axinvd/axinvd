# Tasks

## Context

- `README.md` — the profile README, replaced whole.
- `openspec/changes/profile-readme/design.md` — D1–D6: what goes in and what stays out.
- `~/projects/freelance_leads/cv/ai-experience.md` §1–3, §6 and «Честно» — the only source of numbers.
- No specs (`skip_specs: true`), no ADRs in force, no tests.

## 1. README

- [x] 1.1 Rewrite `README.md` per design D1–D6. Verify: `grep -cE '<img|!\[|vercel\.app|herokuapp' README.md`
  today prints `12`, expected `0`; `grep -c 'https://axinvd.github.io' README.md` today `0`,
  expected `1`; `git diff --check` today exit 0, expected exit 0.
- [x] 1.2 Check every link answers: `curl -sL -o /dev/null -w '%{http_code}'` on axinvd.github.io,
  caro.md, infodreamhome.com, the React Native PR — today 200 each (LinkedIn 999 is its bot wall).
- [x] 1.3 Render check on GitHub after the push: the branch's README at 1280 and 390 px, light and
  dark (`colorScheme`), screenshots opened; no broken image, the site link goes to
  `https://axinvd.github.io`.
