# A Scientific Methodology for Verifying the Size of Surface Features in Lander Imagery

**Purpose.** A step-by-step, falsifiable protocol for turning "how big is that thing in
the Mars image?" into a defensible number with an uncertainty attached — built from the
lessons of `VALIDATION_REPORT.md`. It is written for the Mars Pathfinder / Twin Peaks
scene but applies to any lander or rover camera with published calibration.

**Design principles**

1. Work in **angular units** on products of known pixel scale — never in ruler inches on
   a print, unless the print's pixels-per-inch is itself measured and carried through.
2. Get distance from a source that can actually deliver it at the required range;
   propagate its error.
3. Prefer **calibrated archive data** (PDS) over press-release visualizations.
4. Every derived size must pass at least one **independent cross-check** with a known
   answer before the method is trusted on an unknown.
5. State the null hypothesis before interpreting morphology.

---

## Step 0 — Define the target operationally

Name the product and the pixel footprint. "Object X" must become: *product PIA02405,
pixel box (x₁,y₁)–(x₂,y₂)*, so that anyone can re-identify it. A feature that cannot be
pinned to pixels cannot be measured or falsified.

## Step 1 — Use calibrated data, know your product

The archival record for this scene is the IMP Experiment Data Record on the NASA
Planetary Data System (PDS Imaging Node: `pds-imaging.jpl.nasa.gov`, data set
`MPFL-M-IMP-2-EDR-V1.0`, with *The Imager for Mars Pathfinder User's Guide* in the
`document/` directory). Native frames are 256×256 px per eye at 0.98 mrad/pixel (Smith
et al. 1997, *JGR* 102(E2), doi:10.1029/96JE03568).

If a press product must be used, first establish its relation to native pixels. For
PIA02405/06 the catalog page states the frames "were enlarged by 500% and then co-added
using Adobe Photoshop" — hence 1 product px = 0.196 mrad — and warns you it was
colorized and re-balanced. Treat such products as *geometry-approximate, radiometry- and
detail-unreliable*: no sub-native-pixel morphology, no photometric claims, and no stereo
measurement across independently assembled mosaics.

**Resolution floor rule:** the smallest credible morphological detail is ~2 native
pixels: at range Z that is `2 × Z × 0.98 mrad` — ≈1.7 m at 860 m. Anything finer seen in
a 500 %-enlarged product is interpolation.

## Step 2 — The angular-size relation

For a feature at range Z subtending N native pixels:

```
size = Z × N × IFOV        (IFOV = 0.98 mrad/px; small-angle regime)
```

This is exact enough for any Pathfinder scene (worst case here: 40 mrad → error < 0.1 %).
The measurement problem therefore splits into **N** (count pixels — easy, ±1–2 px) and
**Z** (range — the hard part, and where the repo's original system failed).

## Step 3 — Getting Z honestly

Ranked by reliability at this site:

**3a. Orbital identification (best; no Z needed at all).** If the feature can be located
in a *map-projected* orbital image, measure it there directly: pixels × map scale. The
Pathfinder site has HiRISE coverage at "28.5 cm/pixel … map-projected to 25 cm/pixel"
with the lander itself visible (PSP_001890_1995, uahirise.org/PSP_001890_1995) and a
stereo topography observation (PSP_002391_1995). Distance ambiguity vanishes because map
projection already removed perspective. This is how the Twin Peaks themselves were tied
to Viking Orbiter images in 1997: "Sight lines to various landmarks seen along the
horizon in Mars Pathfinder camera images were matched to features seen in Viking Orbiter
images by T. Parker … to within a few hundred meters" (NASA/JPL, PIA01447 caption).

**3b. Lander stereo — inside its validity envelope only.** Range error is
σ_Z = Z²σ_d/(fB) with f = 1000 px, B = 0.15 m, σ_d ≈ 0.2 px:

| Z | σ_Z | usable? |
|---|-----|---------|
| 10 m | ±0.13 m (1.3 %) | yes |
| 30 m | ±1.2 m (4 %) | yes |
| 75 m | ±7.5 m (10 %) | marginal |
| 300 m | ±120 m (40 %) | no |
| 860 m | ±986 m (115 %) | meaningless |

Rule of thumb for IMP: stereo ranging is science-grade only to a few tens of meters.
(The site's rigorous DTM work — Kirk et al. 1999, *JGR* 104(E4),
doi:10.1029/1998JE900012 — used a photogrammetric control network on native frames, and
still concerns the near field for topography.) Distant-peak distances are *inputs from
cartography*, never outputs of lander stereo.

**3c. Ground-plane geometry (near field only).** A ground point at depression angle θ
below the true horizon is at Z = h/tan θ (camera height h = 1.5 m nominal, 1.75–1.85 m
as-deployed; "The imager rests on a pop-up mast 80 cm above the lander and 1.5 m above
the surface," mars.nasa.gov/MPF/mpf/sci_desc.html). Two hard limits: (i) locating the
true horizon to ±2 native px (1.96 mrad) moves Z by more than 100 % beyond ~380 m
(h = 1.5 m) / ~470 m (h = 1.85 m) — the threshold is Z = h/(2δ); at 150 m the excursion
is −16 %/+24 %; (ii) terrain
relief violates the flat-ground assumption everywhere in this scene ("bouldery ridges
and swales," per the caption). Use only below ~50 m, and quote the h and horizon-row
uncertainties.

**3d. What is *not* a method:** linear interpolation of range against image row between
an arbitrary zero mark and distant anchors. `VALIDATION_REPORT.md` §5.2–5.3 shows this
is wrong in form (the true mapping is hyperbolic and non-monotonic over terrain) and in
consequence (×1.84 size inflation at the anchors themselves).

## Step 4 — Heights near the skyline

Apparent summit-to-visible-base extent is a **lower bound**: intervening ridges occlude
the true base (measured here: ≥26.5 m North Twin, ≥22.7 m South Twin, vs 30–35 m
published). For true heights use orbital stereo topography (HiRISE DTM of
PSP_002391_1995) or published control-network results. Never read a height *upward from
the frame bottom*.

## Step 5 — Error budget (worked example: North Twin)

| Term | Value | Contribution to height |
|---|---|---|
| Pixel count N = 34 preview px (±2) | 30.8 mrad (±1.8) | ±6 % |
| IFOV 0.98 vs 1.00 mrad/px | 2 % systematic | ±2 % |
| Product/preview scale (catalog dims) | exact to 0.1 % | — |
| Range 860 m (caption, "approximately") | assume ±5 % | ±5 % |
| Base occlusion | one-sided | −0 / +30 % |
| **Total** | | **26.5 m, −2/+8 m** → consistent with 30–35 m |

Every published size should carry a line like this. If a term cannot be estimated,
the measurement is not finished.

## Step 6 — Falsification gates (run before believing any number)

1. **Known-answer test.** The pipeline must reproduce an independently published size in
   the same scene (here: peak heights 30–35 m; NASA caption). The original scale system
   *failed* this gate (57 m); the corrected angular pipeline *passes* (28.7–31.5 m).
2. **Cross-eye test.** Repeat on the other stereo eye; results must agree within the
   pixel-count error. (Framing offsets between the eyes don't matter for angular extents.)
3. **Ratio test.** Proportions must be independent of assumed range; if a conclusion
   survives only at one privileged distance, it is an artifact of the range assumption.
4. **Resolution gate.** No claim finer than 2 native pixels at the assumed range
   (Step 1). Morphological adjectives ("face," "paws," "carved edge") count as claims.
5. **Provenance gate.** No measurement across mosaic seams; no stereo from
   independently assembled products; note every resampling step between the detector and
   your measurement surface.

## Step 7 — Interpreting morphology (artificiality-type hypotheses)

Size and proportion similarity to a terrestrial monument is **not** evidence of
artificiality: a height/length ratio ~0.28 is shared by ordinary elongated mounds, and
at 860 m the data cannot resolve the sub-2-m detail that distinguishes carving from
erosion. The governing precedent is the Cydonia "Face": imaged at Viking resolution it
supported decades of artifact claims; re-imaged by Mars Global Surveyor (resolving
~1.5 m) it was "shown in the higher-resolution image to be a natural feature similar to
a butte or mesa on Earth" (NASA, PIA03225), a mesa "about 3 km in length … about 250
metres above the surrounding plain" (*Britannica*). The protocol that settled it —
**acquire decisively higher resolution, define discriminators in advance, publish the
null result if that's what comes back** — is available for this scene today at
25 cm/pixel (HiRISE PSP_001890_1995 / PSP_002391_1995).

Concretely, for Object X: (1) register the IMP scene to the HiRISE map product via the
peaks and the lander position; (2) locate Object X's pixel box in the orbital frame;
(3) measure its true plan dimensions and, from the DTM, its relief; (4) compare against
the pre-registered hypothesis (the repo's actual H1: plan length 73 m ± 15 % =
62.05–83.95 m, relief 20 m ± 25 % = 15.0–25.0 m; see ROADMAP.md P3.3) stated with
tolerances *before* looking. That is the experiment; it is decisive either way, and it
costs nothing — the data are public.

---

## Checklist (print this)

- [ ] Target defined as product + pixel box
- [ ] Product's native pixel scale and processing history quoted from source
- [ ] N measured in pixels, with uncertainty
- [ ] Z from orbital cartography, or stereo within its envelope, or near-field geometry — with uncertainty; never from linear print-position interpolation
- [ ] size = Z·N·IFOV, error budget table filled
- [ ] Known-answer, cross-eye, ratio, resolution, provenance gates passed
- [ ] Morphology claims limited to ≥2 native pixels; higher-resolution data sought for anything contested
- [ ] All sources institutional; all quotes verbatim with URLs

## Sources

- Smith et al. (1997), *JGR* 102(E2), doi:10.1029/96JE03568 (IMP: 15.0 cm baseline, 14.4°×14.0°, 0.98 mrad/px, f/18)
- Kirk et al. (1999), *JGR* 104(E4), doi:10.1029/1998JE900012 (site DTM, control network)
- NASA Photojournal PIA02405/PIA02406 catalog pages (product provenance; distances/heights; PDFs preserved in this repo)
- NASA/JPL PIA01447 caption (Parker sight-line triangulation; *Science* 278, 1746)
- NASA/JPL Mars Pathfinder Instrument Descriptions (camera 1.5 m above surface)
- University of Arizona HiRISE: PSP_001890_1995 (25–28.5 cm/px, lander visible), PSP_002391_1995 (site topography)
- NASA PIA03225 (Cydonia "Face" at MGS resolution); *Encyclopædia Britannica* ("Great Sphinx of Giza"; "Mars Global Surveyor")
- NASA PDS Imaging Node, `MPFL-M-IMP-2-EDR-V1.0` + IMP User's Guide (calibrated data)
