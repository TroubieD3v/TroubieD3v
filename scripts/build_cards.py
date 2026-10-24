"""Build assets/card-*.svg: project cards for the profile README, matching the banner.

    python scripts/build_cards.py ONEST.woff2 JETBRAINS_MONO.woff2 [slug]

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
        "name": "WebSec-Lab",
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
    {
        "slug": "cloudgraph",
        "kicker": "engine",
        "name": "CloudGraph",
        "lines": ["Explains how small misconfigurations", "chain into an attack path."],
        "pills": ["41 rules", "Compose / K8s / Terraform", "what-if"],
        "glow": ROSE,
        "visual": "path",
    },
    {
        "slug": "agentshield",
        "kicker": "red team",
        "name": "AgentShield",
        "lines": ["Tests what AI agents actually do,", "not just what they say."],
        "pills": ["46 scenarios", "OWASP LLM / Agentic", "Monitor / Enforce"],
        "glow": AMBER,
        "visual": "trace",
    },
]

# an attack path: each hop is a separate weakness, the last one is the sensitive target
PATH_NODES = [("internet", DIM), ("ingress", GLACIER), ("web pod", AMBER), ("secrets", ROSE)]
# an agent trace: the user asks, a document smuggles in a command, the tool call is stopped by policy
TRACE_NODES = [("request", DIM), ("document", AMBER), ("send_email", ROSE), ("blocked", GLACIER)]
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


def path_visual(x: int, y: int) -> str:
    """Internet -> ingress -> pod -> secrets; dashed hops are conditional, the target pulses."""
    w, h, step = 150, 24, 34
    out = []
    for i, (label, colour) in enumerate(PATH_NODES):
        top = y + i * step - h / 2
        last = i == len(PATH_NODES) - 1
        if i:
            x1, y1, y2 = x + 26, top - step + h, top
            stroke = ROSE if last else RULE
            out.append(f'<path d="M{x1} {y1 + 2} V{y2 - 3}" stroke="{stroke}" stroke-width="2" stroke-dasharray="3 3"/>'
                       f'<path d="M{x1 - 4} {y2 - 7} l4 4 l4 -4" stroke="{stroke}" stroke-width="2" fill="none" '
                       f'stroke-linecap="round" stroke-linejoin="round"/>')
        if last:
            out.append(f'<rect class="hot" x="{x}" y="{top}" width="{w}" height="{h}" rx="12" fill="{ROSE}" '
                       f'fill-opacity=".28" stroke="{ROSE}"/>')
        else:
            out.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="12" fill="{CARD}" stroke="{RULE}"/>')
        out.append(f'<circle cx="{x + 14}" cy="{top + h / 2}" r="4" fill="{colour}"/>')
        out.append(f'<text class="row" x="{x + 26}" y="{top + h / 2 + 4.5}" fill="{FOG if last else MUTED}">{escape(label)}</text>')
    return "".join(out)


def trace_visual(x: int, y: int) -> str:
    """request -> document -> send_email (the unexpected call pulses) -> blocked by policy."""
    w, h, step = 150, 24, 34
    out = []
    for i, (label, colour) in enumerate(TRACE_NODES):
        top = y + i * step - h / 2
        hot, last = label == "send_email", i == len(TRACE_NODES) - 1
        if i:
            x1, y1, y2 = x + 26, top - step + h, top
            stroke = ROSE if hot else (GLACIER if last else RULE)
            out.append(f'<path d="M{x1} {y1 + 2} V{y2 - 3}" stroke="{stroke}" stroke-width="2" stroke-dasharray="3 3"/>'
                       f'<path d="M{x1 - 4} {y2 - 7} l4 4 l4 -4" stroke="{stroke}" stroke-width="2" fill="none" '
                       f'stroke-linecap="round" stroke-linejoin="round"/>')
        if hot:
            out.append(f'<rect class="hot" x="{x}" y="{top}" width="{w}" height="{h}" rx="12" fill="{ROSE}" '
                       f'fill-opacity=".28" stroke="{ROSE}"/>')
        elif last:
            out.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="12" fill="{GLACIER}" fill-opacity=".14" '
                       f'stroke="{GLACIER}" stroke-opacity=".45"/>')
        else:
            out.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="12" fill="{CARD}" stroke="{RULE}"/>')
        out.append(f'<circle cx="{x + 14}" cy="{top + h / 2}" r="4" fill="{colour}"/>')
        out.append(f'<text class="row" x="{x + 26}" y="{top + h / 2 + 4.5}" fill="{FOG if hot or last else MUTED}">{escape(label)}</text>')
    return "".join(out)


def card(p: dict, onest: str, mono: str) -> str:
    sans_text = p["name"] + "".join(p["lines"])
    mono_text = (p["kicker"] + p["kicker"].upper() + "".join(p["pills"]) + "".join(MATRIX_HEAD) + "vulnerablefixed"
                 + "".join(n.split()[0] for n, _ in LAB_ROWS) + "".join(n for n, _ in PATH_NODES)
                 + "".join(n for n, _ in TRACE_NODES))
    visual = {"labs": lambda: labs_visual(352, 62), "matrix": lambda: matrix_visual(382, 62),
              "path": lambda: path_visual(410, 60), "trace": lambda: trace_visual(410, 60)}[p["visual"]]()
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


def main(onest: str, mono: str, only: str | None = None) -> None:
    for p in PROJECTS:
        if only and p["slug"] != only:
            continue
        out = ASSETS / f"card-{p['slug']}.svg"
        out.write_text(card(p, onest, mono), encoding="utf-8", newline="\n")
        print(f"{out} {out.stat().st_size / 1024:.1f} KiB")


if __name__ == "__main__":
    main(*sys.argv[1:4])
