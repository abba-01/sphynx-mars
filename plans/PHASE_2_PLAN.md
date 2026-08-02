# Phase 2 Execution Plan - Pipeline Re-verification at Full Resolution

**Roadmap section:** `ROADMAP.md` Phase 2, tasks P2.1-P2.5.
**Depends on:** Phase 1 complete (`data/PROVENANCE.md` populated and committed); **feeds:** Phases
3-6, which must use the tagged pipeline (`pipeline-v1`) and may cite no file absent from
`data/PROVENANCE.md`.
**Drafted:** 2026-08-02, by an AI agent (claude-fable-5) under the repository's standing rules.

## 1. Objective and scope

Confirm that the preview-based results of `VALIDATION_REPORT.md` (F5 in particular) hold on the
full-resolution archive products acquired in Phase 1, quantify the interpolation floor of the
500 %-enlarged Photojournal products as a measurement rather than an argument, and freeze a single
trusted code path. Exit criteria, quoted from the roadmap:

> "all falsification gates of `SIZE_VERIFICATION_METHODOLOGY.md` Step 6 pass at full resolution;
> pipeline frozen and tagged."

In scope: P2.1 (parameterize `analysis/measure_twin_peaks.py`; one code path for preview and
full-res runs), P2.2 (known-answer gate with full error budget per Step 5), P2.3 (cross-eye gate on
PIA02406), P2.4 (empirical interpolation floor: native EDR frame vs the corresponding region of the
500 %-enlarged product), P2.5 (tag `pipeline-v1`). Out of scope: any measurement of Object X, any
morphology claim, any new hypothesis. The repo's calibrated position stands unchanged throughout
this phase: Object X's size is indeterminate from the IMP image alone (`VALIDATION_REPORT.md` F6);
Phase 2 measures only the Twin Peaks (the known-answer objects) and the instrument products
themselves.

## 2. Inputs and preconditions

- **No step in this phase requires network access.** All inputs are local files acquired in
  Phase 1. The single network-touching contingency: if a required file is missing or fails its
  checksum, execution *returns to Phase 1* (which requires normal egress; the analysis sandbox
  blocks the NASA/UA hosts per `VALIDATION_REPORT.md` §2) rather than improvising a download here.
- Required inputs, each present in `data/PROVENANCE.md` with SHA-256:
  - `PIA02405.tif` (catalog-stated 65.93 MB, 7238x3135 px) and `PIA02406.tif` (7296x3135 px) - P1.1.
  - The native IMP EDR frames of the Twin Peaks super-resolution sequence (256x256 px per eye,
    0.98 mrad/px; 8 frames left eye, 7 right, per the catalog pages) with PDS labels, plus *The
    Imager for Mars Pathfinder User's Guide* - P1.2. Specific frame IDs:
    [recorded in `data/PROVENANCE.md` during Phase 1 execution - do not cite until verified].
- Repository at a head containing `analysis/measure_twin_peaks.py`, `VALIDATION_REPORT.md`,
  `SIZE_VERIFICATION_METHODOLOGY.md`, and the four `preview*.webp` files (used in this phase only
  as regression references for the refactor, never as measurement surfaces).
- Tooling: Python 3 with numpy and Pillow (already required by the script), `sha256sum`, `git`.
  An FFT is available via numpy; no new dependencies without a commit noting them.
- Constants fixed by source, not re-derivable during execution: IFOV 0.98 mrad/native px (Smith et
  al. 1997, doi:10.1029/96JE03568); enlargement factor 5 ("enlarged by 500% and then co-added using
  Adobe Photoshop", PIA02405/06 catalog pages) so 1 product px = 0.196 mrad; caption distances
  860 m (North Twin) and ~1006 m (3300 ft, South Twin); caption heights "approximately 30-35
  meters (~100 feet)".

## 3. Research protocol

Numbered SOP. Every step names its roadmap task ID. "Record" means: append to
`analysis/phase2/RUN_LOG.md` with UTC date-time, code commit hash, input SHA-256s, and agent ID.

- **S1 - Provenance audit** (precondition to all of P2.1-P2.5; Step 6 gate 5). Recompute SHA-256
  for every input listed in §2 and compare against `data/PROVENANCE.md`. Any mismatch: stop the
  phase, record the mismatch, return to Phase 1. No waivers.
- **S2 - Parameterize the script** (**P2.1**). Refactor `analysis/measure_twin_peaks.py` so that
  one code path serves both preview and full-res runs. Required interface: `--image PATH`,
  `--catalog-width W --catalog-height H` (per-product, from the catalog pages: 7238x3135 left,
  7296x3135 right), `--enlargement 5`, `--windows FILE` (a JSON file giving apex-search column
  ranges and base-median column ranges, so window choices are data, not code), `--out DIR`. The
  script must emit machine-readable JSON (fields in §5) alongside its human-readable printout and
  overlay image. **Refactor known-answer test:** the refactored script, run on `preview.webp` with
  windows transcribing the current hard-coded values, must reproduce the numbers recorded in
  `VALIDATION_REPORT.md` §5.4 (apparent extents; lower-bound heights ≥26.5 m North, ≥22.7 m South)
  to printed precision. A refactor that changes any preview number is a defect, not a discovery.
- **S3 - Pre-registration commit** (**P2.2-P2.4**; standing rule "pre-register before you look").
  Before any agent opens a full-resolution TIFF, commit `analysis/phase2/PREREGISTRATION.md`
  containing, with numeric tolerances:
  1. Expected full-res angular extents, computed from the S2 regression run's preview extents times
     the per-eye preview-to-product scale (left: 7238/1568 = 4.616; right: 7296/1568 = 4.653;
     catalog dims and preview width per `VALIDATION_REPORT.md` §2). Worked example, North Twin:
     34 ± 2 preview px (Step 5 error budget) x 4.616 ≈ 157 ± 9 product px.
  2. Duplicate-measurement tolerance: two blind measurers' extents on the same eye must agree
     within ±10 product px (= ±2 preview-px equivalents, 2 x 4.616 = 9.2, rounded up).
  3. Known-answer band (**P2.2**): corrected heights must land "within (or explainably below,
     given base occlusion)" NASA's 30-35 m (roadmap P2.2). Operationally: with measured height m
     and pixel-count uncertainty σ, the interval [m − σ, (m + σ) x 1.30] must intersect
     [30 m, 35 m] (the +30 % term is the one-sided occlusion allowance of Step 5), and m − σ must
     not exceed 35 m. Occlusion, if invoked, must be documented with the occluding ridge's pixel
     rows.
  4. Cross-eye tolerance (**P2.3**): left/right angular extents must agree within the quadrature
     sum of the two per-eye pixel-count uncertainties (framing offsets between the independently
     assembled mosaics do not affect angular extents - Step 6 gate 2).
  5. Interpolation-floor prediction (**P2.4**): the Photoshop co-add adds no real information above
     the native Nyquist frequency (0.5 cycles/native px); the previews already carry "nearly all
     the real information in the products" (`VALIDATION_REPORT.md` §2). Stated as falsifiable: if
     the product region shows coherent power above native Nyquist that is *also present* in the
     independently aligned native frame, the prediction survives; excess power absent from the
     native frame is interpolation/co-add artifact; power present in the native frame but absent
     from the preview would falsify the "previews suffice" claim and must be reported as such.
  This commit is the **barrier** (§5): its hash must precede every measurement commit.
- **S4 - Full-res left-eye measurement** (**P2.1, P2.2**). Two blind measurers (§5) each
  independently choose windows and run the frozen S2 code on `PIA02405.tif`, reporting pixel
  quantities only. The orchestrator converts to angles and meters after collection.
- **S5 - Full-res right-eye measurement** (**P2.3**). Same protocol on `PIA02406.tif` with two
  further blind measurers. The orchestrator computes the cross-eye comparison against tolerance
  §3.S3(4).
- **S6 - Error budget** (**P2.2**). Compile the full Step 5 table for both peaks at full
  resolution: pixel count ± uncertainty, IFOV systematic (0.98 vs 1.00 mrad/px, 2 %),
  product/preview scale term (now retired - full-res is the measurement surface), caption range
  term (±5 % assumption, stated as such), one-sided base-occlusion term. An independent statistics
  checker re-derives every line from the raw JSON.
- **S7 - Interpolation floor** (**P2.4**). Two analysts, working independently with no shared
  code: (a) align one native EDR frame (from P1.2) to its region of `PIA02405.tif` by
  cross-correlation of the 5x-upsampled native frame (bicubic and nearest-neighbour upsampling
  both run, as bracketing cases; alignment accepted when the correlation peak is unambiguous);
  (b) compute radially averaged power spectra of the product region, the upsampled native frame,
  and the corresponding preview region; (c) report the spatial frequency (cycles/native px) above
  which the product's power is not corroborated by the native frame, and any seam or co-add
  artifacts found by difference imaging. This converts the Step 1 "resolution floor rule" (~2
  native px; ≈1.7 m at 860 m) into a measured curve.
- **S8 - Falsification-gate ledger** (**P2.2-P2.4**). Run all five Step 6 gates at full resolution
  and record pass/fail with numbers in `analysis/phase2/GATE_LEDGER.md`: (1) known-answer
  (§3.S3(3)); (2) cross-eye (§3.S3(4)); (3) ratio - the North/South extent ratio at full res must
  match the preview-derived ratio within propagated pixel uncertainties, and no conclusion may
  depend on a privileged range; (4) resolution - no claim finer than 2 native px (= 10 product px);
  (5) provenance - S1 passed, no measurement window crosses a seam or artifact identified in S7,
  and every resampling step between detector and measurement surface is listed.
- **S9 - Adversarial review and sign-off** (all tasks). Adversarial verifiers and auditors (§5)
  attack the ledger. The repository owner reviews the ledger, the adversarial reports, and the
  pre-registration diff, and signs off (or does not) in a committed note.
- **S10 - Freeze and tag** (**P2.5**). On sign-off: commit the final state and tag `pipeline-v1`.
  Later phases must check out or reference the tag; running un-tagged pipeline code in Phases 3-6
  is a protocol violation.

## 4. Academic-integrity protocol

- **Provenance and checksums.** Every run records input SHA-256s; S1 verifies them against
  `data/PROVENANCE.md` before measurement and V1 (§5) re-verifies after S8, so no silent file
  substitution can occur mid-phase. No analysis touches a file absent from the provenance log.
- **Verbatim quotation.** All quoted language in Phase 2 documents comes from the source register
  of `VALIDATION_REPORT.md` §8 / `SIZE_VERIFICATION_METHODOLOGY.md` Sources, with URL and access
  date carried from Phase 1's live-page audit (P1.5). Phase 2 introduces **no new sources**; any
  step found to need one records
  "[source to be located and verified during execution - do not cite until verified]" and the need
  is queued for a networked session, never satisfied from memory.
- **Pre-registration discipline.** The S3 commit precedes every measurement commit; git history is
  the timestamp. `PREREGISTRATION.md` is append-only after S3 - amendments go in a dated
  "Amendments" section and never alter the original tolerances.
- **Blinding and confirmation-bias controls.** Measurers work blind to each other (no access to
  sibling outputs), report pixels rather than meters (the orchestrator applies the conversion, so
  no measurer can steer toward 30-35 m), and are prompted with the image path and interface
  contract only - not with the target band. Blinding is procedural (prompt-level) and is verified
  afterward by transcript audit: an adversarial verifier checks each measurer transcript for reads
  of `VALIDATION_REPORT.md` §5 or of sibling outputs; a violated blind voids that measurement.
- **AI-assistance disclosure.** Every document and commit produced in this phase states that it was
  generated by AI agents (claude-fable-5) under human direction, continuing the disclosure practice
  the repo adopted after the F8 finding (`VALIDATION_REPORT.md` §6). No AI output is represented
  as human measurement.
- **Error-correction and retraction.** Errors found after the `pipeline-v1` tag are fixed by
  appending a correction note and tagging `pipeline-v1.1` (etc.); history is never rewritten. If a
  full-res result contradicts a preview-based statement in `VALIDATION_REPORT.md`, the report gains
  an appended correction block citing the Phase 2 commit - the expectation recorded there ("no
  conclusion below is expected to change") is itself a falsifiable claim and is treated as one.
- **Null results.** If the gates fail, the failure is written up in `GATE_LEDGER.md` with the same
  completeness a pass would have received, committed, and left visible. A failed Phase 2 is a
  result, not an obstacle.

## 5. Agent fan-out design

Executed with Claude Code Workflow orchestration (`agent()` / `parallel()` / `pipeline()`); all
agents inherit the session model, claude-fable-5.

| Role | ID(s) | Count | Independence / blinding arrangement |
|---|---|---|---|
| Pipeline engineer | E1 | 1 | Refactors code (S2); forbidden from opening any full-res TIFF; work judged only by the preview regression test |
| Blind measurers, left eye | M1, M2 | 2 | Each independently chooses windows and runs the frozen code on PIA02405.tif; no access to sibling output, to VALIDATION_REPORT §5 numbers, or to meters (pixels only) |
| Blind measurers, right eye | M3, M4 | 2 | As M1/M2 on PIA02406.tif; additionally blind to all left-eye outputs |
| Interpolation analysts | I1, I2 | 2 | Independent implementations of S7; no shared code; blind to each other's cutoff estimate until both JSONs are collected |
| Statistics checker | T1 | 1 | Re-derives the S6 error budget from raw measurer JSON only; does not see the compiled table first |
| Adversarial verifiers | A1-A3 | 3 | Prompted to REFUTE the gate ledger: hunt window tuning, code-path divergence between preview/full-res modes, arithmetic errors, blinding violations (transcript audit), checksum drift; each works alone |
| Constants/source auditor | C1 | 1 | Checks every numeric constant in code and Phase 2 documents against the §8 register and in-repo catalog PDFs; flags any number with no source and any citation not already in the register |
| Provenance auditor | V1 | 1 | Runs S1 before measurement and re-verifies all checksums after S8 |

**Correlated-error limitation.** All duplicate agents (M1/M2, M3/M4, I1/I2) are instances of the
same model, claude-fable-5. Procedural isolation prevents information leakage between them but not
shared model-systematic priors: two instances can make the same mistake for the same internal
reason. Duplicate agreement therefore bounds procedural/transcription error only, not
model-systematic error. Where the protocol supports it, duplicates must take methodologically
distinct routes, named in the relevant step - here, M1/M2 and M3/M4 each independently choose
measurement windows (S4, S5), and I1/I2 produce independent implementations of S7 with no shared
code (§3.S7). A human spot-check of a randomized sample of duplicate outputs is a standing
checkpoint before phase close, folded into the owner's S9 review.

**Orchestration pattern.**

```
pipeline(
  V1(S1) -> E1(S2) -> orchestrator(S3 pre-registration commit)   # sequential head
  == BARRIER ==                                                   # the one genuine barrier
  parallel( M1, M2, M3, M4, I1, I2 )                              # measurement fan-out
  -> orchestrator collates JSON, applies conversions, drafts S6/S8
  parallel( A1, A2, A3, T1, C1, V1-recheck )                      # verification fan-out
  -> human checkpoint (owner sign-off, S9) -> S10 tag
)
```

The single genuinely required barrier is between the S3 pre-registration commit and the measurement
fan-out: no agent may see full-resolution pixels before the tolerances are committed, because a
tolerance written after a look is not a pre-registration. Everything downstream of the barrier is
embarrassingly parallel within its stage.

**Structured-output contracts (JSON).**

- Measurer (M1-M4): `{"agent_id", "image_path", "image_sha256", "code_commit",
  "windows": {"north_apex_cols": [a,b], "south_apex_cols": [a,b], "north_base_cols": [...],
  "south_base_cols": [...]}, "north": {"apex_xy": [x,y], "base_row": r, "extent_px": n,
  "extent_sigma_px": s}, "south": {...}, "anomalies": "free text"}` - pixel units only.
- Interpolation analyst (I1-I2): `{"agent_id", "edr_frame_id", "alignment_offset_px",
  "alignment_peak_correlation", "upsample_methods": [...], "cutoff_cycles_per_native_px",
  "excess_power_above_native_nyquist": "corroborated|artifact|absent-from-preview",
  "seam_artifacts": [...], "method_summary"}`.
- Statistics checker (T1): `{"agent_id", "recomputed_heights_m": {...}, "recomputed_sigmas": {...},
  "line_item_discrepancies": [...], "pass": bool}`.
- Adversarial verifier (A1-A3): `{"agent_id", "verdict": "REFUTED|NOT_REFUTED",
  "attack_vector", "reproduction_cmd", "evidence", "gate_attacked": 1-5}`.
- Auditors (C1, V1): `{"agent_id", "items_checked": N, "failures": [{"item", "expected", "found"}],
  "pass": bool}`.

**Acceptance thresholds.**

- Duplicate measurement: per eye, the two extents must agree within ±10 product px (§3.S3(2)). On
  disagreement, one additional blind measurer runs; the median of three is used only if the full
  spread is then ≤ 10 px - otherwise the measurement fails and the discrepancy is investigated as
  a defect, not averaged away.
- Cross-eye: within the quadrature-summed per-eye sigmas (§3.S3(4)); no re-measurement to force
  agreement.
- Known-answer: the §3.S3(3) interval test, exactly as pre-registered.
- Interpolation floor: I1 and I2 cutoff estimates within 15 % (relative, in cycles/native px) and
  concordant on the three-way classification; else a third independent implementation, and if
  discordance persists the P2.4 deliverable reports the disagreement rather than a number.
- Adversarial: any refutation with a reproduction command that the orchestrator verifies kills the
  affected gate outright (a single verified refutation suffices). Unreproduced concerns held by a
  majority (2 of 3 verifiers) escalate to the owner rather than being dismissed.
- Statistics: T1 must reproduce heights and sigmas within rounding (±0.1 m); any line-item
  discrepancy blocks S9 until resolved in writing.

**Human-in-the-loop checkpoints.** (1) The owner approves `PREREGISTRATION.md` before the barrier
lifts - tolerances are the owner's commitments, not the agents'. (2) The owner reviews the gate
ledger, adversarial reports, and audit JSONs before the `pipeline-v1` tag (S9/S10). (3) Any gate
failure's disposition - record-as-failed vs return-to-Phase-1 for data problems - is the owner's
call and is committed as a signed note.

## 6. Quality gates and exit criteria

Measurable statements of the roadmap's exit criteria ("all falsification gates of
`SIZE_VERIFICATION_METHODOLOGY.md` Step 6 pass at full resolution; pipeline frozen and tagged"):

1. Step 6 gate 1 (known-answer): both peaks pass the §3.S3(3) interval test at full resolution,
   with the Step 5 error budget table complete - every line filled or the measurement is not
   finished. [P2.2]
2. Step 6 gate 2 (cross-eye): PIA02406 extents agree with PIA02405 within §3.S3(4). [P2.3]
3. Step 6 gate 3 (ratio): full-res North/South extent ratio consistent with the preview ratio
   within propagated uncertainties; no result depends on a privileged range assumption. [P2.2]
4. Step 6 gate 4 (resolution): no Phase 2 claim finer than 2 native px; the S7 measured cutoff is
   documented and cited by the ledger. [P2.4]
5. Step 6 gate 5 (provenance): S1 and the V1 re-check both pass; the resampling chain for every
   measurement surface is enumerated; no window crosses an identified seam. [P2.1, P2.4]
6. Single code path verified: the preview regression (S2) and full-res runs use the same script at
   the same commit, differing only in CLI arguments; A1-A3 confirm no mode-conditional logic. [P2.1]
7. Tag `pipeline-v1` exists, pointing at a commit at which items 1-6 are all true, with owner
   sign-off committed. [P2.5]

## 7. Failure modes and stopping rules

Failed hypotheses are recorded as failed, never rescued post hoc. Specifically:

- **Known-answer failure.** If full-res heights miss the pre-registered band, the pipeline is not
  tagged, the failure is committed to `GATE_LEDGER.md`, and the phase stops. Diagnosis hypotheses
  (window error, product geometry, constant error) are each a *new* pre-registration tested on new
  runs - the tolerance band itself is never widened to admit the result.
- **Duplicate or cross-eye disagreement beyond tolerance** after the third-measurer rule: the
  measurement fails; the disagreement is the finding.
- **Checksum mismatch or missing input** (S1/V1): hard stop; return to Phase 1. No file is used
  whose provenance cannot be verified, and no download is attempted from within this phase.
- **Interpolation study surprises.** If S7 finds real information in the products above the
  preview's carrying capacity, the `VALIDATION_REPORT.md` §2 expectation is falsified in part:
  record it, append a correction, and re-run the affected preview-vs-full-res comparisons under an
  amended pre-registration. This is error-correction, not rescue - the amendment is dated,
  appended, and re-committed before re-measurement.
- **Verified adversarial refutation** of any gate: that gate reverts to failed until the defect is
  fixed at a new commit and the full gate ledger re-runs from S4 (measurements downstream of a
  refuted defect are void).
- **Phase failure** is declared if, after one diagnosis-and-refix cycle, any Step 6 gate still
  fails: the phase is written up as failed, `pipeline-v1` is not created, and Phases 3-6 do not
  proceed. The null result is published in-repo with the same care as a pass (standing rule;
  Cydonia precedent, `VALIDATION_REPORT.md` §7).

## 8. Deliverables

- `analysis/measure_twin_peaks.py` - parameterized, single code path (P2.1), with JSON output.
- `analysis/phase2/PREREGISTRATION.md` - tolerances, committed before measurement (barrier commit).
- `analysis/phase2/RUN_LOG.md` - every run: UTC time, commit, input SHA-256s, agent ID.
- `analysis/phase2/measurements/*.json` - raw measurer, analyst, checker, and auditor outputs.
- `analysis/phase2/ERROR_BUDGET.md` - Step 5 tables for both peaks at full resolution (P2.2).
- `analysis/phase2/INTERPOLATION_FLOOR.md` + spectra figures - the measured floor (P2.4).
- `analysis/phase2/GATE_LEDGER.md` - all five Step 6 gates, pass/fail with numbers, adversarial
  reports appended, owner sign-off note (P2.2-P2.4).
- Commits: provenance-audit commit (S1); refactor commit with preview regression evidence (S2);
  pre-registration commit (S3); measurement commits (S4-S7); ledger commit (S8); sign-off commit
  (S9). Commit messages reference task IDs (P2.x).
- Tag: `pipeline-v1` (P2.5) - created only on full gate passage plus owner sign-off; all later
  phases reference this tag.
