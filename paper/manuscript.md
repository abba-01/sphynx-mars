# Angular Re-derivation of Feature Dimensions from a Historical Mars Pathfinder Super-Resolution Product: Correction of a ×1.84 Scale-Model Error, Validation Against Published Ground Truth, and a Null Result for an Anomalous Feature

**E. D. Martin**¹

¹ Independent researcher. *(Affiliation and corresponding-author details to be completed before submission.)*

**Manuscript status.** Draft prepared for submission as a methods/measurement note
(target: *Planetary and Space Science*, or preprint under arXiv astro-ph.IM/astro-ph.EP).
**Not yet submitted; not yet peer reviewed.** All analysis, data, and code are public so
that any reader may execute the referee's role directly (§Data and Code Availability).

---

## Abstract

Historical planetary press products — mosaics prepared for public release rather than for
photogrammetry — are frequently used as measurement substrates by non-specialists, and
occasionally by specialists, without accounting for the processing applied to them. We
examine a documented case: a hand-measured, ruler-based scale system applied to a
large-format print of the Mars Pathfinder Imager for Mars Pathfinder (IMP)
"super-resolution" Twin Peaks mosaics (NASA products PIA02405/PIA02406), whose catalog
text states the constituent frames were "enlarged by 500% and then co-added using Adobe
Photoshop." We show that (i) the linear mapping of range to vertical print position
underlying the original system is geometrically invalid, since ground range at the frame
bottom is ~2.7–3.3 m rather than zero and the interval 860 m → ∞ compresses into ~1.7
native pixels; (ii) the resulting per-anchor conversion factors (73.44 and 87.42 ft
inch⁻¹) overestimate the true *transverse* angular scale (40.0 and 47.2 ft inch⁻¹) by a
factor of **1.84**, whose closed form is 1/(38.125 in × 0.01429 rad in⁻¹) = 1.836; and
(iii) stereo ranging of the peaks from these products is infeasible, the geometric
disparity at 860 m being 0.174 native px while the two independently assembled mosaics
differ in framing by 161–172 product px, ~200× larger. Applying the corrected angular
relation to the *unaltered original ruler measurements* returns North and South Twin Peak
heights of 31.5 m and 28.7 m, recovering the independently published value of "30–35
metres" and thereby passing a known-answer test that the uncorrected system fails
(57.4 m). The measurements were therefore accurate at approximately the native-pixel
level; the scale model, not the measurement, was in error. We then characterise the
silhouette of the annotated anomalous feature ("Object X") in the full-resolution right-eye
product: a connected dark cluster of 33.5 × 14.1 mrad (aspect 0.42) that decomposes into
53 sub-features and whose absolute size is indeterminate across a factor-of-33 range
ambiguity (1.0 × 0.4 m at 30 m to 33.7 × 14.2 m at 1006 m). At every plausible range the
morphological detail that would discriminate artificial from natural relief lies at or
below the two-native-pixel floor (0.06–1.97 m), a regime in which the 500% enlargement
generates interpolated structure. We conclude that the feature's anomalous appearance is
not supported as evidence of artificiality by these data, identify the decisive
observations that would settle the question (orbital map-projected imagery; native IMP
Experiment Data Records), and discuss the general result that measurement fixes geometry
while identification is supplied by the describer.

**Keywords:** Mars Pathfinder; photogrammetry; angular size measurement; image resolution;
data provenance; pareidolia; null result

---

## 1. Introduction

Two distinct failure modes recur when planetary images reach a general audience. The
first is *provenance loss*: a product prepared for public release is treated as
calibrated data, and the processing history that would forbid certain measurements is
not carried forward. The second is *identification without scale*: a striking morphology
is named before its dimensions or range are established, after which subsequent
measurement tends to be organised around the name.

The Mars Pathfinder "Twin Peaks in Super Resolution" products (PIA02405, left eye;
PIA02406, right eye) are an instructive substrate for both. They are visually detailed,
widely reproduced, and — per their own catalog text — assembled by five-fold enlargement
and co-addition in a raster graphics editor, then colourised. They are consequently
geometry-approximate and detail-unreliable at the sub-native-pixel level, while
*appearing* to be high-resolution data.

This paper analyses a specific, documented measurement campaign conducted on a
large-format (~99 in) print of PIA02405 by one of us, in which a 43-inch ruler axis was
imposed on the print and object dimensions were derived from per-anchor
feet-per-inch conversion factors calibrated against the two Twin Peaks, whose distances
NASA's caption states. The campaign produced an apparent anomaly: a feature designated
"Object X" whose derived dimensions (192.8 ft × 55.1 ft) were 80% and 83% of the
published dimensions of the Great Sphinx of Giza, with an almost identical aspect ratio.

We treat this as a test case rather than an anecdote. The questions are: what
does the correct angular treatment give; does the corrected pipeline pass an independent
known-answer test; what can and cannot be established about the anomalous feature; and
what general lesson applies to measurement on historical press products.

Our contribution is fourfold: a quantified diagnosis of the scale-model error with a
closed-form correction factor; a known-answer validation of the corrected pipeline against
NASA's published peak heights; a reproducible silhouette characterisation of the
anomalous feature with a full range-ambiguity treatment; and an explicit account of where
identification enters an otherwise neutral measurement chain. The result for the anomaly
is null, and is reported as such.

## 2. Data and provenance

### 2.1 Products

Analysis uses the full-resolution NASA Photojournal products, held locally and
hash-verified:

| Product | Dimensions | Bytes | SHA-256 (first 16) |
|---|---|---|---|
| PIA02405 (left eye) | 7238 × 3135 | 65,926,165 | `d32ee9af29b6505e` |
| PIA02406 (right eye) | 7296 × 3135 | 70,574,265 | `49de98486fbfc183` |

Both match the dimensions stated on their catalog pages; the left-eye byte count matches
the catalog's stated 65.93 MB. Independent copies acquired in a separate,
timestamp-documented session from science.nasa.gov are byte-identical to the analysis
inputs, satisfying the provenance check.

### 2.2 Processing history (the constraint that governs everything downstream)

The catalog text for PIA02405 states, verbatim:

> "The composite color frames that make up this 'left-eye' image consist of 8 frames,
> taken with different color filters that were **enlarged by 500% and then co-added using
> Adobe Photoshop** to produce, in effect, a super-resolution panchromatic frame that is
> sharper than an individual frame would be. This panchromatic frame was then colorized
> with the red, green, and blue filtered images from the same sequence."

and, for scale and range:

> "The peaks are approximately 30-35 meters (~100 feet) tall. North Twin is approximately
> 860 meters (2800 feet) from the lander, and South Twin is about a kilometer away
> (3300 feet). The scene includes bouldery ridges and swales or 'hummocks' of flood debris
> that range from a few tens of meters away from the lander to the distance of the South
> Twin Peak."

Both passages were verified word-for-word against pages saved directly from NASA in an
independent session.

Two consequences follow immediately and are used throughout. First, one product pixel
corresponds to 1/5 native IMP pixel; with the IMP instantaneous field of view of
0.98 mrad px⁻¹ (Smith et al., 1997), **1 product px = 0.196 mrad**. Second, structure
finer than one native pixel in these products is interpolation, not measurement.

### 2.3 Instrument constants

From Smith et al. (1997): stereo baseline 15.0 cm; field of view 14.4° × 14.0° per eye;
256 × 256 px per frame; f/18; resolving power 0.98 mrad px⁻¹. Focal length 23 mm with
23 µm pixels gives f = 1000 px, consistent with the stated IFOV to 2%, a difference
carried as a systematic term in §4. The camera height is 1.5 m above the surface
(nominal, per NASA's instrument description: "The imager rests on a pop-up mast 80 cm
above the lander and 1.5 m above the surface"), with mission reports giving ~1.75–1.85 m
as deployed; both values are propagated where relevant.

### 2.4 The original measurement record

The print-based system is preserved in the repository as photographs of the annotated
print and machine-readable transcriptions. Its structure: a ruler axis from "0 inches" at
the top edge of the print to a "43 inch mark" at the bottom, designated D and treated as
range zero; two anchors of known distance (North Twin at ruler 4⅞ in, "2800 feet from D";
South Twin at 5¼ in, "3300 feet"); and per-anchor conversion factors 2800/38.125 =
73.44 ft in⁻¹ and 3300/37.75 = 87.42 ft in⁻¹. Object dimensions were computed as ruler
inches × the nearest anchor's factor. The annotation notes, in the author's hand, "Only
B. and C. are Known" — an accurate statement of the calibration basis.

## 3. Methods

### 3.1 The angular relation

For a feature at range Z subtending N native pixels, in the small-angle regime,

  **s = Z · N · IFOV**,  IFOV = 0.98 mrad px⁻¹  (1)

with fractional error below 0.1% for the largest angles considered here (~40 mrad). The
measurement problem separates into N (a pixel count, straightforwardly bounded) and Z
(range, which lander imagery of this kind cannot supply at these distances; §4.5).

The print-based analogue of (1) requires the print's angular scale. The 3135-px product
height spanning 43 inches gives 72.9 product px in⁻¹, hence

  **14.29 mrad in⁻¹ = 0.01429 rad in⁻¹.**  (2)

An independent check from the annotator's own North Twin extent (2 9/16 in) against the
same extent re-measured in pixels (≈194 product px) gives 75.7 px in⁻¹, agreeing with (2)
to 4% and confirming the print was produced from the full product at the stated width.

### 3.2 Skyline extraction and peak metrology

Peak angular extents are measured from a per-column skyline trace: for each image column,
the first row at which luminance falls persistently below 94% of the local sky level. Apex
and visible-base rows are extracted within fixed windows defined once in a reference
coordinate frame and scaled linearly to whatever product resolution is supplied, so that
preview-scale and full-resolution runs share a single code path. Apparent height is
computed via (1) with the caption ranges. Because intervening ridges occlude the true
bases, all such heights are **lower bounds**.

### 3.3 Silhouette characterisation of the anomalous feature

For the anomalous feature the procedure is: (a) extract a measurement window around the
annotated location in the full-resolution right-eye product; (b) estimate the local
terrain background by a wide Gaussian (σ = 30 px) and form the dark-feature residual;
(c) threshold at the 80th percentile of the residual and morphologically close (radius
3 px) to merge adjacent dark elements, taking the largest connected component as the
**cluster envelope**; (d) measure the envelope bounding box and its width profile per
row; (e) separately decompose the *un-closed* thresholded field into connected
sub-features to establish what the envelope is composed of; (f) convert to angle via
0.196 mrad px⁻¹ and to metric size via (1) as a function of assumed Z.

Step (c) is a deliberate modelling choice and is treated as such in §5.3: the closing
operation is what converts a field of separate dark elements into a single outline.

## 4. Results

### 4.1 The linear range mapping is geometrically invalid

For a camera at height h above locally level ground, a point at range Z appears at
depression angle ≈ h/Z below the horizon — a hyperbolic, not linear, mapping. Three
consequences falsify the "0 ft at the 43-inch mark" premise:

1. The frame bottom corresponds to ground at **2.7 m** (h = 1.5 m) to **3.3 m**
   (h = 1.85 m), not zero; range zero (the ground beneath the camera) is not in frame.
2. The flat-ground horizon lies at √(2Rh) = **3.19–3.54 km**.
3. Between 860 m and infinity the depression angle changes by only **1.7 mrad ≈ 1.7
   native px ≈ 0.12 print inches**: the entire far field is compressed into a sliver.

A direct falsification is available within the annotation itself: the nearer anchor
(2800 ft) is placed *above* the farther (3300 ft) on the print, whereas the geometry
requires the opposite ordering — by 0.25 native px, i.e. unmeasurably. The visible
"bases" are set by occluding terrain, not range. Correspondingly, the two anchors yield
mutually inconsistent factors (73.44 vs 87.42 ft in⁻¹, 19% apart) for objects separated
by 0.375 in on the print.

### 4.2 The ×1.84 transverse-scale error

Even granting the anchor ranges, the derived factors answer the wrong question. The
quantity 2800 ft ÷ 38.125 in is an average *radial* gradient (how fast ground range grows
per print inch). The height or width of an object at range Z instead requires the
*transverse* scale, Z × (2):

| Anchor | Original factor | True transverse factor | Ratio |
|---|---|---|---|
| North Twin (2800 ft, 860 m) | 73.44 ft in⁻¹ | 40.0 ft in⁻¹ | **×1.84** |
| South Twin (3300 ft, 1006 m) | 87.42 ft in⁻¹ | 47.2 ft in⁻¹ | **×1.85** |

The ratio has the closed form 1/(38.125 × 0.01429) = **1.836**, independent of the anchor
distance — it is fixed by the print geometry alone. Every dimension derived from the
original system is therefore inflated by this factor.

### 4.3 Known-answer validation

The Twin Peaks provide an independently published answer ("approximately 30-35 meters"),
printed in the same caption sentence as the anchor distances. Applying the corrected
angular scale to the **unmodified original ruler measurements**:

| Quantity | Original system | Corrected (this work) | Published |
|---|---|---|---|
| North Twin height (2 9/16 in) | 188.2 ft = 57.4 m | **103.3 ft = 31.5 m** | 30–35 m |
| South Twin height (2 in) | 174.8 ft = 53.3 m | **94.3 ft = 28.7 m** | 30–35 m |

The uncorrected system fails the known-answer test by a margin no measurement uncertainty
can absorb; the corrected pipeline passes for North Twin and falls marginally below for
South Twin. Since 1/16 in ≈ 0.9 mrad ≈ 1 native px, the original ruler readings were
accurate at approximately the native-pixel level. **The measurement was sound; the model
was not.** This is the paper's central methodological result: a scale-model error is not
detectable from internal consistency, only from an external known answer.

### 4.4 Full-resolution and cross-eye verification

The pipeline was re-run against the full-resolution products after first confirming that
the refactored code reproduces the earlier preview-scale results exactly.

| Quantity | Preview (0.905 mrad px⁻¹) | Full-res left (0.196) | Full-res right |
|---|---|---|---|
| North Twin extent | 30.8 mrad | **30.4 mrad** | **32.1 mrad** |
| South Twin extent | 22.6 mrad | **22.5 mrad** | **22.0 mrad** |
| North Twin apparent height @860 m | 26.5 m | 26.1 m | 27.6 m |
| South Twin apparent height @1006 m | 22.7 m | 22.7 m | 22.1 m |

Preview and full-resolution agree to ≤0.4 mrad; the two eyes agree to 1.7 mrad (North)
and 0.5 mrad (South), within the ±2-native-px (±1.96 mrad) pixel-count tolerance. The
apparent heights are lower bounds owing to base occlusion and are consistent with the
published range under the error budget of Appendix A.

### 4.5 Stereo ranging is infeasible from these products

With f = 1000 px and B = 0.15 m, the geometric disparity is d = fB/Z:

| Z | Disparity (native px) | Disparity (product px) | σ_Z at σ_d = 0.2 px |
|---|---|---|---|
| 860 m | 0.174 | 0.87 | ±986 m (115%) |
| 1006 m | 0.149 | 0.75 | ±1349 m (134%) |

using σ_Z = Z²σ_d/(fB). The nominal matching precision exceeds the entire signal. Measured
on the products themselves, the two eyes' summit positions differ by **172 product px**
(North) and **161 product px** (South) — framing offsets from independent mosaic assembly,
~200× the geometric disparity. Any range derived by matching features between these two
products is dominated by assembly differences. Published site ranges derive instead from
cartographic triangulation of horizon landmarks against orbital imagery (Parker, in
Golombek et al., 1997; Oberst et al., 1999, who localised the lander to ~40 m by this
method); rigorous three-dimensional site mapping used photogrammetric control networks on
native frames (Kirk et al., 1999).

### 4.6 Silhouette geometry of the anomalous feature

Applying §3.3 to the annotated feature in PIA02406:

| Quantity | Value |
|---|---|
| Cluster envelope | 171 × 72 product px = **33.5 × 14.1 mrad**; aspect (H/W) 0.42 |
| Equivalent in native px | 34.2 × 14.4 px |
| Original ruler silhouette | 191 × 55 product px = 37.4 × 10.8 mrad; aspect 0.29 |
| Constituent sub-features | **53** connected dark blobs; largest 82 native px; median ≈1 native px |
| Width profile | narrow upper element (~1–8 mrad) over a broad basal mass (~31 mrad), with an intervening width minimum |

Horizontal extents from the independent pixel measurement and the original ruler agree to
~10%. Vertical extent is less well constrained (10.8–14.1 mrad) because the feature is not
skylined: its lower boundary is set by the segmentation threshold rather than by a sky
contact.

Absolute size is **indeterminate**, because range is unconstrained. NASA's caption places
the hummock field between "a few tens of meters" and the South Twin distance — a factor of
~33:

| Assumed Z | Envelope size | 2-native-px floor |
|---|---|---|
| 30 m | 1.0 × 0.4 m | 0.06 m |
| 100 m | 3.4 × 1.4 m | 0.20 m |
| 300 m | 10.1 × 4.2 m | 0.59 m |
| 860 m | 28.8 × 12.1 m | 1.69 m |
| 1006 m | 33.7 × 14.2 m | 1.97 m |

For reference, the corrected ruler dimensions at an assumed 860 m are 31.9 m × 9.1 m,
consistent with the independent pixel envelope (28.8 × 12.1 m) to within the segmentation
uncertainty.

The comparison that motivated the original campaign can now be evaluated. Against the
Great Sphinx of Giza (240 ft = 73 m long, 66 ft = 20 m high):

| | Length vs Sphinx | Height vs Sphinx |
|---|---|---|
| Original (uncorrected) dimensions | 80% | 83% |
| Corrected dimensions (assuming Z = 860 m) | 44% | 45% |

The aspect-ratio agreement (0.286 vs 0.275) survives correction, since ratios are
invariant under a uniform scale error — but an aspect ratio near 0.28 is shared by a
large fraction of elongated low mounds and carries negligible discriminating power.

## 5. Discussion

### 5.1 The resolution floor governs identification

The smallest credible morphological detail is ~2 native px, i.e. 2·Z·IFOV: 0.06 m at
30 m, 1.69 m at 860 m. The features that would distinguish carving from erosion —
edges, facets, bilateral symmetry, discrete appendages — are at or below this floor at
every plausible range for this object, whose total height is only 14.4 native px (the
floor is thus 14% of the feature's full height). Because the products were enlarged
five-fold before co-addition, the sub-native-pixel regime is not empty but *populated by
interpolation*: the enlargement supplies smooth, plausible structure exactly where the
discriminating evidence would have to live. The measurement chain from detector to
conclusion in the original campaign was: native frame → 5× upsample and co-add → JPEG →
web-scale re-encode → ~99-inch print → hand ruler. Three of those steps add structure that
was not on the surface.

### 5.2 Range indeterminacy is not reducible with these data

A factor-of-33 range ambiguity produces a factor-of-33 size ambiguity, and §4.5 shows the
products cannot break it. Any statement of the form "the feature is X metres across" is
therefore conditional on an assumed range, and the assumption does all the work. We note
that the *only* claim invariant to this ambiguity is the aspect ratio — which, as shown,
does not discriminate.

### 5.3 Where identification enters

The neutral measurement is compatible with two mutually exclusive descriptions:

- **A (form):** a reclining figure — a raised head, a neck at the measured width minimum,
  a body extending away, the head foreshortened relative to Sphinx proportions because it
  has eroded or fallen.
- **B (null):** an irregular low mound or outcrop with shadowed relief and surrounding
  talus, one of many hummocks of flood debris, at unknown range.

The measured quantities are identical under both. Everything separating them is supplied
by the describer. Three specific observations:

1. The width minimum is a real, reproducible geometric feature; "neck" is a name applied
   to it. A constriction between two masses is common in natural outcrops.
2. Hypothesis A's explanation for the discrepancy in head proportion — erosion or loss of
   the upper element — is **unfalsifiable at this resolution**. Positing the destruction
   of the diagnostic feature reconciles the hypothesis with any silhouette, and no
   observation available here can test it. A hypothesis that survives only by removing the
   evidence that would test it has not been tested.
3. The segmentation choice in §3.3(c) — morphological closing — is itself the operation
   that converts 53 separate dark elements into one object. "One object" is a modelling
   decision, not an observation.

By parsimony and by the resolution gate, B is favoured and A is not supported by these
data. We emphasise that this is a statement about what the data can license, not a proof
of impossibility.

### 5.4 Precedent

The governing precedent is the Cydonia "Face," which supported an artificial
interpretation at Viking resolution and was resolved by re-imaging at ~1.5 m, at which
scale NASA reported a landform "shown in the higher-resolution image to be a natural
feature similar to a butte or mesa on Earth," approximately 3 km long and rising ~250 m.
The methodological content of that episode is not that the interpretation was wrong but
that it was *settled by acquiring decisively higher resolution*, not by argument at the
original resolution.

### 5.5 Limitations

(i) The silhouette analysis uses the right-eye product only; a left-eye cross-measurement
remains to be performed, and the ~170 px inter-eye framing offset means the feature's
left-eye pixel box must be derived independently. (ii) Segmentation parameters (percentile
threshold, closing radius, background σ) were chosen once and not swept; a sensitivity
analysis over these would tighten the quoted envelope uncertainty. (iii) The physical
print's dimensions are not fully reconciled: the print-source PDF specifies a 92-inch page
while the ruler geometry implies ~99 inches, a ~7% discrepancy that propagates into
print-inch-to-pixel conversions and must be resolved before further print-based work.
(iv) Sub-native-pixel structure has not yet been quantified empirically against native
frames; that test requires the archival Experiment Data Records. (v) Ranges used are
caption values quoted as approximate and are treated as ±5%.

## 6. Falsifiable predictions and the decisive test

The competing descriptions make divergent predictions that are testable with existing,
public data:

- **Prediction 1 (from B):** in map-projected orbital imagery of the site, the feature's
  plan dimensions and relief will fall inside the distribution of the surrounding hummock
  population, on metrics fixed in advance.
- **Prediction 2 (from A):** the feature will be an outlier on those metrics, exceeding
  the population envelope in at least one, with a symmetry statistic above the
  pre-registered population quantile.

The decisive observations are HiRISE PSP_001890_1995 (28.5 cm px⁻¹; 25 cm px⁻¹
map-projected, with the lander visible) and the stereo pair PSP_002391_1995. At 860 m,
IMP's native sampling is 0.84 m px⁻¹, so map-projected HiRISE is 3.4× finer linearly
(11.4× by area) — and, decisively, **carries no range ambiguity at all**, since map
projection removes perspective. Additionally, the native IMP Experiment Data Records
(PDS `MPFL-M-IMP-2-EDR-V1.0`) permit direct measurement of what the 500% enlargement adds
relative to genuine native-resolution signal.

We commit in advance to reporting the outcome of these tests irrespective of direction,
with hypotheses, metrics, thresholds, and the comparison population fixed before the
orbital data are examined.

## 7. Conclusions

1. A linear range-versus-print-position mapping is geometrically invalid for lander
   imagery; the true mapping is hyperbolic, the frame bottom is ~3 m rather than 0 m, and
   the far field occupies ~1.7 native pixels.
2. Per-anchor radial conversion factors overestimate transverse scale by a factor with
   closed form 1/(d·θ) — here **1.836** — inflating every derived dimension by ~84%.
3. Corrected with the angular relation, the original hand measurements reproduce the
   independently published peak heights (31.5 m, 28.7 m vs 30–35 m). The measurements were
   accurate at the native-pixel level; the error was entirely in the scale model. Internal
   consistency did not reveal it; an external known answer did.
4. Stereo ranging from independently assembled press mosaics is infeasible: the framing
   offset (161–172 product px) exceeds the geometric disparity (0.87 product px) by ~200×.
5. The anomalous feature is a real, measurable geometric structure (33.5 × 14.1 mrad,
   53 sub-features) whose absolute size is indeterminate over a factor-of-33 range
   ambiguity and whose diagnostic morphology lies below the resolution floor at all
   plausible ranges. **The artificiality interpretation is not supported by these data.**
6. Generally: measurement fixes geometry; identification is conferred. A pipeline can be
   internally consistent, carefully executed, and confidently wrong, and only an external
   known-answer test will reveal it. We recommend that any dimensional claim derived from
   a press-release product state the product's processing history, the assumed range with
   its uncertainty, and the two-native-pixel floor at that range.

---

## Appendix A. Error budget (North Twin, full-resolution left eye)

| Term | Value | Contribution |
|---|---|---|
| Pixel count 155 product px (±10 px = ±2 native px, base-median sensitivity) | 30.4 ± 2.0 mrad | ±6% |
| IFOV 0.98 vs 1.00 mrad px⁻¹ (FOV- vs focal-length-derived) | systematic | ±2% |
| Product/preview scale (catalog dimensions) | exact to 0.1% | — |
| Range 860 m (caption "approximately"; assumed ±5%) | ±43 m | ±5% |
| Base occlusion by intervening ridges | one-sided | −0 / +30% |
| **Total** | | **26.1 m, −2.1/+8.5 m** → consistent with 30–35 m |

Any published dimension should carry an equivalent budget; where a term cannot be
estimated, the measurement is incomplete.

## Data and code availability

All products, intermediate data, analysis code, and the complete measurement record are
public at the project repository. Principal artefacts: `analysis/measure_twin_peaks.py`
(peak metrology, one code path for preview and full resolution),
`analysis/object_x_silhouette.py` (silhouette characterisation),
`analysis/FULLRES_RERUN.md` (full-resolution verification and gate results),
`analysis/OBJECT_X_SILHOUETTE_REPORT.md` (extended silhouette report),
`data/PROVENANCE.md` (acquisition and hash verification),
`data/SOURCING_LIST.md` (outstanding primary-source acquisitions).
Every numerical result in this manuscript is regenerable by executing the two scripts.

## Erratum note

An earlier internal draft stated that map-projected HiRISE offers a "~3400× finer ground
sample" than the IMP view at this range. That figure is incorrect by ~10³: the correct
comparison is 0.25 m px⁻¹ versus 0.84 m px⁻¹, i.e. 3.4× finer linearly and 11.4× by area.
The error was found during preparation of this manuscript and corrected in the underlying
documents. It does not affect any conclusion — the decisive advantage of orbital data is
the elimination of range ambiguity, not sampling density — but it is recorded here in
keeping with the project's error-correction policy.

## Disclosure of AI assistance

Analysis code, statistical treatment, and manuscript drafting were performed with
substantial assistance from a large language model (Claude, Anthropic), operating under an
explicit protocol requiring that: no citation be introduced that is not verifiable at an
institutional source; every numerical claim trace to executable code or a quoted primary
document; and null results be reported. All measurements are reproducible from the
published code independently of the assistant. Earlier documents in this project's
history, also AI-generated but produced without such constraints, were found to contain
fabricated citations, circular validation, and invented probability figures; those
documents are retained in the repository, annotated, as part of the record. This
disclosure is made because the failure mode is relevant to the paper's subject.

## References

Golombek, M. P., Cook, R. A., Economou, T., Folkner, W. M., Haldemann, A. F. C.,
Kallemeyn, P. H., Knudsen, J. M., Manning, R. M., Moore, H. J., Parker, T. J., Rieder, R.,
Schofield, J. T., Smith, P. H., & Vaughan, R. M. (1997). Overview of the Mars Pathfinder
mission and assessment of landing site predictions. *Science*, 278(5344), 1743–1748.
https://doi.org/10.1126/science.278.5344.1743

Kirk, R. L., et al. (1999). Digital photogrammetric analysis of the IMP camera images:
Mapping the Mars Pathfinder landing site in three dimensions. *Journal of Geophysical
Research: Planets*, 104(E4). https://doi.org/10.1029/1998JE900012

NASA/JPL. Mars Pathfinder instrument descriptions. https://mars.nasa.gov/MPF/mpf/sci_desc.html

NASA/JPL Photojournal. PIA01008, *Big Crater as viewed by Pathfinder lander*.
NASA/JPL Photojournal. PIA02405, *Twin Peaks in super resolution — left eye*.
NASA/JPL Photojournal. PIA02406, *Twin Peaks in super resolution — right eye*.
NASA. PIA03225, *Highest-resolution view of "Face on Mars."*

Oberst, J., Jaumann, R., Zeitler, W., Hauber, E., Kuschel, M., Parker, T., Golombek, M.,
Malin, M., & Soderblom, L. (1999). Photogrammetric analysis of horizon panoramas: The
Pathfinder landing site in Viking orbiter images. *Journal of Geophysical Research:
Planets*. https://doi.org/10.1029/98JE01429

Smith, P. H., et al. (1997). The imager for Mars Pathfinder experiment. *Journal of
Geophysical Research*, 102(E2), 4003–4025. https://doi.org/10.1029/96JE03568

University of Arizona, HiRISE. PSP_001890_1995; PSP_002391_1995.
https://www.uahirise.org/PSP_001890_1995 ; https://www.uahirise.org/PSP_002391_1995

*Encyclopædia Britannica.* Great Sphinx of Giza. https://www.britannica.com/topic/Great-Sphinx

**Note on reference verification.** Full texts of Golombek et al. (1997), Oberst et al.
(1999), Kirk et al. (1999) and Smith et al. (1997) have not yet been retrieved and read in
full by the present author; citations were verified as to existence, authorship, venue and
DOI, and their content used only where corroborated by an accessible abstract or by NASA
caption text. Retrieval and full verification is scheduled prior to submission
(`data/SOURCING_LIST.md`, Tier B) and any citation that cannot be verified in full will be
removed.
