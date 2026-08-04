# Fixing the Zero Point: Why the Origin Cannot Be Repaired, and What Replaces It

**The question.** The original scale system needed a range origin. One was chosen: a
point on the print treated as 0, positioned at the bottom edge (the "43 inch mark,"
point D) after allowing for the camera's near-field foreshortening — the "nose." Given
that this choice was arbitrary and is now known to be wrong, *why not simply go back and
put the zero in the right place?*

**The short answer.** Because there is no right place. The origin is not merely
misplaced: the true reference line is at the opposite end of the print (§1), and the
model that requires an origin is the wrong *shape*, so no relocation can rescue it (§2).
The repair is not relocation; it is replacement. §3 then reports something better — read
against the correct reference, the annotation's own anchor marks turn out to be an
accurate measurement of the peaks, agreeing to 1 % with each other and to ~1 product
pixel with the machine. Results computed by `analysis/corrected_range_chart.py`;
the overlay is `analysis/corrected_overlay.py`.

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

## 3. CORRECTED — the anchors are summits, and read correctly they *measure the peaks*

**An earlier version of this section (2026-08-04, same day) claimed the two anchors were
"0.018 inches apart geometrically versus 0.375 inches as annotated, ×21 too far," and
concluded that the calibration baseline carried no range information. That was wrong,
and the error is instructive.** It applied the *ground-range* depression formula
Z = h_cam/tan θ to two marks that are not ground points at all.

The annotation's own table settles what B and C are: `B. 4 7/8 TO F. 7 7/16 = 2 9/16`.
The interval from B to F is 2.5625 in — exactly the North Twin height measurement. So
**B is the summit of North Twin and F its visible base**; C is likewise the South Twin
summit. They are not ground positions, and the depression formula does not apply to them.

Read correctly, a summit's elevation *above the horizon* is θ = h_peak/Z, and the marks
become a measurement:

| Anchor | Elevation above horizon | Range | h = Z·θ |
|---|---|---|---|
| B, North Twin summit | 2.405 in = 34.4 mrad | 860 m | **29.6 m** |
| C, South Twin summit | 2.030 in = 29.0 mrad | 1006 m | **29.2 m** |

The two independent solutions **agree with each other to 1 %** and sit just below NASA's
published 30–35 m. And the predicted separation of the two marks for peaks ~30 m tall is
0.354 in against the 0.375 in actually annotated — a 6 % match. **The anchor separation
is geometrically meaningful after all**; it encodes summit elevation h/Z, not ground range.

Two further checks of the annotation's quality, both passing:

- The B and C marks land on product rows 355.4 and 382.8; the pipeline's independently
  measured apex rows are 356 and 382. **Agreement within 1 product pixel** (0.2 native px,
  0.04 mrad).
- The North Twin base mark F (7.4375 in) sits 0.16 in below the measured horizon line
  (7.28 in) — i.e. the peak's visible base is essentially *on* the horizon, exactly as the
  geometry requires for a distant peak whose true base is occluded.

### What still fails, and now for the right reason

The linear model remains invalid, and the anchors prove it cleanly. The true relation is
Z = h/θ, so **Z × (inches above horizon) is constant** for peaks of equal height:

- North: 860 × 2.405 = 2068
- South: 1006 × 2.030 = 2042  (agreement 1.3 %)

The hyperbolic law holds. The annotation's *linear* law does not: propagating North's
factor (73.44 ft/in) to South predicts 2772 ft where the caption says 3300 ft — **−16 %**.
That single failure is why two mutually inconsistent factors (73.44 and 87.42 ft/in) were
needed at all. Forcing a hyperbolic relation into a linear form requires a new constant at
every anchor, which is precisely the symptom recorded in `VALIDATION_REPORT.md` §5.2.

And the deeper circularity stands: recovering Z from a summit's elevation requires knowing
h — the peak height — which is the quantity the exercise set out to measure. The marks can
give height *given* range (as above), or range *given* height, but never both.

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
