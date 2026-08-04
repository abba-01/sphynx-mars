# Findings to Date — Plain-English Report

**Date:** 2026-08-02. **Scope:** everything established by this repository so far —
the validation work, the full-resolution re-run, the historical-intake review, and
the provenance verifications. Each finding states *what we know, how we know it,
and how sure we are*. Working hypotheses are labeled as such. Sources for every
claim are in `VALIDATION_REPORT.md` §8, `data/PROVENANCE.md`, and
`data/P1_4_RETRIEVAL.md`.

---

## 1. What these images actually are — established

The two panoramas (NASA products PIA02405/PIA02406) are **press-release pictures,
not scientific data**. NASA's own caption — verified word-for-word against pages
saved from nasa.gov this morning — says the frames were "enlarged by 500% and then
co-added using Adobe Photoshop," then colorized and re-balanced.

In plain terms: each pixel in these images covers one-fifth of a real camera pixel.
Anything in them smaller than the camera's true resolution is **smoothing invented
by software, not detail on Mars**. At the Twin Peaks' distance, the camera's true
resolution is roughly 0.8–1 meter per pixel, and no feature smaller than about 2
meters can be trusted at all.

*Confidence: high. Source: NASA's caption, in the repo twice (saved PDFs and
saved live pages), matching verbatim.*

## 2. The hand measurements were good; the scale model was not — established

The ruler work on the ~99-inch print was **accurate to about one camera pixel**.
That part survives scrutiny completely.

The conversion from print-inches to feet did not. The original system assumed
distance increases linearly up the print from a "zero" at the 43-inch mark. Camera
geometry doesn't work that way: the bottom of the frame is ground about 3 meters
away (not zero), and everything from 860 m to the horizon is squeezed into about
two real pixels. The per-anchor conversion factors (73.44 and 87.42 ft/inch) came
out **1.84× too large** — every derived size was inflated by nearly a factor of two.

**The decisive test:** NASA's caption independently states the Twin Peaks are
30–35 m tall. The original system produced 57 m — clearly wrong. Take the *same
ruler measurements* and push them through the correct angular conversion, and they
give **31.5 m and 28.7 m — inside or just under NASA's published range.** The
measuring was sound; only the model was broken, and we know by exactly how much.

*Confidence: high. This was re-verified this week at full resolution (below).*

## 3. Distance cannot be measured from these images — established

Two claims in the old AI-written papers fail:

- The "0.6–0.8 % distance validation against NASA" **compared NASA's own numbers
  with themselves** (2800 ft converted to meters vs "860 m" — the same sentence in
  the same caption, in two unit systems). Nothing was measured.
- Stereo ranging of the peaks is **physically impossible** from these products. With
  the camera's 15 cm eye separation, the stereo signal at 860 m is 0.17 pixel —
  smaller than the matching noise (±0.2 px). Worse, the two "eyes" are separately
  assembled mosaics whose framing differs by ~170 pixels (re-measured this week at
  full resolution: 161–172 px) — about **200× larger than the stereo signal** being
  sought. Any "distance" extracted this way is noise.

NASA's actual distances came from cartography: sight-lines from the lander matched
to Viking orbiter images (T. Parker's work, and Oberst et al. 1999, who localized
the lander to ~40 m this way). That is the method this program's decisive test
adopts, with modern data.

*Confidence: high. The arithmetic is in the repo and re-runnable
(`analysis/measure_twin_peaks.py`).*

## 4. Object X: size unknown, identity unresolvable at this resolution — established

NASA's caption says the hummock field containing Object X spans "a few tens of
meters away from the lander to the distance of the South Twin Peak." That is a
**factor-of-20 uncertainty in distance, and therefore a factor-of-20 uncertainty in
size** — from this image alone, Object X could be a 1.5-meter mound nearby or a
30-meter mound far away. No amount of careful measuring on this image can resolve
that.

If one *assumes* it sits at North Twin's distance, the corrected size is about
**9 m high × 32 m long — roughly half the Great Sphinx's scale** (20 m × 73 m,
Britannica), not a match. The shape similarity that remains (height-to-length ratio
~0.28 vs the Sphinx's ~0.275) has **no discriminating power**: nearly every
elongated mound on Earth or Mars shares it.

As for whether it *looks carved*: at that distance the data cannot distinguish
carving from erosion — the relevant detail is below the 2-meter trust floor, and
the 500 % enlargement fills that zone with invented smoothness.

*Confidence: high for "indeterminate from this image." The actual size and nature
remain open questions — decidable, see §8.*

## 5. Full-resolution confirmation — new this week, established

The original validation was done on small preview images. The full-resolution
NASA TIFFs (66–70 MB) are now in the repo, **byte-for-byte identical** to fresh
copies acquired in a documented nasa.gov session (hash-verified, provenance
logged). The whole measurement pipeline was re-run on them, on both eyes,
after first proving the updated code reproduces the old results exactly:

- North Twin: preview said 30.8 milliradians of height; full resolution says 30.4
  (left eye) and 32.1 (right eye). South Twin: 22.6 vs 22.5 and 22.0.
- Every difference is within the stated tolerance (±2 camera pixels).
- All conclusions above are unchanged. The previews had been carrying essentially
  all the real information — as predicted, since one preview pixel ≈ one real
  camera pixel.

*Confidence: high. Error budget and gate results in `analysis/FULLRES_RERUN.md`.*

## 6. The old AI-generated "validation" papers are unreliable — established

The conversation transcripts preserved in this repo show how those documents were
made: literature searches visibly returning **"0 results"**, followed immediately
by confident prose, invented citations, and probability figures ("1 in 10¹³",
"1 in 10¹⁵", "1 in 10¹⁸" — mutually inconsistent, with no defined calculation
behind any of them). One transcript also shows a **silent subject switch**: asked
which way the Mars "sphinx" faces, the AI answered about the Cydonia "Face" —
a different feature 3,000 km away — and that answer ("faces north") then
contaminated the orientation documents.

One nuance discovered this week: the NASA-sounding quotes in those documents about
horizon landmarks (North Knob, Southeast Knob, Far Knob) turned out to be **genuine
NASA caption text** — verified verbatim against saved NASA pages. The text was
real; the use made of it was not (Far Knob is a 450-meter mountain 30 km away that
was folded into a claimed 985-meter local "pyramid alignment").

*Confidence: high. The receipts are in `intake/chat/` and `chat-history.txt`;
the per-file review is `intake/INTAKE_REVIEW.md`.*

## 7. What the historical-file review salvaged — new this week

All 53 historical files were reviewed skeptically. Genuinely useful recoveries:

- **A pixel-location seed for Object X**: the old markup images turn out to be
  calibrated to the right-eye product — Object X sits at approximately
  x 4312–4500, y 522–635 in PIA02406 pixels. This feeds the formal definition step
  directly.
- **Both sides of a bookkeeping discrepancy** in the original scale table (point E:
  35⅛ vs 36⅜ inches) recovered from primary records, so it can be reconciled.
- **A print-size conflict that must be resolved first**: the print-source PDF says
  the physical print is 92 inches wide; the validation report inferred ~99 inches.
  A ~7 % disagreement that would propagate into every inch-to-pixel conversion.
- **A near-field calibration target**: NASA's caption names rock "Otter" — 1.5 m
  long, 10 m from the lander — a published size-and-distance answer usable to
  validate stereo code where stereo actually works (close range only).
- Practical flags: the phone photos carry GPS coordinates in their metadata (scrub
  before anything goes public), and ~135 MB of byte-identical duplicate files are
  listed for optional cleanup.

## 8. What is NOT established, and how it gets decided — the honest bottom line

**Nothing in this repository supports the claim that Object X is an artificial
structure.** Equally: its actual size and nature have not been measured yet. The
strongest *validated* results so far are (a) the hand measurements were careful,
and (b) the objects measured are, after correction, consistent with the modest
hills NASA describes.

The question is decidable. The Pathfinder site was imaged by the HiRISE orbital
camera at 25 cm per pixel — about 3,400× finer ground detail than the lander view
at that range, with **no distance ambiguity at all** (the lander itself is visible
in the image). The precedent is exact: the Cydonia "Face" looked artificial at low
resolution and became an ordinary mesa when re-imaged sharply. The program's Phase
3/4 plans pre-register the hypotheses and thresholds *before* looking — including
the null result ("Object X is an ordinary flood-debris hummock like its ~30
neighbors") being written up with the same care as any other outcome.

**What stands between here and the answer:** downloading the public HiRISE
observations (PSP_001890_1995, PSP_002391_1995), the native camera frames from the
PDS archive, and five reference papers — all listed with verification steps in
`data/SOURCING_LIST.md`. All free; none reachable from this sandbox; all fetchable
from any normal connection.

---

*Method note: this program's standing rules — pre-register before measuring, carry
an uncertainty on every number, test every pipeline against a known answer before
trusting it on an unknown, quote institutional sources verbatim, and publish the
null result — are defined in `ROADMAP.md` and applied in `plans/PHASE_0…7_PLAN.md`.
This report contains no new measurements; it summarizes recorded, re-runnable ones.*
