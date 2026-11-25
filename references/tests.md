# Tests every candidate goes through

Run the incumbent and every new candidate through the **same** tests, on the same sheet.
A test that only the favourite sits is a formality. `scripts/contact_sheet.py` produces
most of what is needed in one image.

## The battery

| # | Test | How | Why it matters |
|---|---|---|---|
| 1 | Small-size legibility | View at 60, 40 and 29 pt and at 16 px. Is it still the same picture? | Most sightings are small. Apple advises reviewing at real size on the Home Screen and in Settings |
| 2 | Squint | Blur it or look from across the room. One shape should survive | People remember a gist, not details |
| 3 | No label | Hide the name. Does it still say what kind of thing this is, or at least look like nothing else? | Apple's own check: recognisable without its label |
| 4 | One ink | Every part in a single colour on white | Print, PDFs, stamps, monochrome themes. Parts separated only by colour merge into a blob |
| 5 | Dark | On a near-black field, authored rather than auto-derived | Dark elements vanish; a "hole" drawn in dark has to become something else |
| 6 | Mono / tinted | Greyscale, most recognisable element white | iOS clear and tinted modes and Android themed icons are built from this |
| 7 | Neighbour | Place it in a row of plain tiles in the colours already on the user's screen | A colour unlike its neighbours gives the largest search-speed effect |
| 8 | Masks | Circle and squircle crops, content within the central ~60% | Android masks vary by device |
| 9 | Misread | Ask what else it could be. Use the table below, then ask someone who has not seen the brief | A second reading dilutes the first |
| 10 | Confusion | Search for existing marks built from the same construction, in any category | Lookalikes cost uniqueness and can bring legal trouble |
| 11 | Truth | Does the picture promise something the product does not do? | A mark that implies the wrong category sets the wrong expectation in a store listing |
| 12 | Portability | Does it depend on a currency sign, a letter, a script or a local symbol? | Matters when other markets or languages are on the roadmap |

Sources for the tests: Apple's icon design sessions and Icon Composer documentation
(1, 3, 5, 6), Android's adaptive-icon guide (8), Nielsen Norman Group on icon testing,
recognition out of context and time-to-find in context (3, 9), Trapp and Wienrich 2018
(7). Details and links are in `evidence.md` and `platform-icons.md`.

Tests 9 to 11 are judgement. Do them honestly against your own favourite; that is where
they are most useful.

## Common misreads

Simple geometric marks collide with pictograms people already know. These came up while
drafting real candidates; check for them before showing anything.

| Construction | Reads as |
|---|---|
| Circle partly hidden by a horizontal bar or edge | Sunrise or sunset, a service bell, a bowler hat |
| Circle floating above a short bar | Webcam, record button |
| Circle above a wider rounded shape | Person or profile avatar, a pawn |
| Three equal horizontal bars | Menu button |
| Three bars of decreasing length | Sort or text-alignment glyph, signal strength |
| Stacked cylinders | Database |
| Three stacked rounded layers or chevrons | The generic "layers" glyph, and several existing brand marks |
| Round body with a small nub on top | Bomb, ornament, perfume bottle; an onion when the neck is smooth |
| Small tilted ellipse on top of a round body | Fruit with a leaf |
| Circle with a wedge or crescent in a second colour | Pie chart, moon phase |
| A row of circles of decreasing size | Loading dots, planets |

Ways out that worked: tilt or turn the object so it cannot be the familiar pictogram (a
tilted ellipse is a coin, never a sun); add the one detail that fixes the meaning (a
slot turns a pot into a money box); give the body a foot or a collar so it reads as an
object rather than a blob.

## Scorecard

Fill one row per candidate and show it to the user with the rendered sheet. Use plain
words (pass, weak, fail) and say why in a few words for anything that is not a pass.

| Candidate | Small | Squint | One ink | Dark | Mono | Neighbour | Misread risk | Lookalikes | Truthful | Portable |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 incumbent | | | | | | | | | | |
| 1 | | | | | | | | | | |
| 2 | | | | | | | | | | |

A candidate that fails one ink, small size or truthfulness is out, however good it looks
large. Everything else is a trade-off to put in front of the user.
