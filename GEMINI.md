# Phantra

The `phantra-ai` MCP server connects to the person's Phantra account (AI image and video
studio). Sign in once with `/mcp auth phantra-ai`.

Rules for every session:

- Every still, clip and effect costs credits. Get the price first (`quote`, or the quote a
  making tool returns) and show it. Run `approve` or a making call only after the person says
  yes to that price. Never approve on their behalf.
- If a call is refused for credits, stop and tell them. Don't retry on a cheaper model unasked.
- Renders run in the background: poll `job`, or read `scene` for the clips.
- `reformat`, `trim_clip`, `assemble_clips` and `share_link` are free.

The skills in `skills/` cover the common jobs: start with `setup`, then `write-scene` and
`price-and-render`.
