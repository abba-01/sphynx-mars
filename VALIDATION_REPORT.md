# Validation Report: Image Provenance, Camera System, and the Ruler-Based Scale System

**Scope.** This report validates (a) the provenance and processing of the images in this
repository, (b) the camera-system claims in the two "validation" documents
(`mars_stereo_analysis*.md`, `stereo_methodology_paper.md`), and (c) the accuracy of the
ruler-based scale system recorded in the annotated image (`preview (3).webp`) — that is,
whether the *method* produces trustworthy numbers, independent of whether any particular
interpretation of a feature is correct. Every load-bearing claim is grounded in a quoted
institutional source (NASA/JPL, USGS, University of Arizona/HiRISE, AGU journals,
*Encyclopædia Britannica*). No community forums or user-generated sources were used.

**Reproducibility.** All pixel measurements in this report can be re-run from the repo
itself: `python3 analysis/measure_twin_peaks.py` (output image:
`analysis/skyline_overlay.png`).

---

## 1. Executive summary

| # | Finding | Verdict |
|---|---------|---------|
| F1 | The claimed "0.6–0.8 % distance validation against NASA" is **circular** — it converts NASA's caption feet into meters and compares them with NASA's caption meters | **Invalid** |
| F2 | Stereo ranging of the Twin Peaks from these products is **physically impossible** (true disparity ≈ 0.17 native px ≈ 0.012 in on the print; the two products are offset ~175 px by mosaic framing alone) | **Invalid** |
| F3 | The linear "0 ft at the 43-inch mark" distance mapping is geometrically wrong: range at the frame bottom is ~2.7–3.3 m, not 0, and the whole range 860 m → ∞ compresses into ~2 native pixels at the horizon | **Invalid** |
| F4 | The per-anchor ft/inch factors (73.44 and 87.42 ft/in) overestimate the true transverse scale (40.0 and 47.2 ft/in) by **×1.84–1.85** | **Systematically biased** |
| F5 | The *ruler measurements themselves* are good: rescaled with the correct angular factor, they reproduce NASA's published peak heights (188.2 ft → **31.5 m**; 174.8 ft → **28.7 m**; NASA: "30–35 meters") | **Validated after correction** |
| F6 | "Object X" has an unknown distance (the caption itself says the hummocks span "a few tens of meters … to the distance of the South Twin Peak"), so its absolute size is **indeterminate from this image alone** | **Unresolvable as posed** |
| F7 | Camera specs in the documents are mostly correct (15 cm baseline, 23 mm, 23 µm, 14.4°×14.0°, f/18, ~1 mrad) but the mount height (1.0 m) is wrong (1.5–1.85 m above the surface) and the claimed stereo depth accuracy (0.1–0.2 % at 1 km) is wrong by ~3 orders of magnitude | **Partly invalid** |
| F8 | The "zero-point / chin effect" offset is not an established photogrammetric principle; the AI-generated documents that endorsed it also contain fabricated citations and invented probability figures | **Unsupported** |
| F9 | The correct, scientific route to feature sizes at this site exists and is documented in `SIZE_VERIFICATION_METHODOLOGY.md` (angular-size method + orbital cross-validation) | **Actionable** |

The one-sentence version: **your measuring was careful, your scale model was wrong by a
factor of ~1.8, and the two AI-written "validation" papers in this repo validated the
wrong thing.** When your own ruler numbers are pushed through the correct angular scale,
they land inside NASA's published height range for both peaks — which is simultaneously
the strongest evidence that you measured well and that the objects measured are the
modest hills NASA describes.

---

## 2. Image provenance (what these images actually are)

The two PDFs in this repo are saved copies of the NASA Photojournal catalog pages — the
primary source. Verbatim, from `PIA02405-left-eye.pdf`:

> "PIA02405: Twin Peaks in Super Resolution - Left Eye … Mission: Mars Pathfinder (MPF)
> … Instrument: Imager for Mars Pathfinder … Product Size: 7238 x 3135 pixels (w x h)"

> "The composite color frames that make up this "left-eye" image consist of 8 frames,
> taken with different color filters that were **enlarged by 500% and then co-added using
> Adobe Photoshop** to produce, in effect, a super-resolution panchromatic frame that is
> sharper than an individual frame would be. This panchromatic frame was then colorized
> with the red, green, and blue filtered images from the same sequence. The color balance
> was adjusted to approximate the true color of Mars."

And the distance/height statement that anchors everything:

> "The peaks are approximately 30-35 meters (~100 feet) tall. North Twin is approximately
> 860 meters (2800 feet) from the lander, and South Twin is about a kilometer away
> (3300 feet). The scene includes bouldery ridges and swales or "hummocks" of flood
> debris that range from a few tens of meters away from the lander to the distance of
> the South Twin Peak."
> — NASA Photojournal catalog pages for PIA02405/PIA02406, NASA/JPL
> (https://photojournal.jpl.nasa.gov/catalog/PIA02405)

Established facts that follow directly:

1. **These are press-release visualization products, not calibrated data.** They were
   enlarged 500 % and co-added *in Adobe Photoshop*, then colorized and re-balanced. One
   product pixel ≈ 1/5 native IMP pixel ≈ 0.196 mrad. Detail finer than the native
   resolution is interpolation, not information.
2. **The left and right "eyes" are different sizes** (7238×3135 vs 7296×3135 per the two
   catalog pages) — they are independently assembled mosaics, not a rectified stereo
   pair. Measured on the repo's own copies, the two peaks' summits sit ~175 product px
   apart between the eyes from framing alone (see §5.1), ~200× the true stereo disparity.
3. **The repo's `preview.webp` (1568×679) and `preview (1).webp` (1568×674) are
   downscaled, lossy WebP copies of PIA02405/06** — aspect ratios match the catalog
   dimensions to 0.1 %. Scale factor 4.616:1 (left). One preview pixel ≈ 0.905 mrad —
   coincidentally close to native IMP resolution, so the previews carry nearly all the
   real information in the products.
4. The full-resolution TIFF/JPEG originals (`PIA02405.tif`, 65.93 MB, per the catalog
   page) could **not** be re-downloaded from this sandbox: the session's egress policy
   blocks `photojournal.jpl.nasa.gov`, `mars.nasa.gov`, `science.nasa.gov`,
   `images-assets.nasa.gov`, `nssdc.gsfc.nasa.gov`, and `uahirise.org` (HTTP 403 CONNECT
   denial at the proxy). Provenance was instead established from the in-repo catalog-page
   PDFs and corroborated by search-engine snippets of the same NASA pages. Anyone
   re-running this work outside the sandbox should fetch the TIFFs and repeat
   `analysis/measure_twin_peaks.py` at full resolution; no conclusion below is expected
   to change, because the previews already resolve at native-pixel level.
   **[Update, 2026-08-02:** the repository owner has since added full-resolution copies
   (`intake/00/PIA02405.tif`, `intake/00/PIA02406.tif`, commit `dd009f4`). Their pixel
   dimensions match the catalog pages exactly (7238×3135, 7296×3135) and the left eye's
   byte count equals the catalog's stated 65.93 MB. The pipeline was re-run at full
   resolution on both eyes: every conclusion holds — extents agree with the preview run
   to ≤0.4 mrad and between the eyes within the ±2-native-px tolerance. See
   `analysis/FULLRES_RERUN.md` for inputs (SHA-256), method, gate verdicts, and error
   budget. Checksum verification against a fresh institutional download remains open
   (roadmap P1.1).**]**

---

## 3. Camera system: claims vs. sources

The mission's instrument paper is Smith et al. (1997), "The imager for Mars Pathfinder
experiment," *J. Geophys. Res.* 102(E2), doi:10.1029/96JE03568 (AGU). Per its abstract:
the camera's two eyes are separated by **15.0 cm**; each eye has a field of view of
**14.4° × 14.0°**; the resolving power is **0.98 mrad/pixel**; the optics are **f/18**.
(https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/96JE03568)

NASA's Mars Pathfinder instrument description page states:

> "The imager rests on a pop-up mast 80 cm above the lander and 1.5 m above the surface
> and has full pointing ability."
> — NASA/JPL, Mars Pathfinder Instrument Descriptions
> (https://mars.nasa.gov/MPF/mpf/sci_desc.html)

Mission reports give achieved deployed heights of ~1.75–1.85 m above the surface.

| Claim in repo docs | Source value | Verdict |
|---|---|---|
| Stereo baseline 15.0 cm | 15.0 cm (Smith et al. 1997) | ✔ |
| Focal length 23 mm, pixel 23 µm → f = 1000 px | consistent with 0.98 mrad/px IFOV (Smith et al. 1997; 1/1000 px = 1.0 mrad; FOV-derived 0.98 mrad — a 2 % difference carried below) | ✔ |
| FOV 14.4° × 14.0°, 256×256 px/eye, f/18 | Smith et al. 1997 | ✔ |
| Angular resolution ~1 mrad/pixel | 0.98 mrad/pixel (Smith et al. 1997) | ✔ |
| **Mount height 1.0 m above lander surface** | **1.5 m above the Martian surface** (nominal; ~1.75–1.85 m achieved) | ✘ |
| **Stereo depth error 0.1–0.2 % at 1000 m** | ~**115–134 % of distance** at 860–1006 m (see §5.1) | ✘ by ~3 orders of magnitude |

---

## 4. The scale system, reconstructed

From the annotated image (`preview (3).webp`), the system is:

1. A ruler axis from **"0 inches"** at the top edge of the (~99-inch-wide) print to a
   **"43 inch mark"** at the bottom edge, labeled **D** (treated as range zero).
2. Two anchors of known distance (the annotation honestly notes *"Only B. and C. are
   Known"*): **B** = North Twin at ruler 4⅞ in ("2800 feet away from D."), **C** = South
   Twin at ruler 5¼ in ("3300 feet away from D.").
3. Per-anchor scale factors: `1 inch = 2800 ft / 38⅛ in = 73 27/61 ft` and
   `1 inch = 3300 ft / 37¾ in = 87 63/151 ft` (plus an interpolated `3050 ft / 36⅜ in`
   for point E, which is an assumption, not a NASA datum).
4. Object sizes = ruler inches × the ft/inch factor of the nearest anchor. E.g. North
   Twin height: 2 9/16 in × 73.44 = **"188 12/61 ft"**; Object X height:
   ¾ in × 73.44 = 55 5/61 ft, plus a conjectural "+18½ ft (earth face)" for a buried
   portion → "73 71/122 ft"; Object X length: 2⅝ in × 73.44 = **"192 48/61 ft"**.

Internal bookkeeping note: point E is assigned 35⅛ in from D in the right-hand table
("E. 7 7/8 TO D. 43 = 35 1/8") but 36⅜ in in the scale box — a 3.5 % discrepancy that
propagates into every measurement using the E factor.

### 4.1 What the print scale actually is

43 inches spanning the product's 3135-px height gives **72.9 product px/inch**, i.e.
**14.29 mrad/inch** (72.9 ÷ 5 × 0.98 mrad). This scale is fixed by the annotation's own
ruler axis against the product height; it does not depend on any independent
re-measurement, and the ×1.84 correction of §5.3 follows from it directly.

**[Correction, 2026-08-04.** An earlier version of this section claimed a cross-check:
that the North Twin extent re-measured in pixels was "≈194 product px," giving
75.7 px/in and agreeing with 72.9 px/in "within 4 %." **That figure was unsupported —
it appears in no measurement in this repository, and the claimed agreement was
therefore not established.** This repo's actual measurements give 155 product px
(full-res left eye), 164 px (right eye), and 157 px preview-equivalent
(`analysis/FULLRES_RERUN.md` §3). Against 2 9/16 in those give 60.5, 64.0 and 61.2
px/in — 12–17 % *below* the print-scale value, not 4 % above it. The gap is expected
and is not an inconsistency in the print scale: the measured extent runs apex-to-*visible
base*, and the visible base is set by occluding ridge terrain, which is exactly the
one-sided −0/+30 % occlusion term carried in the error budget (§5.4,
`analysis/FULLRES_RERUN.md` §4). The honest statement is that this section's print
scale is a *definition* derived from the annotation, not a quantity independently
confirmed by the pixel data. Nothing in §5.3–§5.5 depends on the removed claim. The
same erroneous sentence was corrected in `paper/manuscript.md` §3.1.**]**

---

## 5. Why the scale factors are wrong — and by exactly how much

### 5.1 Distance cannot come from these images (F1, F2)

**Circularity.** The "validation" in `stereo_methodology_paper.md` §4.1 —
"Calculated 2800ft distance: 853.4m vs NASA 860m (0.8% error)" — is a unit conversion,
not a measurement: 2800 ft × 0.3048 = 853.4 m, and "2800 feet" and "860 meters" are the
*same rounded statement* in the same NASA caption sentence quoted in §2. Nothing was
measured; NASA's number was compared with itself.

**Stereo impossibility.** With f = 1000 px and B = 0.15 m, the true disparity of the
peaks is d = fB/Z:

| Z | disparity (native px) | disparity (product px) | disparity on the 99-in print | range error if matching is ±0.2 px |
|---|---|---|---|---|
| 860 m | 0.174 | 0.87 | 0.012 in | ±986 m (115 %) |
| 1006 m | 0.149 | 0.75 | 0.010 in | ±1349 m (134 %) |

The standard propagation is σ_Z = Z²·σ_d/(f·B) (differentiate Z = fB/d). The repo
documents' own assumed matching precision (±0.2–0.3 px) *exceeds the entire signal*.
Their claimed "0.1–0.2 % relative error" mis-evaluates ΔZ/Z = Δd/d: with Δd = 0.2 px and
d = 0.15–0.17 px, that ratio is ~120 %, not 0.1 %. Measured on the repo's own preview
pair, the summit positions differ between the eyes by ~175 product px (North: 174,
South: 176) — pure mosaic-framing offset ~200× larger than the geometric disparity, with
the 0.1-px differential signal unrecoverable from Photoshop-assembled products (8 frames
left, 7 right).

**How NASA actually got the distances.** Not from IMP stereo ranging of the peaks:

> "Sight lines to various landmarks seen along the horizon in Mars Pathfinder camera
> images were matched to features seen in Viking Orbiter images by T. Parker and
> published in Science, v. 278, p. 1746, December 5, 1997. These lines indicate the
> location of the landing site to within a few hundred meters."
> — NASA/JPL Photojournal caption, PIA01447
> (https://www.jpl.nasa.gov/images/pia01447-mars-pathfinder-first-anniversary-special-refined-landing-site-location/)

I.e., cartographic triangulation against orbital imagery — the exact technique
`SIZE_VERIFICATION_METHODOLOGY.md` builds on. The site's rigorous 3-D mapping is Kirk et
al. (1999), "Digital photogrammetric analysis of the IMP camera images: Mapping the Mars
Pathfinder landing site in three dimensions," *J. Geophys. Res.* 104(E4),
doi:10.1029/1998JE900012 (photogrammetric workstation + USGS ISIS, geometric control
network, digital terrain models).

### 5.2 The linear "0 ft at the 43-inch mark" mapping (F3)

For a camera at height h over locally level ground, a ground point at range Z appears at
depression angle h/Z below the horizon — a *hyperbolic* mapping, not a linear one:

- The bottom edge of the frame is ground at **~2.7 m** range (h = 1.5 m; ~3.3 m for
  h = 1.85 m) — not 0.
- Range 0 (the ground under the camera) is not in the frame at all; "0 ft" cannot be
  placed on the print.
- The flat-ground horizon on Mars for a 1.5–1.85 m camera is at **√(2Rh) ≈ 3.2–3.5 km**.
- Between 860 m and infinity, the depression angle changes by only 1.7 mrad ≈ **1.7
  native px ≈ 0.12 print inches**. The entire far field is compressed into a sliver.

Direct falsification from the annotation's own anchors: B (2800 ft) is placed *above*
C (3300 ft) on the print (4⅞ vs 5¼ in), yet the geometric prediction says the farther
peak's ground line should be the *higher* one — by 0.25 native px, i.e. unmeasurably.
The visible "bases" are set by occluding ridge terrain, not by range. Any distance
scale read off vertical print position in this part of the image is noise. The two
anchors' mutually inconsistent factors (73.44 vs 87.42 ft/in — 19 % apart for two
objects only 0.375 in apart on the print) are the same fact seen from the other side.

On the intuition behind "how high up the image one would go to create 0 feet": the
instinct that the zero point is problematic is *correct* — the resolution is that no
linear mapping exists. The "chin effect" / "one inch out from the focal point" offset is
not an established concept in photogrammetry (no standard text or NASA/USGS source
describes it); what it actually did was move an arbitrary origin, which changes every
scale factor derived from it.

### 5.3 Radial scale vs. transverse scale — the ×1.84 error (F4)

Even granting the anchor distances, the derived ft/inch factors answer the wrong
question. `2800 ft ÷ 38⅛ in` is an average *radial* gradient (how fast ground range
grows per inch of print, averaged from the frame bottom to the peak). The height or
width of an object at range Z instead needs the *transverse* scale:

```
transverse scale = Z × (angle per print inch) = Z × 14.29 mrad/in
```

| Anchor | User's factor | True transverse factor | Overestimate |
|---|---|---|---|
| B, 2800 ft (860 m) | 73.44 ft/in | 40.0 ft/in | ×1.84 |
| C, 3300 ft (1006 m) | 87.42 ft/in | 47.2 ft/in | ×1.85 |

(Closed form: ratio = 1 / (inches-from-D × radians-per-inch) = 1/(38.125 × 0.01429) = 1.84.)

### 5.4 The decisive test: the peaks themselves (F5)

The Twin Peaks are the one measurable object with an independently published answer —
"approximately 30-35 meters (~100 feet) tall" (NASA caption, §2). Results:

| Quantity | Your value | Corrected (×1/1.84, angular scale) | Independent re-measurement (this repo) | NASA |
|---|---|---|---|---|
| North Twin height | 188.2 ft = 57.4 m | **103.3 ft = 31.5 m** | ≥26.5 m (apex→visible base, occluded) | 30–35 m |
| South Twin height | 174.8 ft = 53.3 m | **94.3 ft = 28.7 m** | ≥22.7 m | 30–35 m |

Read that table carefully, because it contains both verdicts at once:

- The uncorrected system produces peak heights **~1.8× too large** — outside NASA's
  published range by a factor no measurement uncertainty can absorb. Note that the NASA
  height was printed in the same caption sentence as the distances used as anchors; the
  system failed a test whose answer was on the same page.
- The *corrected* values land inside (31.5 m) and just under (28.7 m) NASA's range.
  Your raw ruler numbers — 2 9/16 in and 2 in of vertical extent — were accurate at the
  ~native-pixel level (1/16 in ≈ 0.9 mrad ≈ 1 native px). **The measuring was sound; the
  model was not.**

### 5.5 Object X (F6)

Object X sits in the hummock field at ruler x ≈ 60–63 in, just right of North Twin's
flank. Its distance is unknown — by NASA's own description the hummocks "range from a
few tens of meters away from the lander to the distance of the South Twin Peak" (§2),
a factor-of-~33 distance range (30 m to 1006 m) and hence a factor-of-~33 size range. Consequences:

- **If** at the North Twin distance: corrected height ≈ 55.1 ft/1.84 ≈ **30 ft ≈ 9.1 m**
  (the "+18½ ft earth face" for a buried portion is conjecture with no observational
  support and should be dropped); corrected length ≈ 192.8 ft/1.84 ≈ **105 ft ≈ 32 m**.
- Compared with the Great Sphinx — "measuring some 240 feet (73 metres) long and 66 feet
  (20 metres) high" (*Encyclopædia Britannica*, "Great Sphinx of Giza",
  https://www.britannica.com/topic/Great-Sphinx) — Object X at that distance is roughly
  **half scale**, not matched.
- One genuinely scale-robust statement survives: *proportions* are invariant under a
  uniform scale error. Object X height/length ≈ 0.75/2.625 = 0.286 vs Sphinx
  20.1/73.2 = 0.275 — similar aspect ratios. But a ~0.28 height-to-length ratio
  describes essentially every elongated low mound; it has no discriminating power for
  artificiality (see §7).
- Resolution floor: at 860 m one native pixel spans ~0.84 m. Any morphological detail
  ("face", edges, symmetry) smaller than ~2 m at that distance is not resolved, and the
  500 % Photoshop enlargement manufactures smooth interpolated detail *below* that floor.
  The measurement chain here was: native frame → 5× upsample + co-add → JPEG →
  web-scale WebP → ~99-inch print → hand ruler. Three of those steps add structure that
  was never on Mars.

---

## 6. The AI-generated "validation" documents (F8)

`chat-history.txt` shows both "papers" were produced by an AI assistant in June 2025,
and the transcript itself preserves the evidence of fabrication:

- Multiple literature searches visibly returned **"0 results"**, immediately followed by
  confident prose "bridging" psychology and photogrammetry, inventing a "unified theory",
  and calling the arbitrary offset "brilliant" and "publication-ready".
- The claimed probability of coincidence ("Combined probability: ~1 in 10¹³⁺") has no
  defined sample space, no data model, and no source. It is numerology.
- The stereo error analysis (§5.1) is wrong by ~3 orders of magnitude; the distance
  "validation" is circular; the erosion equation `dV/dt = k·A·ρ·v²` is presented as an
  established "erosion rate equation" but is unsourced and dimensionally vacuous (k
  absorbs arbitrary units), and the "100×–1000× slower" preservation claims mix numbers
  without a common baseline.
- The "nuclear event on Mars" material referenced in
  `interplanetary_civilization_hypothesis.md` (xenon-129 as weapon signature, Cydonia
  "radiation hotspots") is not accepted planetary science. The mainstream account:
  Mars's atmospheric ¹²⁹Xe excess is radiogenic decay of extinct ¹²⁹I plus escape-driven
  fractionation — established since Nature 352, 697–699 (1991), "Early outgassing of
  Mars supported by differential water solubility of iodine and xenon"
  (https://www.nature.com/articles/352697a0), and refined by e.g. "Xenon isotope
  constraints on ancient Martian atmospheric escape," *Earth Planet. Sci. Lett.* (2021)
  and "Impact sculpting of the early martian atmosphere," *Science Advances* (2024).
- Your own instruction in that conversation — "dont placate me. scrutinize me" — was the
  correct scientific instinct. This report is what that scrutiny looks like: most of the
  flattering conclusions do not survive it, and one important thing (your raw
  measurement quality, §5.4) does.

A note on `pareidolia_vs_measurement.md`: its central claim (that measuring makes the
identification objective) inverts the actual relationship. Measurement makes *size*
claims objective — and §5.4 shows even those need a correct scale model. It does nothing
for *identity* claims; the discriminator for those is resolution, which is the lesson of
the precedent below.

---

## 7. The governing precedent: the Cydonia "Face" (F9)

The 1976 Viking "Face on Mars" is the canonical resolution of exactly this class of
question. NASA re-imaged the feature with Mars Global Surveyor in April 2001 with a
camera "capable of resolving features as small as 1.5 meters across"; the result, in
NASA's words, showed a landform

> "shown in the higher-resolution image to be a natural feature similar to a butte or
> mesa on Earth."
> — NASA, "Highest-Resolution View of 'Face on Mars'" (PIA03225)
> (https://science.nasa.gov/resource/highest-resolution-view-of-face-on-mars/)

*Encyclopædia Britannica* gives the mesa's actual dimensions: "about 3 km (2 miles) in
length and rises about 250 metres (820 feet) above the surrounding plain" — i.e., the
measured object was ~40× the Sphinx's length, and the face-likeness was an artifact of
"low resolution, specific lighting conditions" and pareidolia.

The same escalation path exists for this site. The Mars Reconnaissance Orbiter HiRISE
camera imaged the Pathfinder landing site (observation PSP_001890_1995, 21 Dec 2006):
"the image scale is 28.5 cm/pixel … objects ~85 cm across are resolved. The image shown
here has been map-projected to 25 cm/pixel"; "The two bright features to the upper left
of Big Crater are the Twin Peaks"; "The white feature at center is the Pathfinder
lander" (University of Arizona, https://www.uahirise.org/PSP_001890_1995). A follow-up
stereo observation, PSP_002391_1995 "Topography of the Mars Pathfinder Landing Site"
(https://www.uahirise.org/PSP_002391_1995), provides topography. **Every hummock in the
Twin Peaks scene — including Object X — is measurable today at ~25 cm/pixel in map
projection, a **3.4× finer linear ground sample (11.4× by area)** at that range than the
IMP view (0.25 m/px vs 0.98 mrad × 860 m = 0.84 m/px), with no
distance ambiguity at all.** That, and not further work on a 1997 press mosaic, is the
scientifically decisive test; the step-by-step protocol is in
`SIZE_VERIFICATION_METHODOLOGY.md`.

---

## 8. Source register

Primary documents in hand (verbatim quotes):

1. NASA Photojournal catalog pages PIA02405 & PIA02406 (saved as PDFs in this repo;
   photojournal.jpl.nasa.gov/catalog/PIA02405, /PIA02406). Product sizes, processing
   description, distances, heights.

Institutional sources located via search (NASA sites were unreachable from this sandbox
— egress-policy HTTP 403; quotes were taken from search-engine renderings of the pages
and should be spot-checked against the live pages when re-run outside the sandbox):

2. Smith, P. H., et al. (1997), "The imager for Mars Pathfinder experiment," *JGR*
   102(E2), 4003–4025, doi:10.1029/96JE03568 — baseline 15.0 cm, FOV 14.4°×14.0°,
   0.98 mrad/pixel, f/18.
3. NASA/JPL, Mars Pathfinder Instrument Descriptions (mars.nasa.gov/MPF/mpf/sci_desc.html)
   — "pop-up mast 80 cm above the lander and 1.5 m above the surface."
4. NASA/JPL Photojournal PIA01447 caption — T. Parker sight-line triangulation against
   Viking Orbiter images; *Science* 278, 1746 (1997).
5. Kirk, R. L., et al. (1999), "Digital photogrammetric analysis of the IMP camera
   images…," *JGR* 104(E4), doi:10.1029/1998JE900012 — control network + DTM mapping of
   the site.
6. University of Arizona HiRISE, PSP_001890_1995 and PSP_002391_1995 pages — 28.5 cm/px
   (25 cm/px map-projected), lander and Twin Peaks identified, site topography.
7. *Encyclopædia Britannica*, "Great Sphinx of Giza" — 240 ft (73 m) long, 66 ft (20 m)
   high.
8. NASA, PIA03225 "Highest-Resolution View of 'Face on Mars'"; *Britannica*, "Mars
   Global Surveyor" — 2001 re-imaging, natural mesa ~3 km × 250 m.
9. Nature 352, 697 (1991); *EPSL* (2021); *Science Advances* (2024) — mainstream
   accounts of Martian ¹²⁹Xe.

Repository-internal evidence: `preview (3).webp` (annotated scale system),
`preview (2).webp` (ruler-on-print photograph), `chat-history.txt` (provenance of the
AI-written documents), `analysis/measure_twin_peaks.py` (all computations in this
report, re-runnable).
