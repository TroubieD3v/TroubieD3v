"""Build the profile artwork: assets/banner.svg and assets/card-*.svg.

    python scripts/build_art.py ARCHIVO.woff2

The look follows vgteam.top: black and white only, one typeface (Archivo at 125% width) and the
logo's bar as the only ornament. ARCHIVO.woff2 is the variable Archivo (wght 100-900, wdth 62-125,
SIL OFL 1.1). It is pinned to 125% width, subset to the glyphs each image uses and embedded, because
an SVG shown through <img> cannot load external fonts. Text is measured with the same font, so names
shrink to fit instead of running off the card. Needs fonttools and brotli.
"""

from __future__ import annotations

import base64
import io
import sys
from functools import cache
from pathlib import Path
from xml.sax.saxutils import escape

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ASSETS = Path(__file__).resolve().parent.parent / "assets"
FONT = ""  # set from argv

# vgteam.top tokens
INK, PAPER = "#000", "#fff"
INK_SOFT, PAPER_SOFT = "#5c5c5c", "#a6a6a6"  # secondary text on paper / on ink
RULE_ON_PAPER, RULE_ON_INK = "#d4d4d4", "#2e2e2e"
DARK = {"bg": INK, "fg": PAPER, "soft": PAPER_SOFT, "rule": RULE_ON_INK}
LIGHT = {"bg": PAPER, "fg": INK, "soft": INK_SOFT, "rule": RULE_ON_PAPER}

# the VG Team mark (viewBox 300 180 600 600): V, bar, ring
MARK = ('<path d="M480 350H560L600 450L640 350H720L600 610Z"/><path d="M660 450H870V510H632Z"/>'
        '<path d="M840 480A240 240 0 1 1 769.71 310.29" fill="none" stroke="currentColor" stroke-width="60"/>')

NAME = "TroubieD3v"
TAGLINE = "I break web apps on purpose, then make sure the fix holds."
TEAM = "Captain, VG Team"

PROJECTS = [
    {"slug": "websec-lab", "kicker": "playground", "name": "WebSec-Lab",
     "text": "Break vulnerable code, watch the fix hold, verify both automatically.",
     "stat": "12", "stat_label": ["labs", "OWASP Top 10:2025"]},
    {"slug": "authscope", "kicker": "API authorization", "name": "AuthScope",
     "text": "Finds authorization bugs in REST APIs by checking who can really reach what.",
     "stat": "5", "stat_label": ["authorization checks", "OWASP API Top 10:2023"]},
    {"slug": "cloudgraph", "kicker": "attack paths", "name": "CloudGraph",
     "text": "Explains how small misconfigurations chain into an attack path.",
     "stat": "41", "stat_label": ["rules", "Compose, K8s, Terraform"]},
    {"slug": "agentshield", "kicker": "AI agents", "name": "AgentShield",
     "text": "Tests what AI agents actually do, not just what they say.",
     "stat": "46", "stat_label": ["attack scenarios", "LLM and Agentic Top 10"]},
    {"slug": "supplychain-radar", "kicker": "supply chain", "name": "SupplyChain Radar",
     "text": "Shows why a vulnerable package is in your project and which upgrade fixes it.",
     "stat": "6", "stat_label": ["lockfile and SBOM formats", "OSV advisories"]},
    {"slug": "rls-sentinel", "kicker": "database", "name": "RLS Sentinel",
     "text": "Proves what PostgreSQL row-level security really lets each role do.",
     "stat": "21", "stat_label": ["rules", "PostgreSQL 15 to 18"]},
    {"slug": "photofinish", "kicker": "race conditions", "name": "PhotoFinish",
     "text": "Proves race conditions in web APIs instead of just sending them.",
     "stat": "0.2", "stat_label": ["ms arrival spread", "single-packet attack"]},
]
# Two per row in the README; alternate like the site's ink and paper sections.
THEMES = [DARK, LIGHT, LIGHT, DARK, DARK, LIGHT, LIGHT]


@cache
def _static(weight: int) -> tuple[dict, list, float]:
    font = instancer.instantiateVariableFont(TTFont(FONT), {"wght": weight, "wdth": 125})
    return font.getBestCmap(), font["hmtx"], font["head"].unitsPerEm


def width(text: str, size: float, weight: int, tracking: float = 0.0) -> float:
    """Advance width in px; tracking is in em, as in CSS letter-spacing."""
    cmap, hmtx, upm = _static(weight)
    return sum(hmtx[cmap[ord(c)]][0] for c in text) / upm * size + tracking * size * len(text)


def fit(text: str, max_w: float, weight: int, largest: float, tracking: float = 0.0) -> float:
    size = largest
    while width(text, size, weight, tracking) > max_w:
        size -= 0.5
    return size


def wrap(text: str, max_w: float, size: float, weight: int) -> list[str]:
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if cur and width(trial, size, weight) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + [cur]


def font_face(text: str) -> str:
    font = instancer.instantiateVariableFont(TTFont(FONT), {"wdth": 125, "wght": (400, 900)})
    options = subset.Options()
    options.layout_features = ["kern", "liga"]
    subsetter = subset.Subsetter(options)
    subsetter.populate(text=text)
    subsetter.subset(font)
    font.flavor = "woff2"
    buffer = io.BytesIO()
    font.save(buffer)
    data = base64.b64encode(buffer.getvalue()).decode()
    return (f"@font-face{{font-family:'Archivo';font-weight:400 900;"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}")


def text(x: float, y: float, s: str, size: float, weight: int, fill: str, *, tracking: float = 0.0,
         anchor: str = "start", upper: bool = False) -> str:
    s = s.upper() if upper else s
    ls = f' letter-spacing="{tracking}em"' if tracking else ""
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size:g}" font-weight="{weight}" fill="{fill}"{ls}{a}>'
            f"{escape(s)}</text>")


def svg(w: int, h: int, title: str, used: str, body: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-labelledby="t">\n<title id="t">{escape(title)}</title>\n'
            f"<style>\n{font_face(used)}\n"
            "text{font-family:'Archivo','Arial Nova',Arial,'Helvetica Neue',sans-serif;font-kerning:normal}\n"
            f"</style>\n{body}\n</svg>\n")


def banner() -> str:
    W, H, pad = 1200, 340, 64
    t = DARK
    label = 18
    out = [f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>']
    # top: the brand lockup on the left, the subject on the right, as in the site's header
    out.append(f'<svg x="{pad}" y="33" width="32" height="32" viewBox="300 180 600 600" fill="{t["fg"]}" '
               f'color="{t["fg"]}">{MARK}</svg>')
    out.append(text(pad + 46, 56, "VG Team", label, 900, t["fg"], tracking=0.26, upper=True))
    out.append(text(W - pad, 56, "Application security", label, 700, t["fg"], anchor="end"))
    # the name, as large as the width allows, with the logo's bar under it
    size = fit(NAME, W - 2 * pad, 900, 168, -0.03)
    base = 226
    out.append(text(pad - size * 0.04, base, NAME, size, 900, t["fg"], tracking=-0.03))
    out.append(f'<rect x="{pad}" y="{base + 22}" width="{W * 0.3:.0f}" height="12" fill="{t["fg"]}"/>')
    # bottom: what this is, and a link-style credit underlined with a 4 px bar
    out.append(text(pad, 302, TAGLINE, 20, 700, t["fg"]))
    team_w = width(TEAM, 20, 700)
    out.append(text(W - pad, 302, TEAM, 20, 700, t["fg"], anchor="end"))
    out.append(f'<rect x="{W - pad - team_w:.1f}" y="311" width="{team_w:.1f}" height="4" fill="{t["fg"]}"/>')
    used = NAME + "VG TEAM" + "Application security" + TAGLINE + TEAM
    return svg(W, H, f"{NAME}: {TAGLINE} {TEAM}.", used, "\n".join(out))


def card(i: int, p: dict) -> str:
    W, H, pad = 600, 320, 40
    t = THEMES[i]
    inner = W - 2 * pad
    out = [f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>']
    if t is LIGHT:  # keeps a white card visible on a white page
        out.append(f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" fill="none" stroke="{t["rule"]}"/>')
    # header row: index and subject, then a hairline rule like the site's tables
    out.append(text(pad, 54, f"{i + 1:02d}", 15, 900, t["fg"], tracking=0.2))
    out.append(text(W - pad, 54, p["kicker"], 15, 700, t["soft"], anchor="end", tracking=0.12, upper=True))
    out.append(f'<rect x="{pad}" y="72" width="{inner}" height="1" fill="{t["rule"]}"/>')
    # name and one sentence
    name_size = fit(p["name"], inner, 800, 46, -0.01)
    out.append(text(pad - 1, 122, p["name"], name_size, 800, t["fg"], tracking=-0.01))
    lines = wrap(p["text"], inner, 21, 400)
    assert len(lines) <= 2, (p["slug"], lines)
    out += [text(pad, 158 + k * 28, ln, 21, 400, t["soft"]) for k, ln in enumerate(lines)]
    # the number, set like the places on the site's results table
    stat_size, stat_y = 96, 288
    stat_w = width(p["stat"], stat_size, 900, -0.03)
    out.append(text(pad - 4, stat_y, p["stat"], stat_size, 900, t["fg"], tracking=-0.03))
    lx = pad + stat_w + 18
    assert lx + max(width(s, 20, 700) for s in p["stat_label"]) <= W - pad, p["slug"]
    out.append(text(lx, stat_y - 32, p["stat_label"][0], 20, 700, t["fg"]))
    out.append(text(lx, stat_y - 4, p["stat_label"][1], 20, 400, t["soft"]))
    used = f"{i + 1:02d}" + p["kicker"].upper() + p["name"] + p["text"] + p["stat"] + "".join(p["stat_label"])
    return svg(W, H, f'{p["name"]}: {p["text"]}', used, "\n".join(out))


def main(font: str) -> None:
    global FONT
    FONT = font
    files = {ASSETS / "banner.svg": banner()}
    files |= {ASSETS / f"card-{p['slug']}.svg": card(i, p) for i, p in enumerate(PROJECTS)}
    for path, content in files.items():
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"{path.name} {path.stat().st_size / 1024:.1f} KiB")


if __name__ == "__main__":
    main(sys.argv[1])
