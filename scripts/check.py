#!/usr/bin/env python3
"""Check the package before a release.  python3 scripts/check.py

- gemini-extension.json, .cursor-plugin/plugin.json (servers inline: a root mcp.json would be
  flagged by Antigravity's strict check), .antigravity-plugin/plugin.json and mcp_config.json
  parse, agree on name and version, and point at https://api.phantra.ai/mcp;
- Gemini's context file is rules/GEMINI.md, where Antigravity reads it as an always-on rule;
- every skills/<dir>/SKILL.md has frontmatter `name` equal to <dir> (1-64 chars, a-z 0-9 -)
  and a `description` of at most 1,024 characters;
- no skill names a tool this server doesn't have: the Claude door's `open_in_studio`, or the
  retired `apply_effect` (scripts/mcp-tools.txt is the live list);
- no skill or listing text names a single assistant ("ChatGPT", "Claude") as the host.
Standard library only. Exit 1 on any failure.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = "https://api.phantra.ai/mcp"
fail = []

def load(rel):
    try:
        return json.loads((ROOT / rel).read_text())
    except Exception as e:
        fail.append(f"{rel}: {e}")
        return {}

gem, cur = load("gemini-extension.json"), load(".cursor-plugin/plugin.json")
agy, agy_mcp = load(".antigravity-plugin/plugin.json"), load("mcp_config.json")
for other, rel in ((cur, ".cursor-plugin/plugin.json"), (agy, ".antigravity-plugin/plugin.json")):
    for key in ("name", "version"):
        if gem.get(key) != other.get(key):
            fail.append(f"{key} differs between gemini-extension.json and {rel}")
if [s.get("httpUrl") for s in gem.get("mcpServers", {}).values()] != [URL]:
    fail.append("gemini-extension.json must declare one server with httpUrl " + URL)
if [s.get("url") for s in cur.get("mcpServers", {}).values()] != [URL]:
    fail.append(".cursor-plugin/plugin.json must declare one server with url " + URL)
if gem.get("contextFileName") != "rules/GEMINI.md" or not (ROOT / "rules/GEMINI.md").is_file():
    fail.append("gemini-extension.json must point contextFileName at rules/GEMINI.md")
for stray in ("mcp.json", "GEMINI.md"):
    if (ROOT / stray).exists():
        fail.append(f"root {stray}: Antigravity's strict check flags it as never loaded")
if [s.get("serverUrl") for s in agy_mcp.get("mcpServers", {}).values()] != [URL]:
    fail.append("mcp_config.json must declare one server with serverUrl " + URL)
for logo_of, rel in ((cur, "Cursor"), (agy, "Antigravity")):
    if not (ROOT / logo_of.get("logo", "missing")).is_file():
        fail.append(f"{rel} logo file missing")
if len(agy.get("suggestedPrompts", [])) > 3:
    fail.append("Antigravity allows at most 3 suggestedPrompts")

tools = {l.strip() for l in (ROOT / "scripts/mcp-tools.txt").read_text().splitlines()
         if l.strip() and not l.startswith("#")}
not_here = {"open_in_studio", "apply_effect"} - tools

skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
for d in skills:
    f = d / "SKILL.md"
    if not f.is_file():
        fail.append(f"{d.name}: no SKILL.md"); continue
    text = f.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        fail.append(f"{d.name}: no frontmatter"); continue
    fm = dict(re.findall(r"^([a-z]+):\s*(.*)$", m.group(1), re.M))
    if fm.get("name") != d.name or not re.fullmatch(r"[a-z0-9-]{1,64}", d.name):
        fail.append(f"{d.name}: frontmatter name must equal the folder name")
    if not fm.get("description") or len(fm["description"]) > 1024:
        fail.append(f"{d.name}: description missing or over 1,024 characters")
    for t in not_here:
        if re.search(rf"`{t}`", text):
            fail.append(f"{d.name}: names `{t}`, which this server doesn't have")
    if re.search(r"\b(ChatGPT|Claude)\b", text):
        fail.append(f"{d.name}: names a single assistant")

for rel in ("README.md", "rules/GEMINI.md"):
    if re.search(r"\bChatGPT\b", (ROOT / rel).read_text()):
        fail.append(f"{rel}: names ChatGPT")

print(f"{len(skills)} skills, {len(tools)} tools checked")
for f in fail:
    print("FAIL", f)
sys.exit(1 if fail else 0)
