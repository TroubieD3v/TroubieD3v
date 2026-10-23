"""Build assets/card-*.svg: project cards for the profile README, matching the banner.

    python scripts/build_cards.py ONEST.woff2 JETBRAINS_MONO.woff2

Same fonts and palette as build_banner.py (fonts subset and embedded). Needs fonttools and brotli.
"""

from __future__ import annotations

import sys
from pathlib import Path
from xml.sax.saxutils import escape

from build_banner import AMBER, CARD, DIM, FOG, GLACIER, LINE, MUTED, PAGE, ROSE, RULE, font_face

ASSETS = Path(__file__).resolve().parent.parent / "assets"
W, H = 600, 320

PROJECTS = [
    {
        "slug": "websec-lab",
        "kicker": "playground",
        "name": "websec-lab",
        "lines": ["Break vulnerable code, watch the fix", "hold, verify both automatically."],
        "pills": ["12 labs", "OWASP Top 10:2025", "EN / RU"],
        "glow": AMBER,
        "visual": "labs",
    },
    {
        "slug": "authscope",
        "kicker": "tool",
        "name": "AuthScope",
        "lines": ["Finds authorization bugs in REST APIs", "by checking who can really reach what."],
        "pills": ["BOLA / BFLA / BOPLA", "OWASP API 2023", "pytest export"],
        "glow": GLACIER,
        "visual": "matrix",
    },
]

LAB_ROWS = [("SQL injection", True), ("IDOR", True), ("JWT forgery", True)]
MATRIX_HEAD = ["guest", "alice", "bob", "admin"]
# per row: cell colours (D = expected deny, A = allow, V = violation)
MATRIX = [("GET /orders/101", "DAVA"), ("PUT /users/101", "DADA"), ("GET /admin/stats", "DDVA")]


def pill_row(pills: list[str], x: int, y: int) -> str:
    out, cur = [], x
    for p in pills:
        w = int(len(p) * 8.6 + 26)
        out.append(f'<rect x="{cur}" y="{y}" width="{w}" height="30" rx="15" fill="{CARD}" stroke="{RULE}"/>'
                   f'<text class="pill" x="{cur + w / 2}" y="{y + 20}" text-anchor="middle">{escape(p)}</text>')
        cur += w + 10
    return "".join(out)


def labs_visual(x: int, y: int) -> str:
    """Each lab: the attack lands on the vulnerable side (amber) and is refused on the fixed side (glacier)."""
    out = [f'<text class="head" x="{x + 112}" y="{y}" text-anchor="middle" fill="{AMBER}">vulnerable</text>',
           f'<text class="head" x="{x + 196}" y="{y}" text-anchor="middle" fill="{GLACIER}">fixed</text>']
    for i, (name, _) in enumerate(LAB_ROWS):
        cy = y + 30 + i * 34
        out.append(f'<text class="row" x="{x}" y="{cy + 5}" fill="{MUTED}">{escape(name.split()[0])}</text>')
        out.append(f'<circle cx="{x + 112}" cy="{cy}" r="9" fill="{AMBER}" fill-opacity=".9"/>')
        out.append(f'<circle cx="{x + 196}" cy="{cy}" r="9" fill="none" stroke="{GLACIER}" stroke-width="2.5"/>'
                   f'<path d="M{x + 191} {cy} l3.5 3.5 l6 -7" stroke="{GLACIER}" stroke-width="2.5" fill="none" '
                   f'stroke-linecap="round" stroke-linejoin="round"/>')
    return "".join(out)


def matrix_visual(x: int, y: int) -> str:
    cell, gap = 38, 12
    out = []
    for j, h in enumerate(MATRIX_HEAD):
        out.append(f'<text class="head" x="{x + j * (cell + gap) + cell / 2}" y="{y}" text-anchor="middle" '
                   f'fill="{DIM}">{h}</text>')
    for i, (_, row) in enumerate(MATRIX):
        for j, kind in enumerate(row):
            cx, cy = x + j * (cell + gap), y + 14 + i * (cell - 8 + gap)
            if kind == "V":
                out.append(f'<rect class="hot" x="{cx}" y="{cy}" width="{cell}" height="{cell - 8}" rx="6" '
                           f'fill="{ROSE}" fill-opacity=".28" stroke="{ROSE}"/>')
            elif kind == "A":
                out.append(f'<rect x="{cx}" y="{cy}" width="{cell}" height="{cell - 8}" rx="6" fill="{GLACIER}" '
                           f'fill-opacity=".14" stroke="{GLACIER}" stroke-opacity=".45"/>')
            else:
                out.append(f'<rect x="{cx}" y="{cy}" width="{cell}" height="{cell - 8}" rx="6" fill="{CARD}" '
                           f'stroke="{RULE}"/>')
    return "".join(out)


def card(p: dict, onest: str, mono: str) -> str:
    sans_text = p["name"] + "".join(p["lines"])
    mono_text = (p["kicker"] + "".join(p["pills"]) + "".join(MATRIX_HEAD) + "vulnerablefixed"
                 + "".join(n.split()[0] for n, _ in LAB_ROWS))
    visual = labs_visual(352, 62) if p["visual"] == "labs" else matrix_visual(382, 62)
    lines = "".join(f'<text class="tag" x="40" y="{200 + i * 30}">{escape(t)}</text>' for i, t in enumerate(p["lines"]))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
<title id="t">{escape(p["name"])}: {escape(" ".join(p["lines"]))}</title>
<style>
{font_face(onest, "Onest", sans_text)}
{font_face(mono, "JetBrains Mono", mono_text)}
.name{{font:600 44px 'Onest',system-ui,sans-serif;letter-spacing:-1px;fill:{FOG}}}
.tag{{font:400 19px 'Onest',system-ui,sans-serif;fill:{MUTED}}}
.kicker{{font:500 14px 'JetBrains Mono',ui-monospace,Consolas,monospace;letter-spacing:1.5px;fill:{p["glow"]}}}
.pill{{font:500 13px 'JetBrains Mono',ui-monospace,Consolas,monospace;fill:{FOG}}}
.head,.row{{font:500 12.5px 'JetBrains Mono',ui-monospace,Consolas,monospace}}
.hot{{animation:pulse 3s ease-in-out infinite}}
@keyframes pulse{{0%,100%{{fill-opacity:.18}}50%{{fill-opacity:.45}}}}
@media (prefers-reduced-motion:reduce){{.hot{{animation:none}}}}
</style>
<defs>
<radialGradient id="g" cx="0.9" cy="-0.15" r="0.9"><stop offset="0" stop-color="{p["glow"]}" stop-opacity=".2"/><stop offset="1" stop-color="{p["glow"]}" stop-opacity="0"/></radialGradient>
<clipPath id="c"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#c)"><rect width="{W}" height="{H}" fill="{PAGE}"/><rect width="{W}" height="{H}" fill="url(#g)"/></g>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{LINE}"/>
<text class="kicker" x="40" y="66">{escape(p["kicker"].upper())}</text>
<text class="name" x="38" y="128">{escape(p["name"])}</text>
{visual}
{lines}
{pill_row(p["pills"], 40, 258)}
</svg>
"""


def main(onest: str, mono: str) -> None:
    for p in PROJECTS:
        out = ASSETS / f"card-{p['slug']}.svg"
        out.write_text(card(p, onest, mono), encoding="utf-8", newline="\n")
        print(f"{out} {out.stat().st_size / 1024:.1f} KiB")


if __name__ == "__main__":
    main(*sys.argv[1:3])
