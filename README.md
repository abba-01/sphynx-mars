# sphynx-mars

Private research notes on Mars surface morphology, stereoscopic analysis, and out-of-place-artifact hypotheses.

## Contents

- `paper/manuscript.md` — **journal-style manuscript** (methods/measurement note, not yet submitted): the ×1.84 scale-model error with closed-form correction, known-answer validation, stereo infeasibility, the Object X silhouette with full range-ambiguity treatment, and a null result on artificiality
- `CORRECTIONS.md` — **corrections log**: errors found in this repository's own work, how each was caught, and what changed downstream (append-only; 25 confirmed in the 2026-08-04 audit)
- `FINDINGS.md` — **plain-English findings to date** (what is established, at what confidence, what remains open, and how it gets decided)
- `book/the-sphinx-on-mars.md` — **narrative chapter draft**: the arc from the appearance, through the seductive first math, the corrected math, and the disproof, as a lesson on exploration (every figure sourced to the validated record)
- `ROADMAP.md` — **phased research roadmap with a rigorous task list per phase** (pre-registration, error budgets, falsification gates, exit criteria)
- `plans/PHASE_0_PLAN.md` … `plans/PHASE_7_PLAN.md` — **per-phase execution plans**: research protocol, academic-integrity protocol, agent fan-out design with acceptance thresholds, quality gates, failure modes, deliverables
- `VALIDATION_REPORT.md` — **rigorous validation of the images, camera claims, and the ruler-based scale system** (sourced, quoted, reproducible)
- `SIZE_VERIFICATION_METHODOLOGY.md` — **step-by-step scientific protocol for verifying feature sizes**, with falsification gates
- `analysis/measure_twin_peaks.py` — reproducible pixel measurements behind the report; one code path serves the previews (default) and the full-res products (`--image intake/00/PIA02405.tif`); `analysis/skyline_overlay*.png` are its outputs
- `analysis/FIXING_THE_ZERO_POINT.md` + `analysis/corrected_range_chart.py` — **why the range origin cannot be repaired by moving it**: the true reference is the horizon (a singularity, 35.7 in from where zero was placed), the mapping is hyperbolic at every origin, and the two calibration anchors are 0.018 in apart geometrically versus 0.375 in as annotated (×21) — plus the corrected near-field range chart that replaces it
- `analysis/corrected_overlay.py` → `analysis/corrected_overlay_scene.png` + `_objectx.png` — **the corrected geometry drawn on the highest-resolution source** (PIA02405, 0.196 mrad/px, selected by a documented survey of all 35 official products): true horizon reference, anchors solved as summit elevations (29.6 m / 29.2 m), resolution-floor bar, Object X envelope with size-vs-range
- `analysis/FULLRES_RERUN.md` — **full-resolution re-run results** (roadmap P2.1–P2.3): preview-based conclusions confirmed on `intake/00/PIA02405.tif` / `PIA02406.tif`, cross-eye gate passed
- `analysis/OBJECT_X_SILHOUETTE_REPORT.md` + `analysis/object_x_silhouette.py` — **measured silhouette geometry of "Object X"** (angular size, width profile, sub-feature decomposition, size-vs-range, resolution floor) with an explicit section on where naming enters; measurement defensible, artificiality interpretation fenced as unsupported at this resolution
- `intake/INTAKE_REVIEW.md` — **per-file review of all 53 historical intake files**: salvageable primary data (Object X pixel-box seeds, point-E reconciliation records, provenance evidence), duplicates, and flagged invalid content; nothing in `intake/` is evidence until it passes its phase gates
- `mars_stereo_analysis.md` + `mars_stereo_analysis (1).md` — stereoscopic photogrammetry working notes
- `stereo_methodology_paper.md` — methodology draft
- `mars_earth_orientation_analysis.md` — orientation correlation notes
- `intelligence_vs_nature_morphology.md` — discrimination criteria for natural-vs-engineered morphology
- `interplanetary_civilization_hypothesis.md` — hypothesis-tracking
- `pareidolia_vs_measurement.md` — pareidolia-discrimination notes
- `universal_morphology_cycles.md` — cyclic-morphology framing
- `visual_tunneling_camera_analysis.md` — tunneling-effect / camera-artifact analysis
- `PIA02405-left-eye.pdf` + `PIA02406-right-eye.pdf` — source documents
- `preview*.webp` — image previews
- `chat-history.txt` — raw research-conversation transcript

## Discipline notes

- All claims here are **working hypotheses**, not deposited findings
- Pareidolia-vs-measurement discrimination is doctrine — assertions about "structure on Mars" might include the falsification test
- The two AI-generated "validation" documents (`mars_stereo_analysis*.md`, `stereo_methodology_paper.md`) contain circular validation and order-of-magnitude stereo-error mistakes — see `VALIDATION_REPORT.md` before citing them

