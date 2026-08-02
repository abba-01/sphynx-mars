# Research Roadmap

**Goal.** Take the question this repository actually poses — *are the features in the
Mars Pathfinder Twin Peaks scene (in particular "Object X") natural landforms or
something anomalous?* — from working hypothesis to a defensible, decided answer, using
only methods that survive the falsification gates in `SIZE_VERIFICATION_METHODOLOGY.md`.

**Standing rules (apply to every phase).**

- **Pre-register before you look.** Any hypothesis to be tested is written down — with
  numeric tolerances — *before* the measurement that could confirm or kill it is made.
  Commits are the timestamp: the pre-registration commit must precede the results commit.
- **Every number carries an error budget** (per `SIZE_VERIFICATION_METHODOLOGY.md`
  Step 5). A measurement without an uncertainty is not finished.
- **Known-answer test first.** No pipeline is trusted on an unknown until it reproduces
  an independently published value in the same scene (here: Twin Peaks heights, 30–35 m,
  NASA caption).
- **Institutional sources only** (NASA/JPL, USGS, PDS, University of Arizona/HiRISE,
  peer-reviewed journals), quoted verbatim with URLs and access dates.
- **Publish the null result.** If a decisive test comes back "ordinary hummock," that
  result gets written up with the same care as a positive would have been. The Cydonia
  precedent (`VALIDATION_REPORT.md` §7) is the model.
- **No post-hoc rescue.** If a pre-registered hypothesis fails its tolerance band, it is
  recorded as failed. A revised hypothesis is a *new* pre-registration, tested against
  *new* (or held-out) data, not against the data that generated it.

Phases 1–4 are sequential (each depends on the last); Phases 5–7 can proceed in
parallel once their inputs exist. Checkbox IDs (P1.1 …) are for cross-referencing in
commits and future documents.

**Detailed execution plans.** Each phase has a full execution plan in `plans/`
(`plans/PHASE_0_PLAN.md` … `plans/PHASE_7_PLAN.md`): step-by-step research protocol,
phase-specific academic-integrity protocol, multi-agent fan-out design (roles,
blinding/independence arrangements, structured-output contracts, acceptance
thresholds, human sign-off checkpoints), quality gates, failure modes, and
deliverables. The roadmap sections below define *scope and exit criteria*; the plans
define *how the work is executed*. On any conflict, the roadmap's exit criteria govern.

---

## Phase 0 — Repository hygiene (can start immediately)

*Objective: make the repo safe to cite from — no reader should be able to mistake an
invalidated claim for a live one.*

- [ ] **P0.1** Add a header block to `mars_stereo_analysis.md`, `mars_stereo_analysis (1).md`,
      and `stereo_methodology_paper.md` stating: AI-generated (June 2025, per
      `chat-history.txt`), contains circular distance validation, ~3-orders-of-magnitude
      stereo-error mistake, and fabricated citations — superseded by
      `VALIDATION_REPORT.md`. Do **not** delete them; they are part of the record.
- [ ] **P0.2** Add a similar header to `interplanetary_civilization_hypothesis.md`
      noting the ¹²⁹Xe material contradicts the established radiogenic/escape account
      (Nature 352, 697; *EPSL* 2021; *Science Advances* 2024) and would need to overturn
      those sources to stand.
- [ ] **P0.3** Annotate `pareidolia_vs_measurement.md` with the correction from
      `VALIDATION_REPORT.md` §6: measurement objectifies *size* claims only, not
      *identity* claims; identity is gated by resolution.
- [ ] **P0.4** Reconcile the point-E bookkeeping discrepancy in the annotated scale
      system (35⅛ in vs 36⅜ in, `VALIDATION_REPORT.md` §4) or mark point E as retired.
- [ ] **P0.5** Rename files with spaces/parentheses (`mars_stereo_analysis (1).md`,
      `preview (1).webp` …) to script-safe names, updating references in all documents.

**Exit criteria:** every document in the repo either passes the validation report's
findings or visibly carries the finding that invalidates it.

---

## Phase 1 — Acquire the primary data (requires normal network access; blocked in the analysis sandbox)

*Objective: replace press-release visualizations with calibrated archive data, with
provenance recorded well enough that a stranger could verify every byte.*

- [ ] **P1.1** Download the full-resolution Photojournal products `PIA02405.tif`
      (65.93 MB) and `PIA02406.tif` from photojournal.jpl.nasa.gov; record URL, access
      date, file size, and SHA-256 checksum in a `data/PROVENANCE.md`.
- [ ] **P1.2** Download the calibrated IMP archive: PDS Imaging Node dataset
      `MPFL-M-IMP-2-EDR-V1.0` (pds-imaging.jpl.nasa.gov) — at minimum the left/right-eye
      frames composing the Twin Peaks super-resolution sequence — plus *The Imager for
      Mars Pathfinder User's Guide* from the dataset's `document/` directory. Checksums
      and label files into `data/PROVENANCE.md`.
- [ ] **P1.3** Download HiRISE observation `PSP_001890_1995` (map-projected, 25 cm/px;
      lander visible) and stereo observation `PSP_002391_1995` from uahirise.org,
      including the published DTM if available from the HiRISE DTM archive; if no
      archived DTM exists, record that fact and plan Phase 4 around the stereo pair.
- [ ] **P1.4** Retrieve the two governing papers for methods detail: Smith et al. 1997
      (doi:10.1029/96JE03568) and Kirk et al. 1999 (doi:10.1029/1998JE900012); also
      Parker's sight-line localization (*Science* 278, 1746, 1997).
- [ ] **P1.5** Spot-check every quote in `VALIDATION_REPORT.md` §8 against the live
      pages (they were taken from saved PDFs and search-engine renderings under the
      sandbox egress block); correct any transcription drift.

**Exit criteria:** all five items checksummed and provenance-logged; no analysis in
later phases may cite a file absent from `data/PROVENANCE.md`.

---

## Phase 2 — Re-verify the measurement pipeline at full resolution

*Objective: confirm that the preview-based results in `VALIDATION_REPORT.md` hold on
the full-resolution products, and freeze a trusted pipeline.*

- [ ] **P2.1** Re-run `analysis/measure_twin_peaks.py` against the full-resolution
      TIFFs; parameterize the script so preview and full-res runs share one code path.
- [ ] **P2.2** Known-answer gate: corrected angular pipeline must again land both peak
      heights within (or explainably below, given base occlusion) NASA's 30–35 m; record
      the full error budget table per `SIZE_VERIFICATION_METHODOLOGY.md` Step 5.
- [ ] **P2.3** Cross-eye gate: repeat the angular extents on PIA02406 (right eye);
      agreement required within the pixel-count uncertainty.
- [ ] **P2.4** Quantify the interpolation floor empirically: compare a native EDR frame
      (P1.2) against the corresponding region of the 500 %-enlarged product; document
      what spatial frequencies the Photoshop co-add actually adds. This turns the
      "resolution floor rule" from an argument into a measurement.
- [ ] **P2.5** Tag the repo (`pipeline-v1`) once P2.1–P2.4 pass; later phases must use
      the tagged code.

**Exit criteria:** all falsification gates of `SIZE_VERIFICATION_METHODOLOGY.md`
Step 6 pass at full resolution; pipeline frozen and tagged.

---

## Phase 3 — Define Object X operationally and pre-register the hypotheses

*Objective: convert "Object X" from an annotation on a print into a falsifiable claim.
This phase deliberately contains **no** new measurements of Object X.*

- [ ] **P3.1** Publish the operational definition: product ID + pixel box
      (x₁,y₁)–(x₂,y₂) on PIA02405, plus the corresponding box on PIA02406, derived from
      the print coordinates (ruler x ≈ 60–63 in) in `preview (3).webp`.
- [ ] **P3.2** Record the two anchor interpretations and their consequences (from
      `VALIDATION_REPORT.md` §5.5): if at North Twin range (860 m), corrected size
      ≈ 9.1 m high × 32 m long; if in the near hummock field (tens of meters), ~20×
      smaller. State explicitly that the IMP image alone cannot decide between them.
- [ ] **P3.3** Pre-register the hypotheses with numeric tolerance bands, e.g.:
      **H0 (null):** Object X is a flood-debris hummock statistically indistinguishable
      (size, aspect ratio, relief) from the local hummock population.
      **H1 (sphinx-scale):** plan length 73 m ± 15 %, relief 20 m ± 25 %, with
      bilateral symmetry exceeding the population distribution.
      Any other hypothesis worth testing gets written here *now*, before Phase 4.
- [ ] **P3.4** Pre-register the discriminating measurements and thresholds: plan
      dimensions from the HiRISE map product; relief from DTM/stereo; a symmetry metric
      defined in advance (e.g., mirror-correlation score about the best-fit long axis);
      and the comparison population (≥30 hummocks in the same flood deposit, selected by
      a stated rule — e.g., all hummocks within 1.2 km of the lander above a stated
      area threshold — *before* any of them is measured).
- [ ] **P3.5** Commit P3.1–P3.4 as the pre-registration commit; nothing in it may be
      edited afterward except by an appending "amendments" section.

**Exit criteria:** a reader in Phase 4 can execute the test with no further judgment
calls — every threshold and selection rule already fixed.

---

## Phase 4 — The decisive orbital test

*Objective: measure Object X and its comparison population at ~25 cm/px, where
distance ambiguity does not exist, and grade the pre-registered hypotheses. This is the
experiment that settles the size question — the Cydonia protocol applied to this scene.*

- [ ] **P4.1** Register the IMP scene to the HiRISE map product: identify the lander
      (visible in PSP_001890_1995) and both Twin Peaks; solve the azimuth of each IMP
      image column from the lander position; verify the solution by predicting the
      azimuth separation of the two peaks and checking against the IMP frame (this is
      the registration's own known-answer test).
- [ ] **P4.2** Cast the sight line through Object X's pixel box (P3.1) from the lander
      position across the HiRISE frame; enumerate every candidate landform along that
      azimuth corridor from near field to beyond South Twin range. If more than one
      candidate exists, record all of them — do not pick the most interesting one.
- [ ] **P4.3** For each candidate: measure plan dimensions (pixels × 25 cm) and relief
      (DTM of PSP_002391_1995, or stereo-derived heights with a stated method) with
      error budgets.
- [ ] **P4.4** Measure the pre-registered comparison population (P3.4) with the same
      pipeline, blind to which hummock is Object X where feasible (e.g., have the
      measurement script process the population in randomized order with neutral IDs).
- [ ] **P4.5** Grade H0/H1 exactly as pre-registered. Record the verdict in a results
      document with the full data table, including the case where the answer is "Object
      X is a 9-meter hummock like its 30 neighbors."
- [ ] **P4.6** Close the loop on the IMP side: with Object X's true range now known,
      recompute its size from the IMP angular measurement (size = Z·N·IFOV) and check
      consistency with the orbital measurement — a final cross-instrument gate.

**Exit criteria:** every pre-registered hypothesis graded pass/fail with data; results
document committed regardless of outcome.

---

## Phase 5 — Near-field science that the lander data can legitimately support (parallel after Phase 1)

*Objective: use IMP stereo only inside its validity envelope (σ_Z ≤ 10 % → Z ≲ 75 m,
per `SIZE_VERIFICATION_METHODOLOGY.md` 3b), where it is genuinely science-grade.*

- [ ] **P5.1** From the native EDR frames (P1.2), build a rectified near-field stereo
      set; validate the disparity pipeline against a known geometry (the lander's own
      hardware visible in-frame, with dimensions from mission documentation).
- [ ] **P5.2** Range and measure near-field hummocks (< 75 m) with error budgets;
      compare relief statistics against the orbital population from P4.4 where coverage
      overlaps — a two-instrument consistency check on the *population*, not just on
      single objects.
- [ ] **P5.3** Reconcile results against Kirk et al. (1999)'s published DTM work as the
      external control; document agreement or disagreement quantitatively.

**Exit criteria:** a near-field size-frequency/relief dataset with two-instrument
consistency demonstrated, or a documented reason it can't be had.

---

## Phase 6 — Morphology and artificiality criteria, done right (parallel; concludes after Phase 4)

*Objective: replace adjective-based artificiality arguments with population
statistics under pre-registered metrics.*

- [ ] **P6.1** Rewrite `intelligence_vs_nature_morphology.md` into a set of computable
      discriminators (symmetry score, edge-angularity statistic, alignment with
      regional flow direction, departure from the hummock size–relief trend), each with
      a stated null distribution estimated from the P4.4 population.
- [ ] **P6.2** State the multiple-comparisons policy in advance (testing many
      discriminators on many hummocks will produce outliers by chance; define the
      correction — e.g., Bonferroni or FDR — before computing anything).
- [ ] **P6.3** Apply the discriminators to Object X and the full population; report
      effect sizes with confidence intervals, not verdicts.
- [ ] **P6.4** Fold `universal_morphology_cycles.md` and
      `mars_earth_orientation_analysis.md` into this framework or mark them as
      untestable-as-posed (a claim with no computable discriminator and no null
      distribution is outside the program's scope by rule).
- [ ] **P6.5** Whatever the outcome, write the comparison to the Cydonia case: same
      question, same protocol, and the resolution followed the higher-resolution data.

**Exit criteria:** no morphology claim in the repo lacks a metric, a null
distribution, and an uncertainty.

---

## Phase 7 — Write-up and external scrutiny

*Objective: expose the work to people incentivized to find its flaws.*

- [ ] **P7.1** Consolidate Phases 1–6 into a single methods-and-results manuscript;
      the honest framing is the methodological one ("recovering quantitative
      measurements from historical lander press products, validated against orbital
      data") — that framing is publishable *regardless* of what Object X turned out
      to be.
- [ ] **P7.2** Have the statistics of Phase 6 checked by someone who did not write them.
- [ ] **P7.3** Submit to review — a planetary-science venue or at minimum a public
      preprint with data and code archived (the repo's provenance discipline from P1
      makes this nearly free).
- [ ] **P7.4** Post-mortem document: what the original scale system got right (careful
      ruler work — `VALIDATION_REPORT.md` F5), what it got wrong (×1.84 model error,
      circular validation), and what procedural rule now prevents each failure. The
      failure analysis is a deliverable, not an embarrassment.

**Exit criteria:** manuscript + archived data/code exist; at least one round of
external feedback incorporated or rebutted in writing.

---

## Dependency summary

```
P0 (hygiene) ──────────────────────────────┐
P1 (data) ──► P2 (pipeline) ──► P3 (pre-reg) ──► P4 (orbital test) ──► P7 (write-up)
   │                                                   ▲
   ├──► P5 (near-field stereo) ────────────────────────┤  (population cross-checks)
   └──► P6 (morphology metrics) ───────────────────────┘  (needs P4.4 population)
```

The single most important ordering rule: **P3 (pre-registration) commits before P4
(measurement) begins.** Everything else can flex.
