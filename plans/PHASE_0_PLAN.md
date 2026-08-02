# Phase 0 Execution Plan - Repository hygiene

## 1. Objective and scope

Roadmap authority: `ROADMAP.md`, "Phase 0 — Repository hygiene (can start immediately)".
Objective, quoted: *"make the repo safe to cite from — no reader should be able to
mistake an invalidated claim for a live one."*

Exit criteria, quoted verbatim from the roadmap: **"every document in the repo either
passes the validation report's findings or visibly carries the finding that invalidates
it."**

Scope is exactly tasks P0.1–P0.5. Phase 0 makes **no new measurements of Mars**, tests
no hypotheses about the scene, and touches historical documents only by (a) prepending
status headers, (b) renaming files, and (c) updating file-path references. The single
in-repo measurement-like activity is P0.4 (re-reading the point-E entries in the
annotated image), which concerns bookkeeping of the *record*, not the Martian surface.
Object X's size remains indeterminate from the IMP image alone (F6); nothing in this
phase changes that.

Out of scope: any content edit to the historical documents' body text; any download;
any quote verification against live pages (that is P1.5); any judgement on whether
Object X is natural or anomalous.

## 2. Inputs and preconditions

| Input | Status | Role |
|---|---|---|
| `VALIDATION_REPORT.md` (findings F1–F9, source register §8) | in repo | sole source of header content and citations |
| `SIZE_VERIFICATION_METHODOLOGY.md` | in repo | referenced by headers as the corrective protocol |
| `ROADMAP.md` Phase 0 | in repo | task definitions P0.1–P0.5 |
| `chat-history.txt` | in repo | provenance evidence for "AI-generated, June 2025" |
| `preview (3).webp` (annotated scale system) | in repo | P0.4 input image |
| `mars_stereo_analysis.md`, `mars_stereo_analysis (1).md`, `stereo_methodology_paper.md` | in repo | P0.1 targets |
| `interplanetary_civilization_hypothesis.md` | in repo | P0.2 target |
| `pareidolia_vs_measurement.md` | in repo | P0.3 target |
| Git working tree clean at a recorded base commit | precondition | diff auditing (§5) requires it |

Dependency phases: **none** — the roadmap marks Phase 0 "can start immediately," and it
blocks nothing except that P0.5's renames should land before later phases hard-code
paths in new scripts.

**Network access: none required.** Every input is in-repo. Headers quote
`VALIDATION_REPORT.md`'s findings and its §8 source register as recorded there; the
report itself notes its external quotes "should be spot-checked against the live pages
when re-run outside the sandbox" — that spot-check is task **P1.5, not Phase 0**, and
each header that carries an external citation must say so (see §4). Any step that would
need a page fetch is out of scope here by construction.

## 3. Research protocol

Executed in three stages; Stage C starts only after the Stage-B barrier (§5).

**Stage A — audit and pre-commitment (parallel):**

1. **[exit-criterion enforcement; no new roadmap ID]** Build the document disposition
   table: list every tracked document (`*.md`, `*.txt`) and classify it as
   (i) *findings/protocol document — passes by construction* (`VALIDATION_REPORT.md`,
   `SIZE_VERIFICATION_METHODOLOGY.md`, `ROADMAP.md`, `README.md`, this plan),
   (ii) *evidence record* (`chat-history.txt` — preserved as-is, labeled in README if
   not already), (iii) *roadmap-named hygiene target* (the five files in P0.1–P0.3), or
   (iv) *other working-hypothesis document* (`intelligence_vs_nature_morphology.md`,
   `mars_earth_orientation_analysis.md`, `universal_morphology_cycles.md`,
   `visual_tunneling_camera_analysis.md`). For class (iv), record which findings F1–F9
   (if any) each document's claims collide with, with section-level pointers, and which
   roadmap task (if any) plans the document's disposition (P6.1 names
   `intelligence_vs_nature_morphology.md`; P6.4 names `universal_morphology_cycles.md`
   and `mars_earth_orientation_analysis.md`; `visual_tunneling_camera_analysis.md` is
   named by **no** roadmap task — its table row must record that gap explicitly as
   "no roadmap disposition task assigned; flagged for owner triage"). Class (iv)
   headers are applied only after owner sign-off (checkpoint HC-3, §5); refusing them
   leaves the exit criterion unmet (§7).
2. **[P0.4 pre-commitment]** Before anyone re-reads the image, fix the decision rule
   (this is the phase's one pre-registration; this plan's commit is its timestamp):
   two independent readers transcribe, from `preview (3).webp` alone, (a) the
   right-hand-table row for point E ("E. 7 7/8 TO D. 43 = 35 1/8" per
   `VALIDATION_REPORT.md` §4) and (b) the E entry in the scale box (36⅜ in per §4).
   Rule: **if** both readers return identical transcriptions **and** exactly one of the
   two recorded values is arithmetically consistent with the transcribed ruler position
   (consistency test: 43 − ruler-x = stated inches-from-D, to the 1/16 in), the
   inconsistent entry is marked erroneous and E's factor is recomputed from the
   consistent one; **otherwise E is retired.** Any recomputed factor must carry a
   propagated uncertainty of at minimum the ±1/16-in transcription resolution over the
   ~35-in baseline: (1/16 in) / 35⅛ in = 0.0625 / 35.125 ≈ 0.0018 ≈ 0.2 %, recorded
   alongside the factor in `analysis/POINT_E_RECONCILIATION.md`. Retirement is the default on any
   ambiguity — the report already notes E "is an assumption, not a NASA datum" (§4),
   so nothing downstream depends on rescuing it.

**Stage B — annotation (parallel per document):**

3. **[P0.1]** Prepend to `mars_stereo_analysis.md`, `mars_stereo_analysis (1).md`, and
   `stereo_methodology_paper.md` a delimited status header stating, per the roadmap:
   AI-generated (June 2025, per `chat-history.txt`); contains the circular distance
   validation (F1); the ~3-orders-of-magnitude stereo-error mistake (F2/F7); fabricated
   citations (F8); **superseded by `VALIDATION_REPORT.md`**; retained unaltered as part
   of the record — do not delete. Header format: an HTML-comment sentinel line, a
   blockquoted `> **STATUS (Phase 0, P0.1):** …` block citing findings by F-number with
   section pointers, a closing horizontal rule. No character of the body text changes.
4. **[P0.2]** Prepend the analogous header to
   `interplanetary_civilization_hypothesis.md`: its ¹²⁹Xe material contradicts the
   established radiogenic/escape account — Nature 352, 697 (1991); *EPSL* (2021);
   *Science Advances* (2024), as registered in `VALIDATION_REPORT.md` §6/§8 item 9 —
   and would need to overturn those sources to stand; see also F8 for the provenance
   of the supporting documents.
5. **[P0.3]** Prepend to `pareidolia_vs_measurement.md` the correction from
   `VALIDATION_REPORT.md` §6: measurement objectifies *size* claims only, not
   *identity* claims; identity claims are gated by resolution (resolution gate,
   `SIZE_VERIFICATION_METHODOLOGY.md` Step 6.4); the Cydonia precedent (§7/F9) is the
   governing example. Header-only; no inline edits.
6. **[P0.4]** Execute the Stage-A rule: two blind readers (§5) transcribe the image;
   arithmetic checker applies the consistency test (note the discrepancy magnitude as
   recorded: 36⅜ − 35⅛ = 1¼ in on ~35 in, ≈ 3.5 %, matching §4's figure). Write
   `analysis/POINT_E_RECONCILIATION.md` recording transcriptions, the rule, and the
   outcome — reconciled or retired — either way (null-result commitment, §4).
7. **[exit-criterion enforcement]** Apply owner-approved class-(iv) headers (from step
   1 + HC-3): a generic status block ("working-hypothesis document; contains claims
   addressed by `VALIDATION_REPORT.md` findings F…; not validated; disposition planned
   in ROADMAP.md P6.1" for `intelligence_vs_nature_morphology.md`, "…P6.4" for
   `universal_morphology_cycles.md` and `mars_earth_orientation_analysis.md`). For a
   class-(iv) document named in **no** roadmap task
   (`visual_tunneling_camera_analysis.md`), the header must instead state "no roadmap
   disposition task assigned; flagged for owner triage" — it may not cite P6.1/P6.4.
8. Commit Stage B: one commit per task ID (`P0.1: …`, `P0.2: …`, `P0.3: …`, `P0.4: …`),
   messages cross-referencing checkbox IDs per the roadmap's convention.

**— barrier: all content edits committed and diff-audited before any rename —**

**Stage C — renames and reference integrity:**

9. **[P0.5]** Rename by the deterministic rule *replace " (N)" with "_N"*, via
   `git mv` only: `mars_stereo_analysis (1).md` → `mars_stereo_analysis_1.md`;
   `preview (1).webp` → `preview_1.webp`; `preview (2).webp` → `preview_2.webp`;
   `preview (3).webp` → `preview_3.webp`. (`preview.webp`, the PDFs, and
   `chat-history.txt` are already script-safe; `analysis/measure_twin_peaks.py`
   references only `preview.webp` and needs no change — verified against the script
   text before this plan was written.)
10. **[P0.5]** Update references in all documents: every occurrence of an old name
    (known sites: `README.md`; `ROADMAP.md` P0.1/P0.5/P3.1; `VALIDATION_REPORT.md`
    §Scope/§2/§4/§8-internal-evidence; plus any found by the scanners) becomes the new
    name — except inside `ROADMAP.md` P0.5 itself and this plan, where the old name is
    the historical subject and is annotated "→ renamed `new_name`". Path-only edits to
    `VALIDATION_REPORT.md`/`ROADMAP.md`; no wording changes.
11. **[P0.5]** Run both independent reference scanners (§5) to zero stale references;
    re-run `python3 analysis/measure_twin_peaks.py` from the repo root as a smoke test
    (it must still find `preview.webp` and regenerate `analysis/skyline_overlay.png`).
12. Commit Stage C (`P0.5: …`); final diff audit; tick the five checkboxes in
    `ROADMAP.md`; tag (§8) after checkpoint HC-4.

## 4. Academic-integrity protocol

- **Provenance and checksums.** Record the base commit hash in
  `analysis/POINT_E_RECONCILIATION.md`. Before/after SHA-256 of every renamed file must
  be identical (`git mv` preserves blobs; the diff auditor verifies). Headers cite
  findings by F-number and section, so a reader can trace every assertion to
  `VALIDATION_REPORT.md` without trusting the header.
- **Verbatim quotation.** Headers may quote only text already recorded in
  `VALIDATION_REPORT.md` / `SIZE_VERIFICATION_METHODOLOGY.md`, reproduced verbatim with
  the URL as registered there. Because the register notes those quotes were captured
  under a sandbox egress block, every external citation in a header carries the tag
  *"as recorded in VALIDATION_REPORT.md §8; live-page verification pending P1.5."* No
  new DOI, URL, dataset ID, author, or quotation may be introduced in this phase; a
  header needing one instead writes "[source to be located and verified during
  execution - do not cite until verified]".
- **Pre-registration discipline.** The only decision with degrees of freedom is P0.4;
  its rule is fixed in §3 step 2 and timestamped by this plan's commit, which must
  precede the P0.4 results commit. The rule may not be revised after the image is read.
- **Blinding and confirmation-bias controls.** The two P0.4 readers receive only the
  image and the transcription task — not §4's recorded values, not each other's output.
  Adversarial verifiers (§5) are prompted to *refute* the headers' adequacy, not to
  affirm it.
- **AI-assistance disclosure.** F8 is this repo's own cautionary tale about undisclosed
  AI authorship. Accordingly: every Phase 0 header, this plan, and all Phase 0 commit
  messages disclose AI drafting (Claude, model claude-fable-5, orchestrated agents)
  with human review by the repository owner. The headers themselves state they were
  added by the Phase 0 process, dated.
- **Error correction and retraction.** If a header is later found to misstate a
  finding, it is corrected by an appended, dated amendment line and a commit explaining
  the error — never by silent rewrite. Historical documents are never edited beyond the
  prepended header; an erroneous header is amended, not the body.
- **Null results.** P0.4's outcome is published in
  `analysis/POINT_E_RECONCILIATION.md` whether E is reconciled or retired. "Could not
  be reconciled" is a complete, reportable result, not a failure to be retried until it
  yields.

## 5. Agent fan-out design

Orchestration: Claude Code Workflow `agent()`/`parallel()`/`pipeline()`; all agents
inherit claude-fable-5. Pattern: `pipeline(Stage A parallel → Stage B parallel →
BARRIER → Stage C)`. The **one genuinely needed barrier** is between Stage B and Stage
C: reference-scanning and diff-auditing are only sound against a frozen file set, so
all content edits must be committed before any rename occurs. Everything else is
embarrassingly parallel.

**Correlated-error limitation (standing).** Duplicate agents are instances of the same
model (claude-fable-5); procedural isolation prevents information leakage but not
shared model-systematic priors, so duplicate agreement bounds procedural/transcription
error only, not model-systematic error. Where the protocol supports it, duplicates must
take methodologically distinct routes, named in the relevant step — here the two P0.5
reference scanners already do (literal grep vs markdown-reference resolution); the
point-E readers and fidelity verifiers share one route, and their agreement is read
with that limitation. A human spot-check of a randomized sample of duplicate outputs
is a standing checkpoint before phase close (folded into HC-4).

| Role | Count | Independence / blinding | Maps to |
|---|---|---|---|
| Inventory auditor | 1 | works from repo + F1–F9 only | exit criterion |
| Header drafters | 6 (one per target doc, incl. class iv) | parallel; shared owner-approved template (HC-1); no cross-reads of drafts | P0.1–P0.3 |
| Finding-fidelity verifiers | 2 per header | independent; each checks every header assertion against `VALIDATION_REPORT.md` text; neither sees the other's report | P0.1–P0.3 |
| Adversarial verifiers | 3 per annotated doc | prompted to REFUTE: "construct a reading in which a reader still mistakes an invalidated claim for a live one"; independent | exit criterion |
| Point-E blind readers | 2 | see only `preview (3).webp` + transcription task; blind to §4 values and to each other | P0.4 |
| Arithmetic checker | 1 | receives transcriptions only after both readers return | P0.4 |
| Rename executor | 1 | executes the fixed §3 rule; no discretion | P0.5 |
| Reference scanners | 2 | independent methods: (a) literal grep for old names repo-wide; (b) walk every markdown file reference and resolve it against the tree | P0.5 |
| Diff auditor | 1 | compares each Stage-B diff to prepend-only pattern; verifies Stage-C blob-hash invariance | all |

**Structured-output contracts (JSON):**

- Header drafter → `{task_id, file, header_text, assertions: [{claim, f_number,
  source_section}]}`
- Fidelity verifier → `{file, verdict: "pass"|"fail", assertions_checked: n,
  mismatches: [{claim, expected_text, found_text, source_section}]}`
- Adversarial verifier → `{file, objection_found: bool, objection: {quoted_passage,
  misreading, severity}, verdict: "header_sufficient"|"header_insufficient"}`
- Point-E reader → `{image, table_row_transcription, scale_box_transcription,
  legibility: "clear"|"ambiguous"}`
- Arithmetic checker → `{consistent_value: "35 1/8"|"36 3/8"|null, computation,
  recommendation: "reconcile"|"retire"}`
- Reference scanner → `{method, stale_references: [{file, line, old_name}], count}`
- Diff auditor → `{commit, files: [{path, prepend_only: bool, blob_hash_unchanged:
  bool}], verdict}`

**Acceptance thresholds:**

- A header ships only if **2/2** fidelity verifiers pass with zero mismatches (a single
  non-verbatim quote fails the header).
- An adversarial objection sustained by **≥2/3** verifiers kills that header version;
  it is revised and re-run through both verifier sets. Maximum 3 revision cycles, then
  escalate to the owner (§7).
- Point E: **2/2** identical transcriptions required to attempt reconciliation; any
  disagreement, or either reader reporting "ambiguous", retires E per the
  pre-registered rule.
- P0.5 closes only when **both** scanners independently report `count: 0` and the smoke
  test (step 11) runs clean; scanner disagreement means fix and re-run both.
- Diff auditor must report `prepend_only: true` for every Stage-B file and
  `blob_hash_unchanged: true` for every rename; any violation reverts the commit.

**Human-in-the-loop checkpoints:**

- **HC-1:** owner approves the header template wording before any header is applied
  (the headers characterize the owner's own documents as containing fabricated
  citations; that statement ships only with the owner's explicit sign-off).
- **HC-2:** owner ratifies the P0.4 outcome (reconcile vs retire) on the readers'
  report — the annotation is the owner's work and the owner may know which entry was
  the transcription slip; the pre-registered rule still governs, the owner's input is
  recorded alongside it.
- **HC-3:** owner approves the class-(iv) disposition list before those headers apply.
- **HC-4:** owner signs off the final repo state before the tag; no Phase 1 work cites
  this repo until HC-4 clears.

## 6. Quality gates and exit criteria

Measurable gates, all required:

1. **Coverage gate:** the disposition table lists 100 % of tracked documents; each row
   is "passes" or "carries header naming the invalidating finding(s)" — the roadmap's
   exit criterion, made enumerable.
2. **Fidelity gate:** 2/2 verifier passes per header; zero verbatim mismatches
   repo-wide.
3. **Adversarial gate:** for every annotated document, ≤1/3 of adversarial verifiers
   can construct a live-claim misreading on the final header version.
4. **P0.4 gate:** `analysis/POINT_E_RECONCILIATION.md` exists and records a
   rule-conformant outcome (reconciled with shown arithmetic, or retired).
5. **Rename gate:** zero filenames containing spaces or parentheses in the tree; both
   scanners report zero stale references; `measure_twin_peaks.py` smoke test passes;
   all renamed blobs hash-identical.
6. **Immutability gate:** diff audit shows no historical body text altered anywhere in
   Phase 0.
7. **Bookkeeping gate:** five roadmap checkboxes ticked; one commit per task ID; HC-1
   through HC-4 recorded.

## 7. Failure modes and stopping rules

- **Owner declines a required header (HC-1/HC-3).** The exit criterion cannot be met;
  Phase 0 is recorded as **blocked, not complete**, with the refusal documented. No
  later phase may describe the repo as "safe to cite."
- **Adversarial deadlock** (3 revision cycles without clearing gate 3): stop, escalate
  to owner with the sustained objections verbatim; do not weaken the objection standard
  to pass.
- **Point E ambiguous or readers disagree:** E is retired per the pre-registered rule.
  This is a *recorded outcome*, not a failure — and it is never rescued post hoc by
  re-reading the image "more carefully" until agreement appears. A future
  reconciliation would require a new pre-registration against evidence not used here
  (e.g., a higher-quality scan acquired in Phase 1).
- **Reference scanners disagree persistently:** stop Stage C, leave the rename commit
  unmerged, report both scanners' raw outputs; do not hand-wave the union.
- **Any Stage-B diff touches body text:** revert that commit entirely and redraft; no
  partial fixes on top of a contaminated diff.
- General rule inherited from the roadmap: no post-hoc rescue. Anything that fails its
  gate is recorded as failed; a fix is a new, documented attempt.

## 8. Deliverables

- **Modified files (header-prepend only):** `mars_stereo_analysis.md`,
  `mars_stereo_analysis (1).md` (→ `mars_stereo_analysis_1.md`),
  `stereo_methodology_paper.md`, `interplanetary_civilization_hypothesis.md`,
  `pareidolia_vs_measurement.md`, plus any owner-approved class-(iv) documents.
- **Renamed files:** `preview_1.webp`, `preview_2.webp`, `preview_3.webp`,
  `mars_stereo_analysis_1.md` (blob-identical to originals).
- **Path-only reference updates:** `README.md`, `ROADMAP.md`, `VALIDATION_REPORT.md`.
- **New files:** `plans/PHASE_0_PLAN.md` (this plan; committed before P0.4 executes),
  `analysis/POINT_E_RECONCILIATION.md` (includes the document disposition table and
  the P0.4 record).
- **Commits:** this plan's commit (pre-registration timestamp), then one commit per
  task ID (`P0.1` … `P0.5`), each message carrying the task ID, the AI-assistance
  disclosure (§4), and the relevant gate results.
- **Tag:** `hygiene-v1` on the final commit after HC-4 — the state later phases may
  cite. (The roadmap's `pipeline-v1` tag remains reserved for P2.5.)
- **Roadmap update:** P0.1–P0.5 checkboxes ticked in `ROADMAP.md`.
