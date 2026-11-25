# design-language

A Claude skill for deciding a product's brand identity and design language: the one
association the brand should own, the logo and app icon, brand colours, typography, icon
style and the overall theme.

It is built around an evidence review of what is actually known about logos, colour and
icons, and a process that ends in a decision made by looking at rendered options.

## What is in it

| Path | What it is |
|---|---|
| `SKILL.md` | The process: read the ground, settle the association, research, draw, render, test, choose, record |
| `references/evidence.md` | Findings on how marks acquire meaning, descriptive versus abstract logos, shape, colour, distinctive assets and icon findability, each with a source and an evidence grade, plus the popular statistics that do not hold up |
| `references/research-briefs.md` | Ready-to-adapt briefs for market, culture and platform research |
| `references/tests.md` | The test battery every candidate sits, common misreads of simple geometric marks, and a scorecard |
| `references/platform-icons.md` | iOS, Android and web icon requirements (compiled November 2026; re-check before shipping) |
| `references/design-language-template.md` | The sections of a one-page design language |
| `references/market-notes-india.md` | A worked example of the cultural colour and symbol check |
| `scripts/contact_sheet.py` | Renders logo candidates at real sizes, in dark, mono and one ink, with a squint test and a neighbour test |

## Install

Personal skill for Claude Code (available in every project):

```bash
git clone https://github.com/sciboyrocks/design-language-skill ~/.claude/skills/design-language
```

Update later with:

```bash
git -C ~/.claude/skills/design-language pull
```

## Use

Ask Claude something like "help me pick brand colours and a logo for this app", or
invoke it directly with `/design-language`.

The contact sheet script also works on its own:

```bash
python3 scripts/contact_sheet.py assets/example-spec.json out --name example
```

It needs Python 3 and no extra packages. It writes an SVG, and a PNG when one of
rsvg-convert, resvg, inkscape, ImageMagick or macOS Quick Look is available.

## A note on the evidence

The research was compiled in November 2026. Samples behind most findings are Western
students or online panels, several sources were read as abstracts only, and platform
rules change yearly. Each reference file says how its rows were verified. Treat the
grades as a guide to how hard to lean on a claim.
