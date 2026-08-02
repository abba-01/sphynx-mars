# Phase 5 Execution Plan - Near-field science within the lander stereo envelope

**Roadmap section:** `ROADMAP.md` Phase 5, tasks P5.1-P5.3.
**Depends on:** Phase 1 complete (EDR frames and documents, P1.2; papers, P1.4; all in
`data/PROVENANCE.md`); parallel with Phases 2-4 per the roadmap, except step S9, which
hard-blocks on the Phase 4 population dataset (P4.4). **Feeds:** Phases 4 and 6.
**Drafted:** 2026-08-02, by an AI agent (claude-fable-5) under the repository's standing rules.

## 1. Objective and scope

Use IMP stereo only where it is genuinely science-grade — inside the validity envelope of
`SIZE_VERIFICATION_METHODOLOGY.md` 3b (σ_Z ≤ 10 % → Z ≲ 75 m) — to produce a near-field
hummock size-frequency/relief dataset with error budgets, cross-checked against two external
controls: the Phase 4 orbital population (P4.4) and the published photogrammetric work of Kirk
et al. (1999, *JGR* 104(E4), doi:10.1029/1998JE900012). Exit criteria, quoted from the roadmap:

> "a near-field size-frequency/relief dataset with two-instrument consistency demonstrated, or
> a documented reason it can't be had."

In scope: P5.1 (rectified near-field stereo set from native EDR frames; disparity pipeline
validated against the lander's own in-frame hardware), P5.2 (range and measure near-field
hummocks < 75 m with error budgets; compare relief statistics against the orbital population
where coverage overlaps), P5.3 (quantitative reconciliation against Kirk et al. 1999). Out of
scope: any ranging of far-field features (`VALIDATION_REPORT.md` F2: at 860 m, σ_Z ≈ 115 % —
meaningless); any morphology/artificiality claim (Phase 6); any privileged treatment of Object
X. The repo's calibrated position stands: **Object X's size is indeterminate from the IMP image
alone** (F6). If a near-field landform in this phase's census lies on the Object X sight-line
corridor (P4.2), it is processed under a neutral randomized ID like every other hummock, and
identified only at collation, by the orchestrator, after measurement.

The envelope is derived, not assumed: d = f·B/Z = (1000 px × 0.15 m)/Z = 150/Z native px
(Smith et al. 1997: B = 15.0 cm; f = 1000 px per `VALIDATION_REPORT.md` §3), so
σ_Z/Z = σ_d/d = 0.2·Z/150 with σ_d ≈ 0.2 px; σ_Z/Z ≤ 10 % ⇔ Z ≤ 75 m. Signal available:
15 px disparity at 10 m, 5 px at 30 m, 2 px at 75 m.

## 2. Inputs and preconditions

- **Network access:** no analysis step requires it. Exactly three contingencies touch the
  network, each executed in a normal-egress session outside the analysis sandbox (which
  blocks the NASA/UA hosts, `VALIDATION_REPORT.md` §2): (i) return-to-Phase-1 if an input is
  missing or fails checksum; (ii) the live-page source-verification agent (Q1, §5), continuing
  the P1.5 practice; (iii) retrieval of any mission-documentation item (hardware dimensions)
  or Kirk et al. supporting material not already captured under P1.2/P1.4.
- Required inputs, each in `data/PROVENANCE.md` with SHA-256: native IMP EDR frames from
  `MPFL-M-IMP-2-EDR-V1.0` (P1.2), both eyes, 256×256 px, 0.98 mrad/px, with PDS labels,
  covering near-field terrain and views containing lander hardware (frame IDs: [recorded in
  `data/PROVENANCE.md` during Phase 1 - do not cite until verified]); *The Imager for Mars
  Pathfinder User's Guide* from the dataset's `document/` directory (P1.2) — expected source
  for pointing-metadata conventions and lander hardware dimensions, the dimensions themselves
  [source to be located and verified during execution - do not cite until verified], with S4
  blocked until a verified value exists; Smith et al. (1997) and Kirk et al. (1999) full texts
  (P1.4).
- Constants fixed by source: baseline 15.0 cm, FOV 14.4°×14.0°, 0.98 mrad/px, f/18 (Smith et
  al. 1997, doi:10.1029/96JE03568); camera height 1.5 m nominal ("The imager rests on a pop-up
  mast 80 cm above the lander and 1.5 m above the surface," NASA/JPL Mars Pathfinder Instrument
  Descriptions), 1.75-1.85 m as-deployed per `VALIDATION_REPORT.md` §3 — the h uncertainty is
  carried in every ground-plane cross-check.
- Soft dependency: if the `pipeline-v1` tag (P2.5) exists, reuse its constants module and
  EDR-handling routines; if Phase 2 has not concluded, Phase 5 may still start (roadmap
  permits it), taking the constants verbatim from the source register. Hard gate on S9 only:
  the P4.4 neutral-ID population dataset; all other steps proceed without Phase 4.
- Tooling: Python 3 with numpy and Pillow; `sha256sum`; `git`. New dependencies (e.g., a PDS
  label reader) are recorded in a commit note before first use.

## 3. Research protocol

Numbered SOP. "Record" means: append to `analysis/phase5/RUN_LOG.md` with UTC date-time, code
commit hash, input SHA-256s, and agent ID.

- **S1 - Provenance audit** (precondition to all tasks). Recompute SHA-256 for every §2 input
  against `data/PROVENANCE.md`. Any mismatch: stop, record, return to Phase 1. No waivers.
- **S2 - Frame inventory** (**P5.1**). From the PDS labels, tabulate per frame: ID, eye,
  filter, azimuth/elevation pointing, exposure metadata ([exact label keywords to be verified
  during execution against the User's Guide]) into a machine-readable catalog; select all
  left/right pairs whose pointing overlaps below the horizon. No pixel measurement in S2.
- **S3 - Rectification build** (**P5.1**). Implement epipolar rectification of the selected
  pairs from label pointing and the 15.0 cm baseline; emit per pair the rectified images,
  transform parameters, and a residual-vertical-parallax statistic. Acceptance, fixed now:
  median residual vertical parallax ≤ 0.5 px; failing pairs are excluded with the failure
  recorded, never hand-fixed per object.
- **S4 - Known-answer validation on lander hardware** (**P5.1**). The disparity pipeline is
  trusted on terrain only after reproducing a documented geometry: (a) orchestrator selects
  ≥ 2 hardware elements visible in rectified pairs with documented dimensions ([located and
  verified during execution]); (b) two blind validators — only after the S5 pre-registration
  commit exists, its hash recorded in `RUN_LOG.md` — independently measure disparity and
  pixel extent, reporting **pixels only**, never shown the documented values; (c) orchestrator
  converts (Z = fB/d; size = Z·N·IFOV) and grades against the S5(1) band. Hardware sits at a
  few meters, where σ_Z/Z ≈ 0.2·Z/150 is sub-1 % — failure here is a pipeline defect, full stop.
- **S5 - Pre-registration commit** (**P5.2, P5.3**). Before K1/K2 collect any pixels and
  before any terrain disparity is measured, commit `analysis/phase5/PREREGISTRATION.md`
  containing:
  1. The S4 hardware pass band: each recovered dimension within its propagated 95 % error
     budget of the documented value, hard cap ±10 %. This item — at minimum — must be
     committed, with its hash recorded in `RUN_LOG.md`, before K1/K2 collect any pixels;
     no S4 pixel collection precedes it.
  2. The census **selection rule**: all discrete positive-relief landforms in the rectified
     set with coarse range ≤ 75 m and apparent area ≥ (2 native px)² at the landform's
     coarse range — instantiating the `SIZE_VERIFICATION_METHODOLOGY.md` Step 1 resolution
     floor (no credible detail finer than 2 native px), not a new threshold — enumerated
     exhaustively; no discretionary inclusion or exclusion afterward.
  3. Duplicate tolerance: the two blind measurers must agree within ±0.5 px disparity (2.5×
     the assumed σ_d = 0.2 px, allowing independent tie-point choice) and ±2 px extent.
  4. Envelope rule as exclusion: any landform whose *measured* Z gives σ_Z/Z > 10 % moves to
     a quarantine table — reported, outside the science set, automatically, no appeal.
  5. The two-instrument comparison (**S9**): the named two-sample test (e.g.,
     Kolmogorov-Smirnov on overlap-population relief distributions), its α, and the
     definition of "overlap population" (landforms identifiable in both the IMP science set
     and the P4.4 orbital set). One test; no test shopping.
  6. Kirk reconciliation targets (**S10**): which published quantities will be compared
     ([specific values to be located in the retrieved paper and verified during execution -
     do not cite until verified]) and the criterion: consistency within the quadrature sum
     of published and Phase 5 uncertainties.
  This commit is the **barrier** (§5): its hash must precede every terrain-measurement commit.
- **S6 - Near-field census** (**P5.2**). A single census agent runs a coarse disparity pass,
  applies S5(2) mechanically, and commits the frozen sample frame: neutral randomized IDs
  (H01, H02, ...), pixel boxes per eye, coarse Z. The ID↔location key is held by the
  orchestrator and withheld from all measurers.
- **S7 - Blind duplicate measurement** (**P5.2**). Two blind measurers independently process
  the census in independently randomized order: refined disparity (stated matching window),
  apparent pixel extents (length; height above local base), per-measurement σ_d. Pixels only;
  no meters, no ID key, no sibling access, no census coarse values beyond the boxes.
- **S8 - Conversion, error budgets, relief statistics** (**P5.2**). Orchestrator converts
  (Z = fB/d, σ_Z = Z²σ_d/(fB), size = Z·N·IFOV); every landform gets a Step 5-style error
  budget (pixel-count, σ_d, IFOV 2 % systematic, rectification residual). Ground-plane
  cross-check (Methodology 3c) below ~50 m: stereo Z vs Z = h/tanθ, h = 1.5-1.85 m as the
  uncertainty band; discrepancies beyond combined errors are flagged, not adjusted.
  Resolution floor per landform: 2 native px = 2·Z·0.98 mrad (2.0 cm at 10 m, 14.7 cm at
  75 m); no morphological claim finer. Output: the size-frequency/relief table.
- **S9 - Two-instrument population comparison** (**P5.2**; blocks on P4.4). Orchestrator
  identifies the overlap population per S5(5) — noting overlap members must span several
  HiRISE pixels (25 cm/px map product, per the register) — runs the pre-registered test
  exactly once, and records statistic, p-value, verdict. Agreement and disagreement are
  equally publishable.
- **S10 - Kirk et al. reconciliation** (**P5.3**). A reconciliation analyst extracts the
  S5(6) quantities from the retrieved Kirk et al. (1999) text, quoting verbatim with page
  reference, and compares per the pre-registered criterion in
  `analysis/phase5/KIRK_RECONCILIATION.md`. A disagreement is a finding about this pipeline,
  not about Kirk et al., until adversarial review says otherwise.
- **S11 - Gate ledger**. Record pass/fail with numbers in `analysis/phase5/GATE_LEDGER.md`
  (Step 6 gates, adapted): (1) known-answer = S4 band; (2) duplicate-measurer tolerance S5(3)
  (cross-eye is intrinsic to stereo matching here); (3) ratio — aspect ratios independent of
  Z by construction, verified on a sample; (4) resolution — no claim finer than 2 native px
  at measured Z; (5) provenance — S1 passed, no window crosses a frame seam, resampling chain
  enumerated (native EDR → rectified grid is the only permitted resampling).
- **S12 - Adversarial review and sign-off**. Adversarial verifiers and auditors (§5) attack
  the ledger and dataset; the repository owner reviews and signs off in a committed note.
  **S13 - Freeze and tag**. On sign-off: tag `nearfield-v1`; Phase 6 consumes the dataset
  only via the tag.

## 4. Academic-integrity protocol

- **Provenance and checksums.** S1 verifies every input before work; V1 re-verifies after S11.
  Every run-log line carries input SHA-256s and the code commit. No analysis touches a file
  absent from `data/PROVENANCE.md`.
- **Verbatim quotation.** All quoted language comes from the `VALIDATION_REPORT.md` §8
  register and `SIZE_VERIFICATION_METHODOLOGY.md` Sources, with URL and access date carried
  from the P1.5 live-page audit. No new sources from memory: hardware dimensions and Kirk et
  al. values enter the record only after Q1 verification of retrieved documents, quoted
  verbatim with location; until then the slot carries the verification placeholder.
- **Pre-registration discipline.** The S5 commit precedes every terrain-measurement commit;
  git history is the timestamp. `PREREGISTRATION.md` is append-only — amendments go in a dated
  "Amendments" section and never alter original tolerances, the selection rule, or the test.
- **Blinding and confirmation-bias controls.** Measurers see neutral IDs in randomized order
  and report pixels only; the orchestrator holds the ID key and applies all conversions, so
  no measurer can steer toward an expected size, the Kirk et al. values, or an Object X
  candidate. S4 validators never see documented hardware dimensions. Blinding is verified by
  transcript audit (A-role): a transcript that reads sibling outputs, the ID key,
  `VALIDATION_REPORT.md` §5 numbers, or the Kirk et al. paper voids that measurement.
- **AI-assistance disclosure.** Every document and commit states it was generated by AI
  agents (claude-fable-5) under human direction, per the practice adopted after F8. No AI
  output is represented as human measurement.
- **Error-correction and retraction.** Errors found after `nearfield-v1` are fixed by
  appended notes and a `nearfield-v1.1` tag; history is never rewritten. If Phase 5 results
  contradict `VALIDATION_REPORT.md` or the methodology, the affected document gains an
  appended correction block citing the Phase 5 commit.
- **Null results.** If the dataset cannot be produced, the roadmap's alternative exit ("a
  documented reason it can't be had") is written with the same care as a success: what was
  tried, what failed, with numbers, committed and left visible.

## 5. Agent fan-out design

Executed with Claude Code Workflow orchestration (`agent()` / `parallel()` / `pipeline()`);
all agents inherit the session model, claude-fable-5.

| Role | ID(s) | Count | Independence / blinding arrangement |
|---|---|---|---|
| Geometry engineer | E1 | 1 | Builds S2 catalog + S3 rectification; judged only by the parallax statistic and S4 outcome; forbidden from measuring terrain |
| Hardware validators | K1, K2 | 2 | Blind duplicates on lander hardware (S4); pixels only; never shown documented dimensions; no access to each other |
| Census agent | N1 | 1 | Applies S5(2) mechanically (S6); emits neutral IDs; never performs fine measurement |
| Blind terrain measurers | M1, M2 | 2 | Independent fine measurement of the full census in independently randomized order (S7); no sibling access, no ID key, no meters |
| Statistics checker | T1 | 1 | Re-derives all S8 conversions, error budgets, and the S9 test from raw JSON only; sees no compiled tables first |
| Adversarial verifiers | A1-A3 | 3 | Prompted to REFUTE: attack rectification residuals, tie-point tuning, envelope leakage (Z > 75 m in the science set), blinding violations (transcript audit), selection-rule drift between S5 and S6; each works alone |
| Kirk reconciliation analyst | R1 | 1 | Extracts published values with verbatim quotes + page refs (S10); works after S8 is frozen; cannot alter any Phase 5 number |
| Source-verification agent | Q1 | 1 | Networked session only: checks every quote and constant in Phase 5 documents against live pages / retrieved PDFs; flags drift; may not edit analysis outputs |
| Provenance auditor | V1 | 1 | Runs S1 before work; re-verifies all checksums after S11 |

**Orchestration pattern.**

```
pipeline(
  V1(S1) -> E1(S2, S3)
  -> orchestrator(S5 pre-registration commit; hash recorded in RUN_LOG.md)
  == BARRIER ==                                  # the one genuine barrier
  parallel(K1, K2)(S4 pixel collection) -> orchestrator(S4 conversion + grading)
  -> N1(S6 census, committed) -> parallel(M1, M2)   # terrain fan-out
  -> orchestrator(S8; S9 when P4.4 exists)
  -> parallel(A1, A2, A3, T1, R1, Q1, V1-recheck)
  -> human checkpoint (owner sign-off, S12) -> S13 tag
)
```

The single genuinely required barrier sits between the S5 pre-registration commit and all
pixel collection — hardware and terrain alike: a pass band, selection rule, or tolerance
written after pixels have been seen is not a pre-registration. The S5 commit — at minimum
the hardware pass band S5(1) — must exist, with its hash recorded in `RUN_LOG.md`, before
K1/K2 collect any pixels. S9 waits on P4.4, but that is an external dependency, not an
internal barrier.

**Structured-output contracts (JSON).**

- E1: `{"agent_id", "code_commit", "pairs": [{"pair_id", "left_frame", "right_frame", "left_sha256", "right_sha256", "transform_params", "median_vertical_parallax_px", "accepted": bool}]}`.
- K1-K2 / M1-M2: `{"agent_id", "pair_id", "target_id", "disparity_px", "sigma_d_px", "extent_px": {"length": n, "height": n, "sigma": s}, "matching_window", "tie_points": [[x,y],...], "anomalies"}` — pixel units only.
- N1: `{"agent_id", "rule_commit", "landforms": [{"neutral_id", "pair_id", "box_left": [x1,y1,x2,y2], "box_right": [...], "coarse_Z_m", "angular_area"}], "excluded_count", "exclusion_reasons": [...]}`.
- T1: `{"agent_id", "recomputed_Z_m": {...}, "recomputed_sizes_m": {...}, "recomputed_sigmas": {...}, "s9_statistic", "s9_p_value", "line_item_discrepancies": [...], "pass": bool}`.
- A1-A3: `{"agent_id", "verdict": "REFUTED|NOT_REFUTED", "attack_vector", "reproduction_cmd", "evidence", "gate_attacked"}`.
- R1: `{"agent_id", "quantities": [{"name", "published_value", "verbatim_quote", "page_ref", "phase5_value", "combined_sigma", "consistent": bool}]}`.
- Q1, V1: `{"agent_id", "items_checked": N, "failures": [{"item", "expected", "found"}], "pass": bool}`.

**Acceptance thresholds.**

- Hardware known-answer: every element within the 95 % propagated band and the ±10 % hard cap
  (S5(1)); any failure is a pipeline defect — no terrain measurement until fixed and re-run.
- Duplicates: within ±0.5 px disparity and ±2 px extent (S5(3)); on disagreement a third blind
  measurer runs that landform, used only if the three-way spread then meets tolerance —
  otherwise the landform is recorded as measurement-failed, not averaged.
- Envelope: automatic quarantine of any landform with measured σ_Z/Z > 10 %; A1-A3 audit for
  leakage. S9: graded exactly as pre-registered; the verdict is recorded whichever way it
  falls. S10: consistency within quadrature-summed uncertainties (S5(6)); inconsistency is
  reported quantitatively and escalated to the owner, never tuned away.
- Adversarial: one verified refutation (reproduction command confirmed by the orchestrator)
  kills the affected gate; a 2-of-3 unreproduced-concern majority escalates to the owner.
- Statistics: T1 must reproduce all conversions within rounding (±0.1 m in Z and size); any
  discrepancy blocks S12 until resolved in writing.

**Human-in-the-loop checkpoints.** (1) The owner approves `PREREGISTRATION.md` before the
barrier lifts — selection rule, tolerances, and the named test are the owner's commitments.
(2) The owner reviews the gate ledger, adversarial reports, and S9/S10 outcomes before the
`nearfield-v1` tag. (3) Any hardware-gate failure disposition (fix-and-rerun vs alternative
exit) is the owner's call, committed as a signed note. (4) On S9/S10 disagreement the recorded verdict closes gate 5 and is disclosed as the
Phase 5 result regardless (per §6 gate 5 and §7); the owner's choice concerns only
whether to *additionally* open a defect investigation under a new pre-registration on
new data — never a re-run against the same data. (5) A human
spot-check of a randomized sample of duplicate outputs (K1/K2, M1/M2) before the
`nearfield-v1` tag (correlated-error limitation, below).

**Correlated-error limitation (standing).** All duplicate agents in this design are
instances of the same model (claude-fable-5). Procedural isolation prevents information
leakage between them but not shared model-systematic priors: duplicate agreement therefore
bounds procedural/transcription error only, not model-systematic error. Where the protocol
supports it, duplicates must take methodologically distinct routes — here, K1/K2 and M1/M2
choose tie points independently and each states its own matching window (S5(3), S7). A
human spot-check of a randomized sample of duplicate outputs is a standing checkpoint
before phase close.

## 6. Quality gates and exit criteria

Measurable statements of the roadmap's exit criteria:

1. Known-answer gate: ≥ 2 lander hardware elements recovered within the S5(1) band by both
   validators. [P5.1]
2. Rectification quality: every science-set pair has median residual vertical parallax
   ≤ 0.5 px, recorded per pair. [P5.1]
3. Dataset completeness: every census landform is in the science table with a full error
   budget (every term filled — a measurement without an uncertainty is not finished) or in
   the quarantine/failed tables with a stated reason; census rule applied with zero
   discretionary exceptions (A-audit confirms S6 matches S5(2)). [P5.2]
4. Envelope integrity: zero science-set entries with σ_Z/Z > 10 %. [P5.2]
5. Two-instrument consistency: the S9 pre-registered test executed exactly once on the
   overlap population with its verdict recorded closes this item either way. A pass
   demonstrates consistency; a recorded, quantified disagreement satisfies the roadmap's
   alternative exit ("a documented reason it can't be had"), and `nearfield-v1` may issue
   with the disagreement disclosed as the Phase 5 result. If P4.4 coverage yields no
   overlap population, that fact is documented as the alternative exit for this item. [P5.2]
6. External control: the S10 table complete for every S5(6) quantity, each row marked
   consistent/inconsistent with numbers. [P5.3]
7. Tag `nearfield-v1` exists, pointing at a commit where items 1-6 are true, with owner
   sign-off committed.

## 7. Failure modes and stopping rules

Failed hypotheses are recorded as failed, never rescued post hoc. Specifically:

- **Hardware known-answer failure** (S4): hard stop on terrain work. One diagnosis-and-refix
  cycle is permitted under a dated pre-registration amendment; a second failure declares the
  phase failed ("known-answer test first" is a standing rule).
- **Rectification failure** across the frame set: the phase concludes via the alternative
  exit with the residuals published; the criterion is not loosened to admit pairs.
- **Duplicate disagreement** beyond the third-measurer rule: that landform is recorded as
  failed; systematic disagreement across > 20 % of the census is a pipeline defect and stops
  the phase for diagnosis under a new pre-registration.
- **Checksum mismatch or missing input** (S1/V1): hard stop; return to Phase 1 — no
  improvised downloads from the analysis environment. **Missing hardware dimensions** after a
  networked search: the phase halts at S3 with the blocker documented — no substitute
  known-answer is invented.
- **S9 or S10 disagreement**: not a phase failure — a result, published as found (checkpoint
  4). Per §6 gate 5, the S9 test executed exactly once with its verdict recorded closes
  that item either way: a recorded, quantified disagreement does not block the
  `nearfield-v1` tag, which may issue with the disagreement disclosed as the Phase 5
  result. Forbidden: re-measuring, re-selecting, or re-testing until agreement appears.
- **Verified adversarial refutation**: the affected gate reverts to failed; measurements
  downstream of the defect are void and re-run from the earliest affected step at a new commit.
- **Phase failure** is declared if, after one diagnosis-and-refix cycle, gate 1 or 2 of §6
  still fails: `nearfield-v1` is not created, Phase 6 does not consume near-field data, and
  the failure write-up is committed with the same care as a success (standing rule; Cydonia
  precedent, `VALIDATION_REPORT.md` §7).

## 8. Deliverables

All under `analysis/phase5/`:

- `frame_catalog.json` - S2 inventory (P5.1); `rectify_nearfield.py` + rectified products and
  transform records (P5.1).
- `PREREGISTRATION.md` - tolerances, selection rule, named test (barrier commit).
- `HARDWARE_VALIDATION.md` - S4 known-answer results with error budgets (P5.1).
- `census.json` - frozen neutral-ID sample frame (P5.2); `measurements/*.json` - raw
  validator, measurer, checker, auditor outputs.
- `NEARFIELD_DATASET.md` + machine-readable table - size-frequency/relief dataset with
  per-landform error budgets, quarantine and failed tables (P5.2).
- `TWO_INSTRUMENT_COMPARISON.md` - S9 test, statistic, verdict (P5.2);
  `KIRK_RECONCILIATION.md` - S10 table, verbatim quotes, page refs (P5.3).
- `GATE_LEDGER.md` - gates with numbers, adversarial reports, owner sign-off; `RUN_LOG.md` -
  every run: UTC time, commit, input SHA-256s, agent ID.
- Commits referencing task IDs (P5.x): provenance audit (S1); geometry/rectification (S2-S3);
  pre-registration (S5); census (S6); measurement (S7-S8); comparisons (S9-S10); ledger (S11);
  sign-off (S12). Tag: `nearfield-v1` - created only on full gate passage plus owner
  sign-off; Phase 6 references the tag.
