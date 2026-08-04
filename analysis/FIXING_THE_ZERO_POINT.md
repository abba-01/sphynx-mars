# Fixing the Zero Point: Why the Origin Cannot Be Repaired, and What Replaces It

**The question.** The original scale system needed a range origin. One was chosen: a
point on the print treated as 0, positioned at the bottom edge (the "43 inch mark,"
point D) after allowing for the camera's near-field foreshortening — the "nose." Given
that this choice was arbitrary and is now known to be wrong, *why not simply go back and
put the zero in the right place?*

**The short answer.** Because there is no right place. The origin is not merely
misplaced — the model that requires an origin is the wrong shape, the true reference
line is at the opposite end of the print, and the two anchors used to calibrate it are,
in the real geometry, effectively on top of each other. The repair is not relocation;
it is replacement. All three results below are computed by
`analysis/corrected_range_chart.py`.

---

## 1. The true reference is the horizon, not the bottom edge — and it is a singularity

For a camera at height *h* over locally level ground, a point at range *Z* appears at
depression angle **θ = arctan(h/Z)** *below the horizon*. The reference line is
therefore the horizon, and range is read **downward** from it.

Measured on the repository's own product, the horizon sits at **print inch 7.28 from the
top edge**. The original zero was at inch 43.0 — the bottom edge, **35.7 inches away, at
the far end of the print, and in the opposite direction of measurement.**

And the horizon is not a "zero" in any usable sense. As θ → 0, Z → ∞. The reference
point of the correct model is a **singularity**, not an origin. A scale cannot be hung
from it the way the annotation hung one from point D.

## 2. No origin makes a linear model correct

Z = h/tan θ is hyperbolic. Relocating the origin changes which numbers come out; it
cannot change the functional form. A linear print-position-to-range mapping is wrong at
*every* origin.

The magnitude of the mismatch, from the computed chart (h = 1.5 m nominal):

| Inches below horizon | Depression | True range | Original linear model |
|---|---|---|---|
| 0.25 | 3.6 mrad | 420 m | 794 m |
| 1.00 | 14.3 mrad | 105 m | 777 m |
| 2.00 | 28.6 mrad | 52.5 m | 755 m |
| 4.00 | 57.2 mrad | 26.2 m | 710 m |
| 8.00 | 114.3 mrad | 13.1 m | 620 m |
| 16.00 | 228.6 mrad | 6.4 m | 441 m |
| 35.72 (bottom edge) | 510.4 mrad | **2.7 m** | **0 m** |

The two columns do not differ by a constant, a factor, or anything an origin shift could
absorb. Where the linear model says 0 m, the ground is at 2.7 m; where it says 620 m,
the ground is at 13 m.

## 3. The decisive result: the calibration anchors are 0.018 inches apart

This is the finding that closes the question. The whole system was calibrated on two
anchors of known range — North Twin at 860 m and South Twin at 1006 m. In the true
geometry, those two ranges plot at:

- North Twin: **0.1221 inches** below the horizon
- South Twin: **0.1044 inches** below the horizon

a separation of **0.0177 inches — about 18 thousandths of an inch.** The annotation
placed them **0.375 inches** apart: **21× too far.**

So the vertical separation the annotation measured between its two anchors — the very
quantity from which both feet-per-inch factors were derived — encodes **almost no range
information at all.** What it actually encodes is *where occluding ridge terrain cuts off
the visible base of each peak*. The calibration baseline is terrain, not distance.

That is why relocating the zero cannot rescue the system: you cannot fit a range scale
through two points that the geometry places 18 thousandths of an inch apart while your
measurement places them 375 thousandths apart. Any origin that reproduces one anchor
badly misses the other — which is exactly the observed symptom, the mutually
inconsistent factors 73.44 and 87.42 ft/in (19% apart) reported in
`VALIDATION_REPORT.md` §5.2.

A second confirmation from the same geometry: the anchors' *ordering* is wrong. The
farther peak (South Twin, 1006 m) must plot **higher** on the print (0.1044 in below the
horizon) than the nearer one (North Twin, 0.1221 in). The annotation places the nearer
peak higher. The observed ordering is set by terrain, and it is inverted relative to
range.

---

## What replaces it

**For transverse size — the measurement that actually mattered — no origin is needed at
all.** The angular relation

    s = Z · N · IFOV

requires only the range and the angular extent. It has no datum, no zero mark, and no
"nose." This is why the corrected pipeline works and why it passes the known-answer test
(31.5 m and 28.7 m against NASA's published 30–35 m, `VALIDATION_REPORT.md` §5.4): the
corrected model does not repair the origin, it **eliminates the concept**.

**For near-field range,** the chart in §2 is the honest ruler — the thing the original
system was reaching for, built correctly: measure downward from the horizon, convert
depression to range hyperbolically. Its validity conditions are strict and must be stated
with any use: locally level ground, no intervening relief, and — per
`SIZE_VERIFICATION_METHODOLOGY.md` Step 3c — only below ~50 m, since a ±2-native-px
uncertainty in the horizon row moves Z by more than 100% beyond ~380 m (h = 1.5 m) /
~470 m (h = 1.85 m). Note that the Twin Peaks scene fails the level-ground condition
outright ("bouldery ridges and swales," per the caption), so the chart is offered as the
correct *form* of the calculation, not as a licence to range this particular terrain.

**For far-field range,** nothing on the print will ever work. It comes from orbital
cartography (`data/SOURCING_LIST.md` Tier A7–A9), which is where the program's decisive
test goes.

---

## Why this matters beyond the ruler

The instinct behind the original zero was sound: *something* has to anchor a scale, and
the near-field foreshortening is real. What went wrong was not carelessness — it was that
an arbitrary choice, once made, stopped looking arbitrary. The origin was fixed on some
particular afternoon; by the next week it was simply *where zero was*, and every number
derived afterward inherited an authority the geometry never granted it.

The correction is instructive precisely because it is not a nudge. The reference line was
at the wrong end of the print, measured in the wrong direction, in a model of the wrong
shape, calibrated on a baseline that carries no signal. And yet the *measurements* taken
against it were accurate to about one camera pixel. That is the separation this project
keeps returning to: **the observations were good; the frame around them was invented, and
inventions harden into facts unless something external is allowed to test them.**

*Computed by `analysis/corrected_range_chart.py`; horizon located from `preview.webp` via
the same skyline routine used in `analysis/measure_twin_peaks.py`. Camera height 1.5 m
nominal / 1.85 m as-deployed (NASA/JPL instrument description). Angular scale
14.29 mrad/print-inch from the 43-inch ruler across the 3135-px product height.*
