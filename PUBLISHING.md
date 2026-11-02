# Publishing checklist

One repo, four listings. Nothing here changes the MCP server (`https://api.phantra.ai/mcp`) or
the two plugin repos under review (phantra-claude-plugin, phantra-chatgpt-plugin).

Skills are copied from phantra-chatgpt-plugin at cb48179 (2026-10-20); only the `setup`
description changed ("in ChatGPT" → "in an AI assistant"). When a skill changes there, copy it
here and bump `version` in `gemini-extension.json` and `.cursor-plugin/plugin.json`.

Before every release: `python3 scripts/check.py`

## 0. Create the repo (once)

1. On GitHub, create **public** `zeropage-onryo/phantra-plugin`, empty (no README).
2. From this folder:

       git remote add origin https://github.com/zeropage-onryo/phantra-plugin.git
       git push -u origin main

3. Repo → About (gear icon): description "AI image & video generation for Gemini CLI, Cursor,
   OpenClaw and Hermes", website `https://phantra.ai/mcp`, topics:
   `gemini-cli-extension`, `mcp`, `ai-video`, `image-generation`, `cursor-plugin`.
4. Optional: Releases → new release, tag `v1.0.0` (must match `version`).

## 1. Hermes Agent (done by step 0)

Nothing to submit. Anyone can run `hermes skills tap add zeropage-onryo/phantra-plugin`.

## 2. ClawHub / OpenClaw (≈15 min)

    npm i -g clawhub
    clawhub login
    scripts/publish-clawhub.sh          # dry run, check the commands
    scripts/publish-clawhub.sh --go     # publishes 32 skills as phantra-ai-<skill>

Automated scan, no human review, can be live the same day. Check:
`https://clawhub.ai/api/v1/search?q=phantra`. Publishing also makes the skills findable in
Hermes' Skills Hub.

## 3. Gemini CLI gallery (done by step 0's topic)

No form: the gallery crawls repos with the `gemini-cli-extension` topic daily and lists those
whose root `gemini-extension.json` validates. Test first on a desktop (sign-in opens a browser):

    gemini extensions install https://github.com/zeropage-onryo/phantra-plugin
    /mcp auth phantra-ai

Check geminicli.com/extensions for "Phantra" a day or two later.
Note: Google's docs say Gemini CLI was replaced by Antigravity CLI on 2026-06-18 for unpaid and
Google One users; the gallery still exists, but its audience may be smaller than it was.

## 4. Cursor Marketplace (≈10 min, then a long wait)

1. Test locally: copy this folder to `~/.cursor/plugins/local/phantra-ai`, reload the window,
   check Phantra appears under MCP, sign in, ask for a balance.
2. Submit the repo link at cursor.com/marketplace/publish.

Every plugin is reviewed by hand and must be open source (this repo is MIT). Forum reports put
the wait at weeks to months with no confirmation email; Cursor staff say don't resubmit.
Cursor's plugin docs show only header auth for remote servers; Phantra uses OAuth, which
Cursor's MCP client handles on its own — confirm in the local test.
