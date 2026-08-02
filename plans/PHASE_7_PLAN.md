# Phase 7 Execution Plan - Write-up and external scrutiny

**Roadmap section:** `ROADMAP.md` Phase 7, tasks P7.1-P7.4.
**Depends on:** Phase 1 (`data/PROVENANCE.md`), Phase 2 (`pipeline-v1` tag), Phase 3
(pre-registration commit), Phase 4 (results document, P4.5 verdict), Phase 5 (near-field
dataset or its documented absence), Phase 6 (`morphology-v1` tag). Manuscript scaffolding
(S2-S3) may begin once `pipeline-v1` exists; no results section is drafted before the
owning phase's tag exists. **Feeds:** nothing — this is the program's terminal phase.
**Drafted:** 2026-08-02, by an AI agent (claude-fable-5) under the repository's standing
rules.

## 1. Objective and scope

Expose the work to people incentivized to find its flaws. Exit criteria, quoted from the
roadmap:

> "manuscript + archived data/code exist; at least one round of external feedback
> incorporated or rebutted in writing."

In scope: P7.1 (consolidate Phases 1-6 into a single methods-and-results manuscript under
the honest framing, quoted from the roadmap: "recovering quantitative measurements from
historical lander press products, validated against orbital data" — publishable
*regardless* of what Object X turned out to be); P7.2 (the Phase 6 statistics checked by
someone who did not write them); P7.3 (submission to a planetary-science venue or at
minimum a public preprint with data and code archived); P7.4 (the post-mortem: what the
original scale system got right — careful ruler work, F5 — what it got wrong — the ×1.84
model error, F4, and the circular validation, F1 — and the procedural rule that now
prevents each failure).

Out of scope: any new measurement, any re-analysis, any change to an upstream number. The
manuscript reports what the phase tags contain. If writing exposes an upstream error, the
error is corrected *in the owning phase* under its error-correction policy, producing a
new tag; the manuscript then cites the new tag. The repo's calibrated language is
preserved verbatim in the manuscript: the IMP-only conclusion remains that Object X's
size is indeterminate from the IMP image alone (F6); whatever Phase 4 decided is reported
as Phase 4's graded result, with its error budget, not upgraded in prose. Verdict words
("artificial", "natural") appear only where a graded pre-registered hypothesis licenses
them, in Phase 4/6's own terms.

## 2. Inputs and preconditions

- **Network access:** all drafting, checking, and adversarial review run inside the
  analysis sandbox with no network. Exactly four activities require a normal-egress
  session outside the sandbox (which blocks the NASA/UA hosts, `VALIDATION_REPORT.md`
  §2): (i) the Q1 live-page quote audit (continuing P1.5 practice); (ii) S10 archiving of
  data/code to an external archival repository with a persistent identifier — [source to
  be located and verified during execution - do not cite until verified]; (iii) S11
  venue selection and submission — candidate venues are not in the source register, so:
  [source to be located and verified during execution - do not cite until verified];
  (iv) S12 receipt of and response to external feedback. Submission and reviewer
  correspondence are performed by the repository owner personally, never by an agent
  under the owner's identity.
- Required inputs, verified by V1 before drafting: `data/PROVENANCE.md` complete (P1
  exit criterion); tags `pipeline-v1` and `morphology-v1`; the Phase 3 pre-registration
  commit and its amendment history; the Phase 4 results document with every hypothesis
  graded; the Phase 5 dataset or its documented "reason it can't be had"; every phase's
  gate ledger and run log. A missing input blocks the corresponding manuscript section,
  not the whole phase.
- Repository-internal evidence for P7.4: `VALIDATION_REPORT.md` (F1-F9),
  `chat-history.txt`, `preview_2.webp` / `preview_3.webp` (post-P0.5 names; originally
  `preview (2).webp` / `preview (3).webp`), the Phase 0 supersession headers.
- Tooling: Python 3, `git`, `sha256sum`, the tagged analysis code. The manuscript build
  must be reproducible from a clean clone (X1 tests exactly this).

## 3. Research protocol

Numbered SOP. "Record" means: append to `analysis/phase7/RUN_LOG.md` with UTC date-time,
code commit hash, input tag/SHA-256, and agent ID.

- **S1 - Provenance and tag audit** (precondition; V1). Verify every §2 input exists at
  its stated tag; recompute checksums against `data/PROVENANCE.md`. Any mismatch: stop,
  record, return to the owning phase.
- **S2 - Claim inventory** (**P7.1**). Build `analysis/phase7/CLAIM_INVENTORY.md`: one
  row per result the manuscript will assert — claim text, owning phase and task ID,
  source commit/tag, gate record proving it passed its falsification gates, and the
  uncertainty to be printed. A claim with no row cannot appear in the manuscript; a row
  with no gate record cannot become a claim. Failed pre-registered hypotheses get rows
  too — they are reported as failed (standing rule).
- **S3 - Skeleton and framing** (**P7.1**). Draft the manuscript outline under the
  methodological framing quoted in §1: introduction (the question and the Cydonia
  precedent, `VALIDATION_REPORT.md` §7); data and provenance (Phase 1); pipeline
  validation and known-answer gates (Phase 2); pre-registration (Phase 3); the orbital
  test (Phase 4); near-field stereo (Phase 5); morphology statistics (Phase 6);
  discussion; the post-mortem as a companion section or supplement (P7.4). Owner
  approves outline and framing (checkpoint 1) before drafting.
- **S4 - Section drafting** (**P7.1**). Writers W1-W4 draft sections in parallel, each
  reading only: the claim inventory, the owning phase's tagged outputs, and the source
  register. No writer performs analysis; any derived number in prose must show its
  arithmetic from tagged table values. All quotes come from the register with URL and
  access date.
- **S5 - Number-consistency audit** (**P7.1**). N1 and N2 independently trace every
  numeric value in the draft (text, tables, figures) to a tagged machine-readable source
  or a shown derivation. An untraceable number is removed, never patched. Both auditors
  must return zero orphans.
- **S6 - Independent statistics check** (**P7.2**, internal leg). T1 — an agent with no
  Phase 6 drafting or scoring involvement and no access to Phase 6 transcripts —
  re-derives the Phase 6 null distributions, percentiles, bootstrap CIs, and
  multiple-comparisons correction from the raw score JSON at `morphology-v1`, and checks
  the manuscript's statistics section against its own results. This internal leg is a
  pre-submission gate; it does **not** discharge P7.2's external leg. The external leg
  is satisfied only by a logged external statistical check of the Phase 6 statistics
  obtained via S12, incorporated or rebutted in writing — generic S12 feedback of any
  kind does not discharge P7.2 (§6 gate 8).
- **S7 - Post-mortem** (**P7.4**). W5 drafts `analysis/phase7/POST_MORTEM.md`: a
  finding-by-finding table over F1-F9 — what was right (F5: raw ruler measurements
  reproduce NASA's 30-35 m peak heights once the ×1.84 scale error is corrected), what
  was wrong (F1 circular validation; F2 stereo impossibility; F3 linear range mapping;
  F4 ×1.84 transverse-scale error; F7 stereo-error claim wrong by ~3 orders of
  magnitude; F8 fabricated citations in AI-generated documents), and, per failure, the
  procedural rule now preventing it (known-answer gate; pre-registration; error budgets;
  institutional-sources-only; independent duplicate implementation; AI-disclosure). The
  failure analysis is a deliverable, not an embarrassment (roadmap P7.4).
- **S8 - Internal hostile-referee round.** R1-R3 each write a full referee report,
  prompted to REFUTE: attack circularity, gate evasion, post-hoc language, uncertainty
  omissions, claim-inventory gaps, framing overreach, and any place the manuscript is
  stronger than its tags. Each works alone, without the others' reports.
- **S9 - Revision, ledger, freeze.** Writers revise against S5/S6/S8 outputs; every
  referee point is resolved as fixed or rebutted in writing in the gate ledger. Owner
  reviews the ledger and signs off (checkpoint 2); tag `manuscript-v1`.
- **S10 - Archive data and code** (**P7.3**; network). Package the repository at its
  tags with checksums; deposit in the archival repository (§2); record the persistent
  identifier and access date in `data/PROVENANCE.md` and the manuscript. X1 then
  rebuilds every manuscript number and figure from the archived package alone.
- **S11 - Submission** (**P7.3**; network; owner-performed). Owner selects the venue
  from the verified shortlist (checkpoint 3) and submits; at minimum, the public
  preprint is posted. Submission metadata (venue, date, identifier) is recorded.
- **S12 - External feedback round** (**P7.2** external leg, **P7.3**). The
  external-review solicitation — the venue submission cover material and any solicited
  preprint review request — must explicitly request statistical review of the Phase 6
  statistics. Every external
  comment is logged verbatim in `analysis/phase7/REVIEW_LOG.md` with source and date.
  Each is dispositioned: incorporated (with the commit), or rebutted in writing in
  `RESPONSE_TO_REVIEWERS.md`. Statistical objections route through T1 re-derivation
  before any response. Owner approves every response before it is sent (checkpoint 4).
  Revisions land as `manuscript-v1.1` (v1 history preserved). If formal venue review
  stalls or is rejected, one round of solicited independent expert review of the public
  preprint, archived in the same log, satisfies the exit criterion — the owner decides
  and records the route. P7.2's external leg is discharged only by a logged external
  statistical check of the Phase 6 statistics, incorporated or rebutted in writing;
  if no such check is obtained after the S12 routes are exhausted, the phase may close
  only with an explicit "incomplete at P7.2" status recorded in the gate ledger.
- **S13 - Exit-criteria check.** V1 confirms §6 gates with numbers in
  `analysis/phase7/GATE_LEDGER.md`; owner's final sign-off closes the phase.

## 4. Academic-integrity protocol

- **Provenance and checksums.** S1 verifies every input tag and checksum before writing;
  X1 verifies the archived package regenerates every published number; the persistent
  identifier and checksums are printed in the manuscript. No manuscript claim cites a
  file absent from `data/PROVENANCE.md`.
- **Verbatim quotation.** All quoted language in the manuscript comes from the
  `VALIDATION_REPORT.md` §8 register and `SIZE_VERIFICATION_METHODOLOGY.md` Sources,
  verbatim with URL and access date, re-verified against live pages by Q1 (P1.5
  practice). Any source needed beyond the register — venue, archive service, or added
  literature — enters only after live verification, and is never cited from memory.
- **Pre-registration discipline.** The manuscript reports every pre-registered
  hypothesis with its original tolerance band and its graded outcome, including failures;
  the Phase 3 commit hash is cited as the timestamp. Amendments are reported as
  amendments. No hypothesis is reworded to fit its result.
- **Blinding and confirmation-bias controls.** T1 works from raw JSON without Phase 6
  transcripts or compiled tables; N1/N2 audit independently; R1-R3 are isolated and
  instructed to refute. Writers cannot alter data; checkers cannot rewrite prose.
- **AI-assistance disclosure.** The manuscript, preprint, and every phase document carry
  an explicit statement that analysis and drafting were performed by AI agents
  (claude-fable-5) under human direction, with the human owner responsible for the
  claims — the direct procedural remedy for F8. AI agents are not listed as authors.
- **Error-correction and retraction.** Errors found after `manuscript-v1` produce
  appended corrections and a new tag; errors found after public posting produce a
  versioned, dated correction on the preprint — never a silent edit. An error that
  invalidates a load-bearing claim triggers withdrawal of that claim in an update, with
  the reasoning published.
- **Null results.** If Phase 4/6 returned the null — Object X an ordinary hummock — the
  manuscript is written and submitted with identical care under the same framing, which
  was chosen in the roadmap precisely because it is publishable regardless of outcome
  (standing rule; Cydonia precedent, `VALIDATION_REPORT.md` §7).

## 5. Agent fan-out design

Executed with Claude Code Workflow orchestration (`agent()` / `parallel()` /
`pipeline()`); all agents inherit the session model, claude-fable-5.

| Role | ID(s) | Count | Independence / blinding arrangement |
|---|---|---|---|
| Section writers | W1-W4 | 4 | Parallel; each reads only the claim inventory, its section's tagged phase outputs, and the register; no analysis rights |
| Post-mortem writer | W5 | 1 | Works only from `VALIDATION_REPORT.md`, `chat-history.txt`, and phase ledgers; no access to manuscript drafts (prevents tone-matching the successes) |
| Number-consistency auditors | N1, N2 | 2 | Independent full traces of every manuscript number to tagged sources; no access to each other's reports |
| Independent statistics checker | T1 | 1 | No Phase 6 involvement or transcript access; re-derives all statistics from raw score JSON at `morphology-v1` (internal leg of P7.2) |
| Adversarial referees | R1-R3 | 3 | Full hostile referee reports, prompted to REFUTE; isolated from each other; see the frozen draft plus tags, not the writers' rationales |
| Source-verification agent | Q1 | 1 | Networked session only: every quote, URL, and access date checked against live pages; may not edit prose |
| Reproducibility agent | X1 | 1 | Fresh clone of the archived package only (no repo working tree); must regenerate every manuscript number and figure |
| Provenance auditor | V1 | 1 | Runs S1 before work and the S13 exit check |
| Response drafter | W6 | 1 | Drafts S12 responses from the review log and T1 output; owner approves each before sending |

**Orchestration pattern.**

```
pipeline(
  V1(S1) -> orchestrator(S2 claim inventory) -> owner(checkpoint 1: outline/framing)
  -> parallel(W1, W2, W3, W4, W5)(S4 drafting; S7 post-mortem)
  -> parallel(N1, N2, T1, Q1)(S5-S6 verification fan-out)
  -> parallel(R1, R2, R3)(S8 hostile-referee round)
  -> orchestrator(S9 revision + gate ledger) -> owner(checkpoint 2: freeze) -> tag manuscript-v1
  == BARRIER ==                                  # the one genuine barrier
  S10 archive -> X1(rebuild check) -> owner(checkpoint 3: venue; performs S11 submission)
  -> S12 external round (W6 drafts; T1 on stats objections; owner checkpoint 4 per response)
  -> V1(S13 exit check) -> owner final sign-off
)
```

The single genuinely required barrier sits between the internal freeze (`manuscript-v1`
with owner sign-off) and any external release: posting a preprint or submitting to a
venue is irreversible in a way no internal step is, so nothing crosses the sandbox
boundary until every internal gate has passed and the owner has signed. Drafting,
auditing, and refereeing all fan out in parallel on either side of it.

**Structured-output contracts (JSON).**

- W1-W6: `{"agent_id", "section", "claims_used": ["inventory_row_ids"], "quotes_used": [{"register_item", "url", "access_date"}], "derived_numbers": [{"value", "derivation", "source_table"}]}`.
- N1/N2: `{"agent_id", "numbers_traced": N, "orphans": [{"location", "value", "reason"}], "pass": bool}`.
- T1: `{"agent_id", "recomputed": {"percentiles": {...}, "cis": {...}, "corrected_results": [...]}, "manuscript_discrepancies": [...], "pass": bool}`.
- R1-R3: `{"agent_id", "verdict": "REFUTED|NOT_REFUTED", "points": [{"severity": "fatal|major|minor", "location", "objection", "evidence"}]}`.
- Q1: `{"agent_id", "quotes_checked": N, "drift": [{"quote", "expected", "live_text", "url", "access_date"}], "pass": bool}`.
- X1: `{"agent_id", "package_id", "numbers_regenerated": N, "mismatches": [...], "figures_regenerated": N, "pass": bool}`.
- V1: `{"agent_id", "items_checked": N, "failures": [...], "pass": bool}`.

**Acceptance thresholds.**

- N1 and N2 must *both* return zero orphan numbers; disagreement on any trace is resolved
  against the tagged source, never against the prose.
- T1 must reproduce every Phase 6 statistic within stated rounding; any discrepancy
  blocks the freeze and routes to Phase 6's error-correction policy — the manuscript is
  never adjusted to split the difference.
- Referees: any point graded fatal by *any* referee, and any point raised by a 2-of-3
  majority, must be fixed or rebutted in writing before the freeze; a fatal point that
  survives rebuttal kills the affected claim (it reverts to failed / is removed).
- Q1: zero unresolved quote drift; X1: 100 % of manuscript numbers and figures
  regenerate from the archived package.

**Human-in-the-loop checkpoints.** (1) Owner approves outline, framing, and the claim
inventory before drafting. (2) Owner reviews the full gate ledger and referee
dispositions, then signs the `manuscript-v1` freeze — nothing crosses the barrier without
this. (3) Owner selects the venue and personally performs the submission and preprint
posting. (4) Owner approves every response to external reviewers before it is sent, and
signs the final S13 close-out.

**Correlated-error limitation (standing).** All duplicate agents in this plan (N1/N2;
R1-R3) are instances of the same model (claude-fable-5). Procedural isolation prevents
information leakage between them but not shared model-systematic priors, so duplicate
agreement bounds procedural/transcription error only, not model-systematic error. Where
the protocol supports it, duplicates must take methodologically distinct routes, named
in the relevant step; a human spot-check of a randomized sample of duplicate outputs is
a standing checkpoint before phase close.

## 6. Quality gates and exit criteria

Measurable statements of the roadmap's exit criteria:

1. Inventory gate: every claim in the manuscript has a `CLAIM_INVENTORY.md` row with tag
   and gate record; every failed pre-registered hypothesis appears, reported as failed.
   [P7.1]
2. Consistency gate: N1 and N2 both report zero orphan numbers. [P7.1]
3. Statistics gate: T1 reproduces all Phase 6 statistics within stated rounding — the
   internal leg of "checked by someone who did not write them." Internal leg only: it
   does not discharge P7.2's external leg (gate 8). [P7.2]
4. Referee gate: every R1-R3 point dispositioned fixed-or-rebutted in the ledger; no
   surviving fatal point. [P7.1]
5. Post-mortem gate: `POST_MORTEM.md` covers F1-F9 with a named preventing rule per
   failure. [P7.4]
6. Archive gate: data/code deposited with persistent identifier and checksums; X1
   rebuild passes at 100 %. [P7.3]
7. Submission gate: venue submission or public preprint exists, with recorded metadata.
   [P7.3]
8. External-feedback gate: at least one round of external feedback logged, with every
   comment incorporated or rebutted in writing (the exit criterion verbatim). [P7.2, P7.3]
   P7.2-specific gate: the external-review solicitation must explicitly request
   statistical review of the Phase 6 statistics, and phase close requires EITHER a
   logged external statistical check, incorporated or rebutted in writing, OR an
   explicit "incomplete at P7.2" status recorded in the gate ledger. Generic gate-8
   feedback of any kind does not discharge P7.2. [P7.2]
9. Tags `manuscript-v1` (and `manuscript-v1.1` if revised) exist with owner sign-offs
   committed.

## 7. Failure modes and stopping rules

Failed hypotheses are recorded as failed, never rescued post hoc. Specifically:

- **Upstream error surfaced by writing or checking** (T1, N-audit, referee, or external
  reviewer finds a defect in a phase result): hard stop on the affected section; the
  defect returns to the owning phase, is fixed under that phase's policy at a new tag,
  and the manuscript cites the new tag. The manuscript itself never becomes the place
  where data are corrected.
- **T1 non-reproduction** that Phase 6 cannot resolve: the affected statistics are
  removed from the manuscript and reported as unresolved in the post-mortem; they are
  not softened into prose claims.
- **Surviving fatal referee point:** the affected claim is removed or reported as failed;
  a manuscript that loses its central methodological claim this way fails the phase.
- **X1 rebuild failure:** external release is blocked until the archived package
  regenerates everything; no "works on the working tree" exception.
- **Venue rejection** is not phase failure: the public-preprint route satisfies the
  P7.3 minimum, and the rejection reviews count as external feedback for gate 8 if
  logged and dispositioned.
- **No external feedback obtainable** after the S12 routes are exhausted: the phase
  cannot claim its exit criterion; it is recorded as incomplete-at-gate-8, with the
  preprint and archive standing. The gate is never waived.
- **Post-publication fatal flaw:** versioned correction or withdrawal of the affected
  claim on the preprint, with reasoning published — the same care as a success
  (standing rule; Cydonia precedent, `VALIDATION_REPORT.md` §7).
- Forbidden in all cases: re-running upstream analyses to make the paper cleaner,
  narrowing reported uncertainties in prose, dropping failed hypotheses from the
  narrative, or citing any source that has not passed Q1 verification.
- **Phase failure** is declared if, after one diagnosis-and-refix cycle, gate 1, 2, 3,
  or 4 of §6 still fails: no external release occurs, and the failure write-up is
  committed with the same care as a success.

## 8. Deliverables

All under `analysis/phase7/` unless noted:

- `CLAIM_INVENTORY.md` - every asserted result with tag, gate record, and uncertainty (S2).
- `manuscript/` - the methods-and-results manuscript source, figures, and
  machine-readable tables (P7.1).
- `POST_MORTEM.md` - the F1-F9 failure analysis with preventing rules (P7.4).
- `statistics_check/` - T1's independent re-derivation and discrepancy report (P7.2).
- `referee_reports/` - R1-R3 internal reports and their dispositions (S8-S9).
- `ARCHIVE_RECORD.md` - persistent identifier, checksums, X1 rebuild report; appended to
  `data/PROVENANCE.md` (P7.3).
- `REVIEW_LOG.md` + `RESPONSE_TO_REVIEWERS.md` - every external comment verbatim, each
  incorporated or rebutted in writing, with owner approvals (P7.2, P7.3).
- `GATE_LEDGER.md` - §6 gates with numbers and owner sign-offs; `RUN_LOG.md` - every
  run: UTC time, commit, input tags/SHA-256s, agent ID.
- Commits referencing task IDs (P7.x): inventory (S2); outline (S3); drafts (S4, S7);
  audits (S5-S6); referee round (S8); freeze (S9); archive (S10); submission record
  (S11); external round (S12); close-out (S13). Tags: `manuscript-v1` at the freeze,
  `manuscript-v1.1` after external revision — each created only on full gate passage
  plus owner sign-off.
