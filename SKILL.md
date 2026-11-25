---
name: design-language
description: Decide a product's brand identity and design language with an evidence-based process — the one association the brand should own, the logo or mark and app icon, brand colours and palette roles, typography, icon and illustration style, and the overall design theme. Use this skill whenever the user wants to choose, create, revisit or sanity-check a logo, app icon, brand colours, colour palette, theme, visual identity, "look and feel" or the foundations of a design system for an app, website or product. Also use it when they ask about the psychology of logos or colours, want an icon people will remember, ask what their brand colours should be, or are starting a new product and have not settled how it should look, even if they never say "design language".
---

# Design language

Help the user decide how a product looks and what it stands for, and leave them with a
decision they can defend: one association, one owned colour with a palette around it, a
mark that survives real-world tests, and the rules for everything else.

The output is a **decision**, reached by looking at rendered options together. It is not
a research report and not a mood board. Brand work is pleasant and visible, so it tends
to expand; keep it to one sitting where you can, and do not rebuild assets before the
user has picked.

## What the evidence says, in short

Read `references/evidence.md` for sources, sample sizes and grades. The load-bearing
points:

- **Design does not hardwire an association. Use does.** Nothing in the research shows a
  drawing alone makes people think of a category. Famous icons are the result of years of
  repeated pairing with the product. Design buys two things: faster early learning and
  being findable.
- **A descriptive mark helps an unknown brand most.** Depicting what the product does
  raises evaluations for unfamiliar brands, and the effect fades with familiarity. It
  reverses when the category is viewed negatively.
- **Uniqueness matters more than meaning.** An asset is worth having when it cues this
  brand and no other. Colour alone is the hardest asset to own; a shape plus a colour is
  far stronger.
- **People remember a gist.** Almost nobody can redraw a logo they see daily. One bold
  shape and one colour is all that is retained.
- **On a crowded screen, a colour unlike its neighbours is found fastest.**
- **Shape nudges traits, not liking.** Round reads caring, angular reads robust.
- **Behaviour cues belong in the product.** No study links a logo to saving, exercising
  or any behaviour; cues inside the product at the moment of action do work.

Say this plainly to the user, including when it contradicts what they hoped. Several
statistics that circulate in this area are untraceable; `evidence.md` lists them so they
are not repeated.

## The process

### 1. Read the ground

Before proposing anything, find what already exists: colour tokens, fonts, icon files,
design docs, the website, the app's splash and primary button. Render the current icon
and look at it.

Then frame the job as **ratify, evolve or replace**, with the incumbent as candidate
zero. Most products that ask for "a brand" already have most of one. Name what the files
actually leave undecided. It is usually only two or three things, for example: which
colour the brand owns (docs and icon often disagree), and whether the mark depicts
anything. Propose ratifying the rest in one line rather than reopening it.

If the project has a plan or a freeze on design work, say in one sentence that this is
outside it and time-box accordingly. Do not edit shipped assets during the decision.

### 2. Settle the one association

Ask what single thing the mark should bring to mind, and take the user's answer at face
value. Then pressure-test it once:

- **Depict an act or an object, not a promise.** "Helps me save money" is a promise; a
  coin going into a slot is an act. The famous marks the user will cite depict the act or
  the object too.
- **Check it against what the product does.** A mark that implies a different kind of
  product (a savings account when it is a tracker) sets the wrong expectation.
- **Check it against the product's own voice.** If the product refuses to give advice,
  the mark should not promise an outcome.

Write the association down in one sentence before any drawing. Candidates are judged
against it.

### 3. Research what changes per product

`evidence.md` and `platform-icons.md` cover the general findings. Fresh research is for
the market, the culture and this year's platform rules. Use the briefs in
`references/research-briefs.md`:

1. What is already on the user's screen: competitor and neighbour icon colours and
   pictograms, and lookalikes of the incumbent.
2. What the candidate colours and symbols mean to this audience.
3. The current platform icon requirements, from the vendors' docs.

Run them in parallel when subagents are available. The briefs carry rules learned the
hard way: ask questions rather than handing over a concept, require sources and grades,
keep private details out of queries, and time-box every brief so it returns.
`references/market-notes-india.md` is a worked example of the cultural check.

Start drawing while research runs; steps 4 and 5 do not depend on it, and the first
round of drafts always needs replacing anyway.

### 4. Draw candidates that span a real choice

Three or four candidates including the incumbent. Make them differ in **kind**, so the
user is choosing a direction and not a nuance:

- the incumbent, as it is
- one that depicts the act
- one that depicts the object
- one that evolves the incumbent toward the association, or depicts the name

Draw each as SVG in a 100 by 100 box using two to four flat filled shapes, with colours
written as placeholders so one drawing can be rendered in every appearance. Flat filled
shapes are what survives small sizes and what the platforms ask for.

### 5. Render them and look

Use `scripts/contact_sheet.py` (see the docstring for the JSON spec, and
`assets/example-spec.json` for a starting point). The script lives in this skill's
folder, not in the user's project, so call it by its full path and keep the spec and the
output in a scratch folder rather than in the project tree:

```bash
python3 <this skill's folder>/scripts/contact_sheet.py spec.json out_dir --name round1
```

It renders every candidate at real home-screen sizes, in dark, mono and one ink, blurred
for a squint test, and in a row of competitor-coloured tiles. Open the PNG and look at
it yourself **before** showing the user. Expect to throw most of round one away: simple
geometry collides with pictograms people already know, and you only see it once it is
rendered. `references/tests.md` lists the usual misreads and ways out.

Author the dark palette by hand. The derived one is a placeholder, and dark elements on
a dark field simply vanish.

Do two or three rounds. Stop when three candidates each read cleanly at 29 pt.

### 6. Put every candidate through the same tests

`references/tests.md` has the battery and a scorecard. The incumbent sits every test the
newcomers sit. A candidate that fails one ink, small size or truthfulness is out however
good it looks large.

### 7. Choose the owned colour

Decide this with the mark, since the icon is where the colour lives.

- Pick **one** owned colour and give every other colour a role: ground, ink, surfaces,
  semantic colours, data.
- Prefer a hue that is thinly used on the audience's screen and still fits the category
  and culture. Evidence on matching versus breaking the category colour is mixed;
  uniqueness is the safer bet for a newcomer.
- Check both meanings of the hue for this audience. A colour can be auspicious on a cover
  and alarming on a number.
- Reserve semantic colours for their meanings. If green means "money arrived", the brand
  cannot also be green without spending that signal.
- If existing tokens and the icon disagree, resolve it now and retire the stray hex.

### 8. Present, recommend, ask one question

Show the rendered candidates (inline if the environment can draw, otherwise the PNG),
the scorecard, and a recommendation with the reasoning. Then ask one question: which
direction. Do not stop at a research summary; the user asked for a decision.

Keep work private unless the user says otherwise. Do not publish candidates to a public
page or a repository on your own initiative.

### 9. Complete the language and record it

After the pick, settle the rest using `references/design-language-template.md` as the
checklist: type roles, shape, motion, iconography, imagery, voice, and a definition of
done. Most of it is usually ratification.

Record the decision where the project keeps decisions. Write a full design-language
document only if the user asks for one. Then, and only then, produce final assets to the
requirements in `references/platform-icons.md`, re-checking the vendors' pages first.

## Reference files

| File | Read it when |
|---|---|
| `references/evidence.md` | Grounding a claim, answering "what does the psychology say", or the user quotes a statistic |
| `references/research-briefs.md` | Writing briefs for market, culture and platform research |
| `references/tests.md` | Vetting candidates; checking for misreads; filling the scorecard |
| `references/platform-icons.md` | Drawing constraints and final asset specs for iOS, Android and web |
| `references/design-language-template.md` | Settling everything beyond the mark and colour |
| `references/market-notes-india.md` | The audience is Indian, or as a model for another market's notes |
| `scripts/contact_sheet.py` | Rendering candidates for comparison |

All paths above are relative to this skill's folder.

## Things that go wrong

- **Promising hardwiring.** The user often arrives believing a clever mark will make
  people think of the category. Correct this early and kindly; the rest of the decision
  gets easier once the mark's job is "be found, be recognised, be ours".
- **Research that confirms.** A brief that names the favoured concept returns it
  approved. Ask open questions and ask for disconfirming evidence.
- **Briefs that never return.** A forty-row audit with no budget can run until the
  session ends. Cap tool calls and accept rows marked as recalled.
- **Judging at large size.** Everything looks good at 240 px. Decide at 29 pt and in one
  ink.
- **A second reading.** If a mark can be read as a sunrise, it will be. Fix the drawing
  rather than explaining the intent.
- **Borrowed symbols.** A culturally rich symbol may already belong to a brand or a show
  in the same market. Search for the word as well as the image.
- **Starting over.** Replacing a whole system when two decisions were open wastes the
  equity already built and the user's time.
