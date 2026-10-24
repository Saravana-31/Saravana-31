# Asset notes

Everything in `assets/` is original and generated from code, so it can be edited and regenerated.

| File | Size | Purpose |
| :-- | :-- | :-- |
| `assets/profile-banner.png` | 1200 x 320 | README header. A scattered node field resolves into an ordered UI frame: the model side feeding the product side. |
| `assets/ai-engineering-visual.png` | 1200 x 480 | Five-stage map (data, models, services, storage, interface) grouped into AI and full-stack work. Conceptual, not a claim about one system. |
| `assets/project-showcase.png` | 1200 x 600 | Six project cards with status, stack and repository. Uses real repositories only; contains no screenshots or metrics. |
| `assets/src/*.svg` | | Editable vector sources for the three PNGs. |
| `tools/build_assets.py` | | Single script that writes the SVGs and renders the PNGs. |

## Regenerating

```bash
pip install -r tools/requirements.txt
# Install Space Grotesk and Inter (SIL Open Font License) so cairo can find them.
python tools/build_assets.py
```

Change project cards by editing the `PROJECTS` list in `tools/build_assets.py`; text wrapping and pill widths are measured from the real font files, so longer text reflows instead of overflowing.

## Palette and type

Navy `#040912` to `#0a1830`, panels `#0b1a33`, cyan `#22d3ee`, blue `#60a5fa`, text `#e6f1ff` / `#9fb3c8`. Headings in Space Grotesk, body in Inter.

## External images in the README

The stats cards are loaded from third-party services at view time. They are not stored in this repository.

- GitHub stats and top languages: `github-readme-stats.vercel.app`. The maintainers describe this public instance as best-effort and recommend self-hosting for reliability.
- Contribution streak: `streak-stats.demolab.com`.
- Activity graph: `github-readme-activity-graph.vercel.app`.
- LeetCode card: `leetcard.jacoblin.cool`.

If a card goes down for good, delete its `<img>` block; the fallback sentence under each group already points to the native GitHub and LeetCode pages. No tokens or secrets are used anywhere.
