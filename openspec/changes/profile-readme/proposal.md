# Proposal

## Why

The profile page github.com/axinvd shows a README built years ago by a generator: a gif, "a kind
person", a Google Doc as the portfolio, skill icons for languages not in the work (Swift, Rust,
Kotlin), stale socials and two third-party stat cards whose hosts fail. A visitor cannot tell in ten
seconds who this is and where to look; the owner now presents himself as an AI product & frontend
engineer, and the CV site `https://axinvd.github.io` carries that title.

## What Changes

- `README.md` is rewritten in English and short: a name, one positioning line (AI product &
  frontend engineer), five bullets about the work with numbers taken only from
  `~/projects/freelance_leads/cv/ai-experience.md`, the stack as text, and links to the CV site,
  caro.md, infodreamhome.com, LinkedIn and the email.
- Removed: the gif, the Google Doc portfolio link, all skill and social icons (images from
  raw.githubusercontent.com of a foreign repo), the socials CodePen, CodeSandbox, Facebook,
  Instagram, X, and the github-readme-stats / streak cards.
- No images at all: nothing on the page loads from another domain.
- Pinned repositories are changed by the owner by hand; the step proposes which in the pull request.

## Capabilities

### New Capabilities

None: a profile README is content, not behaviour (`skip_specs: true`).

### Modified Capabilities

None.

## Impact

`README.md` only. No code, no dependencies. The profile page renders the new README after the merge
into `main`.
