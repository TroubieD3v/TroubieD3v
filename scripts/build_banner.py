"""Build assets/banner.svg: the profile header, in the colours and type of websec-lab.

    python scripts/build_banner.py ONEST.woff2 JETBRAINS_MONO.woff2

The fonts (Onest Variable, JetBrains Mono Variable; both SIL OFL 1.1) are subset to the glyphs the
banner uses and embedded, because an SVG shown through <img> cannot load external fonts.
Needs fonttools and brotli.
"""

from __future__ import annotations

import base64
import io
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from fontTools import subset
from fontTools.ttLib import TTFont

OUT = Path(__file__).resolve().parent.parent / "assets" / "banner.svg"

# palette (websec-lab tokens)
PAGE, CARD, LINE, RULE = "#121418", "#1a1d22", "#252930", "#333842"
FOG, MUTED, DIM = "#f3f1ec", "#a2a6ae", "#8e939c"
AMBER, GLACIER, ROSE = "#e8a33d", "#7cc4e8", "#e5776f"

NAME = "TroubieD3v"
TAGLINE = ["I break web apps on purpose,", "then make sure the fix holds."]

# (text, colour) runs per code line; the first line is shared by both states.
INPUT = [[('name = ', MUTED), ('"\' OR 1=1 --"', FOG)]]
VULNERABLE = [
    [("db.execute(", MUTED), ('f"SELECT * FROM users', FOG)],
    [("  WHERE name = ", FOG), ("'{name}'", AMBER), ('")', FOG)],
    [("# every row comes back", ROSE)],
]
FIXED = [
    [("db.execute(", MUTED), ('"SELECT * FROM users', FOG)],
    [("  WHERE name = ", FOG), ("?", GLACIER), ('", (name,))', FOG)],
    [("# no rows: it is just a name", DIM)],
]
LABELS = {"vulnerable": AMBER, "fixed": GLACIER}


def font_face(path: str, family: str, text: str) -> str:
    options = subset.Options()
    options.flavor = "woff2"
    options.layout_features = ["kern", "liga", "calt"]
    font = TTFont(path)
    subsetter = subset.Subsetter(options)
    subsetter.populate(text=text)
    subsetter.subset(font)
    buffer = io.BytesIO()
    font.flavor = "woff2"
    font.save(buffer)
    data = base64.b64encode(buffer.getvalue()).decode()
    return f"@font-face{{font-family:'{family}';font-weight:100 900;src:url(data:font/woff2;base64,{data}) format('woff2')}}"


def code_line(runs: list[tuple[str, str]], x: int, y: int) -> str:
    spans = "".join(f'<tspan fill="{colour}">{escape(text)}</tspan>' for text, colour in runs)
    return f'<text class="code" x="{x}" y="{y}" xml:space="preserve">{spans}</text>'


def main(onest: str, mono: str) -> None:
    sans_text = NAME + "".join(TAGLINE)
    mono_text = "".join(t for line in INPUT + VULNERABLE + FIXED for t, _ in line) + "".join(LABELS)

    cx, cy, cw, ch = 628, 60, 512, 220  # code card
    code_x, first_y, step = cx + 28, cy + 98, 33

    def state(name: str, lines: list) -> str:
        colour = LABELS[name]
        body = "".join(code_line(line, code_x, first_y + step * (i + 1)) for i, line in enumerate(lines))
        label = (
            f'<circle cx="{cx + 34}" cy="{cy + 33}" r="5" fill="{colour}"/>'
            f'<text class="label" x="{cx + 50}" y="{cy + 39}" fill="{colour}">{name}</text>'
        )
        return f'<g class="{name}">{label}{body}</g>'

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="1200" height="340" role="img" aria-labelledby="t">
<title id="t">{NAME}: {" ".join(TAGLINE)}</title>
<style>
{font_face(onest, "Onest", sans_text)}
{font_face(mono, "JetBrains Mono", mono_text)}
.name{{font:600 76px 'Onest',system-ui,sans-serif;letter-spacing:-2px;fill:{FOG}}}
.tag{{font:400 25px 'Onest',system-ui,sans-serif;fill:{MUTED}}}
.code{{font:400 19.5px 'JetBrains Mono',ui-monospace,Consolas,monospace;font-variant-ligatures:none}}
.label{{font:500 16px 'JetBrains Mono',ui-monospace,Consolas,monospace}}
.vulnerable,.aura-v{{animation:show-v 9s infinite}}
.fixed,.aura-f{{animation:show-f 9s infinite}}
.aura-v,.aura-f{{animation-timing-function:ease-in-out}}
.sweep{{animation:sweep 9s infinite cubic-bezier(.22,1,.36,1)}}
@keyframes show-v{{0%,45%{{opacity:1}}48.5%,96.5%{{opacity:0}}100%{{opacity:1}}}}
@keyframes show-f{{0%,48.5%{{opacity:0}}52%,93%{{opacity:1}}96.5%,100%{{opacity:0}}}}
@keyframes sweep{{0%,45%{{transform:translateX(-{cw}px);opacity:0}}47%{{opacity:1}}56%,100%{{transform:translateX({cw}px);opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.vulnerable,.aura-v,.sweep{{animation:none;opacity:0}}.fixed,.aura-f{{animation:none;opacity:1}}}}
</style>
<defs>
<radialGradient id="gv" cx="0.82" cy="-0.1" r="0.75"><stop offset="0" stop-color="{AMBER}" stop-opacity=".2"/><stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></radialGradient>
<radialGradient id="gf" cx="0.82" cy="-0.1" r="0.75"><stop offset="0" stop-color="{GLACIER}" stop-opacity=".18"/><stop offset="1" stop-color="{GLACIER}" stop-opacity="0"/></radialGradient>
<linearGradient id="gs"><stop offset="0" stop-color="{GLACIER}" stop-opacity="0"/><stop offset=".5" stop-color="{GLACIER}"/><stop offset="1" stop-color="{GLACIER}" stop-opacity="0"/></linearGradient>
<clipPath id="card"><rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="12"/></clipPath>
<clipPath id="page"><rect width="1200" height="340" rx="18"/></clipPath>
</defs>
<g clip-path="url(#page)">
<rect width="1200" height="340" fill="{PAGE}"/>
<rect class="aura-v" width="1200" height="340" fill="url(#gv)"/>
<rect class="aura-f" width="1200" height="340" fill="url(#gf)"/>
</g>
<rect x=".5" y=".5" width="1199" height="339" rx="18" fill="none" stroke="{LINE}"/>
<text class="name" x="64" y="156">{NAME}</text>
<text class="tag" x="66" y="214">{escape(TAGLINE[0])}</text>
<text class="tag" x="66" y="250">{escape(TAGLINE[1])}</text>
<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="12" fill="{CARD}" stroke="{RULE}"/>
<line x1="{cx}" y1="{cy + 64}" x2="{cx + cw}" y2="{cy + 64}" stroke="{LINE}"/>
{code_line(INPUT[0], code_x, first_y)}
{state("vulnerable", VULNERABLE)}
{state("fixed", FIXED)}
<g clip-path="url(#card)"><rect class="sweep" x="{cx}" y="{cy + 63}" width="{cw}" height="2" fill="url(#gs)"/></g>
</svg>
"""
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(svg, encoding="utf-8", newline="\n")
    print(f"{OUT} {OUT.stat().st_size / 1024:.1f} KiB")


if __name__ == "__main__":
    main(*sys.argv[1:3])
