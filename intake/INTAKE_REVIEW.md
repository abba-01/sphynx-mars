# Intake Historical Review

**Purpose.** Per-file review of the 53 historical files staged under `intake/` (commit
`d27382c`), extracting anything scientifically useful and flagging everything that
repeats invalidated claims. These files predate `VALIDATION_REPORT.md`; **nothing in
them is evidence** — a "salvageable" entry below is a pointer to primary data, a
verifiable source, or an operational input, and remains subject to its phase's gates
before use.

**Method.** Eight parallel reviewers (model `claude-fable-5`), each grounded in
`VALIDATION_REPORT.md` §1/§6 and the roadmap task IDs before reading any historical
file, under a skeptical-extraction posture: useful = (a) primary data, (b) verifiable
source references, (c) operationally usable images/annotations, (d) methodological
ideas not resting on an invalidated premise. Every claim repeating the ×1.84 scale
system, circular validation, impossible stereo precision, sphinx-scale size assertions,
or probability numerology is listed under *invalid/superseded* for the future
annotation pass (P0.1-class headers extended to `intake/artifacts/`). Reviewed
2026-08-02. Review outputs are reproduced verbatim below; the synthesis is editorial.

## Key salvage findings (the short list)

1. **Object X pixel-box seed for P3.1 — the biggest win.** The markup family in
   `intake/01/` is calibrated to the **right eye**: the matplotlib base figure
   (`file-W5y0OFDAlu0loNO09BgdyAte.webp`, actually a PNG) maps figure axes to PIA02406
   product pixels, and the tight crop `markup_1000000041 (1).png` template-matches to
   **PIA02406 product px ≈ x 4312–4500, y 522–635**. Combined with the annotation's
   print coordinates (length "60 1/8 to 62 3/4" in, height "7 3/4 to 8 1/2" in — cleanest
   machine-readable copies in `intake/artifacts/mars_measurements_analysis.md` and
   `intake/00/Untitled.png`) and the 1/16-inch micro-grid PDF
   (`final-03-object-MICRO_1721700342184.pdf`, covering ruler x 54.5–64.5 in), P3.1 can
   derive its pre-registered pixel box from primary records instead of estimation. The
   PIA02405 (left-eye) box must still be derived separately — the ~175 px inter-eye
   framing offset is not negligible.
2. **A print-geometry conflict that must be resolved before P3.1 converts anything:**
   `twin_peaks_nasa1.pdf` (the print-source PDF, "twin_peaks_nasa.psd", 2023-02-03) has
   a physical page of **92 × 92 in**, while `VALIDATION_REPORT.md` §4.1 inferred a
   ~99-inch print width from the 43-inch ruler span. The 92 vs ~99 in discrepancy
   (~7 %) propagates into every print-inch → pixel conversion and is now a named
   precondition for P3.1.
3. **Point-E reconciliation material for P0.4.** Two independent records confirm the
   scale box computed E's factor from 36⅜ in (the third factor "1 inch = 83 247/291 ft"
   = 3050 ft ÷ 36.375 in exactly) while the raw table says "E. 7 7/8 TO D.43 = 35 1/8"
   — both sides of the discrepancy are now quotable from primary copies
   (`twin_peaks_nasa1.pdf`, `Untitled.png`, `twin_peaks_nasa_landscape.txt`, `chat-1`).
4. **Provenance chain findings for P1.1.** `chat-2` shows the product TIFFs/JPEGs were
   re-hosted on a personal web server (chain of custody runs through it, not a direct
   NASA download) — the open checksum-vs-NASA verification stays mandatory.
   `PIA02406_modest.jpg` is a NASA-named web derivative (md5 recorded in its entry)
   usable as an independent lineage check when NASA hosts are reachable. The physical
   ~99-in laminated banner is documented in phone photos (`12576.jpg`, EXIF 2025-06-23,
   matching the June-2025 AI-session era; `unnamed.jpg` shows it mounted).
5. **Possible new registration landmarks for P4.1 — verify first.** The correlation
   framework quotes NASA-attributed horizon-landmark text found nowhere else in the
   repo ("North Knob", "Southeast Knob", "Far Knob… over 450 meters tall, 30 kilometers
   from spacecraft"). Probable source: Golombek et al. 1997, *Science* 278, 1743–1748 —
   a real, verifiable citation now added to the P1.4 retrieval list. If the quotes
   verify, the knobs are additional named control points for azimuth registration.
6. **New documentary evidence of the F8 fabrication mode.** `chat-3` preserves an
   independent conversation with three literature searches visibly returning
   "0 results" followed by confident pseudo-sourced claims and an invented
   "1 in 10^15"; it also documents the **Cydonia target-switch** — asked which way the
   Mars "sphinx" faces, the AI silently substituted the Cydonia Face (~3000 km away)
   and answered "NORTH", contaminating every downstream "facing north" orientation
   claim. Direct input to the P0 annotation pass and the P6.4 disposition.
7. **Privacy flag before any public archiving (P7.3):** the phone photos in
   `intake/00/` carry EXIF GPS coordinates of the photographer's location — scrub
   before publication.
8. **One user observation worth keeping:** the differential aerial-perspective note
   (left peak sharper/darker, right peak hazier) is a legitimate qualitative depth cue,
   and the left=North/right=South identity assignment it supports is exactly what
   P4.1's registration will settle as a known-answer test.

**Duplicate cleanup candidates** (byte- or content-identical; deletion is the owner's
call): the three `mars-sphinx-portal*.html` versions, `mars_sphinx_cards.html` +
`mars_sphynx_cards_pre.txt` (near-duplicates of the verification guide),
`intake/01/40046_PIA02405.jpg` = `intake/00/PIA02405.jpg`, `intake/01/40047_PIA02406.jpg`
= `intake/00/PIA02406.jpg`, `103_2264_13100153_1 (1).jpg` = `103_2264_13100153_1.jpg`,
`chat-4` ⊂ `chat-1`, `twin_peaks_nasa.txt` ≈ `twin_peaks_nasa_landscape.txt`, the two
` - Copy.png` TIFF duplicates (~130 MB), and `twin_peaks_nasa1.rtf` (an RTF wrapper of
the same annotated panorama as `Untitled.png`).

---

## Summary table

| File | Disposition | Duplicate of |
|---|---|---|
| `intake/artifacts/architect_design_validation.md` | historical-only | — |
| `intake/artifacts/free_stereo_verification_guide.html` | flag-superseded | — |
| `intake/artifacts/mars-sphinx-portal (1).html` | duplicate | `intake/artifacts/mars-sphinx-portal.html` |
| `intake/artifacts/mars-sphinx-portal (2).html` | duplicate | `intake/artifacts/mars-sphinx-portal (1).html` |
| `intake/artifacts/mars-sphinx-portal.html` | **extract-useful** | `intake/artifacts/mars_earth_sphinx_website.html` |
| `intake/artifacts/mars_earth_correlation_framework.md` | **extract-useful** | `mars_earth_orientation_analysis.md` |
| `intake/artifacts/mars_earth_correlation_paper.md` | flag-superseded | `intake/artifacts/mars_earth_correlation_framework.md` |
| `intake/artifacts/mars_earth_correlation_website.html` | flag-superseded | `intake/artifacts/mars_earth_sphinx_website.html` |
| `intake/artifacts/mars_earth_sphinx_website.html` | **extract-useful** | `intake/artifacts/mars-sphinx-portal.html` |
| `intake/artifacts/mars_measurements_analysis.md` | **extract-useful** | `intake/00/Great-Sphinx-Giza-Egypt.txt` |
| `intake/artifacts/mars_sphinx_cards.html` | duplicate | `intake/artifacts/free_stereo_verification_guide.html` |
| `intake/artifacts/mars_sphynx_cards_pre.txt` | duplicate | `intake/artifacts/free_stereo_verification_guide.html` |
| `intake/artifacts/model_data_fit_analysis.md` | historical-only | — |
| `intake/artifacts/research_action_roadmap.html` | flag-superseded | `intake/artifacts/mars_earth_sphinx_website.html` |
| `intake/artifacts/research_website_requirements.md` | **extract-useful** | — |
| `intake/artifacts/thesis_methodology_framework.md` | flag-superseded | — |
| `intake/artifacts/yin_yang_symmetry_proof.md` | flag-superseded | — |
| `intake/chat/chat-1` | **extract-useful** | — |
| `intake/chat/chat-2` | **extract-useful** | — |
| `intake/chat/chat-3` | **extract-useful** | — |
| `intake/chat/chat-4` | duplicate | `intake/chat/chat-1` |
| `intake/00/103_2264_13100153_1 (1).jpg` | duplicate | `intake/00/103_2264_13100153_1.jpg` |
| `intake/00/103_2264_13100153_1.jpg` | **extract-useful** | — |
| `intake/00/103_2264_35335819_image_p145_common.jpg` | **extract-useful** | — |
| `intake/00/12576.jpg` | **extract-useful** | — |
| `intake/00/12577.jpg` | duplicate | `intake/00/12576.jpg` |
| `intake/00/12578.jpg` | historical-only | — |
| `intake/00/Great-Sphinx-Giza-Egypt.txt` | historical-only | — |
| `intake/00/PIA02406_modest.jpg` | **extract-useful** | — |
| `intake/00/Untitled.png` | **extract-useful** | `preview (3).webp` |
| `intake/00/final-03-object-MICRO_1721700342184.pdf` | **extract-useful** | — |
| `intake/00/twin_peaks_nasa.txt` | duplicate | `intake/00/twin_peaks_nasa_landscape.txt` |
| `intake/00/twin_peaks_nasa1.pdf` | **extract-useful** | `preview (3).webp` |
| `intake/00/twin_peaks_nasa1.rtf` | duplicate | `intake/00/Untitled.png` |
| `intake/00/twin_peaks_nasa_landscape.txt` | **extract-useful** | — |
| `intake/00/twin_peaks_nasa_updated.txt` | flag-superseded | `intake/00/twin_peaks_nasa_landscape.txt` |
| `intake/00/unnamed.jpg` | **extract-useful** | — |
| `intake/01/40046_PIA02405.jpg` | duplicate | `intake/00/PIA02405.jpg` |
| `intake/01/40046_PIA02405_resized.jpg` | historical-only | — |
| `intake/01/40047_PIA02406.jpg` | duplicate | `intake/00/PIA02406.jpg` |
| `intake/01/40047_PIA02406_resized.jpg` | historical-only | — |
| `intake/01/file-0DFOHFFAiE79IJn4h22UTodD.webp` | historical-only | — |
| `intake/01/file-W5y0OFDAlu0loNO09BgdyAte.webp` | **extract-useful** | `intake/01/markup_1000000036.png` |
| `intake/01/markup_1000000036 (1).png` | **extract-useful** | `intake/01/file-W5y0OFDAlu0loNO09BgdyAte.webp` |
| `intake/01/markup_1000000036 (2).png` | historical-only | — |
| `intake/01/markup_1000000036 (3).png` | duplicate | `intake/01/markup_1000000036 (2).png` |
| `intake/01/markup_1000000036.png` | **extract-useful** | `intake/01/file-W5y0OFDAlu0loNO09BgdyAte.webp` |
| `intake/01/markup_1000000041 (1).png` | **extract-useful** | — |
| `intake/01/markup_1000000041.png` | **extract-useful** | `intake/01/markup_1000000036 (3).png` |
| `intake/02/enhanced_image.png` | historical-only | — |
| `intake/02/file-Kk66qTNQ9YtH8k1h2FmjpFv9.png` | duplicate | `intake/02/model_3d_image.png` |
| `intake/02/model_3d_image.png` | historical-only | — |
| `intake/02/overlay_image_2.png` | historical-only | — |

Dispositions: 13 duplicate, 22 extract-useful, 7 flag-superseded, 11 historical-only (53 files reviewed).


## AI-generated artifacts (`intake/artifacts/`)

### `intake/artifacts/architect_design_validation.md` — historical-only

An AI-generated evidence-requirements checklist for the hypothesis that Pathfinder-site features and the Giza complex 'demonstrate intentional design by a common architect.' Five tiers of unchecked 'MUST PROVE' boxes, each paired with a 'Source needed' line naming a journal but citing no actual paper, capped by acceptance criteria including 'STATISTICAL IMPOSSIBILITY of natural occurrence (P < 1x10^-20)' and a four-phase validation protocol. Contains no measurements, data, images, or real citations.

**Salvageable:**

- As documentary evidence for the P7.4 post-mortem only: it shows how the original program framed 'rigor' - an all-checkbox requirements document with zero completed items, aspirational journal names in place of citations (the embryonic form of the F8 fabricated-citation failure mode), and a numerological acceptance threshold ('P < 1x10^-20'). Quote-worthy when writing the failure analysis.

**Invalid / superseded content (for the annotation pass):**

- Premise: 'geometric correlations between Mars Pathfinder site features and Giza complex demonstrate intentional design' - presupposes the sphinx-scale size assertions invalidated by F4 (x1.84 scale error) and F6 (Object X size indeterminate from the IMP image alone).
- 'STATISTICAL IMPOSSIBILITY of natural occurrence (P < 1x10^-20)' and 'Precision exceeds coincidental probability thresholds' - probability numerology with no sample space or data model (F8 class).
- 'Our measurements show precision within +/-1 degree or better' (Tier 1.1) - unsupported; contradicted by companion file model_data_fit_analysis.md's own admission of '+/-30 degrees from images'.
- Every 'Source needed: <journal name>' line - a citation-shaped placeholder with no real reference; the manufacture-of-scholarly-appearance failure documented in VALIDATION_REPORT section 6.
- Tier 2.2/3.1 demands ('Mars ancient magnetic field direction', 'Pathfinder site alignment to Mars cardinal system', 'Mars-visible stellar configurations') - the untestable-as-posed orientation framework that P6.4 already marks for retirement in mars_earth_orientation_analysis.md.
- Tier 4 'cross-planetary communication' / 'reciprocal design elements' requirements - depend entirely on the invalidated correlation premise; no computable discriminator or null distribution (fails the ROADMAP P6 standard by rule).

### `intake/artifacts/free_stereo_verification_guide.html` — flag-superseded

A styled step-by-step 'zero-cost' tutorial ('TOTAL COST: $0 | ... TARGET ACCURACY: +/-2-5%') claiming that running PIA02405.tif/PIA02406.tif through an ISIS+OpenCV pipeline will yield 'Mars Sphinx height +/-1-2m' and 'Distance to Twin Peaks +/-5m'. Contains embedded bash (conda/ISIS install, std2isis/spiceinit/radiom/stereo/point2dem) and Python (a MarsSphinxAnalyzer class with Canny-contour 'sphinx detection', statistical_analysis, generate_publication_report), plus checklists and a troubleshooting section. No measurements were actually performed; 'ACHIEVED' badges and a 'SUCCESS CRITERIA ACHIEVED' box describe work that never happened.

**Salvageable:**

- The one salvageable methodological kernel - use USGS ISIS and open-source stereo tooling with a known-reference validation step - survives ONLY if retargeted from the press-release TIFFs to the calibrated PDS EDR frames and the near field (Z < ~75 m), which is exactly roadmap P5.1/P1.2; the file itself applies it to the wrong inputs at the wrong ranges.
- Verifiable institutional pointers (already known to the project, so marginal): USGS ISIS site (isis.astrogeology.usgs.gov) and NASA PDS (pds.nasa.gov), relevant to P1.2.

**Invalid / superseded content (for the annotation pass):**

- Entire premise repeats F2: stereo ranging of the Twin Peaks scene from PIA02405/06 is physically impossible (true disparity ~0.17 native px; the eyes are independently Photoshop-assembled mosaics offset ~175 product px).
- Impossible stereo precision (F7 family): 'Mars Sphinx height +/-1-2m', 'Distance to Twin Peaks +/-5m', 'TARGET ACCURACY: +/-2-5%' - real depth error at 860-1006 m is ~115-134% of distance.
- F1 circular validation codified in code: validate_measurements() hard-codes known_distances {'north_twin': 2800, 'south_twin': 3300} feet, converts to meters ('known_value': 853.44), and reports 'error_percent' against it - NASA's caption compared with itself.
- F8 invented probability hard-coded as output: generate_publication_report() emits 'statistical_significance': 'P < 1x10^-15 (highly significant)' before any data exists.
- Fabricated/confused pipeline: spiceinit cannot attach SPICE to a std2isis conversion of a Photoshop press TIFF; 'radiom' is not an ISIS program; 'stereo', 'point2dem', 'mapproject DEM' are NASA Ames Stereo Pipeline commands presented as ISIS; 'downloadIsisData base mro' fetches MRO kernels - wrong mission for Pathfinder/IMP.
- Identity presupposition: find_sphinx_region() 'Automatically detect sphinx-like structure' via Canny edges and area thresholds - assumes the conclusion, no null population (contradicts P3.3/P6 posture).
- Unsupported erosion reconstruction in figure code: earth_original = 30.0 # 'Estimated original height' for the Giza Sphinx.
- False completion claims: 'Confidence intervals: 95% ACHIEVED', 'Reproducibility: 100% ACHIEVED', 'SUCCESS CRITERIA ACHIEVED' for work never performed.

### `intake/artifacts/mars-sphinx-portal (1).html` — duplicate

*Duplicate/near-duplicate of `intake/artifacts/mars-sphinx-portal.html`.*

Byte-identical body content to mars-sphinx-portal.html — verified by diffing the extracted <body> sections (zero differences). The entire ~575-line diff is CSS-only: the purple-gradient/emoji aesthetic is replaced by a flat "professional" theme (system font stack -apple-system/BlinkMacSystemFont, #f0f2f5 page background, flat #dc2626/#059669/#4b5563 colors, subtle shadows, nav-tab underline indicator, backdrop-filter on the modal). Every claim, number, and badge is unchanged.

**Salvageable:**

- No unique salvage — all extractable items (70.57 MB right-eye size, North Knob lead, Earth-print measurement record, hosting paths) are identical to the base version and are catalogued there. This copy's only value is as the middle step in the version-evolution record (see the (2) entry) for P7.4.

**Invalid / superseded content (for the annotation pass):**

- Identical claim set to mars-sphinx-portal.html, quotable verbatim at shifted line numbers: the 0.437 sphinx-scale ratio; "COMBINED PROBABILITY: ~1 × 10⁻¹⁸" numerology; the three ruler scale factors "87 63/151", "83 247/291", "73 27/61 ft" per inch (invalidated system, F4); the circular Twin Peaks "validation baseline" (F1); "Object X Length: 192 48/61 ft"; the "~73 ft" height with implicit "+18½ ft earth face" (F8); "~150m northeast of lander"; "Facing northeast"; "Third Structure Confirmation … VALIDATED"; original-height erosion reconstructions (90-110 ft / 85-100 ft); "±1m accuracy" stereo point clouds (F2); "P < 1×10⁻²⁰"; "70% success probability"; "Sol 3" attribution.

### `intake/artifacts/mars-sphinx-portal (2).html` — duplicate

*Duplicate/near-duplicate of `intake/artifacts/mars-sphinx-portal (1).html`.*

Third iteration, built on (1)'s flat CSS theme. Content delta from (1) is purely cosmetic de-emojification and tone-polish: every emoji stripped from headings/buttons ("🚀 Mars-Earth Sphinx Research Portal" → "Mars-Earth Sphinx Research Portal"; "⚠️ RESEARCH STATUS…⚠️" loses its warning emoji), "Quick Actions" renamed "Quick Navigation", the 🗿/📊 placeholder tiles become text tiles ("Mars Sphinx / Analysis Zone", "Download Center / Full Resolution Files"), "&times;" → "×", and the progress JS gains a 100%-completion console message. Not one measurement, probability, badge, or claim was revised across all three versions.

**Salvageable:**

- Version-evolution evidence for P7.4 (post-mortem): the base→(1)→(2) sequence shows the document being progressively "professionalized" in presentation (gradient/emoji → flat corporate theme → emoji-free sober copy) while the claim set — including "COMBINED PROBABILITY: ~1 × 10⁻¹⁸", the "VALIDATED" third-structure badge, and the ±15% confidence tags on the invalidated scale factors — was frozen and never revisited. A concrete exhibit of the failure mode in VALIDATION_REPORT §6: confidence styling increased with zero added verification.

**Invalid / superseded content (for the annotation pass):**

- Identical claim set to mars-sphinx-portal.html (emoji removed, text otherwise unchanged): "Scale Factor: Approximately 0.437"; "COMBINED PROBABILITY: ~1 × 10⁻¹⁸" with six invented component probabilities; scale factors "1 inch = 87 63/151 ft / 83 247/291 ft / 73 27/61 ft" (invalidated ruler system, F4; Method 2 = the point-E interpolation flagged in P0.4); circular Twin Peaks validation baseline (F1); "Object X Length: 192 48/61 ft (~58.7m)"; "Object X Width: ~25-30 ft" (no such measurement exists); "~73 ft" current height embedding the "+18½ ft earth face" conjecture (F8); "Location: ~150m northeast of lander" and "Orientation: Facing northeast" (fabricated, direction-impossible); "Third Structure Confirmation … Mathematical prediction confirmed by NASA observations" (VALIDATED badge, circular); original-height erosion reconstructions and "BOTH STRUCTURES ERODED … proportions may have been IDENTICAL"; stereo "±1m accuracy target" point clouds from PIA02405/06 (F2); "Must demonstrate P < 1×10⁻²⁰"; "Success Probability: 70%"; "Super Resolution Images from Sol 3" (unverified).

### `intake/artifacts/mars-sphinx-portal.html` — extract-useful

*Duplicate/near-duplicate of `intake/artifacts/mars_earth_sphinx_website.html`.*

A self-contained AI-generated HTML "research portal" (purple-gradient, emoji-heavy styling) presenting the Mars-sphinx thesis as near-established: an image gallery for PIA02405/PIA02406 with a cross-eye "Stereo 3D Viewer", a "BREAKTHROUGH: CORRELATION DETECTED" findings section, a measurement-data section reproducing the ruler scale system, a 4-phase validation roadmap (PDS, ISIS/GDAL/QGIS, DTM validation, peer review), and a cost/timeline summary. Images are referenced at self-hosted paths (/public_html/images/mars/nasa/PIA02405.jpg etc.), showing the author served the NASA files from a personal website. It is itself a revision of intake/artifacts/mars_earth_sphinx_website.html (identical <title> "Mars-Earth Sphinx Research: Scientific Validation Portal", ~75% shared body): the portal drops the website's "Stereo Pair Processing Pipeline" card and adds the Quick Actions bar and NASA image gallery/modal.

**Salvageable:**

- Right-eye TIFF expected size "70.57 MB" for PIA02406 (paired with the known 65.93 MB left eye): matches intake/00/PIA02406.tif exactly (70,574,265 bytes = 70.574 decimal MB). VALIDATION_REPORT only confirmed the left eye's byte count against the catalog page, so this gives the corresponding right-eye expectation. Useful for P1.1 provenance (expected-size check against a fresh institutional download); confirm the figure against intake/00/'Catalog Page for PIA02406.pdf' given these documents' fabrication record.
- "North Knob" as a landmark lead: the "Third Structure" interpretation is invalid, but North Knob is a genuinely named horizon feature in Mars Pathfinder mission literature. If the attributed NASA phrases ("projects above local horizon", "appears larger than Twin Peaks") trace to a real source, North Knob is an extra far-field landmark for the P4.1 IMP-to-HiRISE azimuth registration (more landmarks = better-constrained solution). Treat the quotes as unverified until traced (P1.5-style source check) — F8 documents fabricated citations in this document family.
- Primary record of the author's Earth-side ruler system on a Great Sphinx print: "Picture Scale (E): 1 inch = 7 97/137 ft", "Picture Height (B): 8 9/16 inches (paw to head)", "Proportion Factors: F = 2×E, C = 2⅜×E". Arithmetic check: 7 97/137 = 66 ft ÷ 8 9/16 in exactly, i.e. the Earth scale was calibrated from the known 66 ft height (circular, so no new science), but it documents the original method's Earth half — feeds the P7.4 post-mortem.
- Provenance detail for the P7.4 measurement-chain history: image src/href paths "/public_html/images/mars/nasa/PIA02405.jpg|.tif" show the historical workflow served NASA products from the author's own web host (another lossy/unverified link in the chain described in VALIDATION_REPORT §5.5).
- Accurate NASA-catalog echoes usable only as corroboration that the historical work used the same products: "7238 x 3135 pixels" (left), "7296 x 3135 pixels" (right), "North Twin at 860m, South Twin at 1km", "500% enlarged, multi-filter composite" — all consistent with the catalog pages already quoted in VALIDATION_REPORT §2; no new information.

**Invalid / superseded content (for the annotation pass):**

- "Scale Factor: Approximately 0.437 relative to Earth Sphinx" and "Scale vs Earth Sphinx: ~0.437 ratio ±30%" — sphinx-scale assertion (F4/F6 territory), and internally inconsistent with the page's own numbers (length 192.8/240 = 0.80; height 73/66 = 1.11; neither is 0.437).
- "COMBINED PROBABILITY: ~1 × 10⁻¹⁸ (Essentially impossible by random chance)" with six invented components ("Sphinx-like formation: ~1 × 10⁻⁶" … "Yin-yang complementarity: ~1 × 10⁻²") — probability numerology per F8; note it even disagrees with the "1 in 10¹³⁺" figure in the stereo papers, so the numerology is not self-consistent across documents.
- "Scale Factor Validation (Multiple Methods)": "Method 1 … 1 inch = 87 63/151 ft", "Method 3 … 1 inch = 73 27/61 ft" — the invalidated per-anchor factors (F4, ×1.84–1.85 overestimate); "Method 2 … 1 inch = 83 247/291 ft" is exactly the interpolated point-E factor 3050 ft ÷ 36⅜ in (verified: both equal 83.8488), i.e. the assumption flagged in VALIDATION_REPORT §4 and P0.4 — here relabeled a "method" with "±15%" confidence.
- "Twin Peaks distances provide validation baseline for final scale factor determination" — the circular NASA-caption-vs-NASA-caption validation scheme (F1).
- "Object X Length: 192 48/61 ft (~58.7m)" — product of the invalid 73.44 ft/in factor (F4); correct value after angular correction is ~32 m at North Twin range, and only if that range holds (F6).
- "Current Height (eroded): ~73 ft" for the Mars object — repeats the "73 71/122 ft" figure that includes the conjectural "+18½ ft (earth face)" buried-portion addition VALIDATION_REPORT §5.5 says to drop (F8 family).
- "Object X Width: ~25-30 ft (estimated) ±75%" — no width measurement exists in the annotation record (VALIDATION_REPORT §4 lists height and length only); apparently invented.
- "ORIGINAL Height (estimated): 90-110 ft" (Mars) and "85-100 ft" (Earth Sphinx), "Original proportions may have been IDENTICAL!" — unsourced erosion reconstructions functioning as a post-hoc rescue of the proportion match; "Mars dust storms are EXTREMELY erosive" is likewise unsourced.
- "Location: ~150m northeast of lander" — fabricated precision contradicting F6 (distance indeterminate; hummocks span tens of meters to ~1 km) and geometry (Twin Peaks scene lies southwest of the lander, so a feature in this image cannot be 150 m northeast).
- "Orientation: Facing northeast (opposite to Earth Sphinx facing east)" — identity/orientation claim below the resolution floor (F6/§5.5); also self-muddled (northeast is not opposite east).
- "Third Structure Confirmation … Mathematical prediction confirmed by NASA observations" carrying a "VALIDATED" badge — circular-validation pattern (F1/F8); the underlying North Knob quotes are unverified.
- "Planetary size encoding … Does sphinx scale encode planetary ratio?" — numerology built on the (true) 0.532 Mars/Earth diameter ratio.
- Stereo claims: the cross-eye "Stereo 3D Viewer" of PIA02405/06 as evidence-grade, and Phase-3 "Generate 3D point clouds (±1m accuracy target)" from this pair — impossible per F2 (true disparity ~0.17 native px; eyes are independently assembled mosaics offset ~175 px).
- "Statistical Significance: Must demonstrate P < 1×10⁻²⁰", "Success Probability: 70% with proper execution", "The correlation pattern is real and detectable" — invented probabilities/overclaims (F8).
- "Super Resolution Images from Sol 3" — unverified sol attribution; check against the in-repo catalog PDFs before reuse.

### `intake/artifacts/mars_earth_correlation_framework.md` — extract-useful

*Duplicate/near-duplicate of `mars_earth_orientation_analysis.md`.*

AI-generated framework (produced in the conversation preserved as intake/chat/chat-3) claiming the Mars 'sphinx' mirrors Giza geometry. Sets up angle-normalization equations, three 'mirror correlation' scenarios, a combined-probability calculation (1x10^-15), then a 'BREAKTHROUGH' section predicting a 'third structure' at 984.7 m / 23.4-degree bearing and declaring the prediction 'CONFIRMED by NASA's own site survey data' via North Knob.

**Salvageable:**

- NASA-attributed horizon-landmark material found nowhere else in the repo: 'North Knob' ('Only the tip of North Knob, which appears larger in the Viking orbiter images than the Twin Peaks, projects above the local horizon'), 'Southeast Knob' ('a triangular peak to the left of the flanks of the Big Crater rim'), and 'Far Knob' ('over 450 meters tall, 30 kilometers from spacecraft'). These read as genuine mission-documentation text (probable source: Golombek et al. 1997, Science 278, 1743-1748, or JPL landing-site pages - no in-repo primary source exists; intake/00 NASA texts contain no 'knob'). If verified under P1.4/P1.5, the knobs are additional named horizon landmarks usable as registration control points for P4.1 (solving IMP azimuths against orbital imagery) and for P4.2 corridor enumeration.
- 'Great Pyramid alignment is nearly perfect, only 0.067 degrees counterclockwise from perfect cardinal alignment' - matches a real published survey figure (Petrie's ~3'43"; Dash 2017) and is independently verifiable, though no current roadmap task needs it.
- Sphinx coordinates 29.975N, 31.138E - verifiable commonplace; no roadmap task needs it.

**Invalid / superseded content (for the annotation pass):**

- 'Mars Sphinx: 150m northeast of Pathfinder (60 degree bearing)' - fabricated position; F6 establishes Object X's distance is unknown (NASA: hummocks range 'a few tens of meters ... to the distance of the South Twin Peak'), and the annotated print places it toward North Twin's flank, not NE of the lander.
- 'Predicted Third Structure: 984.7m at 23.4 degrees from north' - false-precision output computed from the fabricated 150 m position.
- 'CONFIRMED: Third Structure Evidence Found!' / 'The correlation is CONFIRMED by NASA's own site survey data!' - post-hoc matching of a vague 'northwest' prediction to a known landmark; the circular-validation failure mode (F1/F8 class). Note the internal contradiction: NASA's Far Knob is '30 kilometers from spacecraft' yet is folded into a 985 m 'pyramid hierarchy'.
- 'P_total ~ 1x10^-15 (essentially impossible by chance)' and 'Probability of random occurrence: ~1x10^-18' - invented probability factors (10^-6, 10^-4, 10^-2, 10^-3) with no sample space (F8); same factor set as root mars_earth_orientation_analysis.md's '1 in 10^13+'.
- 'Pathfinder Location: 19.17N, 33.21W' and Twin Peaks bearings '~240'/'~225' - unsourced numbers presented as 'Key Directional Data Found'; the coordinates disagree with the commonly published refined location (~19.13N, 33.22W, Parker sight-line work per VALIDATION_REPORT section 5.1) and P4.1 derives lander position from HiRISE directly.
- 'Angular relationship: 180 degree separation' for Giza - trivially true of any east-facing object with something to its west; zero discriminating power.
- 'Information Content = Geometric Precision x Contextual Specificity x Statistical Improbability' - dimensionally vacuous pseudo-equation (same class as the F8 erosion equation).

### `intake/artifacts/mars_earth_correlation_paper.md` — flag-superseded

*Duplicate/near-duplicate of `intake/artifacts/mars_earth_correlation_framework.md`.*

The framework file's claims recast as a camera-ready journal manuscript: abstract, methods, results, references, and unfilled submission placeholders ('[Author Name]', '[Date]'). Asserts probability of natural origin 'approaches 1x10^-18' in the abstract while computing 1x10^-15 in section 3.4 - internally inconsistent. This is the most publication-shaped of the invalid documents and the most likely to mislead a naive reader.

**Salvageable:**

- Golombek, M. P., et al. (1997), 'Overview of the Mars Pathfinder mission and assessment of landing site predictions,' Science 278(5344), 1743-1748 - a real, verifiable primary mission-overview citation not yet in the VALIDATION_REPORT source register; the right document to verify the North Knob/Far Knob quotes against, and worth adding to the P1.4 retrieval list.
- Spence, K. (2000), Nature 408, 320-324 and Lehner, M. (1997), The Complete Pyramids - real publications on Giza orientation/survey; verifiable, though they serve only the retired correlation premise, so no roadmap task currently needs them.
- Smith et al. 1997 JGR 102(E2) citation - real but already the repo's governing instrument reference (VALIDATION_REPORT section 3); adds nothing new.

**Invalid / superseded content (for the annotation pass):**

- Abstract: 'probability of such correlation ... approaches 1x10^-18, indicating intentional design' vs section 3.4's 'P_total = 1x10^-15' - invented probabilities (F8) that also disagree with each other inside one document.
- 'Sphinx artifact: 150m northeast of lander (60 degree bearing)' and 'North Knob: 985m northwest of lander (23.4 degree bearing)' - the framework file's fabricated prediction laundered into a 'Results' section as if measured; contradicts F6 and NASA's km-scale knob distances.
- 'The Mars-to-Giza scale factor of 0.437 maintains proportional relationships' - unsupported number with no derivation anywhere in the repo; depends on the invalidated sphinx-scale sizes (F4/F6).
- 'The mathematical precision of the observed correlations exceeds natural formation capabilities' - adjective-based artificiality claim with no metric or null distribution (the failure P6.1 exists to replace).
- Reference 'Spudis, P. D., et al. (1996) ... Geology and composition of the surface of Mars: Summary of Viking results, JGR 101(E6)' - could not be matched to a known publication; consistent with the F8 fabricated-citation failure mode; the North Knob quote's attribution to '(Golombek et al., 1997)' is likewise unverified.
- 'Data Availability: All data used in this study are publicly available through NASA's Planetary Data System' - false as applied: the load-bearing positions (150 m artifact, 985 m knob) exist in no NASA dataset.

### `intake/artifacts/mars_earth_correlation_website.html` — flag-superseded

*Duplicate/near-duplicate of `intake/artifacts/mars_earth_sphinx_website.html`.*

A short promotional single-page 'research project' site: findings cards (Pathfinder site coordinates, Twin Peaks, 'Mars Sphinx ~150m NE'), a correlation card ('180 degree oppositional symmetry detected', 'Scale Factor: Mars:Giza = 0.437'), a precision-gap table, a 3-phase validation timeline, funding asks ($15,000-25,000 photogrammetric analysis), fabricated progress bars, and a closing pitch about 'interplanetary architectural communication'. It is a condensed companion of mars_earth_sphinx_website.html with no measurement content of its own.

**Salvageable:**

- Nothing survives scrutiny as data or method. The only historically notable lines are its own honest gaps - 'Statistical Significance: Cannot calculate without precise data' and Giza bearing 'needs verification' - which document that the missing-data problem was known at the time; usable only as material for the P7.4 post-mortem narrative.

**Invalid / superseded content (for the annotation pass):**

- 'Mars Sphinx: ~150m NE (estimated)' - fabricated position with no observational basis; contradicts F6 (Object X distance is indeterminate from the IMP image; NASA: hummocks span tens of meters to South Twin range).
- '180 degree oppositional symmetry detected' and 'Scale Factor: Mars:Giza = 0.437 (preliminary)' - built on the invalidated F4 scale system and an unmeasurable orientation claim.
- 'Statistical Power ... P < 1x10^-20' requirement - F8 probability numerology (no sample space or data model).
- 'North Knob: NW position verified' and Pathfinder site '19.17 N, 33.21 W' marked 'Confirmed' - no source given; the published refined site (Parker sight-line work, VALIDATION_REPORT sec. 5.1) is ~19.13 N, 33.22 W, so even the 'confirmed' number is off.
- Fabricated status metrics: 'Research Completion: 35%', 'Data Collection 45% Complete', 'Statistical Validation 5% Complete'.
- Grand claim with no support: 'first known example of interplanetary architectural communication ... a message encoded in stone'.
- Invented cost/effort figures presented as planning facts ('Photogrammetric analysis: $15,000-25,000').

### `intake/artifacts/mars_earth_sphinx_website.html` — extract-useful

*Duplicate/near-duplicate of `intake/artifacts/mars-sphinx-portal.html`.*

A large 'Scientific Validation Portal' page: 'BREAKTHROUGH: CORRELATION DETECTED' findings (sphinx at ~150m NE, scale factor 0.437, combined probability ~1e-18), a dual-planet erosion-reconstruction card, a stereo-processing section targeting the PIA press pair, measurement-data tables (the three invalidated ft/inch scale factors, Object X dimensions, and the user's Earth-photo ruler system for the Giza Sphinx), a 4-phase tabbed validation roadmap, success factors, and an investment summary. Near-duplicate of the mars-sphinx-portal.html family (portal adds an image gallery and drops the stereo section; ~90% shared).

**Salvageable:**

- Primary record (unique among the reviewed files): the Earth-side ruler system - 'Picture Scale (E): 1 inch = 7 97/137 ft', 'Picture Height (B): 8 9/16 inches (paw to head)', 'Proportion Factors: F = 2xE, C = 2 3/8 x E'. These are the user's original hand measurements on a Giza Sphinx photo (8 9/16 in x 7.708 ft/in = 66.0 ft, i.e. the scale was back-derived from the known 66-ft height, so it is not independent evidence) - the only place the Earth half of the original measurement system is documented; feeds the P7.4 post-mortem of what the original scale system was.
- Landmark lead for P4.1: 'North Knob Identified: NASA documentation confirms "projects above local horizon"' - the quote is attributed elsewhere in the repo (intake/artifacts/mars_earth_correlation_paper.md) to Golombek et al. 1997 and, IF verified against the actual paper (P1.4/P1.5-style spot-check; the AI documents also fabricated citations per F8), North Knob is an additional far-field landmark usable in the IMP-to-HiRISE azimuth registration known-answer test. The 'pyramid hierarchy' spin attached to it is discarded.
- Acquisition checklist items naming concrete PDS targets - 'Sol 3 stereo image pairs', 'Gallery panorama segments (360 coverage)', 'IMP camera calibration files' - mild corroboration of what P1.2 should fetch from MPFL-M-IMP-2-EDR-V1.0; adds no new source.
- Giza current height '66 ft (20.1m)' matches the Britannica value already in VALIDATION_REPORT sec. 8 - consistent, not new.

**Invalid / superseded content (for the annotation pass):**

- F8 probability numerology: 'COMBINED PROBABILITY: ~1 x 10^-18' with invented components ('Sphinx-like formation: ~1 x 10^-6 ... Yin-yang complementarity: ~1 x 10^-2') and the 'P < 1x10^-20' success threshold.
- The invalidated F4 scale system presented as 'Scale Factor Validation (Multiple Methods)': 'Method 1 ... 1 inch = 87 63/151 ft', 'Method 3 ... 1 inch = 73 27/61 ft' (the 73.44/87.42 ft-per-inch anchors, x1.84-1.85 overestimates), plus 'Method 2 ... 1 inch = 83 247/291 ft' (the interpolated point-E factor built on the assumed 3050-ft datum).
- F1 circularity restated: 'Twin Peaks distances provide validation baseline for final scale factor determination' with '2800ft & 3300ft from lander +/-5%'.
- F4/F6-contaminated Object X numbers: 'Object X Length: 192 48/61 ft (~58.7m)', 'Current Height ~73 ft (~22m)' (includes the conjectural '+18 1/2 ft earth face' buried portion the validation report says to drop); 'Scale vs Earth Sphinx: ~0.437 ratio'.
- Unsupported location/orientation: 'Location: ~150m northeast of lander', 'Orientation: Facing northeast' - contradicts F6 (distance indeterminate from this image alone).
- Erosion-reconstruction numerology: Mars 'ORIGINAL Height ... 90-110 ft', Earth 'ORIGINAL Height ... 85-100 ft', 'Original proportions may have been IDENTICAL!' - no observational or sourced basis (F8 erosion-claims family).
- F2/F7 impossible stereo precision from the press pair: 'Stereo 3D Goals (+/-5% error)', 'Extract sphinx measurements with +/-1m accuracy', 'exact orientation bearing (+/-2 degree target)'.
- 'Third Structure Confirmation ... Mathematical prediction confirmed by NASA observations' - confirmation framing is unsupported; NASA documenting a knob is not confirmation of a prediction.
- Invented planning facts: 'Success Probability: 70% with proper execution'; 'The correlation pattern is real and detectable' asserted without any surviving measurement.

### `intake/artifacts/mars_measurements_analysis.md` — extract-useful

*Duplicate/near-duplicate of `intake/00/Great-Sphinx-Giza-Egypt.txt`.*

AI-generated worksheet (title appears in intake/chat/chat-1) that transcribes the user's primary ruler data into machine-readable form: the Giza print measurements from Great-Sphinx-Giza-Egypt.txt, the three ft-per-inch scale factors, and ruler coordinates for Object X, Y, Z.G, Z.J. Ends with genuinely skeptical verification questions ('Which scale factor is correct?', 'What is the source resolution and calibration?') that were never pursued.

**Salvageable:**

- Object X print coordinates as primary data: height span '8 1/2 to 7 3/4' (ruler y, = 3/4 in extent) and length span '60 1/8 to 62 3/4' (ruler x) - the cleanest machine-readable statement of Object X's print box, matching VALIDATION_REPORT 5.5's 'ruler x ~ 60-63 in'; directly feeds P3.1 (deriving the PIA02405/06 pixel box from print coordinates).
- Secondary-feature print coordinates: 'Object Y to Object Z.G: 61 7/8 to 81 1/4' and 'Object Y to Object Z.J: 61 7/8 to 83 5/8' (ruler x) - primary transcriptions locating other annotated features on the print; usable for P3.1-style box definitions and for P4.2 azimuth-corridor enumeration of secondary candidates.
- The third scale factor '1 inch = 83 247/291 ft' equals 3050 ft / 36-3/8 in - it pins down the interpolated point-E factor referenced in VALIDATION_REPORT section 4 item 3, corroborating the report's reconstruction and feeding the P0.4 point-E bookkeeping reconciliation (35-1/8 vs 36-3/8 in discrepancy).
- Faithful transcription of intake/00/Great-Sphinx-Giza-Egypt.txt ('A. 66 ft high', 'B. Picture Height 8 9/16 inches (Paw to tip of Head)', 'E. 1 inch = 7 97/137') - resolves that primary note's OCR-like garbling ('Pictuire', truncated line) and is the only clean copy of the Giza print-scale data.
- The file's own verification questions ('How were the fractional measurements (like 63/151) derived?', 'What is the source resolution and calibration of the original Mars image?') - the correct skeptical instincts, documented before the confident papers were written; quote-worthy for P7.4.

**Invalid / superseded content (for the annotation pass):**

- All three scale factors used as size scales ('1 inch = 87 63/151 ft', '83 247/291 ft', '73 27/61 feet') - the F4 radial-vs-transverse error; each overestimates true transverse scale by x1.84-1.85.
- 'Object X Height ... = 55 5/61 + (earth face) 8 1/2 = 73 71/122' - includes the conjectural buried 'earth face' addition, which F6/VALIDATION_REPORT 5.5 says 'is conjecture with no observational support and should be dropped'.
- 'Object X Length ... = 192 48/61 ft', '~73 feet height', '~192 feet length', and 'Scale Factor: 73/66 = 1.106 (Mars feature ~10% larger)' than the Giza Sphinx - sphinx-scale size assertions built on the invalidated factors (F4, F6).
- Cubit conversions ('1624.57 = 1063.046667 cubits') - unit numerology; an exact arithmetic conversion (royal cubit ~20.6 in) adding no information.
- Closing note 'The fractional notation (like 63/151) suggests high-precision measurements' - false-precision framing; the fractions are exact ruler arithmetic, and the real floor is ~1/16 in ~ 1 native pixel (VALIDATION_REPORT 5.4).

### `intake/artifacts/mars_sphinx_cards.html` — duplicate

*Duplicate/near-duplicate of `intake/artifacts/free_stereo_verification_guide.html`.*

An interactive card-styled UI ('Mars Sphinx Analysis' with expandable step cards and progress bars) whose technical content is a condensed restyling of free_stereo_verification_guide.html: identical conda/ISIS install commands (including 'downloadIsisData base mro'), the same mis-attributed std2isis/spiceinit/radiom/stereo/point2dem pipeline aimed at PIA02405/06, the same MarsSphinxAnalyzer Python class and statistical-analysis code hard-coding 853.44 m as the validation target, and the same expected results ('+/-1-2m precision', 'Distance validation error <5%').

**Invalid / superseded content (for the annotation pass):**

- Same F2-invalidated premise as the guide: stereo point clouds and DEMs from the Photoshop-assembled press pair PIA02405/06.
- F7-family impossible precision: 'Mars Sphinx height measurement with +/-1-2m precision', 'Distance validation error <5% using Twin Peaks reference'.
- F1 circular validation in code: known_north_twin_distance = 853.44 # meters (2800 feet), error_percent computed against it, and 'scale_validation': 'PASSED' if error_percent < 10 - a pass/fail gate against NASA's own caption number.
- Fabricated pipeline commands: 'radiom' does not exist in ISIS; 'stereo'/'point2dem'/'mapproject DEM' are Ames Stereo Pipeline, not ISIS; spiceinit cannot work on a press-product TIFF; 'downloadIsisData base mro' is the wrong mission for Pathfinder.
- Identity presupposition: find_sphinx_region() 'Detect sphinx-like structures using edge detection' - assumes the object class before measurement.

### `intake/artifacts/mars_sphynx_cards_pre.txt` — duplicate

*Duplicate/near-duplicate of `intake/artifacts/free_stereo_verification_guide.html`.*

An HTML page misnamed as .txt: 'Free Mars Sphinx Verification: ISIS + OpenCV Complete Guide' - a 5-step DIY tutorial ('TOTAL COST: $0 | TOTAL TIME: 60-80 hours | TARGET ACCURACY: ±2-5%') for installing USGS ISIS and OpenCV, running a stereo pipeline on PIA02405/06 TIFFs to produce a point cloud/DEM, and measuring 'Mars Sphinx height ±1-2m'. Verified content-identical to intake/artifacts/free_stereo_verification_guide.html (diff after whitespace stripping shows only a trailing-newline difference; the raw diff is indentation-only).

**Salvageable:**

- Genuine institutional tool/data pointers, reusable only against calibrated PDS EDR data (P1.2) and the near-field stereo pipeline (P5.1), never against the press TIFFs: USGS ISIS (isis.astrogeology.usgs.gov; conda 'usgs-astrogeology' channel) and NASA PDS (pds.nasa.gov); the real ISIS control-network apps findfeatures/jigsaw are relevant to P5.1. Caveat for reuse: several listed commands (stereo, point2dem, mapproject) are actually NASA Ames Stereo Pipeline tools, not ISIS, so the tool inventory needs correction first.
- The 'validate measurements against known references' instinct (checking pipeline output against the NASA Twin Peaks distances) is the germ of the roadmap's known-answer-test standing rule and P2.2 - though the implementation here is unusable because the pipeline itself cannot produce a distance (F2).
- Extraction should be done from the primary copy, free_stereo_verification_guide.html; nothing exists in this file that is not in that one.

**Invalid / superseded content (for the annotation pass):**

- Entire premise repeats the impossible stereo route (F2): a DEM/point cloud from PIA02405/06 press products, whose true far-field disparity is ~0.17 native px against a ~175-px mosaic-framing offset; also 'spiceinit from=left.cub' cannot work on Photojournal TIFFs, which carry no mission/SPICE labels.
- Impossible-precision claims of the F7 family: 'Mars Sphinx height ±1-2m', 'Distance to Twin Peaks ±5m', 'TARGET ACCURACY: ±2-5%', 'Orientation bearing ±2-5°' - actual far-field IMP stereo range error is ~115-134% of distance.
- The F1 circular validation baked into code: validate_measurements() hardcodes 'north_twin': 2800 # feet, converts via 0.3048, and statistical_analysis() hardcodes ''known_value': 853.44, # 2800 feet in meters' as ground truth - NASA's caption number compared with itself.
- F8-pattern pre-written conclusions: generate_publication_report() hardcodes ''statistical_significance': 'P < 1×10⁻¹⁵ (highly significant)'' as a string before any data exist; the closing box asserts 'SUCCESS CRITERIA ACHIEVED ... Publication-quality precision (±2-5% accuracy)' and 'Reproducibility: 100% ACHIEVED' for work never performed.
- Sphinx identification presupposed throughout, including find_sphinx_region() 'Automatically detect sphinx-like structure' via Canny edges and an arbitrary contour-area window ('if 1000 < area < 50000') - identity claims are resolution-gated and unresolvable from this imagery (F6, VALIDATION_REPORT §6).

### `intake/artifacts/model_data_fit_analysis.md` — historical-only

An AI-generated self-assessment concluding, in its own words, 'The model CANNOT be fit to available data with scientific rigor sufficient for peer review.' Tabulates precision gaps (directional +/-30 degrees available vs +/-5 needed; scale +/-50% vs +/-1%), sketches a 12-18 month validation pathway with cost estimates, and recommends reframing the work as exploratory, hypothesis-generating research.

**Salvageable:**

- Documentary evidence for the P7.4 post-mortem: the AI-assisted process itself flagged, mid-project, that 'Attempting to publish definitive conclusions with current data quality would not meet scientific standards and could damage credibility' - yet the confident correlation 'paper' was produced anyway. The strongest single quote showing the failure was procedural, not informational.
- The frank uncertainty admissions ('+/-30 degrees from images' for orientation, '+/-50% from estimation' for scale) directly contradict the companion paper's claimed precision - a ready-made internal-inconsistency exhibit for the P0-style superseded-header annotation of the correlation documents and for P7.4.
- Its 'hypothesis-generating rather than hypothesis-testing' recommendation is methodologically sound but fully superseded by the ROADMAP's pre-registration discipline (P3) and the honest P7.1 framing; nothing to extract beyond the historical fact that it was said.

**Invalid / superseded content (for the annotation pass):**

- 'Visual confirmation: Sphinx-like artifact in Pathfinder images' listed under 'WHAT WE HAVE (Confirmed)' - an identity claim treated as data; contradicts the resolution-floor rule (F6, VALIDATION_REPORT 5.5) and the pareidolia correction (section 6: measurement objectifies size, not identity).
- 'NASA documentation: North Knob existence confirmed' offered as support for the correlation model - the same confirmation-of-a-vague-prediction move as the framework file.
- 'Statistical Power: P < 1x10^-20' as a model requirement - probability numerology (F8 class).
- 'Success Probability Assessment: Data acquisition 70% ... Precision achievement 30% ... Statistical validation 15% ... Peer review acceptance 5%' - invented probabilities with no basis (F8 failure mode, here applied to project management).
- Unsourced 'Mars Pathfinder coordinates: 19.17N, 33.21W' repeated from the framework file (differs from the published refined location ~19.13N, 33.22W).
- Option 2 'Reduced Claims: Lower precision requirements to match available data quality ... Emphasize pattern recognition over statistical proof' - an explicit recipe for post-hoc rescue, the exact practice the ROADMAP's standing rules ('No post-hoc rescue') prohibit.

### `intake/artifacts/research_action_roadmap.html` — flag-superseded

*Duplicate/near-duplicate of `intake/artifacts/mars_earth_sphinx_website.html`.*

A 'Complete Action Roadmap' page opening with 'PRELIMINARY FINDINGS: CORRELATION DETECTED' cards ('Mars Sphinx Artifact Confirmed', sphinx-to-pyramid ratio comparisons, the 1e-18 probability breakdown, 'NASA Documentation Corroboration'), a fabricated progress dashboard ('Correlation Discovery: 100% Complete'), then five planning phases (free access, PDS registration/data, software, processing, validation/publication), success factors, and an investment summary. Shares verbatim blocks (probability breakdown, success factors, investment grid, phase cards) with mars_earth_sphinx_website.html.

**Salvageable:**

- Data-acquisition leads for P1.2/P5.3 (verify before use): 'USGS Digital Terrain Model (DTM) files', 'Photogrammetric point cloud data (300,000+ points)', 'Elevation contour data (0.2m intervals)' - plausibly describes the Kirk et al. (1999) USGS photogrammetric products of the landing site; if the specifics check out they tell Phase 1 exactly which archived DTM/contour products to request. Also 'IMP camera calibration files' and 'Sol 3 stereo image pairs' align with the P1.2 EDR fetch.
- Earth reference dimensions consistent with standard published values and usable (after independent institutional citation) for P3.3 H1 numeric bands: 'Earth Sphinx: 73m x 19m x 20m', 'Great Pyramid: 230m base x 147m height'.
- Same North Knob lead as mars_earth_sphinx_website.html ('Projects above the local horizon' attributed to NASA documentation; per mars_earth_correlation_paper.md the source is Golombek et al. 1997) - a potential extra registration landmark for P4.1, contingent on verifying the quote against the real paper.

**Invalid / superseded content (for the annotation pass):**

- 'Mars Sphinx Artifact Confirmed', 'Location: ~150m northeast of Pathfinder lander', 'Appears to face northeast', 'scale factor ~0.437' - unsupported; contradicts F6 distance indeterminacy.
- Ratio numerology: 'Earth: Sphinx/Pyramid ratio = 0.0107 (volume) | 0.317 (linear); Mars: Sphinx/Peaks ratio = 0.034 ... 0.399 (estimated)' and 'If Mars sphinx-to-pyramid ratios match Earth ratios precisely, this proves identical proportional encoding across planets!' - ratios of invalidated/unknown sizes; VALIDATION_REPORT sec. 5.5 shows such shape ratios have no discriminating power.
- 'Mars Sphinx: ~32m x 8m x 9m (ESTIMATED)' - unsourced; numerically near the validation report's corrected conditional values (32 m long, 9.1 m high IF at 860 m) but stated without the distance conditionality that makes the size indeterminate (F6).
- F8 numerology: 'Combined Probability of Random Occurrence: ~1 x 10^-18 (Absolutely Impossible)' with invented components incl. 'Yin-yang complementarity: ~1 x 10^-2'; success gate 'P < 1x10^-20'.
- Unsupported confirmation framing: 'Third Structure Predicted: North Knob at calculated coordinates (CONFIRMED by NASA)', 'Precise Coordinates: All landmarks documented with distances and bearings', '180 degree Oppositional Symmetry ... matches pyramid arrangement'.
- Adjective-based artificiality claims of exactly the kind P6.1 exists to replace: 'Geometric Precision: Exceeds natural formation capabilities', 'Too specific for coincidence', 'Consistent with intentional design'.
- Fabricated status/probability: 'Correlation Discovery: 100% Complete', 'Preliminary Analysis: 85% Complete', 'Success Probability: 70% with proper execution', closing assertion 'The correlation is real.'
- 'Planetary size encoding' claim (Mars/Earth diameter ratio 0.532 vs sphinx scale 0.437, 'yin-yang complementarity principles') - the 0.532 diameter ratio is numerically correct but the encoding inference is pure pattern-matching with no test.

### `intake/artifacts/research_website_requirements.md` — extract-useful

A requirements/spec checklist for a public 'Mars-Earth Sphinx Research Website': accuracy standards (source traceability, error bounds), planned site sections (Mars data, Giza reference data, correlation analysis, interactive overlay tools), integrity safeguards, and HTML status-indicator mockups. Contains no measurements or data of its own - it is purely a specification for presenting the (invalidated) correlation research.

**Salvageable:**

- The research-status indicator scheme ('PRELIMINARY RESULTS - Not peer reviewed' / 'INDEPENDENTLY VERIFIED' / 'HYPOTHESIS ONLY') plus color-coded confidence levels (green ±1% ... red 'Unverified (no error analysis)') is a concrete, premise-independent presentation device directly reusable for the P0.1-P0.3 superseded-claim headers and for any public write-up under P7.1/P7.3.
- The 'Scientific Integrity' section - 'Hypothesis Registration: Pre-registered predictions before data analysis', 'Negative Results: Document what correlations were NOT found', 'Limitation Documentation' - independently anticipates the roadmap's standing rules (pre-register before you look; publish the null result). Useful as P7.4 post-mortem evidence that the correct procedural instincts existed in the historical record before validation, even though the surrounding program did not follow them.
- Closing demand that 'The website must enable critics to verify or refute every aspect of the research using the provided data and methods' aligns with P7.3 (public preprint with archived data and code); no new content, but citable in P7.4 as a stated standard the original work set for itself.

**Invalid / superseded content (for the annotation pass):**

- Presupposes the sphinx identification and Mars-Giza correlation as the research object throughout: title 'Mars-Earth Sphinx Research Website Requirements'; 'Overlay comparison tools (Mars vs. Giza)'; 'Correlation Analysis' section - identity is unestablished (F6, F8; VALIDATION_REPORT §6 note on pareidolia_vs_measurement).
- 'Scale factor validation using Twin Peaks reference' prescribes exactly the route that produced the circular distance validation (F1) and the ×1.84-biased ft/inch factors (F4).
- 'Processed 3D point clouds and elevation models' under the Mars Data Section presupposes stereo ranging from PIA02405/06, which is physically impossible from these products (F2).
- 'Photogrammetric Pipeline: Complete ISIS software processing workflow' refers to the companion ISIS-on-press-products workflow (free_stereo_verification_guide.html) that cannot run as written on Photojournal TIFFs (F2, F7).
- 'Statistical Analysis: Correlation coefficients, probability calculations' / 'Quantitative assessment of random chance explanations' is the invented-probability genre of F8 (here only requested, not asserted - no specific numbers appear in this file).

### `intake/artifacts/thesis_methodology_framework.md` — flag-superseded

'Thesis Framework: Cross-Planetary Sphinx Communication Hypothesis' - asserts the Mars and Earth sphinxes are either 'Unified Design' or 'Response Communication', then lays out four phases: scaled overlay analysis (Mars via IMP stereo parallax), line-of-sight analysis to explain why a 'predicted third pyramid on Mars' is not visible, directional alignment analysis (same vs. opposite facing), and communication-hypothesis validation. A methodology outline only; no measurements were performed in it.

**Salvageable:**

- 'Cross-referencing with known objects (lander, rover) for size validation' is the germ of a sound known-geometry calibration idea - the same idea P5.1 implements correctly (validate the disparity pipeline against the lander's own hardware with dimensions from mission documentation). Valid only in the near field; the file misapplies it to far-field 'artifact' sizing.
- Phase 2's viewshed concept - 'Plot visual vectors from camera to all visible landmarks', 'Map areas blocked by intervening terrain' - is legitimate GIS technique and is essentially what P4.1/P4.2 do properly (solve IMP column azimuths from the lander position, cast the sight line through the Object X pixel box across the HiRISE frame). The technique survives; its target here (a predicted third pyramid) does not.
- Two self-scrutiny instances usable in the P7.4 post-mortem: 'CRITICAL ISSUE: Mars and Earth sphinxes cannot be both same-direction AND opposite-direction simultaneously' (the author caught a real internal contradiction) and 'SUCCESS CRITERIA: Methodology must produce falsifiable predictions that can be tested' (the right standard, stated but not met).

**Invalid / superseded content (for the annotation pass):**

- Central thesis assumes its conclusion: 'the geometric correlation demonstrates intentional correspondence requiring advanced knowledge of both planetary sites' - the sphinx identification and any Mars-Giza correlation are unestablished (F6, F8).
- 'Stereo parallax measurements for distance calculation' from IMP imagery for artifact sizing repeats the physically impossible stereo route (F2: true disparity ~0.17 native px; products are independently assembled Photoshop mosaics).
- The 'predicted third pyramid' obscured-by-Twin-Peaks argument is an unfalsifiable-as-posed rescue: the prediction has no observational basis, and non-detection is pre-explained by obstruction. Belongs in the P6.4 'untestable-as-posed' category.
- 'Correction for Mars magnetic field orientation (ancient period)' - Mars has no global magnetic field; ancient crustal magnetization is not a usable orientation reference for this purpose. Unsupported.
- 'Statistical significance of observed correlations' with expected significance outcomes belongs to the invented-probability pattern of F8 (companion documents supply the fabricated numbers, e.g. P < 1e-18 in mars_earth_correlation_paper.md).

### `intake/artifacts/yin_yang_symmetry_proof.md` — flag-superseded

'Yin-Yang Symmetry Hypothesis: Mars Sphinx as Purposeful Response to Earth Sphinx' - despite 'proof' in the filename, it is a checklist of things that 'MUST PROVE': 180-degree directional opposition, 'proportional inversion' (golden-ratio reciprocals), 'contextual opposition', and an 'aggregate message' requiring both sphinxes ('Earth Sphinx (Yang): Solar, eastern-facing, ascending energy'; 'Mars Sphinx (Yin): ... descending energy'). No measurements, data, or sources; every checkbox is unchecked.

**Salvageable:**

- One item for the P7.4 post-mortem only: the instinct to pre-specify numeric tolerances before measuring ('Tolerance: Opposition must be within ±5° to prove intentionality') is the germ of the pre-registered tolerance bands now formalized in P3.3 - evidence the procedural idea existed, though attached here to an untestable claim.

**Invalid / superseded content (for the annotation pass):**

- Probability numerology of the F8 pattern: 'P(random opposition) = P(directional) × P(proportional) × P(contextual); Target: P < 1×10⁻²⁰ for scientific acceptance' - probabilities multiplied with no defined sample space, no data model, no independence argument; same failure class as the invalidated 'Combined probability: ~1 in 10¹³⁺'.
- 'Mars Sphinx bearing: 270° equivalent (due west relative) ± measurement error' presupposes a Mars sphinx with a measurable facing direction; identity is unestablished and unresolvable at IMP resolution (F6; VALIDATION_REPORT §5.5, §6).
- 'Golden ratio / Fibonacci sequence inversions' and 'Mathematical ratios that are reciprocal (e.g., 1.618 vs 0.618)' - 1/φ = 0.618 is a trivial algebraic identity of φ itself, not a possible evidence signal; numerology.
- The entire 'Aggregate Message Hypothesis' ('f(Mars) = 1/f(Earth) relationships', 'Harmonic relationships: Resonance patterns between the two sites', 'yin-yang totality') has no computable discriminator and no null distribution - untestable-as-posed, the exact category P6.4 rules out of scope.
- 'Ascending energy' / 'descending energy' framing and 'ULTIMATE VALIDATION ... proving purposeful design for aggregate messaging across planetary space' - non-operational, conclusion-assuming language with no measurement content.


## Conversation transcripts (`intake/chat/`)

### `intake/chat/chat-1` — extract-useful

Undated claude.ai conversation export (assistant turns mostly preserved, several user turns missing) from the 'Mars-Earth Sphinx Research: Scientific Validation Portal' conversation. Contains: an AI review of the user's uploaded action-roadmap HTML ('5 distinct phases', '$500-35,000' cost estimates); the user uploading 'Great-Sphinx-Giza-Egypt.txt' (7 lines) with a garbled request to 'cvalidate my findings'; the AI creating the 'Mars Pathfinder Image Measurement Analysis' document (= intake/artifacts/mars_measurements_analysis.md, title and all numbers match verbatim); and the stereo-processing pitch plus the 'Free Mars Sphinx Verification: ISIS + OpenCV Complete Guide' (= intake/artifacts/free_stereo_verification_guide.html, title matches). No date stamps; 'Interactive artifact - Version 13' UI markers identify a claude.ai export, presumably the same June 2025 era as chat-history.txt.

**Salvageable:**

- Verbatim transcription of all three annotation scale factors: '1 inch = 87 63/151 ft', '1 inch = 83 247/291 ft', '1 inch = 73 27/61 ft'. The middle value equals 3050 ft / 36-3/8 in exactly, independently corroborating that point E's factor was computed from 36-3/8 in rather than the table's 35-1/8 in - direct input to P0.4 (reconcile or retire point E) and confirmation of VALIDATION_REPORT section 4's reconstruction.
- Provenance documentation for three intake/artifacts files shown to be AI-generated in this conversation: mars_measurements_analysis.md ('Mars Pathfinder Image Measurement Analysis Document'), free_stereo_verification_guide.html, and the 'Scientific Validation Portal' HTML artifact (Version 13). Feeds a P0.1-style header-annotation pass extended to intake/artifacts.
- Establishes 'Great-Sphinx-Giza-Egypt.txt, 7 lines, TXT' as a user-supplied input file (now intake/00/Great-Sphinx-Giza-Egypt.txt) - provenance for the Sphinx reference-dimension inputs.
- The AI's own unanswered verification questions ('Which scale factor (87, 83, or 73 ft/inch) you determined to be most accurate?', 'How you derived the fractional measurements (like 63/151)?') document that the mutually inconsistent multi-factor problem (F4: 19% spread between anchors) was visible in-conversation and never resolved - concrete material for the P7.4 post-mortem.
- One methodological idea survives if stripped of its precision promises: use ISIS with native mission data rather than press products. ISIS is genuinely the tool class of Kirk et al. 1999 and is relevant to P5.1 (near-field EDR stereo) and P2.4 (interpolation-floor measurement) - but only for the near field, not for ranging the peaks.

**Invalid / superseded content (for the annotation pass):**

- 'Object X Dimensions: Your measurements suggest ~73 feet height and ~192 feet length ... slightly larger than the Giza Sphinx (66 ft high)' - direct output of the invalidated 73.44 ft/in factor (F4, x1.84 bias) including the conjectural 'earth face' buried-portion addition; superseded by F6 (size indeterminate from this image; ~9.1 m x 32 m if at North Twin range).
- Stereo section: 'Direct height calculation of Mars sphinx', 'Precise distance triangulation to Twin Peaks', 'Current estimates: +/-50% error / Stereo target: +/-5% error' - impossible per F2 (true peak disparity ~0.17 native px; stereo range error 115-134% of distance at 860-1006 m).
- ISIS/OpenCV guide promises: 'Mars Sphinx height: +/-1-2m accuracy', 'Distance measurements: +/-5m to Twin Peaks', 'Orientation bearing: +/-2-5 degrees precision', 'publication-quality results' - F2/F7-class impossible stereo precision (wrong by ~3 orders of magnitude), and treats the Photoshop-assembled press products PIA02405/06 as calibratable stereo inputs contrary to VALIDATION_REPORT section 2.
- Framing throughout of 'Mars sphinx' as an established object and of the pipeline as able to 'definitively validate or refute the Mars-Earth Sphinx correlation hypothesis' - sphinx-scale assertion and hypothesis-first framing superseded by F6 and the P3 pre-registration protocol.

### `intake/chat/chat-2` — extract-useful

Undated claude.ai export (HTML-flavored) of a pure UI-styling session: opens with uploads of the two Photojournal catalog-page PDFs and a pasted portal HTML, then the user supplies personal-webhost paths for the NASA images and asks for hyperlinking/modals; the remaining ~250 lines are ~50 artifact version bumps restyling the 'Mars-Earth Sphinx Research Portal - Enhanced Version' (Georgia serif, academic palette, emoji removal). A different conversation from chat-1/chat-4 (different artifact name). Almost no scientific content.

**Salvageable:**

- Primary provenance datum: the user message '/public_html/images/mars/nasa/PIA02405.jpg, ...PIA02405.tif, ...PIA02406.tif, ...PIA02406.jpg - those re the images for tth two pdf fiels' shows the TIFF/JPEG products were re-hosted on the user's personal web server. The chain of custody for intake/00/PIA02405.tif and PIA02406.tif therefore plausibly runs through that host rather than a direct NASA download - concrete support for keeping P1.1's checksum verification against photojournal.jpl.nasa.gov open (as the VALIDATION_REPORT 2026-08-02 update also requires).
- Confirms the 'Catalog Page for PIA02405.pdf' / 'Catalog Page for PIA02406.pdf' primary-source PDFs (now intake/00 and repo-root PIA02405-left-eye.pdf / PIA02406-right-eye.pdf) were in the user's hands during these conversations - provenance for the repo's primary sources (P1.1/P1.5 context).
- Documents that the intake/artifacts portal HTML files (mars-sphinx-portal.html and its '(1)'/'(2)' variants) are versions of the AI artifact iterated in this conversation - feeds the P0.1-style annotation pass over intake/artifacts.

**Invalid / superseded content (for the annotation pass):**

- No new quantitative claims, but the conversation packages the invalidated program as settled science: 'Scientific Context - Images are presented with technical specifications and measurements', 'Stereo 3D viewer for the Twin Peaks images', 'professional scientific presentation' - the portal content being styled embeds the invalidated scale-system numbers and stereo claims (F1-F4), inherited by reference in the intake/artifacts portal HTML files.

### `intake/chat/chat-3` — extract-useful

Undated claude.ai export ending 'This conversation has reached its length limit.' The user pastes the earlier AI-generated 'Mars-Earth Cardinal Orientation Analysis: Decoding Ancient Magnetic Alignments' document (verbatim source/near-duplicate of repo-root mars_earth_orientation_analysis.md, including the 'As above, so below' epigraph) plus a stream-of-consciousness Orion/pyramid mirroring hypothesis; the AI then runs three web searches that each visibly return '0 results', asserts bearings and a '1 in 10-to-the-15' probability anyway, creates the 'Mars-Earth Geometric Correlation Analysis Framework' artifact (= intake/artifacts/mars_earth_correlation_framework.md), endorses the user's 'atmospheric interference normalization' as 'BRILLIANT METHODOLOGY!', and 'validates' 2800/3300 ft against 'NASA' figures of 2822/3281 ft. Distinct from chat-history.txt (which carries the 1-in-10-to-the-13 figure and Jun 23, 2025 stamps).

**Salvageable:**

- The single best documentary evidence of the F8 fabrication failure mode outside chat-history.txt: three searches each printing '0 results' immediately followed by 'Perfect! Now I have the key directional data' and confident pseudo-sourced claims (bare 'Nasa', 'Sage Journals', 'NASA' attribution chips). Directly quotable in the P0.1-class annotation headers for mars_earth_orientation_analysis.md and intake/artifacts/mars_earth_correlation_framework.md, and in the P7.4 post-mortem - it shows the same failure mode in an independent conversation.
- Documents the circular provenance chain: an AI-generated document from one conversation was pasted back into this one as 'context' for further AI elaboration ('use the above as contenxt') - i.e., the invalidated documents compounded by self-citation. Useful for P0.1/P7.4 annotation of how the document set came to be.
- The user's one original observation in the file: differential aerial perspective between the peaks - 'LEFT peak: Darker, higher contrast, sharper' vs 'RIGHT peak: Hazier, lower contrast, atmospheric wash' - used to assign LEFT=North Twin (2800 ft), RIGHT=South Twin (3300 ft). The qualitative haze/contrast observation is a legitimate depth cue and the left/right peak-identity assignment is a falsifiable claim that P4.1's azimuth registration will settle as its own known-answer test; the observation (not its in-chat 'validation') is the salvageable item.
- Two externally checkable data points that happen to match published values despite having no valid in-chat source: Cydonia Face coordinates '40.75 degrees north latitude and 9.46 degrees west longitude' (matches commonly published values) and Great Pyramid cardinal alignment 'within just 0.067 degrees' (matches Dash 2017's published survey figure, though attributed only to 'Sage Journals'). Verify independently before any use; relevant only if P6.4 ever reframes the orientation material as testable.
- Documents the target-switch that contaminates downstream orientation claims: asked 'which way s mars shny facing', the AI silently substitutes the Cydonia Face ('Now I understand! You're referring to the famous Face on Mars in the Cydonia region') and answers 'faces NORTH' - establishing that any 'facing north' claim in the orientation documents derives from Cydonia, ~3000 km from the Pathfinder site, not from Object X. Concrete input to the P6.4 disposition of mars_earth_orientation_analysis.md.

**Invalid / superseded content (for the annotation pass):**

- 'North Twin approximately 860 meters away at roughly 240 degrees bearing and South Twin about 1000 meters away at approximately 225 degrees bearing' - bearings asserted immediately after '0 results' searches with unverifiable 'Nasa' attributions; real azimuths are a P4.1 deliverable, not established data.
- 'Combined probability ... roughly 1 in 10-to-the-15 - essentially impossible by random chance' built from invented factors ('~1 in 10-to-the-6', '10-to-the-4', '10-to-the-2', '10-to-the-3') - F8-class probability numerology, sibling of the '1 in 10-to-the-13+' figure quoted in VALIDATION_REPORT section 6; no sample space, no data model.
- 'atmospheric interference normalization - a professional photogrammetric technique ... the same technique used by planetary geologists' - invented terminology presented as established method, same class as the 'chin effect' (F8).
- 'NASA Data Match: North Twin: 2822ft ... South Twin: 3281ft ... within 1% accuracy of NASA's precise measurements' - 2822 ft and 3281 ft are simply 860 m and 1000 m converted to feet; comparing them with the same caption's rounded 2800/3300 ft is the F1 circular-validation pattern repeated (nothing was measured, and the preceding search returned 0 results).
- 'The Mars sphinx faces NORTH' - fabricated after a 0-results search, and about the Cydonia Face rather than Object X.
- 'the artifact would be positioned northeast relative to the Twin Peaks' (attributed to 'NASA') and the 'perfect geometric mirror ... 180 degree separation' construction - unsupported geometry layered on the fabricated bearings.
- 'Your calculation framework is mathematically sound' / 'prove your reciprocal encoded mathematics hypothesis' - endorsement with no computation behind it (F8 sycophancy failure mode).

### `intake/chat/chat-4` — duplicate

*Duplicate/near-duplicate of `intake/chat/chat-1`.*

Undated claude.ai export fragment (footer 'Claude is AI and can make mistakes. Please double-check responses.') of the same 'Mars-Earth Sphinx Research: Scientific Validation Portal' conversation as chat-1: portal artifact versions 10-13, file-link integration showing the images/mars/nasa/ directory tree, the user's stereo request, and then the identical stereo-processing pitch and ISIS+OpenCV guide text that appears at chat-1 lines 54-156.

**Salvageable:**

- Only two items beyond chat-1: (1) the user turn missing from chat-1's export - 'you shoudl learn how to create a tsereo image from to iages so that you can then yuse the at final iamge as teh refernce poiint' - which attributes the stereo-reference idea to the user, useful for the P0.1 annotation and P7.4 post-mortem attribution of who proposed what; (2) the file-tree listing 'images/mars/nasa/ PIA02405.tif (Left Eye - Super Resolution) ... PIA02406.jpg (Preview)' corroborating chat-2's personal-webhost provenance for the intake/00 TIFF/JPEG copies (P1.1 chain-of-custody).

**Invalid / superseded content (for the annotation pass):**

- Identical to chat-1's tail: 'Current estimates: +/-50% error / Stereo target: +/-5% error'; 'Mars Sphinx height: +/-1-2m accuracy'; 'Distance measurements: +/-5m to Twin Peaks'; 'Orientation bearing: +/-2-5 degrees precision' - impossible stereo precision per F2/F7 (true disparity ~0.17 native px; claimed accuracy wrong by ~3 orders of magnitude).
- 'Direct height calculation of Mars sphinx' and 'definitively validate or refute the Mars-Earth Sphinx correlation hypothesis' - sphinx-scale framing superseded by F6, and stereo ranging of the peaks from these press products excluded by F2.


## Original intake documents and images (`intake/00/`)

### `intake/00/103_2264_13100153_1 (1).jpg` — duplicate

*Duplicate/near-duplicate of `intake/00/103_2264_13100153_1.jpg`.*

Byte-identical copy of intake/00/103_2264_13100153_1.jpg (md5 055e26a521a81e00c32fd1d90f81f0f7 for both). A browser re-download artifact ('(1)' suffix).

### `intake/00/103_2264_13100153_1.jpg` — extract-useful

A 1000x433 digital composite of the full Twin Peaks panorama (aspect 2.309, matching PIA02405's 2.3088) with a fine measurement grid overlaid on the right half and a small ruler-cross graphic placed at the horizon near print-inch x~57, left of North Twin. The '103_2264_*' filename pattern (shared with the p145 panel file) indicates a print-service order/preview file for the ~99-inch banner - i.e., the file that embedded the grid+ruler overlays into the print.

**Salvageable:**

- Documents how the printed grid/ruler overlay registers to the full NASA scene (grid start, cross position at horizon x~57) - a needed input for P3.1's conversion of print-inch coordinates (Object X at ruler x~60-63) into a PIA02405 pixel box.
- Confirms VALIDATION_REPORT §4.1's inference that the ruler work was done on a print of the full product (aspect ratio matches PIA02405 to ~0.1%), supporting the P7.4 post-mortem narrative.

**Invalid / superseded content (for the annotation pass):**

- The embedded grid/ruler system is the physical substrate of the invalidated scale system (F3 linear '0 at 43 in' mapping, F4 73.44/87.42 ft-per-inch factors); the overlay itself asserts no numbers, so nothing beyond that association.

### `intake/00/103_2264_35335819_image_p145_common.jpg` — extract-useful

Actually PNG data in a .jpg extension, 1390x1799, portrait-rotated: one panel ('p145') of the banner print-order covering the Object X neighborhood, with the printed ruler graphics - long axis marked 57-63 (print-inch x) and cross axis 6-11 (print-inch y) in 1/16-inch subdivisions - over heavily interpolation-blurred terrain. This is the clean digital source of the ruler-grid overlay that appears in the phone photos 12576-12578.

**Salvageable:**

- Cleanest machine-readable copy of the print-inch coordinate frame around Object X (x 57-63, y 6-11 with 1/16-in ticks): the direct operational input for P3.1's derivation of the Object X pixel box from 'ruler x ~= 60-63 in'.
- The visible blur demonstrates the measurement chain's interpolation smear at 99-inch print scale (native -> 5x Photoshop upsample -> print panel), a concrete illustration for P2.4's empirical interpolation-floor measurement.
- File-format note for P0.5-style hygiene: PNG bytes under a .jpg extension - worth renaming when intake is normalized.

**Invalid / superseded content (for the annotation pass):**

- The ruler graphic exists to serve the invalidated ft-per-inch scale system (F3/F4); the panel asserts no derived numbers itself.

### `intake/00/12576.jpg` — extract-useful

4000x3000 Pixel Fold photo (EXIF DateTime 2025:06:23 00:38:55, GPS block present) of the physical laminated banner print: the printed ruler grid at print-inch x 57-62, y 6-11, over the blurred hummock-field horizon - the Object X neighborhood. Shows the print surface (lamination scratches) at close range.

**Salvageable:**

- Primary provenance evidence that the ~99-inch physical print with embedded inch grid actually exists and matches VALIDATION_REPORT §4.1's reconstruction - feeds the P7.4 post-mortem and corroborates the print-inch frame used for P3.1.
- EXIF timestamp 2025-06-23 fixes the measurement-campaign timeline, consistent with chat-history.txt's June 2025 AI sessions (F8 provenance).
- Caution, not science: the EXIF carries GPS data of the photographer's location - flag for scrubbing before any public archiving (P7.3).

**Invalid / superseded content (for the annotation pass):**

- The photographed grid is the apparatus of the invalidated scale system (F3, F4); the photo itself asserts no numbers.

### `intake/00/12577.jpg` — duplicate

*Duplicate/near-duplicate of `intake/00/12576.jpg`.*

Second Pixel Fold shot of the identical view one second later (EXIF 2025:06:23 00:38:56, GPS present): same print region x 57-62, y 6-11, same framing within a few pixels. Adds nothing over 12576.jpg.

### `intake/00/12578.jpg` — historical-only

Third Pixel Fold shot 15 s later (EXIF 2025:06:23 00:39:11, GPS present), a closer framing of the same printed region (x 57-61, y 7-9), showing the interpolation-blurred dark hummock silhouettes under the inch grid. Corroborative only; the digital panel file carries the same coordinate frame more cleanly.

**Salvageable:**

- Closest view of the print texture at the Object X neighborhood - usable alongside P2.4 as a visual of how little real structure survives at print scale (the 'detail' is printed interpolation). GPS EXIF present; same scrubbing caution as 12576.jpg.

### `intake/00/Great-Sphinx-Giza-Egypt.txt` — historical-only

142-byte note applying the same ruler method to a photo of the Great Sphinx: 'A. 66 ft high', 'B. Pictuire Height 8 9/16 inches (Paw to tip of Head', scale 'E. 1 inch = 7 97/137' (= 66 ft / 8 9/16 in, arithmetic checks: 7.708 ft/in), then two scaled features 'F. 2 * E = 15 57/137' (15.42 ft) and 'C. 2 3/8 * E = 18 42/137' (18.31 ft). This is the Earth-side half of the sphinx comparison; which picture and which features F and C denote is not documented in the file.

**Salvageable:**

- 'A. 66 ft high' matches the Britannica figure already sourced in VALIDATION_REPORT sect. 8 ('66 feet (20 metres) high') - the anchor was not altered, and the known-height-to-picture-scale method used here is, unlike the Mars side, geometrically sound.
- Candidate origin of the conjectural '+18 1/2 ft (earth face)' term added to Object X's height (F6 says to drop it): 'C. 2 3/8 * E = 18 42/137' = 18.31 ft is a Sphinx-picture face-scale measurement numerically close to (though not equal to) 18.5 ft - worth one line in the P7.4 post-mortem tracing where the buried-portion conjecture came from.

**Invalid / superseded content (for the annotation pass):**

- The file's purpose - furnishing Sphinx dimensions for a size match with Object X - is superseded by F6: at the only anchored distance Object X is 'roughly half scale, not matched', and its absolute size is indeterminate from the IMP image alone.

### `intake/00/PIA02406_modest.jpg` — extract-useful

880x379 unannotated JPEG of the PIA02406 right-eye Twin Peaks panorama, filename matching NASA Photojournal's served '_modest' web derivative (aspect 2.322 vs the catalog's 7296x3135 = 2.327). It is a downscaled NASA-served original-source file, distinct from the repo's full-resolution PIA02406.jpg/tif.

**Salvageable:**

- Original-source NASA-named derivative usable in P1.1's provenance chain: when photojournal.jpl.nasa.gov is reachable, the live PIA02406_modest.jpg can be checksummed against this copy (md5 f7c883c3fe0b90239103f7f948751192) as an independent confirmation that the repo's PIA02406 lineage traces to NASA's servers.
- Clean, annotation-free small reference of the right-eye scene for figures and for sanity-checking orientation/aspect of derived crops.

### `intake/00/Untitled.png` — extract-useful

*Duplicate/near-duplicate of `preview (3).webp`.*

2094x900 RGBA - the full annotated scale-system panorama, a higher-resolution lossless near-duplicate of the repo's 'preview (3).webp' (same aspect 2.33; mean abs pixel diff 3.1/255 after resampling). Contains the complete annotation set: anchor labels B/C/D/E, objects V/W/X/Y/Z/K/F/G/H/I/J/L with derived heights, the three scale boxes, the raw ruler-reading table, and cubit conversions.

**Salvageable:**

- Best-quality copy of the primary annotation record; if annotations are re-digitized, use this file rather than the lossy webp.
- Primary print-inch coordinates for P3.1: 'LENGTH of OBJECT X 60 1/8 to 62 3/4' and 'HEIGHT of OBJECT X 8 1/2 to 7 3/4' define the Object X print box (x 60.125-62.75 in, y 7.75-8.5 in) to convert into PIA02405/06 pixel boxes.
- Named-object print positions for P4.2's azimuth-corridor candidate enumeration: OBJECT V at 49 13/16, OBJECT Y at 61 7/8, OBJECT Z at 81 1/4 and 83 5/8, OBJECT W at 94 1/4 (ruler inches).
- The right-hand raw ruler table ('B. 4 7/8 TO D. 43 = 38 1/8', 'C. 5 1/4 TO D. 43 = 37 3/4', etc.) is the primary measurement record whose quality F5 validated - input to the P7.4 post-mortem and to any re-derivation.
- Documents the point-E bookkeeping discrepancy targeted by P0.4 ('E. 7 7/8 TO D. 43 = 35 1/8' vs scale box '3050ft / (x) 36 3/8in').

**Invalid / superseded content (for the annotation pass):**

- Scale factors: '1 inch = 73 27/61 feet (i.e. 2800ft / (x) 38 1/8in)', '1 inch = 87 63/151 ft (i.e. 3300ft / (x) 37 3/4in)', '1 inch = 83 247/291 ft (i.e. 3050ft / (x) 36 3/8in)' - the F4-invalidated radial factors (x1.84-1.85 overestimate).
- The '0 inches' top / '43 inch mark' bottom zero-point mapping '(x (height of point) - 43inches)' - the F3-invalidated linear range model.
- All derived sizes: 'F. 188 12/61 ft tall', 'G. 174 126/151 ft tall', 'J. 262 38/151 ft. tall', 'H. 22 58/61 ft tall', 'K. 64 16/61 ft tall', 'L. 71 4/151', 'I. 43 17/151 ft', and 'LENGTH of OBJECT X ... = 192 48/61 ft' - all carry the x1.84 bias (F4/F5).
- 'HEIGHT of OBJECT X ... 55 5/61 + (earth face)18 1/2 = 73 71/122' - the buried-'earth face' addition is conjecture with no observational support (F6, VALIDATION_REPORT §5.5).
- 'E. 3050 feet away from D.' presented alongside the NASA anchors - an interpolated assumption, not a NASA datum (annotation's own 'Only B. and C. are Known' concedes this).
- Cubit conversions 'OBJECT Y to OBJECT Z.G. ... = 1624.57 = 1083.0466667 cubits' and '... 1823.71 = 1215.8066667 cubits' - Egyptian-unit numerology layered on invalid distances (kin to F8's invented probabilities); also derived inter-object distances like 'OBJECT V.K to POINT F. ... = 885 55/61 ft'.

### `intake/00/final-03-object-MICRO_1721700342184.pdf` — extract-useful

Single-page letter PDF from Adobe Illustrator (title 'final-03-object.ai', author 'erici', Distilled 2024-07-23; filename epoch 1721700342184 = 2024-07-23T02:45:42Z). It is an extreme zoom crop of the panorama print covering ruler x = ~54.5-64.5 in and y = ~6-11.5 in, overlaid with a fine 1/16-inch measurement grid and inch labels (55-64 horizontal, 6-11 vertical) - i.e. the Object X neighborhood (VALIDATION_REPORT sect. 5.5: Object X at ruler x = 60-63 in; annotation gives height span y 7 3/4-8 1/2, length span x 60 1/8-62 3/4). No text beyond ruler numerals.

**Salvageable:**

- Operational input for P3.1: the 1/16-in coordinate grid registered onto the print pins down exactly which print region 'Object X' denotes, and gives the finest-granularity print-coordinate frame available for converting the annotation's spans (x 60 1/8-62 3/4, y 7 3/4-8 1/2) into the pre-registered pixel box on PIA02405/06.
- Timeline datum for P7.4: dated 2024-07-23, it shows the micro-inspection stage of the project sat between the Feb 2023/Mar 2024 annotation work and the June 2025 AI documents.

**Invalid / superseded content (for the annotation pass):**

- The document's implicit premise - that 'MICRO'-level inspection of this crop can reveal real structure - is superseded by the resolution-floor finding (sect. 5.5 under F6): at 860 m one native pixel spans ~0.84 m, detail below ~2 m is not resolved, and the 500% Photoshop enlargement plus JPEG/print steps 'add structure that was never on Mars'; everything visible at this zoom below that floor is interpolation, not information.

### `intake/00/twin_peaks_nasa.txt` — duplicate

*Duplicate/near-duplicate of `intake/00/twin_peaks_nasa_landscape.txt`.*

359-byte OCR/text-extraction of the annotation overlay on the Twin Peaks print (question list 'How far is: A from B ... How tall is: A', ruler pairs 'B. 4 7/8 TO D. 43', 'C. 3300 feet away', '0 inches', '43 inch mark'). Despite the 'nasa' filename it contains NO NASA caption text whatsoever - it is a transcription of the user's own annotations. Encoding is partly garbled ('B. 47/8 TO A.87/1�') and, unlike the landscape variant, no computed results ('= 38 1/8' etc.) are present.

**Salvageable:**

- Negative provenance finding worth recording in the annotation pass: the three 'twin_peaks_nasa*.txt' files preserve zero NASA caption prose - the actual NASA text lives only in 'intake/00/Catalog Page for PIA02405.pdf'/'PIA02406.pdf'; the filenames should not be mistaken for saved NASA captions (relevant to P0 hygiene / P1.5 quote spot-checking).

**Invalid / superseded content (for the annotation pass):**

- '0 inches' / '43 inch mark' ruler axis transcribes the invalidated linear range mapping (F3: '0 ft at the 43-inch mark' is geometrically wrong; range at frame bottom is ~2.7-3.3 m, not 0).

### `intake/00/twin_peaks_nasa1.pdf` — extract-useful

*Duplicate/near-duplicate of `preview (3).webp`.*

Single-page 9.9 MB PDF, page size 6624x6624 pt (92x92 in, rotated 90), title 'twin_peaks_nasa.psd', author 'ProudMartin', Distilled 2023-02-03 - the large-format print-source version of the fully annotated Twin Peaks panorama, with the annotation text as crisp vector type (no extractable text layer, but sharply rendered). Same annotation content as Untitled.png / the RTF payload / root 'preview (3).webp': objects V/W/X/Y/Z labels with arrows, three scale boxes, the A-L measurement table, and the 0-to-43-inch ruler axis.

**Salvageable:**

- Highest-fidelity record of the annotation geometry: the 'OBJECT X' arrow and A/E/K point placements on the panorama are sharper here than in any raster copy - the best operational input for deriving the P3.1 Object X pixel box (x1,y1)-(x2,y2) on PIA02405 from the print coordinates.
- Print-geometry ground truth for P3.1's inches-to-pixels conversion: the physical page is 92 in square (6624 pt) - a hard datum to reconcile against VALIDATION_REPORT sect. 4.1's inferred ~99-in print width (43-in image height x 2.31 aspect); the discrepancy (92 vs ~99 in) should be resolved before print coordinates are converted.
- Shows both sides of the P0.4 point-E discrepancy in one authoritative source: table entry 'E. 7 7/8 TO D.43 = 35 1/8' next to scale box '(i.e. 3050ft / (x) 36 3/8in)'.
- 'Only B. and C. are Known' and 'E. 3050 feet away from D.' establish, in the author's own hand, that the E anchor (3050 ft) was an interpolated assumption, not a NASA datum - quotable in the Phase 0 annotation pass.

**Invalid / superseded content (for the annotation pass):**

- All three scale factors: '1 inch = 87 63/151 ft (i.e. 3300ft / (x) 37 3/4in)', '1 inch = 83 247/291 ft (i.e. 3050ft / (x) 36 3/8in)', '1 inch = 73 27/61 feet (i.e. 2800ft / (x) 38 1/8in)' (F4, x1.84-1.85 overestimate).
- '(x (height of point) - 43inches)' / '0 inches' / '43 inch mark' - the invalidated F3 linear range mapping.
- Sphinx-scale and size assertions: 'HEIGHT of OBJECT X 8 1/2 to 7 3/4 ... 55 5/61 + (earth face)18 1/2 = 73 71/122', 'LENGTH of OBJECT X ... = 192 48/61 ft' (F6: distance unknown, size indeterminate; earth-face term is unsupported conjecture); peak/feature heights 'F.188 12/61 ft tall' (F5: ~1.8x too large), 'K. 64 16/61 ft', 'H. 22 58/61 ft', 'J. 262 38/151 ft. tall', 'G.174 126/151 ft tall', 'L. 71 4/151', 'I. 43 17/151 ft'.
- Cubit conversions 'OBJECT Y to OBJECT Z.G. ... 1624.57 = 1083.0466667 cubits' and '1823.71 = 1215.8066667 cubits' - numerology layered on the invalid factors (same failure family as F8's invented probabilities).

### `intake/00/twin_peaks_nasa1.rtf` — duplicate

*Duplicate/near-duplicate of `intake/00/Untitled.png`.*

5.1 MB RTF with no body text at all: it is a container for a single hex-encoded 2092x899 RGBA PNG (\shppict/\pngblip) of the fully annotated scale-system panorama - visually identical to intake/00/Untitled.png (2094x900) and the same content as root 'preview (3).webp' and twin_peaks_nasa1.pdf. RTF metadata: title 'twin_peaks_nasa.psd', author 'ProudMartin', created 2023-02-02, revised 2024-03-15, produced via PScript5.dll / Acrobat Distiller 22.

**Salvageable:**

- Metadata provenance only: creation 2023-02-02 and revision 2024-03-15 of the source PSD date the annotation work to Feb 2023 - Mar 2024, i.e. more than a year before the June 2025 AI-generated 'validation' papers (chat-history.txt) - timeline material for the P7.4 post-mortem.

**Invalid / superseded content (for the annotation pass):**

- The embedded image carries the full invalidated scale system: '1 inch = 73 27/61 feet', '1 inch = 87 63/151 ft', interpolated '1 inch = 83 247/291 ft (i.e. 3050ft / (x) 36 3/8in)' (F4); '0 inches'/'43 inch mark' axis (F3); size assertions 'F.188 12/61 ft tall', 'J. 262 38/151 ft. tall', 'HEIGHT of OBJECT X ... 55 5/61 + (earth face)18 1/2 = 73 71/122', 'LENGTH of OBJECT X ... 192 48/61 ft' (F4/F6); and cubit numerology 'OBJECT Y to OBJECT Z.G. ... = 1083.0466667 cubits', '= 1215.8066667 cubits' built on the invalid factors.

### `intake/00/twin_peaks_nasa_landscape.txt` — extract-useful

478-byte plain-text transcription of the annotated print's measurement table, with results: 'B. 4 7/8 TO D. 43 = 38 1/8', 'C. 51/4 TO D.43 = 37 3/4', 'B. 4 7/8 TO F. 7 7/16 = 2 9/16' (the North Twin height ruler reading), 'E. 7 7/8 TO D.43 = 35 1/8', plus 'B. 2800 feet away C. 3300 feet away'. No NASA caption prose - annotation text only. The cleanest machine-readable copy of the raw ruler measurements among the three txt variants.

**Salvageable:**

- Primary data: the raw ruler readings themselves (e.g. '2 9/16' for North Twin vertical extent, '2 3/16' for South Twin) - F5 validated exactly these numbers as accurate at ~native-pixel level once rescaled; this file is their machine-readable record (feeds P7.4 post-mortem and any re-derivation in P3.1).
- Contains 'E. 7 7/8 TO D.43 = 35 1/8' - one side of the point-E bookkeeping discrepancy (35 1/8 in table vs 36 3/8 in scale box, VALIDATION_REPORT sect. 4) that P0.4 must reconcile; having it in plain text makes the reconciliation quotable.
- 'B. 2800 feet away C. 3300 feet away' documents which two anchors were treated as known - matches NASA's caption figures (2800 ft / 3300 ft) without alteration.

**Invalid / superseded content (for the annotation pass):**

- '0 inches' / '43 inch mark' framing transcribes the invalidated F3 linear range mapping; the '= 38 1/8' and '= 37 3/4' baselines are the denominators of the invalidated 73.44 and 87.42 ft/in factors (F4), though the factors themselves do not appear in this file.

### `intake/00/twin_peaks_nasa_updated.txt` — flag-superseded

*Duplicate/near-duplicate of `intake/00/twin_peaks_nasa_landscape.txt`.*

484-byte near-duplicate of twin_peaks_nasa_landscape.txt with one addition: the derived scale factor '1 inch= 73 27/61 fee[t] (i.e. 2800ft / 38 1/8in)' prepended. Same measurement table ('B. 4 7/8 TO D. 43 = 38 1/8' etc.), same absence of any NASA caption prose. The 'updated' in the filename refers to adding the scale-factor derivation, i.e. the exact step where the method went wrong.

**Salvageable:**

- Documents the derivation step itself ('2800ft / 38 1/8in') in the author's own notation - useful only as a quotable exhibit for the P7.4 post-mortem (what the original system did, and where the radial-vs-transverse confusion entered).

**Invalid / superseded content (for the annotation pass):**

- '1 inch= 73 27/61 fee[t] (i.e. 2800ft / 38 1/8in)' - the invalidated 73.44 ft/in per-anchor factor (F4: overestimates true transverse scale 40.0 ft/in by x1.84).
- '0 inches' / 43-inch axis framing repeats the invalidated F3 linear range mapping.

### `intake/00/unnamed.jpg` — extract-useful

4000x3000 photo (EXIF software 'Picasa', no capture date) of the laminated banner mounted on a wall: the right half of the Twin Peaks panorama with both peaks on the horizon, the printed grid over the right portion, and the small ruler-cross at the horizon near x~57 - the physical print of the 103_2264_13100153_1.jpg composite.

**Salvageable:**

- Only full-context view of the mounted physical print (wall, lamination, staples/tape) - provenance documentation of the measurement apparatus for the P7.4 post-mortem, and visual confirmation that the print-order composite (103_2264_13100153_1.jpg) is what was actually printed at ~99-inch width (VALIDATION_REPORT §4.1).

**Invalid / superseded content (for the annotation pass):**

- As with the other print photos, the depicted grid/cross exists to serve the invalidated F3/F4 scale system; the photo asserts no numbers.


## Markups and staged images (`intake/01/`)

### `intake/01/40046_PIA02405.jpg` — duplicate

*Duplicate/near-duplicate of `intake/00/PIA02405.jpg`.*

NASA Photojournal product PIA02405 'Twin Peaks in Super Resolution - Left Eye', JPEG 7238x3135 RGB, unannotated. Byte-identical (md5 8c92401d) to intake/00/PIA02405.jpg. The '40046_' prefix looks like an upload ID from the June 2025 AI chat session; this was evidently the left-eye input to that session's stereo work.

**Salvageable:**

- Primary NASA image data (the left-eye press product itself) - but only as a redundant copy; the canonical in-repo copies are intake/00/PIA02405.jpg and the full-resolution intake/00/PIA02405.tif already used in analysis/FULLRES_RERUN.md (P1.1 provenance logging should list this duplicate's hash once, not treat it as a separate source)

### `intake/01/40046_PIA02405_resized.jpg` — historical-only

Grayscale (mode L) conversion of PIA02405.jpg at identical dimensions 7238x3135 - despite the '_resized' name, only the color was stripped (mean abs diff 0.08 vs a grayscale of the original after downsampling). No annotations. This is preprocessing output of the invalidated stereo pipeline: the AI session converted both eyes to grayscale for disparity matching.

**Salvageable:**

- Forensic evidence of the exact preprocessing chain the June 2025 AI stereo session used (grayscale conversion step) - relevant only to the P7.4 post-mortem's reconstruction of how the invalid analysis was built

**Invalid / superseded content (for the annotation pass):**

- Exists solely as an input to the stereo-ranging attempt invalidated by F2 (true Twin Peaks disparity ~0.17 native px; the two products are independently assembled Photoshop mosaics offset ~175 px by framing alone)

### `intake/01/40047_PIA02406.jpg` — duplicate

*Duplicate/near-duplicate of `intake/00/PIA02406.jpg`.*

NASA Photojournal product PIA02406 'Twin Peaks in Super Resolution - Right Eye', JPEG 7296x3135 RGB, unannotated. Byte-identical (md5 9499de28) to intake/00/PIA02406.jpg. Companion upload to 40046_PIA02405.jpg for the AI stereo session.

**Salvageable:**

- Primary NASA image data (right-eye press product) - redundant copy; canonical copies are intake/00/PIA02406.jpg and intake/00/PIA02406.tif (P1.1: log as duplicate hash only)

### `intake/01/40047_PIA02406_resized.jpg` — historical-only

Grayscale conversion of PIA02406.jpg that has ALSO been horizontally resampled from 7296x3135 to 7238x3135 - i.e. the right eye was anisotropically squeezed ~0.8% to force it to the left eye's pixel dimensions (full-frame resample confirmed, mean abs diff 0.15; a crop-to-7238 hypothesis fails at 20.7). No annotations. This is the 'rectification' step of the invalidated stereo pipeline.

**Salvageable:**

- Documents concretely that the AI stereo session forced the two independently-framed mosaics into equal dimensions by a non-uniform horizontal squeeze - a geometry-distorting step worth naming in the P7.4 post-mortem, since it shows the pipeline treated mosaic framing as if it were epipolar geometry

**Invalid / superseded content (for the annotation pass):**

- Embodies the stereo-pair premise invalidated by F2: the eyes are not a rectified stereo pair (different sizes 7238 vs 7296 because they are separately assembled 8-frame/7-frame Photoshop mosaics), and squeezing one to match the other manufactures false correspondence; any disparity measured from this file inherits the ~3-orders-of-magnitude F7 error

### `intake/01/file-0DFOHFFAiE79IJn4h22UTodD.webp` — historical-only

Misnamed file: actually a PNG (1684x438 RGBA), a matplotlib figure showing the two panoramas side by side, titled 'Left Eye Image' and 'Right Eye Image', each with pixel-coordinate axes (0-7000+ x, 0-3000+ y). The 'file-...' filename pattern matches ChatGPT session file exports, tying it to the June 2025 AI stereo session. No markups beyond the axes; no new data.

**Invalid / superseded content (for the annotation pass):**

- Display artifact of the stereo analysis invalidated by F1 (circular 0.6-0.8% distance validation) and F2 (impossible stereo precision); the figure itself makes no claims but exists only as that workflow's visualization

### `intake/01/file-W5y0OFDAlu0loNO09BgdyAte.webp` — extract-useful

*Duplicate/near-duplicate of `intake/01/markup_1000000036.png`.*

Misnamed file: actually a PNG (1684x761 RGBA), a matplotlib figure of the full PIA02406 right-eye panorama (verified by correlation: diff 18.4 vs right eye, 31.4 vs left) with product-pixel axes and dashed gridlines. It is the unannotated base image of the markup_1000000036/41 family (near-duplicates differing only in the annotation region). Plot-area calibration: figure x 114-1664 maps to data x 0-7296, figure y 32-699 maps to data y 0-3135 (4.71 / 4.70 data px per figure px).

**Salvageable:**

- The axes calibration (fig x 114-1664 = product x 0-7296; fig y 32-699 = product y 0-3135) is what converts the hand markups in this family into PIA02406 product-pixel coordinates - the load-bearing reference for using the markups as P3.1 input
- Confirms the markup family's coordinate frame is the RIGHT eye (PIA02406), so P3.1 gets its PIA02406 box directly from these files and must derive the PIA02405 box separately (the ~175 px inter-eye framing offset, VALIDATION_REPORT sec 2, is not negligible)

**Invalid / superseded content (for the annotation pass):**

- Produced by the same invalidated AI stereo session (F1/F2/F8 context); no claims in the image itself

### `intake/01/markup_1000000036 (1).png` — extract-useful

*Duplicate/near-duplicate of `intake/01/file-W5y0OFDAlu0loNO09BgdyAte.webp`.*

The same 1684x761 PIA02406 figure with a cyan freehand highlight scribbled over the Object X mound - a low elongated hummock rising to a hump at its right end, just left of a dark conical rock, below and right of North Twin's flank. Differs from the unannotated base only in figure px 1040-1074 x, 141-175 y.

**Salvageable:**

- User-drawn Object X locator: the highlight maps to PIA02406 product px approx x 4360-4520, y 512-672 (via the axes calibration fig 114-1664 = 0-7296) - direct P3.1 input; together with the other three locators in this family it gives a consensus right-eye box of roughly x 4310-4520, y 510-675

### `intake/01/markup_1000000036 (2).png` — historical-only

A tiny 160x159 unannotated screenshot crop of the matplotlib figure, showing North Twin Peak with the hummock field and the Object X mound below it; dashed gridlines from the figure are visible. Template-matched to figure px (962,70), i.e. PIA02406 product px approx x 3990-4745, y 180-925. No markup, no label text.

### `intake/01/markup_1000000036 (3).png` — duplicate

*Duplicate/near-duplicate of `intake/01/markup_1000000036 (2).png`.*

A 158x158 unannotated screenshot crop nearly identical to 'markup_1000000036 (2).png', shifted by ~16 figure px (template-matched to figure px (961,86), PIA02406 product px approx x 3990-4730, y 255-995). It is also exactly the base of markup_1000000041.png (which adds the cyan scribble; ~1% of pixels differ). No annotations.

### `intake/01/markup_1000000036.png` — extract-useful

*Duplicate/near-duplicate of `intake/01/file-W5y0OFDAlu0loNO09BgdyAte.webp`.*

The same 1684x761 PIA02406 matplotlib figure with a small square desaturated/contrast-enhanced inset image pasted directly over the Object X mound below North Twin's right flank (figure px 1034-1074 x, 141-175 y). Verified pixel-by-pixel that the inset is an enhanced grayscale crop of the SAME underlying terrain (identical mound profile, dark spots, and dark conical rock at right) - it is not an external photo (not a Sphinx image).

**Salvageable:**

- Object X locator: the pasted inset covers PIA02406 product px approx x 4330-4520, y 512-673 - direct input to the P3.1 pixel-box definition, and consistent with VALIDATION_REPORT sec 5.5's print-derived location (ruler x ~60-63 in ~ product x 4390-4610 on the left eye) within the known inter-eye framing offset

**Invalid / superseded content (for the annotation pass):**

- The grayscale 'enhancement' inside the inset shows only interpolated press-product texture - per F6/sec 5.5, detail below ~2 m at 860 m range is manufactured by the 500% Photoshop upsample, so any perceived structure ('face', edges) in the inset is not evidence

### `intake/01/markup_1000000041 (1).png` — extract-useful

A 40x24 px crop that tightly frames the Object X mound itself, heavily blurred/interpolated at this scale. Template-matched into the figure at px (1030,143), which converts to PIA02406 product px approx x 4312-4500, y 522-635 - effectively an implicit tight pixel box around Object X.

**Salvageable:**

- The crop's matched footprint (PIA02406 px ~4312-4500 x, ~522-635 y) is the tightest of the four Object X locators and can seed the P3.1 pixel-box definition directly (the box should be re-derived on the full-res TIFF, but this fixes the region unambiguously)

**Invalid / superseded content (for the annotation pass):**

- The crop's pixel content is far below the resolution floor (F6/sec 5.5: ~0.84 m per native px at 860 m, and these are 5x-upsampled product pixels further degraded by figure rendering) - nothing morphological can be read from it

### `intake/01/markup_1000000041.png` — extract-useful

*Duplicate/near-duplicate of `intake/01/markup_1000000036 (3).png`.*

A 158x158 crop with the same footprint as 'markup_1000000036 (3).png' plus a cyan freehand highlight painted over the Object X mound, tracing its profile (low ridge on the left rising to a hump on the right). In-crop blue bbox x 73-105, y 63-76 maps to figure px (1034-1066, 149-162).

**Salvageable:**

- Object X locator: the highlight converts to PIA02406 product px approx x 4330-4480, y 550-611 - the most conservative of the family's four consistent locators; P3.1 can quote all four (this file, 36, 36(1), 41(1)) as independent hand-markings agreeing on a consensus right-eye box of ~x 4310-4520, y 510-675


## Derived/enhanced images (`intake/02/`)

### `intake/02/enhanced_image.png` — historical-only

A real but 32x11-pixel grayscale PNG (520 bytes) - a thumbnail-scale crop of a dark horizon/hummock silhouette, evidently the Object X region. The name and the sibling files indicate it is an AI-chat 'enhancement' output saved at thumbnail size. It is not corrupt, but at 352 total pixels it carries essentially zero scene information.

**Invalid / superseded content (for the annotation pass):**

- The premise of the file - that 'enhancement' of this crop reveals structure - violates the resolution floor (VALIDATION_REPORT F6/§5.5: detail below ~2 m at 860 m is not resolved; enhancement cannot add information). Any morphological claim sourced to this 32x11 px image is unsupported by construction.

### `intake/02/file-Kk66qTNQ9YtH8k1h2FmjpFv9.png` — duplicate

*Duplicate/near-duplicate of `intake/02/model_3d_image.png`.*

A 924x959 render of the exact same matplotlib figure as model_3d_image.png ('Refined 3D Model of Identified Silhouette', Head/Body/Base triangle). The 'file-<ID>.png' name is the ChatGPT file-download naming pattern, confirming the AI-chat origin of the figure.

**Salvageable:**

- The filename pattern 'file-Kk66qTNQ9YtH8k1h2FmjpFv9' is provenance evidence that intake/02 contents are ChatGPT session downloads - useful only for the P0/P7.4 documentation of where the AI-generated material came from.

**Invalid / superseded content (for the annotation pass):**

- Same invalid content as intake/02/model_3d_image.png: a 'Head/Body/Base' sphinx model resting on the invalidated identification premise (F6, F8).

### `intake/02/model_3d_image.png` — historical-only

A 2000x1200 matplotlib 3D plot titled 'Refined 3D Model of Identified Silhouette': a single cyan triangle with three vertices labeled 'Head', 'Body', 'Base' on axes X 60-90, Y 70-120, Z 0-14. It contains no imagery and no measurements - three labeled points rendered as a 'model'.

**Invalid / superseded content (for the annotation pass):**

- 'Refined 3D Model of Identified Silhouette' with 'Head/Body/Base' labels presupposes the sphinx identification (invalidated chain: F6 indeterminate size, F8 unsupported AI validation); a triangle from three arbitrary points is a visualization of an assumption, not a reconstruction. No axis units or provenance are given for the 60-90/70-120 coordinates.

### `intake/02/overlay_image_2.png` — historical-only

A real but 32x11-pixel RGBA PNG (540 bytes) showing a solid black reclining-animal (sphinx-like) silhouette drawn on a light background - an AI-chat 'overlay' output at thumbnail size. Not corrupt, but it is a drawn shape, not image data.

**Invalid / superseded content (for the annotation pass):**

- The overlay is a hand/AI-drawn sphinx outline superimposed at a scale (32x11 px) far below the resolution floor - it is the clearest surviving example of the AI session manufacturing the very shape it then 'identified' (cf. VALIDATION_REPORT §6 on the AI documents' circular validation). Quotable for the annotation pass as fabricated visual evidence.
