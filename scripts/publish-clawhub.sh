#!/usr/bin/env bash
# Publish every skill to ClawHub as phantra-ai-<skill>. Hermes finds them there too.
# Needs: npm i -g clawhub && clawhub login   (a GitHub account old enough for ClawHub's upload gate)
# Usage: scripts/publish-clawhub.sh            # dry run: prints the commands
#        scripts/publish-clawhub.sh --go       # publishes
set -euo pipefail
cd "$(dirname "$0")/.."
VERSION=$(python3 -c 'import json;print(json.load(open("gemini-extension.json"))["version"])')
python3 scripts/check.py
for dir in skills/*/; do
  skill=$(basename "$dir")
  title=$(echo "$skill" | tr '-' ' ' | sed 's/\b\(.\)/\u\1/g')
  cmd=(clawhub skill publish "$dir" --slug "phantra-ai-$skill" --name "Phantra AI: $title" --version "$VERSION")
  if [[ "${1:-}" == "--go" ]]; then "${cmd[@]}"; else printf '%q ' "${cmd[@]}"; echo; fi
done
