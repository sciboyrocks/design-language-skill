#!/usr/bin/env python3
"""Render logo / app-icon candidates side by side so they can be judged by looking.

For every candidate the sheet shows:
  - the default icon, large
  - true home-screen sizes at 2x (60pt, 40pt, 29pt) and a 16px favicon at 2x
  - a squint test (the 60pt tile, blurred)
  - the dark appearance and a mono / tinted appearance
  - a single-ink version on white, large and at favicon size
and, when competitor colours are supplied, a neighbour strip: each candidate sitting in a
row of plain tiles in the colours already on the user's home screen.

Usage:
    python3 contact_sheet.py spec.json out_dir [--name sheet]

Writes out_dir/<name>.svg and, when a renderer is installed, out_dir/<name>.png.
Renderers tried in order: rsvg-convert, resvg, inkscape, magick, qlmanage (macOS).
No third-party Python packages are needed.

Spec (JSON):
{
  "candidates": [
    {
      "name": "0 current",
      "svg": "<circle cx='50' cy='50' r='24' fill='{a}'/>",
      "palettes": {
        "default": {"bg": "#F3EFE5", "a": "#103C32", "b": "#C0562F"},
        "dark":    {"bg": "#1C1B1A", "a": "#E7E5E1", "b": "#F08A63"}
      }
    }
  ],
  "neighbours": ["#5F259F", "#00BAF2", "#00D09C", "#0B0B0B", "#FFFFFF"]
}

Drawing rules for "svg":
  - Draw the mark only, in a 100 x 100 box. The rounded-square field is added for you
    and filled with the palette's "bg".
  - Write colours as placeholders: {bg} plus any keys you like ({a}, {b}, {coin}, ...).
    Every key used must exist in the "default" palette.
  - If the fragment needs an id (clipPath, mask), write it as "{id}" so each copy on the
    sheet gets a unique one, e.g. <clipPath id='{id}'> ... clip-path='url(#{id})'.

Palettes "dark", "mono" and "one" are optional. Missing ones are derived:
  dark: the default colours on a near-black field
  mono: first colour key white, the rest mid grey, on dark grey (stands in for tinted)
  one : every colour the same ink on white. If the mark collapses into a blob here, its
        parts are separated only by colour and it needs gaps or knock-outs.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

INK = "#1A1A1A"
SHEET_BG = "#E9E6DF"
LABEL = "#222222"
CAPTION = "#6B6B66"
OUTLINE = "#C9C4B8"

_counter = [0]


def _fill(fragment, palette):
    _counter[0] += 1
    out = fragment.replace("{id}", f"cs{_counter[0]}")
    for key, value in palette.items():
        out = out.replace("{" + key + "}", value)
    return out


def _derive(palettes):
    default = palettes["default"]
    keys = [k for k in default if k != "bg"]
    full = dict(palettes)
    if "dark" not in full:
        full["dark"] = {**default, "bg": "#1C1B1A"}
    if "mono" not in full:
        mono = {"bg": "#2C2C2C"}
        for i, key in enumerate(keys):
            mono[key] = "#FFFFFF" if i == 0 else "#8C8C8C"
        full["mono"] = mono
    if "one" not in full:
        full["one"] = {"bg": "#FFFFFF", **{key: INK for key in keys}}
    return full


def _tile(cand, palette, x, y, size, outline=False, blur=False):
    scale = size / 100.0
    stroke = f' stroke="{OUTLINE}" stroke-width="1"' if outline else ""
    filt = ' filter="url(#squint)"' if blur else ""
    return (
        f'<g transform="translate({x} {y}) scale({scale})"{filt}>'
        f'<rect width="100" height="100" rx="22.5" fill="{palette["bg"]}"{stroke}/>'
        f'{_fill(cand["svg"], palette)}</g>'
    )


def _text(x, y, s, size=13, colour=CAPTION):
    safe = s.replace("&", "&amp;").replace("<", "&lt;")
    return f'<text x="{x}" y="{y}" font-family="Helvetica, Arial, sans-serif" font-size="{size}" fill="{colour}">{safe}</text>'


def build(spec):
    cands = spec["candidates"]
    for cand in cands:
        cand["_pal"] = _derive(cand["palettes"])
    neighbours = spec.get("neighbours") or []

    col_w, pad = 300, 30
    per_row = min(len(cands), 4)
    block_h = 800
    rows = (len(cands) + per_row - 1) // per_row
    strip_h = (len(cands) * 104 + 60) if neighbours else 0
    width = pad * 2 + col_w * per_row - 30
    height = pad + rows * block_h + strip_h
    side = max(width, height)  # square canvas: some thumbnailers crop to a square

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{side}" height="{side}" viewBox="0 0 {side} {side}">',
        '<defs><filter id="squint" x="-10%" y="-10%" width="120%" height="120%">'
        '<feGaussianBlur stdDeviation="5"/></filter></defs>',
        f'<rect width="{side}" height="{side}" fill="{SHEET_BG}"/>',
    ]

    for i, cand in enumerate(cands):
        pal = cand["_pal"]
        x = pad + (i % per_row) * col_w
        y0 = pad + (i // per_row) * block_h
        out.append(_text(x, y0 + 16, cand["name"], 17, LABEL))
        out.append(_tile(cand, pal["default"], x, y0 + 32, 240, outline=True))
        y = y0 + 300
        out.append(_text(x, y, "60 / 40 / 29 pt and 16 px, at 2x"))
        out.append(_tile(cand, pal["default"], x, y + 10, 120, outline=True))
        out.append(_tile(cand, pal["default"], x + 132, y + 10, 80, outline=True))
        out.append(_tile(cand, pal["default"], x + 222, y + 10, 58, outline=True))
        out.append(_tile(cand, pal["default"], x + 222, y + 78, 32, outline=True))
        y = y0 + 456
        out.append(_text(x, y, "dark / mono"))
        out.append(_tile(cand, pal["dark"], x, y + 10, 120))
        out.append(_tile(cand, pal["mono"], x + 132, y + 10, 120))
        y = y0 + 612
        out.append(_text(x, y, "one ink / squint"))
        out.append(_tile(cand, pal["one"], x, y + 10, 120, outline=True))
        out.append(_tile(cand, pal["one"], x + 132, y + 10, 32, outline=True))
        out.append(_tile(cand, pal["default"], x + 176, y + 10, 104, blur=True))

    if neighbours:
        y = pad + rows * block_h
        out.append(_text(pad, y + 16, "neighbour test: each candidate among colours already on the home screen", 15, LABEL))
        tile, gap = 76, 22
        for i, cand in enumerate(cands):
            ry = y + 36 + i * 104
            slots = neighbours[:3] + [None] + neighbours[3:7]
            for j, colour in enumerate(slots):
                tx = pad + j * (tile + gap)
                if colour is None:
                    out.append(_tile(cand, cand["_pal"]["default"], tx, ry, tile, outline=True))
                else:
                    out.append(
                        f'<rect x="{tx}" y="{ry}" width="{tile}" height="{tile}" rx="{tile * 0.225}" '
                        f'fill="{colour}" stroke="{OUTLINE}" stroke-width="1"/>'
                    )
            out.append(_text(pad + len(slots) * (tile + gap) + 6, ry + 44, cand["name"]))

    out.append("</svg>")
    return "".join(out), side


def render(svg_path, png_path, side):
    px = str(min(max(side, 1200), 2400))
    attempts = [
        ("rsvg-convert", ["rsvg-convert", "-w", px, "-o", str(png_path), str(svg_path)]),
        ("resvg", ["resvg", "-w", px, str(svg_path), str(png_path)]),
        ("inkscape", ["inkscape", str(svg_path), "--export-type=png", f"--export-filename={png_path}", "-w", px]),
        ("magick", ["magick", "-background", "none", "-density", "192", str(svg_path), str(png_path)]),
    ]
    for tool, cmd in attempts:
        if shutil.which(tool):
            result = subprocess.run(cmd, capture_output=True)
            if result.returncode == 0 and png_path.exists():
                return tool
    if shutil.which("qlmanage"):
        subprocess.run(["qlmanage", "-t", "-s", px, "-o", str(png_path.parent), str(svg_path)], capture_output=True)
        produced = png_path.parent / (svg_path.name + ".png")
        if produced.exists():
            produced.replace(png_path)
            return "qlmanage"
    return None


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    spec_path, out_dir = Path(argv[1]), Path(argv[2])
    name = argv[argv.index("--name") + 1] if "--name" in argv else "sheet"
    spec = json.loads(spec_path.read_text())
    for cand in spec["candidates"]:
        missing = [k for k in ("name", "svg", "palettes") if k not in cand]
        if missing or "default" not in cand.get("palettes", {}):
            print(f"candidate {cand.get('name', '?')}: needs name, svg and palettes.default")
            return 2
    out_dir.mkdir(parents=True, exist_ok=True)
    svg, side = build(spec)
    svg_path = out_dir / f"{name}.svg"
    png_path = out_dir / f"{name}.png"
    svg_path.write_text(svg)
    print(f"wrote {svg_path}")
    tool = render(svg_path, png_path, side)
    if tool:
        print(f"wrote {png_path} (rendered with {tool})")
    else:
        print("no SVG renderer found: open the .svg in a browser, or install librsvg (rsvg-convert)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
