# Phase 3 Execution Plan - Operational Definition of Object X and Pre-Registration

**Roadmap section:** `ROADMAP.md` Phase 3 (tasks P3.1–P3.5). **Standing rules apply**
(pre-register before you look; every number carries an error budget; no post-hoc rescue;
publish the null result).

## 1. Objective and scope

Convert "Object X" from an annotation on a ~99-inch print (`preview (3).webp`;
post-P0.5 name `preview_3.webp`) into a
falsifiable claim: a pixel-box operational definition on the archival products, plus
pre-registered hypotheses with numeric tolerance bands and a fully specified Phase 4
test. Per the roadmap, *"This phase deliberately contains **no** new measurements of
Object X."* The only image operations permitted are **geometric registration** steps
(print-to-pixel conversion, cross-eye framing offset); any size, relief, or morphology
measurement of Object X is out of scope and constitutes a protocol breach.

Roadmap exit criteria, quoted verbatim and adopted unchanged:

> "a reader in Phase 4 can execute the test with no further judgment calls — every
> threshold and selection rule already fixed."

Scope boundaries:

- In scope: P3.1 (pixel boxes on PIA02405 and PIA02406), P3.2 (anchor interpretations
  and their consequences), P3.3 (hypotheses with tolerances), P3.4 (discriminating
  measurements, thresholds, comparison-population selection rule), P3.5
  (pre-registration commit, append-only thereafter).
- Out of scope: any inspection of HiRISE pixels at or near the Object X sight line
  (that is Phase 4 data contact); any re-measurement of Twin Peaks beyond the
  known-answer registration check; any edit to existing repo documents.

Calibrated-language rule (F6): all Phase 3 text must preserve the finding that
**Object X's size is indeterminate from the IMP image alone** — the caption places the
hummocks "a few tens of meters away from the lander to the distance of the South Twin
Peak" (NASA Photojournal PIA02405 catalog page), a factor-of-~33 range and size ambiguity
(30 m to 1006 m).

## 2. Inputs and preconditions

Hard dependencies (phase may not start until all exist):

1. **Phase 1 complete.** `data/PROVENANCE.md` lists, with SHA-256: `PIA02405.tif`
   (65.93 MB per catalog page), `PIA02406.tif` (P1.1); the P1.3 record of whether an
   archived HiRISE DTM exists for PSP_002391_1995 (the *text* of that record only — no
   HiRISE pixels are opened in Phase 3); the P1.5 quote spot-check results.
2. **Phase 2 complete.** Tag `pipeline-v1` exists; falsification gates of
   `SIZE_VERIFICATION_METHODOLOGY.md` Step 6 passed at full resolution (P2.5). The
   Phase 2 pipeline supplies the measured summit pixel columns of North and South Twin
   used as this phase's known-answer registration check.
3. Repository-internal inputs: `preview (3).webp` (annotated scale system; post-P0.5
   name `preview_3.webp`); `preview.webp` (left-eye downscale, 4.616:1 per
   `VALIDATION_REPORT.md` §2); `preview (1).webp` (right-eye downscale; post-P0.5 name
   `preview_1.webp`; ratio 7296 px / 1568 px = 4.653:1);
   `analysis/measure_twin_peaks.py` at tag `pipeline-v1`.
4. Constants carried from the validated record: product sizes 7238×3135 (left) and
   7296×3135 (right); 43-in print height spanning 3135 px → 72.9 product px/in;
   1 product px = 0.196 mrad; IFOV 0.98 mrad/px (Smith et al. 1997,
   doi:10.1029/96JE03568); cross-eye mosaic framing offset ≈175 product px at the
   summits (North 174, South 176; `VALIDATION_REPORT.md` §5.1).

**Network access: none.** Every step in this phase runs inside the analysis sandbox on
files already provenance-logged in Phase 1. If any P1.5 live-page spot-check is still
pending, source verification (step 8 below) checks against the in-repo catalog PDFs and
the §8 register only, and the pre-registration document flags the affected quotes as
"live verification pending (P1.5)". No new downloads, no new sources.

## 3. Research protocol

Numbered SOP. Every step names its roadmap task ID. "Product px" means pixels of the
full-resolution TIFFs.

1. **[P3.1] Freeze inputs.** Record SHA-256 of `preview (3).webp`, `preview.webp`,
   `preview (1).webp` (post-P0.5 names: `preview_3.webp` / `preview_1.webp`),
   `PIA02405.tif`, `PIA02406.tif` into
   `preregistration/audit/inputs_sha256.json`; verify against `data/PROVENANCE.md`.
2. **[P3.1] Derive the left-eye pixel box (two blind duplicates).** Each box-derivation
   agent, independently: (a) reads the Object X annotation extents off
   `preview (3).webp` (`preview_3.webp` post-P0.5; ruler x ≈ 60–63 in per `VALIDATION_REPORT.md` §5.5, just right
   of North Twin's flank); (b) converts print inches → product px two ways —
   via the sole traceable relation, 3135 px / 43 in = 72.907 product px/in (the
   width route 7238 px / ~99 in is algebraically the same relation, not an
   independent one, and is not used), cross-checking by locating the annotation
   box on `preview.webp` and scaling by 4.616:1; (c) reports the box
   (x₁,y₁)–(x₂,y₂) in product px with a per-edge uncertainty. Expected x-range from
   the stated print coordinates: 60×72.907 to 63×72.907 ≈ 4374–4593 product px
   (derivation shown; final values are whatever the reconciled duplicates report).
3. **[P3.1] Known-answer registration gate.** Each duplicate also predicts the summit
   pixel columns of North and South Twin from their print coordinates via the same
   conversion, and compares against the `pipeline-v1` measured summit columns.
   Tolerance: |Δ| ≤ 25 product px (≈5 native px ≈ 1/3 print inch) for both peaks. A
   deriver failing this gate is discarded and rerun fresh; the conversion is not
   trusted until the gate passes.
4. **[P3.1] Reconcile duplicates.** Orchestrator compares the two blind boxes. Accept
   if all four edges agree within ±25 product px; the published box is the union of
   the two, with the disagreement recorded as the box-edge uncertainty. On failure,
   one additional blind deriver runs; if no two of three agree within tolerance, the
   box is **indeterminate** — see §7 stopping rules.
5. **[P3.1] Derive the right-eye box (two blind duplicates).** Starting estimate:
   left box + summit framing offset (174–176 px). Each cross-eye agent refines the
   local offset by cross-correlating a horizontal skyline strip near (but excluding)
   the box between the two TIFFs — a registration measurement, explicitly not a
   measurement of Object X. Acceptance: the two offset estimates agree within
   ±10 product px (≈2 native px); boxes reconciled as in step 4.
6. **[P3.2] Record the anchor interpretations** verbatim from `VALIDATION_REPORT.md`
   §5.5, with consequences: **(i)** if at North Twin range (860 m): corrected height
   ≈ 9.1 m, corrected length ≈ 32 m — roughly half Sphinx scale (Sphinx: 73 m long,
   20 m high, *Encyclopædia Britannica*, "Great Sphinx of Giza"); **(ii)** if in the
   near hummock field ("a few tens of meters"): ~20× smaller. State explicitly that
   the IMP image alone cannot decide between them (F6), and that the aspect ratio
   (≈0.286 vs Sphinx 0.275) has no discriminating power for artificiality
   (`VALIDATION_REPORT.md` §5.5). The "+18½ ft earth face" buried-portion conjecture
   is recorded as dropped (no observational support).
7. **[P3.3] Draft the hypotheses with tolerance bands** (drafting agent, HiRISE-blind):
   - **H0 (null):** Object X is a flood-debris hummock statistically indistinguishable
     in plan long axis, aspect ratio, and relief from the local hummock population.
   - **H1 (sphinx-scale):** plan length 73 m ± 15 % → acceptance band 62.05–83.95 m
     (73×0.85 = 62.05; 73×1.15 = 83.95); relief 20 m ± 25 % → band 15.0–25.0 m; AND
     bilateral symmetry exceeding the comparison-population distribution at the
     pre-registered percentile (step 8).
   - Any additional hypothesis proposed by the repository owner is written here now,
     with numeric tolerances, or it may not be tested in Phase 4.
8. **[P3.4] Draft the discriminating measurements and fixed decision rules:**
   - Plan dimensions: pixels × 25 cm on the map-projected HiRISE product
     (PSP_001890_1995, "map-projected to 25 cm/pixel", uahirise.org page).
   - Relief: from the PSP_002391_1995 DTM if the P1.3 record says one is archived;
     otherwise the **fixed no-DTM fallback branch recorded in the Phase 1 plan §3 step S6
     no-DTM row**, restated here so the pre-registration is self-contained: relative
     heights from the PSP_001890_1995 / PSP_002391_1995 stereo pair by area-based
     image correlation on map-projected tiles; vertical datum from ≥ 5 control points
     on terrain of assumed-zero relative relief; parallax-to-height conversion from
     the observation geometry stated on the two HiRISE catalog pages; error model
     propagating matching precision (assumed ±0.5 px until measured) through that
     geometry; software toolchain as named in the P1.3 provenance record at
     acquisition time, marked "[software to be located and verified during execution -
     do not cite until verified]". Whichever branch applies is fixed *now*, in
     writing, from the P1.3 text alone — no mid-phase improvisation is possible.
   - Symmetry metric, fixed in advance: mirror-correlation score about the best-fit
     long axis (as named in roadmap P3.4), computed identically for each candidate and
     every population member. H1's symmetry clause passes for a candidate only if its
     score exceeds the empirical 1 − (0.05/kc) quantile of the population's scores
     (linear-interpolation empirical quantile estimator), where kc = number of
     enumerated candidates graded — a cross-candidate correction (kc = 1 recovers the
     95th percentile: 1 − 0.05/1 = 0.95). If 0.05/kc < 1/(n+1), the quantile lies
     beyond the data (e.g., n = 30, kc = 2: 0.05/2 = 0.025 < 1/31 ≈ 0.032); in that
     case the clause is graded against the population **maximum**, and this fallback
     is stated in the results table. (The threshold rule is a protocol parameter
     fixed at pre-registration; adversarial review may adjust it *before* the P3.5
     commit, never after.)
   - Comparison population selection rule, fixed before any member is examined: all
     hummocks within 1.2 km of the lander position whose plan long axis is ≥ 5 m
     (= 20 px at 25 cm/px — a resolution-motivated floor, derivation shown), target
     n ≥ 30 per roadmap P3.4. Enumeration and measurement happen in Phase 4 (P4.4),
     in randomized order with neutral IDs; Phase 3 fixes only the rule text.
   - Grading rule, H1: H1 passes only if **all three** clauses (plan length, relief,
     symmetry) pass; any clause failing its band fails H1.
   - Grading rule, H0 (per candidate, fully numeric): H0 is graded **per enumerated
     candidate**. For each candidate and each named primary metric (the H0 metrics:
     plan long axis, aspect ratio, relief; k = 3), compute the candidate's value and the
     comparison population's empirical distribution (linear-interpolation empirical
     quantile estimator; n = population size). H0 is rejected for a candidate **iff**
     its value falls outside the population's observed min–max envelope on at least
     one primary metric. Significance derivation: under H0 the candidate's value and
     the n population values are n+1 exchangeable draws from one distribution, so the
     probability the candidate is the strict one-sided extreme (above the max, or
     below the min) of the n+1 values is ≤ 1/(n+1); an envelope exceedance therefore
     has one-sided empirical p ≤ 1/(n+1) (e.g., n = 30 → p ≤ 1/31 ≈ 0.032).
   - Multiplicity: report m = k × (number of candidates graded); the family-wise
     bound on any envelope rejection is m/(n+1). A rejection is CONFIRMATORY only if
     m/(n+1) ≤ 0.10 (e.g., k = 3, one candidate, n = 30: m = 3, 3/31 ≈ 0.097 ≤ 0.10);
     otherwise it is recorded verbatim as "suggestive, not confirmatory" and cannot
     support an artificiality-related claim.
   - Gradability: envelope/percentile clauses are gradable iff the population has
     n ≥ 20; below that the clause is recorded "not gradable (n < 20)" — never
     improvised.
   - Association gate: the overall Object X verdict is conditional on the P4.6
     cross-instrument association gate — only candidates passing P4.6 association
     bear on the Object X hypotheses; per-candidate verdicts for non-associated
     candidates are reported but bear only on population characterization.
   - Ambiguity resolution (multiple candidates on the sight line) follows P4.2:
     enumerate all candidates; each is graded; no post-hoc choice.
9. **[P3.5] Assemble, verify, sign, commit.** Assemble steps 1–8 into the
   pre-registration document; run the verification fan-out (§5); obtain owner
   sign-off; commit as the pre-registration commit; tag `prereg-v1`. After this
   commit, the document may only gain an appending "Amendments" section.

## 4. Academic-integrity protocol

- **Provenance and checksums.** Every input file's SHA-256 recorded (step 1) and
  re-verified against `data/PROVENANCE.md`; the pre-registration document's own SHA-256
  is computed at sign-off and quoted in the P3.5 commit message. No file outside
  `data/PROVENANCE.md` may be cited (Phase 1 exit rule).
- **Verbatim quotation.** Every quoted source string in the pre-registration is copied
  character-for-character from `VALIDATION_REPORT.md` §8 register entries or the in-repo
  catalog PDFs, with URL and access date as recorded there. **No new DOI, URL, dataset
  ID, author, or quotation may be introduced in this phase.** A needed-but-absent source
  is written as "[source to be located and verified during execution - do not cite until
  verified]".
- **Pre-registration discipline.** The P3.5 commit is the timestamp; roadmap standing
  rule: the pre-registration commit must precede the Phase 4 results commit. Nothing in
  the committed document is edited afterward except by appending amendments; an
  amendment made after Phase 4 data contact may clarify execution ambiguity but may
  never alter a tolerance band, threshold, percentile, or selection rule.
- **Blinding and confirmation-bias controls.** No Phase 3 agent or human opens HiRISE
  pixels (PSP_001890_1995 / PSP_002391_1995) at any point; hypotheses and thresholds
  are therefore written blind to Object X's orbital appearance. Box derivation runs as
  blind duplicates (§5). Only the P1.3 *textual* DTM-availability record may be read.
  A blinding breach is recorded permanently in the pre-registration (see §7).
- **AI-assistance disclosure.** The pre-registration document carries a disclosure
  section: drafted and verified by claude-fable-5 agents under the orchestration in §5,
  with agent prompts and JSON outputs archived in `preregistration/audit/`. This repo's
  history (F8: AI-fabricated citations in the 2025 documents) is the explicit reason
  the source-verification role exists.
- **Error-correction and retraction.** Arithmetic or transcription errors found after
  P3.5 are corrected in the Amendments section showing old value, new value, and cause.
  If the pixel box is later shown to misidentify the annotated feature, all Phase 4
  results derived from it are voided, the void is recorded, and any re-run happens
  under an amended definition labeled as such — never silently.
- **Null-result commitment.** The pre-registration itself must contain the sentence
  committing to publish the H0-favorable outcome (e.g., "Object X is a 9-meter hummock
  like its 30 neighbors," roadmap P4.5) with the same care as any positive, per the
  Cydonia precedent (`VALIDATION_REPORT.md` §7; NASA PIA03225).

## 5. Agent fan-out design

Orchestration: Claude Code Workflow `agent()`/`parallel()`/`pipeline()`; all agents
inherit claude-fable-5. All agents are sandboxed to the repo, given only the inputs
their role names, and **denied HiRISE files** by instruction and by input manifest.

**Correlated-error limitation (standing).** Duplicate agents are instances of the same
model (claude-fable-5). Procedural isolation prevents information leakage between
duplicates but not shared model-systematic priors, so duplicate agreement bounds
procedural/transcription error only, not model-systematic error. Where the protocol
supports it, duplicates must take methodologically distinct routes. **Note (correction,
2026-08-04):** for the A1 box derivers no such distinct route exists — the "horizontal
via print width" and "vertical via 43-in/3135-px" conversions are algebraically the same
relation, so the duplicates provide **procedural independence only** (independent
transcription and boundary judgement), not methodological independence. The genuinely
independent cross-check available to them is locating the annotation box on
`preview.webp` and scaling by 4.616:1, which is a different raster. This limitation is
stated rather than papered over. A human spot-check of a randomized sample of duplicate
outputs is a standing checkpoint before phase close.

| Role | Count | Independence / blinding arrangement |
|---|---|---|
| A1 Box deriver (left eye) | 2 (+1 on tiebreak) | Isolated worktrees; identical inputs (`preview (3).webp` [`preview_3.webp` post-P0.5], `preview.webp`, `PIA02405.tif`, conversion constants); no access to each other's output; must not open HiRISE or right-eye files |
| A2 Cross-eye registrar | 2 | Run only after A1 reconciliation; identical inputs (both TIFFs, reconciled left box, summit offsets); blind to each other; forbidden from measuring inside the box |
| A3 Pre-registration drafter | 1 | Drafts steps 6–8 text from `ROADMAP.md` P3.2–P3.4 and `VALIDATION_REPORT.md` §5.5 only; never sees any image file at all |
| A4 Adversarial verifier | 3 | Each independently prompted to **REFUTE** the assembled draft: find any step a Phase 4 stranger could not execute without a judgment call, any unfalsifiable clause, any nondeterministic selection rule; fresh contexts; not shown each other's verdicts |
| A5 Source verifier | 2 | Independently diff every quote, number, URL, and citation in the draft against the §8 register, in-repo PDFs, and P1.5 results; flag any citation absent from the register |
| A6 Statistics checker | 1 | Recomputes all tolerance-band arithmetic; checks H0/H1 are jointly exhaustive-or-gradable, the symmetry percentile rule is well-defined against an n ≥ 30 empirical distribution, and the grading rule has no undefined branch |

**Pattern.** `pipeline( parallel(A1×2) → reconcile → parallel(A2×2, A3) → ASSEMBLY
BARRIER → parallel(A4×3, A5×2, A6) → disposition → human sign-off → commit )`.
The one genuinely necessary barrier is **assembly**: A4/A5/A6 must review the
byte-exact document that will be committed, so every upstream output must be merged and
frozen (hash recorded) before the verification fan-out launches. Everything before it
is ordinary pipeline dependency; everything after is the human gate.

**Structured-output contracts** (JSON, one file per agent in `preregistration/audit/`):

- A1: `{"role":"box_derivation","eye":"left","product_id":"PIA02405","box_product_px":{"x1":0,"y1":0,"x2":0,"y2":0},"edge_uncertainty_px":0,"px_per_print_inch":{"horizontal":0,"vertical":0},"known_answer":{"north_twin_delta_px":0,"south_twin_delta_px":0,"pass":true},"inputs_sha256":{},"method_notes":""}`
- A2: `{"role":"cross_eye","product_id":"PIA02406","box_product_px":{},"framing_offset_px":0,"offset_method":"skyline strip cross-correlation excluding box","residual_px":0}`
- A4: `{"role":"adversarial","verdict":"NO_OBJECTION|OBJECTION","objections":[{"target":"P3.x / draft §","claim":"","severity":"blocking|minor","proposed_fix":""}]}`
- A5: `{"role":"source_verification","quotes_checked":0,"mismatches":[],"unregistered_citations":[],"pending_live_checks":[]}`
- A6: `{"role":"stats_check","checks":[{"item":"","expected":"","found":"","pass":true}],"overall":"pass|fail"}`

**Acceptance thresholds.**

- A1 pair: all four edges within ±25 product px AND both known-answer deltas
  ≤ 25 product px per deriver; else tiebreak deriver; no two-of-three agreement →
  phase failure path (§7).
- A2 pair: framing offsets within ±10 product px; boxes within ±25 px per edge.
- A4: a blocking objection sustained by ≥ 2 of 3 verifiers after one revision-and-rereview
  round **kills** the affected clause (it is removed or the phase halts) — an
  adversarial majority is a veto, not advice. A single sustained blocking objection
  requires a written disposition in the audit log before sign-off.
- A5: hard gate — zero unregistered citations and zero verbatim mismatches tolerated.
- A6: `overall: pass` required; any failed check is corrected and the *entire*
  verification fan-out reruns on the reassembled draft (new hash, new barrier).

**Human-in-the-loop checkpoints** (repository owner sign-off required, recorded in the
audit log):

1. After step 4: owner confirms the box overlay figure marks the feature they intended
   as "Object X" — the one judgment only the annotator can make.
2. After verification: owner signs the final document hash; only then does the P3.5
   commit proceed.
3. Any post-commit amendment requires owner sign-off before it is appended.

## 6. Quality gates and exit criteria

All must hold, measurably, at phase close:

1. Both pixel boxes published with per-edge uncertainties; duplicate agreement within
   the ±25/±10 product-px thresholds; known-answer registration gate passed by every
   accepted deriver (both peaks, ≤ 25 product px).
2. Every hypothesis clause carries a numeric band traceable to roadmap P3.3 or a
   derivation shown in the document; A6 reports `pass`.
3. Zero unregistered citations (A5); every quote verbatim with URL and access date.
4. Zero sustained blocking adversarial objections outstanding (A4). A written
   disposition in the audit log may resolve an objection; any unresolved sustained
   blocking objection blocks the P3.5 commit and the `prereg-v1` tag.
5. F6 language intact: the document states that Object X's size is indeterminate from
   the IMP image alone and that Phase 3 measured nothing about Object X.
6. Owner sign-off recorded; P3.5 commit and `prereg-v1` tag exist; commit precedes any
   Phase 4 activity (the roadmap's "single most important ordering rule").
7. Roadmap exit criterion satisfied as written: a Phase 4 executor needs no further
   judgment calls — verified operationally by A4's failure to construct one.

## 7. Failure modes and stopping rules

- **Box indeterminate** (no two-of-three deriver agreement, or owner cannot confirm the
  feature at checkpoint 1): Phase 3 **fails**. Record the failure; Object X remains an
  annotation, not a measurable claim; Phase 4's P4.2 sight-line cast cannot proceed.
  The recorded options are (a) recover better annotation provenance and re-run Phase 3
  from step 2, or (b) close the Object X question as unfalsifiable-as-posed and publish
  that. No box may be "improved" by peeking at HiRISE to see what is there.
- **Blinding breach** (any Phase 3 participant views HiRISE pixels of the site): the
  breach is permanently disclosed in the pre-registration; the pre-registration is
  demoted from "blind" to "disclosed-exposure" status in all later write-ups. It is
  never quietly re-run to launder the status.
- **Untestable clause discovered** (e.g., P1.3 records no DTM and no executable stereo
  relief method can be specified): the relief clause is recorded as untestable and H1
  is graded in Phase 4 on its remaining clauses, with the gap disclosed — the clause is
  not deleted from history and no substitute is improvised mid-Phase-4.
- **Precondition violation** (Phase 2 gates unpassed, provenance entries missing):
  hard stop; return to the earlier phase. No Phase 3 output produced under a violated
  precondition is retained.
- **Standing rule, restated as the stopping rule for everything above:** a
  pre-registered hypothesis that fails its band in Phase 4 is recorded as failed. A
  revised hypothesis is a *new* pre-registration (appended amendment, new commit,
  tested against new or held-out data) — never a retro-fit to the data that killed its
  predecessor.

## 8. Deliverables

| Deliverable | Path / ref | Content |
|---|---|---|
| Operational definition | `preregistration/OBJECT_X_DEFINITION.md` | P3.1 boxes (both eyes, uncertainties), P3.2 anchor interpretations, F6 statement, overlay figure reference |
| Pre-registration | `preregistration/PREREGISTRATION.md` | P3.3 hypotheses with bands, P3.4 measurements/thresholds/selection rule, grading rules, null-result commitment, AI-assistance disclosure, (later) Amendments section |
| Box overlay figure | `analysis/phase3_box_overlay.png` | Reconciled boxes drawn on downscaled copies of both eyes |
| Audit trail | `preregistration/audit/*.json` | All agent JSON outputs, input hashes, objection dispositions, owner sign-offs |
| Pre-registration commit | git commit referencing P3.1–P3.5 | Message quotes the document SHA-256; this is the timestamp Phase 4 is measured against |
| Tag | `prereg-v1` | On the P3.5 commit; Phase 4 cites the tag, not a branch tip |

No existing repository file is modified in this phase; Phase 3 only adds the files
above.
