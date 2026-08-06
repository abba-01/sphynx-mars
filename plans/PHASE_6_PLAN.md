# Phase 6 Execution Plan - Morphology and artificiality statistics

**Roadmap section:** `ROADMAP.md` Phase 6, tasks P6.1-P6.5.
**Depends on:** Phase 1 (data + provenance); the P4.4 neutral-ID population dataset with
its P4.4 error budgets, and the P4.3 candidate measurements (plan dimensions and relief),
for all data-bearing steps; the P4.5 verdict for the P6.5 comparison
document. Definition work (P6.1-P6.2) may run parallel with Phase 4, provided it commits
before any Phase 6 agent reads P4.4 values (§5 barrier). **Feeds:** Phase 7 (P7.2 checks
this phase's statistics). **Drafted:** 2026-08-02, by an AI agent (claude-fable-5) under
the repository's standing rules.

## 1. Objective and scope

Replace adjective-based artificiality arguments with population statistics under
pre-registered metrics. Exit criteria, quoted from the roadmap:

> "no morphology claim in the repo lacks a metric, a null distribution, and an uncertainty."

In scope: P6.1 (rewrite `intelligence_vs_nature_morphology.md` into computable
discriminators — symmetry score, edge-angularity statistic, alignment with regional flow
direction, departure from the hummock size–relief trend — each with a null distribution
estimated from the P4.4 population); P6.2 (multiple-comparisons policy stated in advance);
P6.3 (apply discriminators to Object X and the full population; report effect sizes with
confidence intervals, not verdicts); P6.4 (fold `universal_morphology_cycles.md` and
`mars_earth_orientation_analysis.md` into the framework or mark them untestable-as-posed);
P6.5 (the Cydonia comparison, written whatever the outcome).

Out of scope: any new size or range measurement (Phases 4-5 own those); any identity claim
from the IMP products — identity is gated by resolution (`VALIDATION_REPORT.md` §6), and
the repo's calibrated position stands: **Object X's size is indeterminate from the IMP
image alone** (F6), with the distance ambiguity resolved only by the Phase 4 orbital test.
Morphology work here operates on the HiRISE map product (25 cm/px, per the register) and
the P4.3/P4.4 measurements, never on the 500 %-enlarged press mosaics, whose sub-native
detail is interpolation (F2/§5.5; Methodology Step 1 resolution-floor rule). A standing
language rule for every Phase 6 output: percentiles, effect sizes, and intervals — the
words "artificial" and "natural" never appear as conclusions of this phase.

## 2. Inputs and preconditions

- **Network access:** no analysis step requires it. Exactly two contingencies touch the
  network, each in a normal-egress session outside the analysis sandbox (which blocks the
  NASA/UA hosts, `VALIDATION_REPORT.md` §2): (i) the live-page source-verification agent
  (Q1, §5), continuing the P1.5 practice; (ii) retrieval of any regional-geology reference
  for the flow-direction discriminator, should the internal definition in S3 prove
  insufficient — [source to be located and verified during execution - do not cite until
  verified]; until verified, only the internal definition is used.
- Required inputs, each traceable to `data/PROVENANCE.md` with SHA-256: the HiRISE map
  product for PSP_001890_1995 and the DTM or stereo-derived relief from PSP_002391_1995
  (P1.3; if Phase 1 recorded "no archived DTM," the degraded path in S2.4 applies); the
  P4.4 neutral-ID population dataset (≥30 hummocks per the P3.4 selection rule) with its
  P4.4 error budgets, consumed only via Phase 4's tagged results commit; the P4.3
  candidate measurements (plan dimensions and relief, with error budgets) for the P4.2
  candidate list (if more than one Object X candidate exists, every candidate is scored);
  the Phase 3
  pre-registration commit (P3.3-P3.4), which already fixes the symmetry metric family
  (mirror-correlation about the best-fit long axis) and the comparison population —
  Phase 6 may extend that battery but never amend it retroactively.
- Repository documents to be triaged or superseded: `intelligence_vs_nature_morphology.md`,
  `universal_morphology_cycles.md`, `mars_earth_orientation_analysis.md`, each carrying its
  Phase 0 header. Originals are never deleted (P0.1 practice); they are annotated and
  superseded.
- Tooling: Python 3 with numpy and Pillow; `sha256sum`; `git`; the `pipeline-v1` constants
  module (P2.5) where shared constants are needed. New dependencies (e.g., a raster reader
  for the HiRISE product) are recorded in a commit note before first use.

## 3. Research protocol

Numbered SOP. "Record" means: append to `analysis/phase6/RUN_LOG.md` with UTC date-time,
code commit hash, input SHA-256s, and agent ID.

- **S1 - Provenance audit** (precondition to all tasks). Recompute SHA-256 for every §2
  input against `data/PROVENANCE.md`; verify the P4.4 dataset is read from Phase 4's tagged
  commit. Any mismatch: stop, record, return to the owning phase. No waivers.
- **S2 - Discriminator specification** (**P6.1**). Write the formal definition of each
  discriminator as an executable function of the map product and relief data:
  1. **D1 symmetry:** mirror-correlation score about the best-fit long axis (the P3.4
     metric), computed on the plan-view outline and interior shading within the landform's
     pixel mask.
  2. **D2 edge angularity:** a statistic of boundary turning angles along the extracted
     plan outline (exact estimator, smoothing scale, and outline-extraction rule fixed in
     this specification, not at run time).
  3. **D3 flow alignment:** angular deviation of the landform's long axis from the
     regional flow direction, where flow direction is defined *internally* as the circular
     mean of long-axis orientations over the P4.4 population with the target landform
     excluded (leave-one-out, so no landform's score depends on its own orientation).
  4. **D4 size–relief departure:** residual of the landform's relief against the trend
     fitted to the population's plan-size/relief pairs (fit form fixed in the spec).
  Every discriminator carries its resolution gate: no term may depend on structure finer
  than 2 map pixels (0.5 m at 25 cm/px), the Step 6 resolution-gate analog for the orbital
  product. **S2.4 degraded path:** if no DTM exists and Phase 4 relief is stereo-derived
  with larger errors, D4 carries those errors; if relief is unavailable for a landform, D4
  is recorded as not-computable for it — never imputed.
- **S3 - Known-answer fixtures** (**P6.1**; standing rule "known-answer test first").
  Build synthetic fixtures with analytically known scores: an exactly mirror-symmetric
  mask (D1 must score at the metric's maximum), an isotropic random field (D1/D2 must land
  in the stated null band), a rectangle and a smoothed ellipse (D2 must rank the rectangle
  above the ellipse), and orientation sets with known circular means (D3 exact recovery).
  Two independent implementations of each discriminator (§5, E1a/E1b) must pass every
  fixture and agree on fixture scores within the S4 tolerance before any real data is
  touched.
- **S4 - Pre-registration commit** (**P6.2**; the §5 barrier). Before any Phase 6 agent
  reads a P4.4 value, commit `analysis/phase6/PREREGISTRATION.md` containing:
  1. The frozen discriminator specifications (S2) and fixture results (S3).
  2. Dual-implementation tolerance: E1a and E1b scores must agree per landform within a
     numeric tolerance stated per discriminator in this commit.
  3. The null-distribution estimator: for each discriminator, the empirical distribution
     over the P4.4 population, leave-one-out for the scored landform; CIs on percentiles
     by bootstrap resampling of the population (resample count fixed here).
  4. **Multiple-comparisons policy** (named here, in full — no menu, no deferral): the
     primary (confirmatory) family is ONE pre-registered family — all enumerated P4.2
     candidates (Object X among them) × all primary discriminators; there are no
     per-candidate families. Correction for that single family: Holm–Bonferroni at
     family-wise α = 0.05. All secondary/exploratory analyses — including the
     all-landforms × all-discriminators screen — use Benjamini–Hochberg FDR at
     q = 0.05 and are always labeled *exploratory*; the screen can flag nothing as a
     finding — outliers by chance are the expected behavior the policy exists to
     contain. Deterministic rule: FWER control (membership in the Holm–Bonferroni
     primary family) is mandatory for any result that could support a confirmatory
     artificiality-related claim.
  5. The reporting format: per discriminator, Object X's score, its population percentile,
     the bootstrap CI, and the corrected significance status — no verdict field exists in
     the schema.
  6. The P6.4 computability rubric (S9) verbatim, before triage begins.
  This file is append-only; amendments go in a dated "Amendments" section and never alter
  tolerances, estimators, or the correction policy.
- **S5 - Blind scoring** (**P6.3**). The orchestrator unseals the P4.4 neutral-ID dataset
  (IDs randomized by Phase 4; the ID↔location key stays with the orchestrator). E1a and
  E1b independently score every landform on every computable discriminator, in
  independently randomized order, emitting scores only — neither knows which ID is Object
  X (or a P4.2 candidate), neither sees the other's output.
- **S6 - Reconciliation.** Orchestrator compares E1a/E1b per landform per discriminator
  against the S4(2) tolerance. Disagreements route to a third blind implementation for
  that landform only; if the three-way spread still exceeds tolerance, that
  landform×discriminator cell is recorded as measurement-failed, never averaged.
- **S7 - Null distributions and effect sizes** (**P6.3**). Orchestrator computes the
  leave-one-out null distributions, bootstrap CIs, and the corrected primary-family
  results exactly as pre-registered, then unblinds Object X's ID and assembles the report:
  effect sizes with confidence intervals, per S4(5). Run once; no re-runs after unblinding.
- **S8 - Rewrite of the morphology document** (**P6.1**). Draft
  `analysis/phase6/MORPHOLOGY_DISCRIMINATORS.md` superseding
  `intelligence_vs_nature_morphology.md`: each qualitative "signature" in the original
  (precision, complexity, boundary sharpness, etc.) is either mapped to a discriminator
  with its null distribution or explicitly retired as uncomputable at the available
  resolution (the sub-2-m detail that distinguishes carving from erosion is unresolved at
  IMP range per §5.5, and tool-mark-scale claims are below even the HiRISE floor). The
  original file gains an appended header pointing to the successor.
- **S9 - Triage of the two framework documents** (**P6.4**). Two independent assessors
  apply the S4(6) rubric claim-by-claim to `universal_morphology_cycles.md` and
  `mars_earth_orientation_analysis.md`. Rubric: a claim is testable iff it names (i) a
  computable metric over data in `data/PROVENANCE.md`, (ii) a null distribution estimable
  from the same data, and (iii) a threshold statable before computation. Testable claims
  are folded into the S2 battery *as new pre-registrations* (a dated S4 amendment, applied
  only to held-out computation, per the no-post-hoc-rescue rule); everything else is
  marked **untestable-as-posed** — outside the program's scope by rule, not refuted.
  Orientation-type claims (e.g., cardinal alignment of the long axis) are candidates for
  folding via D3's machinery; cross-scale "universal cycle" claims name no null
  distribution and are expected to fail the rubric, but the assessors, not this plan,
  decide. Assessor disagreements are resolved by the adversarial panel and owner, recorded.
- **S10 - Cydonia comparison** (**P6.5**; after the P4.5 verdict). Write
  `analysis/phase6/CYDONIA_COMPARISON.md`: same question class, same protocol — the 1976
  Viking feature re-imaged in 2001 at ~1.5 m resolution was "shown in the
  higher-resolution image to be a natural feature similar to a butte or mesa on Earth"
  (NASA, PIA03225), a mesa "about 3 km (2 miles) in length and rises about 250 metres
  (820 feet) above the surrounding plain" (*Britannica*) — and in both cases the
  resolution followed the higher-resolution data. The document states how this program's
  outcome (whatever P4.5 and S7 returned) instantiates that protocol, including the null
  case.
- **S11 - Gate ledger.** Record pass/fail with numbers in `analysis/phase6/GATE_LEDGER.md`
  (§6). **S12 - Adversarial review and sign-off.** Adversarial verifiers, statistics
  checker, and auditors (§5) attack the ledger; the owner signs off in a committed note.
  **S13 - Freeze and tag** `morphology-v1`; Phase 7 consumes only the tag.

## 4. Academic-integrity protocol

- **Provenance and checksums.** S1 verifies every input before work; V1 re-verifies after
  S11. Every run-log line carries input SHA-256s and the code commit. No analysis touches
  a file absent from `data/PROVENANCE.md`; P4.4 data enters only via Phase 4's tag.
- **Verbatim quotation.** All quoted language comes from the `VALIDATION_REPORT.md` §8
  register and `SIZE_VERIFICATION_METHODOLOGY.md` Sources, with URL and access date
  carried from the P1.5 live-page audit. No new sources from memory: any flow-direction or
  regional-geology reference enters only after Q1 verification, quoted verbatim with
  location; until then the S2 internal definition stands alone.
- **Pre-registration discipline.** The S4 commit precedes every read of P4.4 values by a
  Phase 6 agent; git history is the timestamp (the standing rule: pre-register before you
  look). Folded P6.4 claims are new pre-registrations via dated amendments, tested on
  held-out computation, never against results already seen.
- **Blinding and confirmation-bias controls.** Scorers see neutral IDs in randomized
  order and never the ID key, the sibling's output, the Phase 3 anchor numbers (9.1 m ×
  32 m at North Twin range, or ~20× smaller in the near field — `VALIDATION_REPORT.md`
  §5.5), or the Sphinx dimensions in the register. Blinding is verified by transcript
  audit (A-role): a transcript that reads the ID key, sibling output, or those numbers
  voids that scoring run. Unblinding happens once, at S7, after all scores are frozen.
- **AI-assistance disclosure.** Every document and commit states it was generated by AI
  agents (claude-fable-5) under human direction, per the practice adopted after F8. No AI
  output is represented as human analysis.
- **Error-correction and retraction.** Errors found after `morphology-v1` are fixed by
  appended notes and a `morphology-v1.1` tag; history is never rewritten. If Phase 6
  results contradict an earlier repo document, that document gains an appended correction
  block citing the Phase 6 commit.
- **Null results.** An Object X that sits mid-distribution on every discriminator is the
  fully written-up outcome S7 must anticipate — reported with the same care and the same
  CI tables as any outlier result (standing rule; Cydonia precedent, §7).

## 5. Agent fan-out design

Executed with Claude Code Workflow orchestration (`agent()` / `parallel()` /
`pipeline()`); all agents inherit the session model, claude-fable-5.

| Role | ID(s) | Count | Independence / blinding arrangement |
|---|---|---|---|
| Metric implementers | E1a, E1b | 2 | Independent implementations of all discriminators from the S2 spec text only; no access to each other's code or scores; both must pass S3 fixtures |
| Third-implementation referee | E1c | 1 | Invoked only on S6 disagreements; blind to which sibling produced which score |
| Statistics checker | T1 | 1 | Re-derives null distributions, bootstrap CIs, and the multiple-comparisons correction from raw score JSON only; sees no compiled tables first |
| Adversarial verifiers | A1-A3 | 3 | Prompted to REFUTE: attack spec ambiguity exploitable at run time, null-estimator leakage (target inside its own null), correction-policy drift, blinding violations (transcript audit), resolution-gate breaches (< 2 map px structure); each works alone |
| Triage assessors | G1, G2 | 2 | Independently apply the S4(6) rubric to the two P6.4 documents; no access to each other; adjudicated by A-panel + owner |
| Comparison writer | W1 | 1 | Drafts S8 and S10 documents; may not alter any score, distribution, or verdict field |
| Source-verification agent | Q1 | 1 | Networked session only: checks every quote and constant in Phase 6 documents against live pages; flags drift; may not edit analysis outputs |
| Provenance auditor | V1 | 1 | Runs S1 before work; re-verifies all checksums after S11 |

**Orchestration pattern.**

```
pipeline(
  V1(S1) -> parallel(E1a, E1b)(S2 spec conformance + S3 fixtures)
  -> orchestrator(S4 pre-registration commit; owner approval)
  == BARRIER ==                                   # the one genuine barrier
  orchestrator unseals P4.4 -> parallel(E1a, E1b)(S5 blind scoring)
  -> orchestrator(S6 reconcile [E1c as needed]; S7 nulls, correction, unblind)
  -> parallel(T1, A1, A2, A3, Q1, V1-recheck)      # verification fan-out
  -> human checkpoint -> W1(S8, S10) -> owner sign-off (S12) -> S13 tag
)
parallel track, joins before S12: parallel(G1, G2)(S9 triage) -> A-panel adjudication
```

The single genuinely required barrier sits between the S4 pre-registration commit and the
unsealing of P4.4 data: a discriminator, tolerance, or correction policy written after the
population scores have been seen is not a pre-registration. The S9 triage track needs no
barrier (it reads documents, not data) but must join before S12 so folded claims and
scope-exclusions appear in the ledger. S10 additionally waits on the P4.5 verdict — an
external dependency, not an internal barrier.

**Structured-output contracts (JSON).**

- E1a/E1b/E1c: `{"agent_id", "code_commit", "fixture_results": [{"fixture_id", "discriminator", "score", "expected", "pass": bool}], "scores": [{"neutral_id", "discriminator", "score", "computable": bool, "resolution_gate_ok": bool}]}` — scores only; no percentiles, no identities.
- T1: `{"agent_id", "recomputed_percentiles": {...}, "recomputed_cis": {...}, "correction_method_verified": bool, "primary_family_results": [...], "line_item_discrepancies": [...], "pass": bool}`.
- A1-A3: `{"agent_id", "verdict": "REFUTED|NOT_REFUTED", "attack_vector", "reproduction_cmd", "evidence", "gate_attacked"}`.
- G1/G2: `{"agent_id", "document", "claims": [{"claim_quote", "metric_named": bool, "null_estimable": bool, "threshold_statable": bool, "disposition": "FOLD|UNTESTABLE_AS_POSED"}]}`.
- Q1, V1: `{"agent_id", "items_checked": N, "failures": [{"item", "expected", "found"}], "pass": bool}`.

**Acceptance thresholds.**

- Fixtures: both implementations pass every S3 fixture; any failure blocks the barrier.
- Duplicates: per-landform scores within the S4(2) tolerance; E1c invoked on failure;
  three-way failure records the cell as measurement-failed, never averaged or dropped
  silently.
- Statistics: T1 must reproduce every percentile, CI, and corrected result within stated
  rounding; any discrepancy blocks S12 until resolved in writing.
- Adversarial: one verified refutation (reproduction command confirmed by the
  orchestrator) kills the affected result — the finding reverts to failed, not to
  "adjusted"; a 2-of-3 unreproduced-concern majority escalates to the owner.
- Triage: G1/G2 dispositions that disagree on any claim go to the A-panel and owner; no
  claim is folded on a single assessor's judgment.

**Correlated-error limitation (standing).** Duplicate agents (E1a/E1b/E1c, G1/G2) are
instances of the same model (claude-fable-5). Procedural isolation prevents information
leakage between them but not shared model-systematic priors: duplicate agreement bounds
procedural/transcription error only, not model-systematic error. Where the protocol
supports it, duplicates must take methodologically distinct routes, named in the relevant
step — for S2/S5, E1a and E1b must realize each discriminator by distinct algorithmic
routes (different outline-extraction and numerical implementations of the same frozen S2
spec), recorded with their fixture results. A human spot-check of a randomized sample of
duplicate outputs is a standing checkpoint before phase close.

**Human-in-the-loop checkpoints.** (1) The owner approves `PREREGISTRATION.md` before the
barrier lifts — the discriminator battery, tolerances, and correction policy are the
owner's commitments. (2) The owner reviews the unblinded S7 effect-size report, T1 and
A1-A3 outputs before any document rewriting begins. (3) The owner approves each S9
disposition (fold vs untestable-as-posed) — scope exclusion of the owner's own documents
is the owner's call, recorded. (4) The correlated-error spot-check: a human reviews a
randomized sample of duplicate outputs (E1a/E1b score pairs, G1/G2 dispositions) before
phase close. (5) Final sign-off before the `morphology-v1` tag.

## 6. Quality gates and exit criteria

Measurable statements of the roadmap's exit criteria:

1. Fixture gate: every discriminator passes all S3 known-answer fixtures in both
   implementations, recorded with numbers. [P6.1]
2. Coverage gate: every landform in the P4.4 population has, per discriminator, either a
   reconciled score or an explicit measurement-failed / not-computable entry with reason;
   zero silent gaps. [P6.1, P6.3]
3. Pre-registration gate: the S4 commit hash precedes every commit containing a P4.4-
   derived number; correction policy named before computation (A-audit confirms). [P6.2]
4. Reporting gate: the S7 report contains, for Object X (and every P4.2 candidate), score
   + percentile + bootstrap CI + corrected status per discriminator, and no verdict
   language; T1 reproduces all of it. [P6.3]
5. Repo-wide claim audit: every morphology claim in every non-superseded repo document
   either carries a metric, a null distribution, and an uncertainty, or carries an
   untestable-as-posed / superseded annotation — verified line-by-line by A-audit against
   a claim inventory in the ledger. [P6.1, P6.4] (This is the roadmap exit criterion made
   checkable.)
6. Triage gate: every claim in the two P6.4 documents has a G1/G2-agreed (or adjudicated)
   disposition; folded claims have dated pre-registration amendments. [P6.4]
7. Cydonia document exists and quotes only register sources, whatever the outcome. [P6.5]
8. Tag `morphology-v1` exists, pointing at a commit where items 1-7 are true, with owner
   sign-off committed.

## 7. Failure modes and stopping rules

Failed hypotheses are recorded as failed, never rescued post hoc. Specifically:

- **Fixture failure** (S3): hard stop before the barrier. One diagnosis-and-refix cycle
  under a dated amendment; a second failure declares the phase failed on that
  discriminator, which is dropped from the battery *by amendment before the barrier* or,
  if already past it, reported as failed — never redefined after data contact.
- **Spec ambiguity discovered after the barrier** (two conforming implementations diverge
  systematically): the affected discriminator's results are void; a clarified spec is a
  new pre-registration, and scoring re-runs from S5 for that discriminator at a new
  commit. More than one such event stops the phase for a written process review.
- **Population shortfall:** if P4.4 delivers fewer landforms than the P3.4 rule promised
  (< 30), the phase proceeds but every null distribution is flagged underpowered with the
  achieved n; the selection rule is never widened by Phase 6 to harvest more objects.
- **Relief unavailable** (no DTM and no usable stereo relief): D4 is reported
  not-computable, with the D1-D3 battery standing alone; no relief is imputed.
- **Checksum mismatch or missing input** (S1/V1): hard stop; return to the owning phase —
  no improvised downloads from the analysis environment.
- **Blinding violation** (transcript audit): the affected scoring run is void and re-run
  by a fresh agent; the violation is recorded in the ledger.
- **Verified adversarial refutation**: the affected result reverts to failed; downstream
  numbers are void and re-run from the earliest affected step at a new commit.
- **A significant post-correction result on some discriminator is not a phase success
  condition,** and a null result on all of them is not a phase failure — both are the
  phase working. Forbidden in all cases: re-scoring, re-selecting the population, adding
  discriminators, or changing the correction until the desired pattern appears.
- **Phase failure** is declared if, after one diagnosis-and-refix cycle, gate 1, 3, or 4
  of §6 still fails: `morphology-v1` is not created, Phase 7 does not consume Phase 6
  statistics, and the failure write-up is committed with the same care as a success
  (standing rule; Cydonia precedent, `VALIDATION_REPORT.md` §7).

## 8. Deliverables

All under `analysis/phase6/` unless noted:

- `discriminator_spec.md` + `discriminators_a/`, `discriminators_b/` - S2 spec and the
  two independent implementations with fixture suites (P6.1).
- `PREREGISTRATION.md` - specs, tolerances, null estimators, correction policy, triage
  rubric (barrier commit; P6.1, P6.2).
- `scores/*.json` - raw E1a/E1b/E1c, T1, A1-A3, G1/G2, Q1, V1 outputs.
- `EFFECT_SIZES.md` + machine-readable table - per-discriminator scores, percentiles,
  bootstrap CIs, corrected primary-family results for Object X, all P4.2 candidates, and
  the population (P6.3).
- `MORPHOLOGY_DISCRIMINATORS.md` - successor to `intelligence_vs_nature_morphology.md`;
  the original gains an appended supersession header (P6.1).
- `TRIAGE_UNIVERSAL_MORPHOLOGY.md`, `TRIAGE_ORIENTATION.md` - claim-by-claim dispositions
  with rubric fields and owner approvals (P6.4).
- `CYDONIA_COMPARISON.md` - the protocol comparison, written after the P4.5 verdict (P6.5).
- `GATE_LEDGER.md` - §6 gates with numbers, claim inventory, adversarial reports, owner
  sign-off; `RUN_LOG.md` - every run: UTC time, commit, input SHA-256s, agent ID.
- Commits referencing task IDs (P6.x): provenance audit (S1); spec + fixtures (S2-S3);
  pre-registration (S4); scoring (S5-S6); statistics (S7); rewrites (S8); triage (S9);
  comparison (S10); ledger (S11); sign-off (S12). Tag: `morphology-v1` - created only on
  full gate passage plus owner sign-off; Phase 7 references the tag.
