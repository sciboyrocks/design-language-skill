# The design language, on one page

Once the association, the owned colour and the mark are chosen, write the rest of the
language down as rules with reasons. The goal is a page from which a new decision can be
**derived instead of guessed**: someone designing a screen that does not exist yet should
be able to work out what it looks like.

Keep it to one page that people read first. Tokens, state machines and screen specs can
live in deeper documents that must not contradict it. If the project already has such a
page, edit it rather than starting a rival.

Write only when the user asks for the document. Otherwise use these sections as the
checklist of decisions to settle in conversation.

## Sections

**1. Thesis.** One sentence saying what the product should feel like, and two or three
more that carry the whole language. Every later rule should trace back to these. Name
two or three reference products and the single thing taken from each.

**2. The association.** The one thing the brand stands for, in the user's words, and
what the mark depicts to carry it.

**3. Physical model.** What the interface is made of (paper, glass, a dark room with lit
surfaces) and where depth comes from. Light and dark modes may use different models on
purpose; say so.

**4. Colour.**
- *Ground and ink*: a short ladder of neutrals for backgrounds, surfaces, lines and text,
  with light and dark values side by side.
- *The owned colour*: one accent, what it is allowed to do (primary actions, the one
  live data series, anything asking for attention) and a cap on how often it appears.
- *Semantic colours*: what success, warning and failure look like, and what they are
  **not** allowed to mean. Decide whether failure colour describes the system's errors
  only or also the user's situation.
- *Data colours*: neutral marks plus one accented series beats a hue per category.
- Never carry information by hue alone. State the contrast floor.

**5. Typography.** One job per face: headings, interface text, numbers, labels, the
wordmark. Say why each face has its job. Rules for numerals (tabular figures, local
number grouping, how negatives and unknowns are written).

**6. Space, shape, elevation.** The spacing scale, corner radii, row heights, hit
targets, how many elevation levels a screen may have, and when to use a card versus a
row.

**7. Motion and haptics.** One curve for everything the user caused. What motion is for
(explaining where something came from) and where it is banned. What Reduce Motion does.

**8. Iconography.** Prefer the platform's own symbol set for interface icons and say
which weight and scale. Reserve drawn icons for the brand's own objects.

**9. Imagery.** The illustration or photo style in one sentence, its palette, and where
it is allowed to appear.

**10. The mark in use.** The app icon in each appearance, the one-ink version, the
wordmark, clear space, minimum size, and the things nobody may do to it.

**11. Voice.** Who speaks, in which person, and a banned list. Facts or advice.

**12. Accessibility floor.** Contrast, type scaling, screen-reader wording, reduced
motion and reduced transparency.

**13. Definition of done.** A checklist a screen must pass. This is what makes the rules
enforceable.

## Rules of thumb for the rules

- **Restraint reads as premium.** One accent, used rarely. Richness comes from type,
  space and real content.
- **Reserve a colour for a meaning and it keeps the meaning.** Spend it on decoration and
  it is gone.
- **Familiarity beats novelty** for controls and navigation; save invention for the mark
  and the moments that are yours.
- **Every rule gets its reason.** A rule without one is dropped the first time it is
  inconvenient.
- **Record what was tried and failed**, so nobody re-runs the experiment.
