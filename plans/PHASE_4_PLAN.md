# Phase 4 Execution Plan - The Decisive Orbital Test

**Roadmap section:** `ROADMAP.md` Phase 4 (tasks P4.1–P4.6). **Standing rules apply**
(pre-register before you look; every number carries an error budget; known-answer
test first; no post-hoc rescue; publish the null result).

## 1. Objective and scope

Execute the experiment that settles the size question. Per the roadmap: *"measure
Object X and its comparison population at ~25 cm/px, where distance ambiguity does not
exist, and grade the pre-registered hypotheses … the Cydonia protocol applied to this
scene."* The data are the HiRISE observations of the Pathfinder site: PSP_001890_1995
("map-projected to 25 cm/pixel", lander and Twin Peaks identified — University of
Arizona HiRISE page, per `VALIDATION_REPORT.md` §7/§8) and the stereo/topography
observation PSP_002391_1995.

Roadmap exit criteria, quoted verbatim and adopted unchanged: *"every pre-registered
hypothesis graded pass/fail with data; results document committed regardless of
outcome."*

In scope: P4.1–P4.6 exactly as itemized in the roadmap. Out of scope: any new
hypothesis, tolerance, threshold, percentile, or selection rule (all frozen at tag
`prereg-v1`); any morphological *identity* claim finer than the resolution gate; any
edit to the pre-registration other than an appending, owner-signed amendment that
clarifies execution without altering a band or rule. Calibrated-language rule (F6):
until the orbital measurement is accepted at P4.5, Object X's size is indeterminate
from the IMP image alone, and all interim text must say so.

## 2. Inputs and preconditions

Hard dependencies (phase may not start until all exist; audited in protocol step 1):

1. **Phase 1 complete.** `data/PROVENANCE.md` lists, with URL, access date, and
   SHA-256: the PSP_001890_1995 map-projected product; PSP_002391_1995; the P1.3
   record of whether an archived HiRISE DTM exists (this fixes the relief branch);
   `PIA02405.tif` / `PIA02406.tif`; the P1.2 EDR frames; the P1.5 spot-check results.
   No file absent from `data/PROVENANCE.md` may be cited or measured.
2. **Phase 2 complete.** Tag `pipeline-v1` exists; all `SIZE_VERIFICATION_METHODOLOGY.md`
   Step 6 gates passed at full resolution. The pipeline supplies the measured summit
   columns of both peaks — inputs to this phase's registration known-answer test.
3. **Phase 3 complete.** Tag `prereg-v1` exists and its commit precedes every Phase 4
   commit (the roadmap's "single most important ordering rule").
   `preregistration/OBJECT_X_DEFINITION.md` supplies the pixel boxes with per-edge
   uncertainties; `preregistration/PREREGISTRATION.md` supplies H0, H1 (plan length
   band 62.05–83.95 m; relief band 15.0–25.0 m; symmetry above the empirical
   1 − (0.05/kc) population quantile, kc = number of candidates graded, with the
   population-maximum fallback when 0.05/kc < 1/(n+1); all clauses required), the
   relief branch, the grading rules, and the
   population rule (hummocks within 1.2 km, plan long axis ≥ 5 m; target n ≥ 30).
4. Constants from the validated record: HiRISE map scale 0.25 m/px (native
   28.5 cm/px); IMP IFOV 0.98 mrad/native px (Smith et al. 1997,
   doi:10.1029/96JE03568); 1 product px = 0.196 mrad; North Twin ≈ 860 m, South Twin
   ≈ 1 km (NASA Photojournal PIA02405 caption); resolution floor 2 native px ≈ 1.7 m
   at 860 m; size = Z·N·IFOV.

**Network access: none required** in the nominal path — every input was downloaded
and checksummed in Phase 1; all analysis runs in-sandbox. Contingent exceptions,
flagged as requiring network outside the analysis sandbox: (a) if the P1.3 record
specifies the stereo relief branch and the sandbox lacks a photogrammetric toolchain,
acquiring one is a network step [software source to be located and verified during
execution - do not cite until verified]; (b) any pending P1.5 spot-check is flagged
"live verification pending (P1.5)" in the results document, not re-fetched in-sandbox.

## 3. Research protocol

Numbered SOP; every step names its roadmap task ID. "Map px" = pixels of the
map-projected PSP_001890_1995 product (0.25 m/px).

1. **[all] Precondition audit.** Verify SHA-256 of every input against
   `data/PROVENANCE.md`; verify tags `pipeline-v1` and `prereg-v1` exist and the
   `prereg-v1` commit predates HEAD; record in
   `results/phase4/audit/preconditions.json`. Any failure: hard stop (§7).
2. **[P4.1] Solve the registration (two blind duplicates).** Each agent independently:
   (a) locates the lander (the caption's "white feature at center") and both Twin
   Peaks in PSP_001890_1995 as pixel centroids with uncertainties; (b) computes
   lander→summit azimuths from pixel offsets at 0.25 m/px; (c) solves the PIA02405
   column→azimuth mapping (column × 0.196 mrad, anchored via the `pipeline-v1` summit
   columns). Known-answer gate, per solver: predicted vs IMP-measured summit
   separation (Δcolumns × 0.196 mrad), |Δ| ≤ 2.0 mrad (2 native px × 0.98 mrad =
   1.96 mrad, rounded outward to 2.0 as the pre-registered tolerance). A failing
   solver is discarded and rerun fresh.
3. **[P4.1] Reconcile.** Accept if lander centroids agree within ±4 map px (±1.0 m)
   and mappings within ±1.0 mrad across the box columns; publish the mean solution
   with half-range uncertainty in `results/phase4/registration_solution.json`. Else
   one tiebreak solver; no two-of-three agreement → phase failure (§7). **Owner
   checkpoint 1** follows.
4. **[P4.2] Cast the corridor.** Convert the Object X box's column extent to an
   azimuth interval; widen by the registration and box-edge uncertainties (all terms
   tabulated). Draw the corridor on PSP_001890_1995 from the lander to 1.2 km — the
   population radius, extending beyond the ≈ 1 km South Twin range per P4.2's "near
   field to beyond South Twin range". Script: `analysis/phase4/cast_corridor.py`.
5. **[P4.2, P4.4] Enumerate (two blind duplicates each).** *Candidates:* every
   discrete landform intersecting the corridor (centroid, extent, range = pixels ×
   0.25 m); reconciled list = the **union**, never the intersection: "If more than
   one candidate exists, record all of them — do not pick the most interesting one"
   (roadmap P4.2); disagreements retained and flagged; the reconciled candidate count
   fixes kc for the H1 symmetry threshold (step 9). *Population:* the `prereg-v1`
   rule applied mechanically — hummocks within 1.2 km, long axis ≥ 5 m (= 20 map px);
   union; n ≥ 30 (§7 if unmet). *Boundary rule (pre-registered):* an object is
   included iff the **mean** of the two duplicates' coarse estimates meets the
   threshold; every object whose coarse estimate lies within one coarse-measurement
   sigma of either boundary (5 m long-axis, 1.2 km range) is flagged in the data
   table; union reconciliation applies to detection disagreements only (one duplicate
   misses an object the other found), never to threshold disagreements (both detect
   it — inclusion then follows the mean rule). **Checkpoint 2**: owner may add, never
   remove.
6. **[P4.3, P4.4] Build the blind pool.** A deterministic script
   (`analysis/phase4/make_tiles.py`) cuts one tile per object (candidates and
   population interleaved), assigns fresh neutral IDs in randomized order, and writes
   the ID→identity mapping to `results/phase4/blind_map_sealed.json`, whose SHA-256
   is committed but whose content is withheld from every measurement agent — P4.4's
   "randomized order with neutral IDs" blinding.
7. **[P4.3, P4.4] Measure, blind.** Each object is measured by two independent blind
   measurers (§5): plan long axis, short axis, long-axis azimuth, and the
   pre-registered mirror-correlation symmetry score, each with an uncertainty and an
   error-budget line per `SIZE_VERIFICATION_METHODOLOGY.md` Step 5. Measurers receive
   the symmetry metric only as a metric-specification excerpt — the algorithm alone,
   stripped of hypothesis bands, thresholds, percentiles, and any mention of
   Object X; the excerpt's SHA-256 is recorded in the audit trail. Relief per the
   branch fixed in the P1.3 record: DTM sampling of PSP_002391_1995 if archived, else
   the fixed fallback recorded in Phase 1 S6 — relative heights from the
   PSP_001890_1995 / PSP_002391_1995 stereo pair by area-based image correlation on
   map-projected tiles; vertical datum from ≥ 5 control points on terrain of
   assumed-zero relative relief; parallax-to-height conversion from the observation
   geometry stated on the two HiRISE catalog pages; error model propagating matching
   precision (assumed ±0.5 px until measured) through that geometry; toolchain as
   named in the P1.3 provenance record, "[software to be located and verified during
   execution - do not cite until verified]". No relief method is improvised mid-phase
   (relief duplicates, §5). Acceptance per object:
   duplicates within max(±0.5 m, ±10 %) per plan axis (0.5 m = 2 map px × 0.25 m —
   derivation shown) and max(±0.5 m, ±15 %) on relief; else a third measurement; no
   two-of-three agreement → recorded "unmeasured — outline ambiguous," never dropped.
8. **[P4.5] Measurement freeze.** All measurement JSONL committed and hash-frozen.
   **This is the unblinding barrier (§5): no mapping is unsealed and no grading
   occurs until this commit exists.** **Owner checkpoint 3** authorizes unsealing.
9. **[P4.5] Grade.** The grader — which never sees an image — joins the unsealed map
   to the frozen measurements and applies the `prereg-v1` rules verbatim. **H1:**
   each candidate graded against H1's three clauses (all required); the symmetry
   threshold is the empirical 1 − (0.05/kc) quantile of the population symmetry
   scores (linear-interpolation quantile estimator; kc = number of enumerated
   candidates graded, fixed at step 5); if 0.05/kc < 1/(n+1) the quantile lies
   beyond the data, and the clause is instead graded against the population
   **maximum**, with that fallback stated in the results table. **H0 — graded per
   candidate:** for each candidate and each of the k = 3 named primary metrics fixed
   at `prereg-v1` (plan long axis, aspect ratio, relief), compare the candidate's
   value against the comparison population's empirical distribution
   (linear-interpolation quantile estimator; n = population size); H0 is rejected
   for a candidate iff its value falls **outside the population's observed min–max
   envelope** on at least one primary metric — such an exceedance has one-sided
   empirical p ≤ 1/(n+1), since a value exchangeable with the n population draws
   ranks above their maximum (or below their minimum) with probability 1/(n+1).
   **Multiplicity:** report m = k × (number of candidates graded) and the
   family-wise bound m/(n+1); a rejection is CONFIRMATORY only if m/(n+1) ≤ 0.10
   (e.g., one candidate, n = 30: m = 3 × 1 = 3, 3/31 ≈ 0.097 ≤ 0.10; two
   candidates: m = 3 × 2 = 6, 6/31 ≈ 0.194 > 0.10); otherwise it is recorded
   verbatim as "suggestive, not confirmatory" and cannot support an
   artificiality-related claim. **Gradability:** envelope/percentile clauses are
   gradable iff population n ≥ 20; below that the clause is recorded "not gradable
   (n < 20)" — never improvised. The statistics checker recomputes everything from
   raw JSONL; verdicts must match exactly. The results document records the full
   data table and the per-candidate verdicts, including the null case: "Object X is
   a 9-meter hummock like its 30 neighbors" (P4.5). The **overall Object X verdict
   is conditional on step 10's P4.6 association gate** and is issued only after it.
10. **[P4.6] Cross-instrument closure.** For each candidate: take its orbital range Z
    (centroid distance × 0.25 m/px), recompute the IMP-side size as Z × N × IFOV
    (N in native px = product px ÷ 5), and compare with the orbital plan length.
    Gate: agreement within combined error budgets (IMP side: ±2 native px counting
    error plus box-edge uncertainty; the IMP *vertical* extent is a lower bound only,
    per Step 4 base-occlusion). A pass confirms the candidate as the IMP feature;
    failure is recorded as "association unconfirmed" — not adjusted. Only candidates
    passing this association gate bear on the Object X hypotheses; the per-candidate
    verdicts (step 9) of non-associated candidates are reported but bear only on
    population characterization.
11. **[P4.5, P4.6] Assemble, verify, sign, commit.** Assemble
    `results/PHASE4_RESULTS.md`; run the verification fan-out (§5); obtain owner
    sign-off; commit referencing P4.1–P4.6; tag `orbital-test-v1`.

## 4. Academic-integrity protocol

- **Provenance and checksums.** Every input verified against `data/PROVENANCE.md`
  before use (step 1); every output's SHA-256 in the audit log; the sealed blind map's
  hash committed *before* measurement so unblinding cannot be silently re-rolled.
- **Verbatim quotation.** Every quoted string is copied character-for-character, with
  URL and access date, from `VALIDATION_REPORT.md` §8 or the methodology's Sources.
  No new DOI, URL, dataset ID, author, or quotation may be introduced; a
  needed-but-absent source is written as "[source to be located and verified during
  execution - do not cite until verified]".
- **Pre-registration discipline.** Phase 4 executes `prereg-v1` and nothing else; the
  results document cites its commit hash. Post-data-contact ambiguity is resolved by
  an appending, owner-signed amendment that may clarify procedure but never alter a
  band, threshold, percentile, or selection rule; the amendment is dated.
- **Blinding and confirmation-bias controls.** Measurement agents receive only
  neutral-ID tiles in randomized order, never told which is Object X or what H1
  predicts; the grader never sees images; the map stays sealed until the freeze
  commit. Enumeration is union-of-duplicates; the owner may add, never remove.
- **AI-assistance disclosure.** The results document discloses that all agents are
  claude-fable-5 (§5), prompts and JSON archived in `results/phase4/audit/`; the
  repo's history of AI-fabricated validation (F8) is why roles B9/B10 exist.
- **Error-correction and retraction.** Post-commit errors are corrected by an
  appended erratum (old value, new value, cause) — never by silent edit. If the
  registration or box definition is later invalidated, every downstream result is
  voided in writing and any re-run labeled as such.
- **Null-result commitment.** The results document is committed "regardless of
  outcome" (roadmap exit criterion); the H0-favorable outcome gets the same data
  table, error budgets, and care as any positive, per the Cydonia precedent
  (`VALIDATION_REPORT.md` §7; NASA PIA03225): higher resolution plus a published null.

## 5. Agent fan-out design

Orchestration: Claude Code Workflow `agent()`/`parallel()`/`pipeline()`; all agents
inherit claude-fable-5. Each agent receives only the inputs its role names (manifests
archived); measurement agents are denied the pre-registration, labels, and each other.

| Role | Count | Independence / blinding arrangement |
|---|---|---|
| B1 Precondition auditor | 1 | Runs first, alone; read-only; pass/fail per item |
| B2 Registration solver | 2 (+1 tiebreak) | Isolated worktrees; identical inputs (PSP_001890_1995, `pipeline-v1` summit columns, constants); blind to each other |
| B3 Candidate enumerator | 2 | Blind duplicates; identical inputs (corridor overlay, PSP_001890_1995); union reconciliation; not told what H1 predicts |
| B4 Population enumerator | 2 | Blind duplicates; apply the `prereg-v1` rule text mechanically; union reconciliation |
| B5 Blind measurer | 3 (2 per object) | Neutral-ID tiles, randomized order, candidates and population interleaved; receive only the algorithm-only metric-specification excerpt (stripped of hypothesis bands, thresholds, percentiles, and any mention of Object X; excerpt SHA-256 in the audit trail); no access to sealed map, the pre-registration itself, or each other |
| B6 Relief measurer | 2 | Blind duplicates on the same neutral IDs; DTM or stereo branch per the P1.3 record; same isolation as B5 |
| B7 Statistics checker | 1 | Recomputes distributions, percentiles, and grades from raw JSONL; implementation independent of B8 |
| B8 Grader | 1 | Sees only reconciled numbers, the unsealed map, and `preregistration/PREREGISTRATION.md`; never sees an image |
| B9 Adversarial verifier | 3 | Each independently prompted to **REFUTE**: a registration flaw, a missed candidate, a blinding leak, a grading deviation from `prereg-v1`, an unfalsifiable statement; fresh contexts; verdicts hidden from each other |
| B10 Source verifier | 2 | Independently diff every quote, number, URL, citation in the draft against the §8 register, methodology Sources, and `data/PROVENANCE.md` |

**Correlated-error limitation.** All duplicate agents are instances of the same
model (claude-fable-5): procedural isolation prevents information leakage between
them but not shared model-systematic priors, so duplicate agreement bounds
procedural/transcription error only, not model-systematic error. Where the protocol
supports it, the duplicates must take methodologically distinct routes — here, B2's
two solvers and B5/B6's paired measurers — with the route each duplicate took named
in the relevant step's audit record. A human spot-check of a randomized sample of
duplicate outputs is a standing checkpoint before phase close, recorded in the audit
log.

**Pattern.** `pipeline( B1 → parallel(B2×2) → reconcile → CHECKPOINT 1 →
parallel(B3×2, B4×2) → reconcile → CHECKPOINT 2 → tile factory →
parallel(B5×3, B6×2) → MEASUREMENT-FREEZE / UNBLINDING BARRIER → CHECKPOINT 3 →
parallel(B8, B7) → assemble → parallel(B9×3, B10×2) → disposition → CHECKPOINT 4 →
commit + tag )`. Everything else is ordinary pipeline dependency; the **one genuinely
necessary barrier is the measurement freeze**: all measurements committed and
hash-frozen before the neutral-ID map is unsealed — unblinding is irreversible.

**Structured-output contracts** (JSON, one file per agent in `results/phase4/audit/`):

- B2: `{"role":"registration","lander_px":{"x":0,"y":0,"sigma_px":0},"north_twin_px":{},"south_twin_px":{},"azimuth_map":{"col0_mrad":0,"mrad_per_product_px":0.196},"known_answer":{"predicted_sep_mrad":0,"imp_measured_sep_mrad":0,"delta_mrad":0,"pass":true},"inputs_sha256":{}}`
- B3/B4: `{"role":"enumeration","kind":"candidate|population","objects":[{"id":"","centroid_px":{},"range_m":0,"approx_long_axis_m":0}],"rule_text_sha256":"","count":0}`
- B5: `{"role":"blind_measure","tile_id":"","long_axis_m":0,"short_axis_m":0,"axis_azimuth_deg":0,"symmetry_score":0,"uncertainties":{},"error_budget":[{"term":"","value":"","contribution":""}]}`
- B6: `{"role":"relief","tile_id":"","relief_m":0,"sigma_m":0,"branch":"dtm|stereo","error_budget":[]}`
- B7: `{"role":"stats_check","population_n":0,"symmetry_threshold":{"quantile":0,"kc":0,"population_max_fallback":false,"value":0},"grades":{"H0_per_candidate":{},"H1_per_candidate":{}},"matches_grader":true,"discrepancies":[]}`
- B8: `{"role":"grading","prereg_commit":"","per_candidate":[{"id":"","plan_clause":"pass|fail","relief_clause":"pass|fail|untestable","symmetry_clause":"pass|fail","H1":"pass|fail","H0":"retained|rejected|not gradable (n < 20)"}],"multiplicity":{"k":0,"candidates_graded":0,"m":0,"fw_bound_m_over_n_plus_1":0,"confirmatory":true},"verdict_text":""}`
- B9: `{"role":"adversarial","verdict":"NO_OBJECTION|OBJECTION","objections":[{"target":"P4.x / draft §","claim":"","severity":"blocking|minor","proposed_fix":""}]}`
- B10: `{"role":"source_verification","quotes_checked":0,"mismatches":[],"unregistered_citations":[],"pending_live_checks":[]}`

**Acceptance thresholds.** B2 pair: numeric gates of §3 steps 2–3 (±4 map px;
±1.0 mrad; known-answer ≤ 2.0 mrad); else tiebreak; no two-of-three agreement →
phase failure (§7). B3/B4: union reconciliation; population n ≥ 30 required. B5/B6:
per-object duplicate agreement per §3 step 7, with third-measurer escalation and
"unmeasured" disclosure. B7 must reproduce B8's every grade exactly; persistent
discrepancy halts the phase (the grading rule was ambiguous — a documented Phase 3
escape). B9: a blocking objection sustained by ≥ 2 of 3 verifiers after one
revision-and-rereview round **kills** the affected result — an adversarial majority
is a veto, not advice; every sustained objection gets a written disposition. B10:
hard gate — zero unregistered citations, zero verbatim mismatches.

**Human-in-the-loop checkpoints** (owner sign-off, recorded in the audit log):
**(1)** registration overlay confirmed before the corridor is cast; **(2)** candidate
list — owner may add, never remove, before tiles are cut; **(3)** unblinding — owner
confirms the freeze commit exists and authorizes unsealing `blind_map_sealed.json`;
**(4)** final results-document hash, before the P4 commit and tag. The owner talks to
measurement agents only through the orchestrator, so checkpoint knowledge cannot leak
identities into blind measurements.

## 6. Quality gates and exit criteria

All must hold, measurably, at phase close:

1. Registration known-answer gate passed (delta ≤ 2.0 mrad per accepted solver);
   duplicates within ±4 map px / ±1.0 mrad; solution published with uncertainties.
2. Candidate list is the union of blind duplicates, zero owner-removed entries; every
   candidate measured or explicitly recorded "unmeasured" with cause.
3. Population n ≥ 30 measured under blinding (or shortfall disclosed per §7); every
   measurement row carries a Step 5 error budget.
4. Unblinding-barrier integrity: freeze commit predates map unsealing in the audit
   log; sealed-map hash matches the pre-measurement commit.
5. Every `prereg-v1` hypothesis graded pass/fail (or a clause recorded untestable per
   the pre-registered branch rules) by B8, reproduced exactly by B7; P4.6 gate
   computed for every candidate, outcome recorded whether it passes or not.
6. Zero unregistered citations (B10); **zero** sustained blocking adversarial
   objections outstanding (B9) — a written disposition may resolve an objection, but
   an unresolved sustained blocking objection blocks the tag; AI-assistance
   disclosure present.
7. Roadmap exit criterion satisfied as written: results document committed regardless
   of outcome; owner sign-off and tag `orbital-test-v1` exist.

## 7. Failure modes and stopping rules

- **Precondition failure** (checksum mismatch, missing tag, ordering violated): hard
  stop; return to the earlier phase; no output under a violated precondition is kept.
- **Registration failure** (known-answer gate unmet by two of three solvers): phase
  halts at P4.1 — a registration failure, not evidence about Object X; the corridor
  is never cast from an unvalidated solution.
- **Empty corridor**: recorded as a result — H1's plan clause fails (no candidate in
  the 62.05–83.95 m band along the sight line). Unanticipated clauses go through an
  owner-signed clarifying amendment, disclosed as post-data-contact.
- **Multiple candidates**: all measured, all graded (P4.2), every grade reported. H1
  is not declared passed by picking the best-performing candidate unless it also
  passes the P4.6 gate; the multiplicity is itself reported.
- **Relief untestable** (no DTM per P1.3 and the named stereo branch inexecutable):
  relief clause graded "untestable as pre-registered" per the Phase 3 rule; H1 graded
  on its remaining clauses, gap disclosed; no substitute method improvised mid-phase.
- **Population shortfall** (n < 30): disclosed; the symmetry-percentile clause is
  graded only if the pre-registration's conditions are met, else recorded
  not-gradable. The radius is **not** widened after data contact — post hoc.
- **Cross-instrument gate failure** (P4.6 inconsistent): the result stands as
  "association unconfirmed"; nothing is adjusted to force closure; it is published.
- **Blinding breach**: affected measurements voided and re-run with fresh agents; the
  breach permanently disclosed, never quietly laundered.
- **Standing rule, restated:** a pre-registered hypothesis that fails its band is
  recorded as failed. A revised hypothesis is a *new* pre-registration tested against
  new or held-out data — never a retro-fit to the data that killed its predecessor,
  never rescued by re-measuring, re-registering, or re-selecting.

## 8. Deliverables

| Deliverable | Path / ref | Content |
|---|---|---|
| Results document | `results/PHASE4_RESULTS.md` | Verdicts for H0/H1 per candidate, full data table, error budgets, P4.6 closure, null-result text if applicable, AI-assistance disclosure, `prereg-v1` hash |
| Data tables | `results/phase4/registration_solution.json`, `{candidates,population}.csv`, `measurements.jsonl` | P4.1 solution with known-answer record; P4.2 union list; P4.4 selection-rule output; all B5/B6 rows frozen at the barrier — neutral IDs throughout |
| Blind map | `results/phase4/blind_map_sealed.json` (+ unsealed copy post-barrier) | ID→identity mapping; sealed hash committed pre-measurement |
| Scripts | `analysis/phase4/{register_imp_hirise,cast_corridor,make_tiles,grade_hypotheses}.py` | Deterministic, re-runnable from provenance-logged inputs |
| Figures | `analysis/phase4_registration_overlay.png`, `analysis/phase4_corridor_overlay.png` | Checkpoint 1 and 2 exhibits |
| Audit trail | `results/phase4/audit/*.json` | All agent JSON, input manifests, objection dispositions, sign-offs, freeze/unseal ordering |
| Commits | referencing P4.1–P4.6 | Measurement-freeze commit distinct from and preceding the grading commit |
| Tag | `orbital-test-v1` | On the results commit; Phases 6 and 7 cite the tag, not a branch tip |

No existing repository file is modified in this phase; Phase 4 only adds files.
