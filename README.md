# Ivan Alexandrov

I'm an AI product & frontend engineer. I build web products in React and Next.js for clients, and
my own agent tooling for Claude Code. I work remotely from Chișinău, Moldova.

### Things I've built

- **[caro.md](https://caro.md)**: imports cars to Moldova from Korea, China and the US. I'm the
  main developer of the Next.js app. Its Korean catalog is read live from the source marketplace
  through rotating proxies, with a cached copy when the source goes down. A calculator turns a car
  on another continent into a turnkey price: auction fees, shipping, Moldovan customs and today's
  exchange rates.
- **[infodreamhome.com](https://infodreamhome.com)**: the site of a Las Vegas general contractor.
  I built most of it. Every page is prerendered and fast on a phone, quote requests land in the
  owner's inbox, and search engines get structured data about the business. Only a production
  build lets search engines in, so a forgotten setting hides a test copy instead of exposing it.
- **An agent harness** (private): how I ship software with Claude Code. Each roadmap step gets
  its own orchestrator, which leads an architect, a tester, an implementer, a designer and a fresh
  verifier, each in a context of its own. No agent checks its own work: the tester writes tests
  from the spec without seeing the code, and the verifier runs commands instead of reading the
  builder's report. My answers go back to the agent that asked, and nothing merges until I approve
  it on GitHub.
- **tg-flow** (private): lets my studio work with those agents from a Telegram chat. The chat
  agent has no shell, only the tools of an MCP server I wrote, and a request becomes a step only
  after a second agent checks it. It reads pages people send, so it reaches only its project and
  is tested against prompt injection on the live model. On GitHub the bot acts as its own app, so
  I can approve its work, and it never falls back to my account.
- **fathom** (private, in progress): personal finance and bill splitting, built solo with agents.
  Every split must balance to zero, and balances are computed from the ledger on every read, never
  stored, so they cannot drift. A fiscal receipt's QR code is parsed by code; only a photo goes to a
  model, and its answer is validated like untrusted input.
- **A lead-research tool** (private): ranks the freelance leads and job posts that reach me and
  finds the real vacancy behind a thin post. The model only reads: it copies facts as written and
  points at pages, and code fetches the pages and computes the score, so the same post always
  scores the same. I chose the model by measuring candidates against answers I checked by hand.

### In the open

- **[recall](https://github.com/axinvd/recall)**: memory for Claude Code kept as plain markdown
  files in your repo. You can read it, edit it and diff it in git. It needs no embeddings, no API
  key and no background service.
- Fixes merged upstream: Android border colors in
  [React Native core](https://github.com/react/react-native/pull/39893), Android 14 support in
  [react-native-navigation](https://github.com/wix/react-native-navigation/pull/7801), and a stuck
  swipe animation in
  [react-native-deck-swiper](https://github.com/webraptor/react-native-deck-swiper/pull/116).

Before going freelance, I led React Native teams and shipped consumer apps for KFC, Papa John's and a
football club.

**Stack:** TypeScript, React, Next.js, React Native · Node.js, NestJS, PostgreSQL · Playwright ·
Python · Claude Code

[Website](https://axinvd.github.io) · [LinkedIn](https://www.linkedin.com/in/axinvd) ·
[axinvd@gmail.com](mailto:axinvd@gmail.com)
