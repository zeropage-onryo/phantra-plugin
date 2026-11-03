# Phantra AI

Phantra is an AI image and video studio. This plugin connects your AI assistant to your
Phantra account so you can create images, videos and product ads from a chat: start with an
idea, a script, reference media or a product photo.

- Generate images and video on the latest models. Ask which model suits the job.
- Turn product photos into short video ads: product shots, UGC-style reviews, unboxings,
  tutorials, try-ons and full ad sets, with a skill for each.
- Edit a still, animate it, add a camera move, upscale a clip or add sound.
- Keep characters, products and places consistent across shots by adding them once as elements.
- Finish in the chat: trim, reshape for vertical, square or widescreen, join clips and get a
  download link, free.

Every still, clip and effect is quoted in credits first and made only when you say yes.

You need a Phantra account (any plan, including the free trial): https://phantra.ai

## What's inside

- **MCP server:** `https://api.phantra.ai/mcp` (streamable HTTP, OAuth sign-in through Phantra;
  no API key to paste).
- **32 skills** in `skills/`: setup, scenes, storyboards, product ads, UGC ads, effects,
  delivery and more.

## Install

**Gemini CLI**

    gemini extensions install https://github.com/zeropage-onryo/phantra-plugin

Then run `/mcp auth phantra-ai` and sign in. Sign-in opens a browser, so it needs a desktop
session.

**Antigravity**

    agy plugin install https://github.com/zeropage-onryo/phantra-plugin

Then open `/mcp`, pick `phantra-ai_phantra`, choose Authenticate, sign in to Phantra in the
browser and paste the code Antigravity's page shows back into the CLI.

**Cursor**

Install Phantra AI from the Cursor Marketplace, or add the server yourself in
Settings → MCP: `https://api.phantra.ai/mcp`.

**OpenClaw (ClawHub)**

Search ClawHub (clawhub.ai) for "Phantra". Each skill is published as `phantra-ai-<skill>`.
Add the MCP server
`https://api.phantra.ai/mcp` to your OpenClaw config.

**Hermes Agent**

    hermes skills tap add zeropage-onryo/phantra-plugin

Then add the MCP server `https://api.phantra.ai/mcp` to your Hermes config.

**Any other MCP client**

Add `https://api.phantra.ai/mcp` as a remote (streamable HTTP) server and sign in when asked.

## Configuration

Nothing to configure. The server signs you in with OAuth the first time a tool is called, and
works only inside your own Phantra workspace. Credits come from your Phantra plan.

## Support

- Docs: https://phantra.ai/mcp
- Email: support@phantra.ai
- Privacy: https://phantra.ai/privacy

## License

MIT
