# Ivan Alexandrov

I'm an AI product & frontend engineer. I build web products in React and Next.js for clients, and
I build the agent tooling I make them with. I work remotely from Chișinău, Moldova.

### Things I've built

- **[caro.md](https://caro.md)**: imports cars to Moldova from Korea, China and the US. I'm the
  main developer of the Next.js app. Its Korean catalog is read live from the source marketplace
  through rotating proxies, with a cached copy when the source goes down. A calculator turns a car
  on another continent into a turnkey price: auction fees, shipping, Moldovan customs and today's
  exchange rates.
- **[infodreamhome.com](https://infodreamhome.com)**: the site of a Las Vegas general contractor.
  I built most of it. Every page is prerendered and fast on a phone, quote requests land in the
  owner's inbox, and search engines get structured data about the business.
- **An agent harness** (private): how I ship software with Claude Code. Each roadmap step gets
  its own orchestrator, which leads an architect, a tester, an implementer, a designer and a fresh
  verifier. The tester writes tests from the spec without seeing the code, and nothing merges
  until I approve it on GitHub.
- **tg-flow** (private): lets my studio work with those agents from a Telegram chat. A request
  becomes a roadmap step through an MCP server I wrote, and a second agent checks the step before
  it lands. The bot acts on GitHub as its own app, never as me. It is tested against prompt
  injection on the live model.
- **fathom** (private, in progress): personal finance and bill splitting, built solo with agents.
  Every split must balance to zero, and receipt scans read by a model are validated like
  untrusted input.

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
