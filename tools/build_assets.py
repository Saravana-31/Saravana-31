#!/usr/bin/env python3
"""Regenerates the profile banner: SVG source in assets/src/, PNG in assets/.

Requirements: pip install cairosvg pillow
Fonts (SIL OFL): Space Grotesk (headings) and Inter (body) must be installed so
cairo can find them. See README_ASSET_NOTES.md.

Usage:  python tools/build_assets.py
"""
import os, random, glob
import cairosvg
from PIL import ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "src")
OUT = os.path.join(ROOT, "assets")
os.makedirs(SRC, exist_ok=True)

# ---- palette -------------------------------------------------------------
BG0, BG1 = "#040912", "#0a1830"
PANEL, PANEL_HI = "#0b1a33", "#0f2447"
LINE, LINE_HI = "#1b3f68", "#2a6ea0"
CYAN, BLUE = "#22d3ee", "#60a5fa"
TXT, TXT_DIM, TXT_MUTE = "#e6f1ff", "#9fb3c8", "#6f8aa8"
HEAD, BODY = "Space Grotesk", "Inter"


# ---- text measurement (real font files, so layouts don't overflow) --------
def _font_file(family_key, hint):
    pats = [os.path.expanduser("~/.fonts/*.ttf"), "/usr/share/fonts/**/*.ttf",
            os.path.join(ROOT, "tools", "fonts", "*.ttf")]
    for pat in pats:
        for p in glob.glob(pat, recursive=True):
            b = os.path.basename(p)
            if family_key in b and hint in b:
                return p
    return None


_F = {}


def tw(txt, size, family=BODY, weight="Regular"):
    key = (family, weight, size)
    if key not in _F:
        f = _font_file("Inter" if family == BODY else "SpaceGrotesk", weight)
        _F[key] = ImageFont.truetype(f, size) if f else None
    f = _F[key]
    return f.getlength(txt) if f else len(txt) * size * 0.58


def wrap(txt, size, maxw, family=BODY, weight="Regular"):
    lines, cur = [], ""
    for w in txt.split():
        t = (cur + " " + w).strip()
        if tw(t, size, family, weight) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size, fill, family=BODY, weight=400, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{esc(s)}</text>')


def defs(w, h, glow_x, glow_y, glow_r):
    return f'''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/></linearGradient>
  <radialGradient id="glow" cx="{glow_x}" cy="{glow_y}" r="{glow_r}" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{CYAN}" stop-opacity="0.16"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#14294a" stroke-width="1" opacity="0.55"/></pattern>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" fill="{CYAN}"/></marker>
</defs>
<rect width="{w}" height="{h}" fill="url(#bg)"/><rect width="{w}" height="{h}" fill="url(#grid)"/><rect width="{w}" height="{h}" fill="url(#glow)"/>'''


def save(name, svg, w, h):
    svg_path = os.path.join(SRC, name + ".svg")
    with open(svg_path, "w", encoding="utf-8") as fh:
        fh.write(svg)
    png_path = os.path.join(OUT, name + ".png")
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=png_path, output_width=w, output_height=h)
    print("wrote", png_path)


# =========================================================================
# 1. BANNER  1200 x 320
# =========================================================================
def banner():
    W, H = 1200, 320
    random.seed(31)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Saravana P, AI Engineering and Full-Stack Development">',
         defs(W, H, 900, 160, 380)]
    # left: identity
    s.append(f'<rect x="64" y="64" width="44" height="4" rx="2" fill="{CYAN}"/>')
    s.append(text(62, 138, "Saravana P", 66, TXT, HEAD, 700, extra='letter-spacing="-1"'))
    s.append(text(64, 186, "AI Engineering × Full-Stack Development", 25, CYAN, HEAD, 600))
    s.append(text(64, 232, "Building intelligent systems into useful products.", 19, TXT_DIM, BODY, 400))
    s.append(text(64, 270, "B.Tech AI & ML, Kongu Engineering College", 14, TXT_MUTE, BODY, 500))
    # centre: network field (model side)
    layers = [(670, [78, 118, 158, 198, 238]),
              (755, [62, 100, 138, 178, 218, 258]),
              (840, [98, 148, 198, 248])]
    for _ in range(34):  # ambient specks
        x, y = random.randint(620, 1180), random.randint(14, 306)
        s.append(f'<circle cx="{x}" cy="{y}" r="{random.choice([1, 1, 1.5])}" fill="{BLUE}" opacity="{random.choice([.25, .35, .5])}"/>')
    for (xa, ya_list), (xb, yb_list) in zip(layers, layers[1:]):  # edges
        for ya in ya_list:
            for yb in yb_list:
                s.append(f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="{LINE_HI}" stroke-width="1" opacity="0.30"/>')
    path = [(670, 158), (755, 138), (840, 148)]  # active signal path
    s.append(f'<polyline points="{" ".join(f"{x},{y}" for x, y in path)}" fill="none" stroke="{CYAN}" stroke-width="2" opacity="0.95"/>')
    for y in layers[2][1]:  # convergence into the interface frame
        s.append(f'<path d="M840 {y} C 888 {y}, 888 160, 936 160" fill="none" stroke="{CYAN}" stroke-width="1.2" opacity="0.55"/>')
    for x, ys in layers:  # nodes
        for y in ys:
            active = (x, y) in path
            s.append(f'<circle cx="{x}" cy="{y}" r="{6 if active else 4.5}" fill="{CYAN if active else BG1}" stroke="{CYAN}" stroke-width="1.5"/>')
    # interface frame (product side)
    fx, fy, fw, fh = 936, 62, 228, 196
    s.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="12" fill="{PANEL}" stroke="{LINE_HI}" stroke-width="1.5"/>')
    s.append(f'<path d="M{fx} {fy + 12} a12 12 0 0 1 12 -12 h{fw - 24} a12 12 0 0 1 12 12 v14 h-{fw} z" fill="{PANEL_HI}"/>')
    for i, c in enumerate(["#2a6ea0", "#2a6ea0", CYAN]):
        s.append(f'<circle cx="{fx + 16 + i * 14}" cy="{fy + 13}" r="3.5" fill="{c}"/>')
    s.append(f'<rect x="{fx + 16}" y="{fy + 42}" width="86" height="8" rx="4" fill="{TXT_DIM}" opacity=".7"/>')
    s.append(f'<rect x="{fx + 16}" y="{fy + 58}" width="54" height="6" rx="3" fill="{LINE_HI}"/>')
    spark = [(fx + 16, fy + 138), (fx + 52, fy + 118), (fx + 86, fy + 126),
             (fx + 120, fy + 98), (fx + 156, fy + 108), (fx + 212, fy + 80)]
    s.append(f'<polyline points="{" ".join(f"{x},{y}" for x, y in spark)}" fill="none" stroke="{CYAN}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>')
    s.append(f'<circle cx="{spark[-1][0]}" cy="{spark[-1][1]}" r="4" fill="{CYAN}"/>')
    for i in range(3):
        s.append(f'<rect x="{fx + 16 + i * 68}" y="{fy + 156}" width="56" height="26" rx="6" fill="{PANEL_HI}" stroke="{LINE}" stroke-width="1"/>')
    s.append("</svg>")
    save("profile-banner", "\n".join(s), W, H)


if __name__ == "__main__":
    banner()
