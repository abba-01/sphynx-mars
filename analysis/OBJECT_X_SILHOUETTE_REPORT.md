# Silhouette Geometry of the Annotated Feature "Object X" in Mars Pathfinder Product PIA02406, and the Resolution Limit on Its Interpretation

**Framing (read first).** This report is written to be *defensible as measurement* and
*explicit about interpretation*. Everything in §§2–4 — the extraction, the angular
geometry, the size-versus-range relation, the resolution floor — is reproducible from
the repository and stands on its own. The identification of the feature as an artificial
form (a "sphinx," a "head," a "neck," a "fallen/eroded head") is **not** contained in any
of those numbers; it is a semantic layer added when the geometry is described in words
rather than mathematics, and §5 shows exactly where that layer enters and why the present
data cannot support it. In the language a referee would use: *the analysis is sound; the
interpretation is conjecture, and at this resolution the parsimonious (natural) reading
is favored.* Only source-resolution data from NASA — native IMP Experiment Data Record
frames, or orbital imagery — could move the interpretation.

## 1. Data and provenance

- Product: **PIA02406**, Mars Pathfinder IMP "Twin Peaks in Super Resolution – Right
  Eye," 7296 × 3135 px. In-repo copy `intake/00/PIA02406.tif`, SHA-256
  `49de98486fbfc1836e2feb26aecc7589bddad2de437bf706e64e5ba4df484199`, verified
  byte-identical to a NASA-session download (`data/PROVENANCE.md`).
- The catalog states the frames were **"enlarged by 500% and then co-added using Adobe
  Photoshop."** Hence 1 product px = 1/5 native px, and the native angular scale is
  0.98 mrad/native px (Smith et al. 1997, *JGR* 102(E2), doi:10.1029/96JE03568), i.e.
  **1 product px = 0.196 mrad.** Structure finer than the native pixel is interpolation,
  not information.
- Feature location: "Object X" is the annotated hummock-field feature at print ruler
  x ≈ 60–63 in. The intake markup family calibrates it to **PIA02406 product px
  ≈ x 4312–4500, y 522–635** (`intake/INTAKE_REVIEW.md`). This report is the right eye
  only; a left-eye (PIA02405) cross-measurement is future work.

## 2. Method (reproducible: `analysis/object_x_silhouette.py`)

1. Extract a measurement window (product px x[4285:4530], y[505:665]) around the
   annotated location.
2. Estimate the local terrain/background level by a wide Gaussian blur (σ = 30 px) and
   form the dark-feature residual (background − image, clipped ≥ 0).
3. Threshold at the 80th percentile of the residual and morphologically close (radius 3
   px) to merge adjacent dark elements into a single connected mass; take the largest
   connected component as the **cluster envelope**. (The separate sub-feature
   decomposition in step 4 uses the 88th percentile, un-closed — the two thresholds
   serve different purposes and are both reported here for reproducibility.)
4. Measure the envelope's bounding box, its **width profile** (envelope width per image
   row — the "neck" test), and, separately, decompose the un-closed thresholded field
   into **constituent dark sub-features** (connected blobs ≥ 4 px).
5. Convert product px → mrad (× 0.196), and mrad → metres as a function of assumed range
   Z (small-angle: size = Z · θ).

## 3. Results — the measured geometry

| Quantity | Value |
|---|---|
| Cluster envelope (this work) | 171 × 72 product px = **33.5 × 14.1 mrad**, aspect H/W = **0.42** |
| Annotator's ruler silhouette | 191 × 55 product px = 37.4 × 10.8 mrad, aspect 0.29 (length 2⅝ in, height ¾ in) |
| Constituent dark sub-features (88th-pct, un-closed) | **53 separate blobs**; largest 2062 product px **of area** = 82 native px² (bounding box 99 × 54 product px = 19.4 × 10.6 mrad; equivalent-square side 8.9 mrad); median blob 24 product px² ≈ 1 native px² |
| Width profile (top → down) | narrow apex (≈1–7.8 mrad) rising **monotonically** through the upper third to a broad basal mass (30.8 mrad); the sole interior width collapse lies at row 56 of 72 (**78 % down**, i.e. near the base, not mid-height), where width drops to 9 product px (1.8 mrad), separating the basal mass from a small lower lobe (max 5.1 mrad) |

The horizontal extent agrees between the independent pixel measurement (33.5 mrad) and
the annotator's ruler (37.4 mrad) to ~10 %. The vertical extent is less certain
(10.8–14.1 mrad) because the feature is **not skylined** — it sits within textured
terrain, so its lower boundary is set by where the segmentation threshold is drawn, not
by a sharp horizon.

**Absolute size is indeterminate**, because the range is unknown (Finding F6,
`VALIDATION_REPORT.md`: NASA's caption places the hummocks anywhere "from a few tens of
metres … to the distance of the South Twin Peak"):

| Assumed range Z | Envelope size | Resolution floor (2 native px) |
|---|---|---|
| 30 m (near field) | 1.0 × 0.4 m | 0.06 m |
| 100 m | 3.4 × 1.4 m | 0.20 m |
| 300 m | 10.1 × 4.2 m | 0.59 m |
| 860 m (North Twin) | 28.8 × 12.1 m | 1.69 m |
| 1006 m (South Twin) | 33.7 × 14.2 m | 1.97 m |

A **factor-of-~33 range ambiguity → a factor-of-~33 size ambiguity.** (Cross-check: at
860 m the 28.8 m width is consistent with the ×1.84-corrected ruler length of 31.9 m in
`VALIDATION_REPORT.md` §5.5 / `book/the-sphinx-on-mars.md`.)

## 4. What the geometry does and does not fix

- **Fixed (defensible):** there is a real, connected, dark, horizontally-elongated
  low mass at this location, ~33 × 14 mrad, tallest toward one end, with a measurable
  width collapse near its base (78 % down); it decomposes into ~53 sub-features. Note
  that the apex-to-body transition is a **monotone widening**, not a constriction.
- **Not fixed:** its absolute size (range unknown), and its morphology. At *every*
  plausible range the features that would distinguish carving from natural relief —
  edges, symmetry, a deliberate "neck" — are at or below the 2-native-px floor
  (0.06 m at 30 m; 1.7 m at 860 m), and the 500 % enlargement *manufactures* smooth
  structure below the native floor. The "one object" reading is itself a choice: the
  morphological close in step 3 is what merged 53 separate dark blobs into a single
  outline.

## 5. Where naming enters — the semantic layer, made explicit

This is the section the measurement exists to enable, and it is the point of the whole
exercise. Take the outline in `analysis/object_x_silhouette.png` and describe it in
words, and two parses fit the *same* geometry equally well:

- **Parse A (form):** a reclining figure — a raised **head** at one end, a **neck** at
  a width minimum, a **body** extending away; the head "short" relative to
  the Great Sphinx's proportions because it has **eroded or fallen away**, as the Great
  Sphinx's own nose/features have been whittled by time. At an assumed 860 m this is a
  ~29 m, sphinx-adjacent object.
- **Parse B (null):** an irregular low mound / rock outcrop with shadowed relief and
  surrounding talus — one of thousands of hummocks of flood debris NASA's caption
  describes — at an unknown distance and therefore an unknown size.

**The measured numbers are identical under both parses.** Everything that separates A
from B is supplied by the describer, not by the pixels:

1. *"Neck"* was, in an earlier draft of this report, said to name a real mid-height
   constriction. **That was wrong, and the corrected measurement weakens Parse A.** The
   width profile rises *monotonically* from apex to basal mass — there is no
   constriction between "head" and "body" at all. The only interior width collapse sits
   at 78 % of the envelope height, near the base, separating the basal mass from a small
   lower lobe: a position consistent with a shadow or talus boundary and not with
   anatomy. A width minimum in the wrong place is not a neck; the metric is real, the
   anatomy is conferred, and here the geometry does not even support the conferral.
2. *"Head eroded / fell off"* is the decisive tell, and it is **unfalsifiable at this
   resolution.** Positing the destruction of a feature to explain its absence can
   reconcile *any* silhouette with the monument hypothesis, and nothing in these data can
   check it — it is the "absence-of-evidence-as-evidence" move that the repository's
   method explicitly fences off. A hypothesis that survives only by invoking erosion of
   the parts that would have tested it has not been tested.
3. *Absolute scale* — the only thing that could make A "sphinx-sized" — requires
   assuming the range, which is exactly what the image cannot provide.

By parsimony and by the resolution gate, **Parse B is favored and Parse A is not
supported by the present data.** This is not a claim that A is impossible; it is a
statement that these images cannot license it, and that the felt force of A comes from
the semantic overlay, not the measurement.

## 6. The decisive test (how A vs B is actually settled)

The question is decidable, and not from a 1997 press mosaic. In map-projected orbital
imagery the range ambiguity vanishes and plan-dimensions and relief are measured
directly:

- HiRISE **PSP_001890_1995** (25 cm/px map-projected, lander visible) and stereo
  **PSP_002391_1995** (`data/SOURCING_LIST.md`, Tier A7–A9) — 0.25 m/px versus
  0.98 mrad × 860 m = 0.84 m/px for the IMP view, i.e. **3.4× finer linearly (11.4× by
  area)**, and — decisively — with no distance ambiguity at all.
- Native IMP **EDR frames** (PDS `MPFL-M-IMP-2-EDR-V1.0`, Tier A5) — the true
  0.98 mrad/px signal *without* the 500 % interpolation, to test whether any of the
  sub-2-native-px structure survives.

Until then the honest statement is the abstract's: the silhouette geometry is measured
and reproducible; the artificial-form interpretation is conjecture that the resolution
cannot support and that parsimony disfavors; and the felt anomaly is a demonstration of
how naming converts neutral structure into "something we recognize."

## 7. Reproducibility and sources

- Measurement: `python3 analysis/object_x_silhouette.py` (Pillow + numpy) →
  `analysis/object_x_silhouette.png` and the numbers in §3.
- Constants: Smith et al. 1997 (0.98 mrad/px); NASA catalog PIA02406 (500 % enlargement,
  product size), verified verbatim in `data/PROVENANCE.md`.
- Range indeterminacy, ×1.84 scale correction, resolution floor: `VALIDATION_REPORT.md`
  §§4–5, 7. Feature location: `intake/INTAKE_REVIEW.md`. Decisive-test data:
  `data/SOURCING_LIST.md`.

*This is an exploratory measurement note, not a claim of artificiality. Its persuasive
content is the geometry and its limits; its conclusion about interpretation is the null.*
