# Ivan Alexandrov

I'm an AI product & frontend engineer. I build web products in React and Next.js for clients, and
my own agent tooling for Claude Code. I work remotely from Chișinău, Moldova.

### Things I've built

- **An agent harness** (private): how I ship software with Claude Code. Each roadmap step gets an
  orchestrator that leads an architect, a tester, an implementer, a designer and a fresh verifier.
  No agent checks its own work: the tester writes tests from the spec without seeing the code, and
  nothing merges until I approve it on GitHub.
- **tg-flow** (private): lets my studio work with those agents from a Telegram chat. The chat agent
  has no shell, only a few allowed tools; it files a request as a step through an MCP server I wrote,
  and it is tested against prompt injection on the live model.
- **A lead-research tool** (private): ranks the job posts that reach me and finds the real vacancy
  behind a thin post. The model only reads: it copies facts as written and points at pages, and code
  fetches the pages and computes the score, so the same post always scores the same.
- **fathom** (private, in progress): personal finance and bill splitting, built solo with agents.
  Balances are computed from the ledger on every read, never stored, so they cannot drift; a receipt
  photo goes to a model, and its answer is validated like untrusted input.
- **[caro.md](https://caro.md)**: imports cars to Moldova from Korea, China and the US; I'm the main
  developer of the Next.js app. Its Korean catalog is read live from the source marketplace through
  rotating proxies, with a cached copy when the source goes down.

- **[infodreamhome.com](https://infodreamhome.com)**: the site of a Las Vegas general contractor; I
  built most of it. Every page is prerendered and fast on a phone, and only a production build lets
  search engines in, so a forgotten setting hides a test copy instead of exposing it.
### In the open

- **[recall](https://github.com/axinvd/recall)**: memory for Claude Code kept as plain markdown
  files in your repo. You can read it, edit it and diff it in git. It needs no embeddings, no API
  key and no background service.
- Fixes merged upstream: Android border colors in
  [React Native core](https://github.com/react/react-native/pull/39893), Android 14 support in
  [react-native-navigation](https://github.com/wix/react-native-navigation/pull/7801), and a stuck
  swipe animation in
  [react-native-deck-swiper](https://github.com/webraptor/react-native-deck-swiper/pull/116).

Earlier, I led React Native teams and shipped consumer apps for KFC, Papa John's and a football club.

**Stack:** Claude Code, MCP, Python · TypeScript, React, Next.js, React Native · Node.js, NestJS,
PostgreSQL · Playwright

[Website](https://axinvd.github.io) · [axinvd@gmail.com](mailto:axinvd@gmail.com) ·
[LinkedIn](https://www.linkedin.com/in/axinvd)
