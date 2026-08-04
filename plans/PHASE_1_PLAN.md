# Phase 1 Execution Plan - Acquire the Primary Data

**Roadmap section:** `ROADMAP.md` Phase 1, tasks P1.1-P1.5.
**Depends on:** nothing hard (Phase 0 hygiene may run in parallel); **feeds:** Phases 2-6, all of
which are forbidden to cite any file absent from `data/PROVENANCE.md`.
**Drafted:** 2026-08-02, by an AI agent (claude-fable-5) under the repository's standing rules.

## 1. Objective and scope

Replace the press-release visualization products this repository has worked from with calibrated
archive data, with provenance recorded well enough that a stranger could verify every byte
(`ROADMAP.md` Phase 1 objective). Exit criteria, quoted from the roadmap:

> "all five items checksummed and provenance-logged; no analysis in later phases may cite a file
> absent from `data/PROVENANCE.md`."

In scope: the five roadmap items P1.1-P1.5 (Photojournal TIFFs; PDS IMP EDR frames + User's Guide;
HiRISE observations and DTM-availability determination; the five governing papers; live-page
spot-check of every quote in `VALIDATION_REPORT.md` §8). Out of scope: any measurement,
registration, or interpretation of the acquired data - that is Phases 2-6. Phase 1 makes **no**
claims about Object X; the repo's calibrated position stands unchanged: Object X's size is
indeterminate from the IMP image alone (`VALIDATION_REPORT.md` F6).

## 2. Inputs and preconditions

- **Network access is required for every acquisition step in this phase.** The roadmap marks
  Phase 1 "requires normal network access; blocked in the analysis sandbox," and
  `VALIDATION_REPORT.md` §2 records HTTP 403 CONNECT denials from the sandbox for
  `photojournal.jpl.nasa.gov`, `mars.nasa.gov`, `science.nasa.gov`, `images-assets.nasa.gov`,
  `nssdc.gsfc.nasa.gov`, and `uahirise.org`. Steps S1, S4-S8 below therefore run only in an
  environment with normal egress; steps S2-S3 and S9 (directory setup, pre-registration,
  consolidation/commit) can run anywhere.
- Repository at current head, containing `VALIDATION_REPORT.md`, `SIZE_VERIFICATION_METHODOLOGY.md`,
  the two catalog-page PDFs (`PIA02405-left-eye.pdf`, `PIA02406-right-eye.pdf`), and the four
  `preview*.webp` files (used only as cross-check references, never as data).
- Tooling: `sha256sum`, a TIFF/image header reader (e.g. Python PIL or ImageMagick `identify`),
  a PDS label parser or plain-text label inspection, `git`.
- Disk: PIA02405.tif alone is 65.93 MB per its catalog page; PDS EDR and HiRISE products are
  expected to be substantially larger. Record exact byte counts on receipt; do not pre-commit to
  sizes the repo documents do not state.
- Expected-property table (Step S3) committed **before** any download commit.

## 3. Research protocol

Numbered SOP. Every step names its roadmap task ID. "Record" always means: append a row to
`data/PROVENANCE.md` with source URL, UTC access date-time, HTTP status, byte count, SHA-256,
local path, and the retrieving agent's ID.

- **S1 - Reachability probe** (supports all of P1.1-P1.5). From the networked environment, issue a
  HEAD/GET to each required host (`photojournal.jpl.nasa.gov`, `pds-imaging.jpl.nasa.gov`,
  `uahirise.org`, `mars.nasa.gov`, `science.nasa.gov`, `www.jpl.nasa.gov`,
  `agupubs.onlinelibrary.wiley.com`, `www.britannica.com`, `www.nature.com`). Log status codes.
  Any unreachable host triggers the retry policy in §7 before its dependent steps run.
- **S2 - Layout** (all tasks). Create `data/photojournal/`, `data/pds/`, `data/hirise/`,
  `data/papers/`, `data/quote-audit/`; initialize `data/PROVENANCE.md` with the row schema above
  plus a free-text "anomalies" column. Commit ("P1: provenance scaffold").
- **S3 - Pre-registration of expected properties** (acquisition known-answer test; standing rule
  "pre-register before you look"). Commit, before any download, a table of every property the
  repo's documents already state, which the downloads must reproduce:
  (a) PIA02405.tif catalog-stated size 65.93 MB; (b) product dimensions 7238x3135 (left) and
  7296x3135 (right) px per the catalog pages; (c) preview aspect ratios match catalog dimensions
  to 0.1 % (`VALIDATION_REPORT.md` §2); (d) native IMP frames 256x256 px per eye at 0.98 mrad/px
  (Smith et al. 1997, via `SIZE_VERIFICATION_METHODOLOGY.md` Step 1); (e) HiRISE PSP_001890_1995
  "map-projected to 25 cm/pixel" with the lander visible (`VALIDATION_REPORT.md` §7). Tolerances:
  dimensions and checksum duplication exact; stated file size to the catalog's printed precision
  under either MB convention (10^6 or 2^20 bytes) - if neither rounds to 65.93, flag, do not
  rationalize; aspect ratio within 0.1 %.
- **S4 - Photojournal products** (**P1.1**). Fetch `PIA02405.tif` and `PIA02406.tif` from
  photojournal.jpl.nasa.gov, each **twice, by two independent agents** (see §5). Record both
  fetches. Verify: SHA-256 of duplicate fetches identical; header dimensions vs S3(b);
  size vs S3(a); aspect-ratio cross-check vs previews per S3(c).
- **S5 - PDS calibrated archive** (**P1.2**). At pds-imaging.jpl.nasa.gov, locate dataset
  `MPFL-M-IMP-2-EDR-V1.0`. Download the dataset index and *The Imager for Mars Pathfinder User's
  Guide* from the dataset's `document/` directory first; record both. From the index and the
  User's Guide, identify the left/right-eye EDR frames composing the Twin Peaks super-resolution
  sequence - the catalog pages state the left-eye product was built from 8 frames and the right
  from 7 (`VALIDATION_REPORT.md` §2, §5.1); the specific frame IDs are
  [to be determined from the dataset index during execution - do not cite until verified].
  Download every identified frame **with its detached/attached PDS label**; record each file and
  each label separately. Verify each label parses and its stated image dimensions match S3(d).
  If the sequence cannot be identified unambiguously from dataset documentation alone, stop and
  escalate (§7) - frame IDs are never guessed.
- **S6 - HiRISE products** (**P1.3**). From uahirise.org, download observation PSP_001890_1995
  (map-projected product, 25 cm/px) and stereo observation PSP_002391_1995, dual-fetched as in S4.
  Search the HiRISE DTM archive
  [archive URL to be located and verified during execution - do not cite until verified] for a
  published DTM of the PSP_001890_1995 / PSP_002391_1995 pair. If found: download, record. If not
  found: record the negative result as a provenance row that carries, besides the negative search
  result ("DTM: none archived as of <date>, search route: <URL>"), the **fixed fallback method**
  that Phases 3 and 4 reference, so no mid-phase improvisation is possible: relative heights from
  the PSP_001890_1995 / PSP_002391_1995 stereo pair by area-based image correlation on
  map-projected tiles; vertical datum from >= 5 control points on terrain of assumed-zero relative
  relief; parallax-to-height conversion from the observation geometry stated on the two HiRISE
  catalog pages; and an error model propagating matching precision (assumed +/-0.5 px until
  measured) through that geometry. The software toolchain is named in the P1.3 provenance record
  at acquisition time and marked "[software to be located and verified during execution - do not
  cite until verified]". Both outcomes are equally valid completions of P1.3.
- **S7 - Governing papers** (**P1.4**). Resolve doi:10.1029/96JE03568 (Smith et al. 1997) and
  doi:10.1029/1998JE900012 (Kirk et al. 1999); retrieve Parker's sight-line localization,
  *Science* 278, 1746 (1997)
  [access route to be located and verified during execution - do not cite until verified].
  Record full bibliographic metadata, resolution URL, access route (open / subscription /
  request-from-author), and SHA-256 of any retrieved PDF. **Copyrighted PDFs are stored locally
  and checksummed but not committed to the repository**; `data/PROVENANCE.md` carries the checksum
  so a holder of the same PDF can verify identity. If a paper is paywalled, record that fact and
  escalate the access decision to the owner; do not substitute unverified copies.
- **S8 - Quote spot-check** (**P1.5**). Enumerate every verbatim quotation in
  `VALIDATION_REPORT.md` (the §8 register plus the block quotes in §2, §3, §5.1, §7). For each:
  fetch the live page, save the retrieved page to `data/quote-audit/`, checksum it, and diff the
  quoted text character-by-character against the live text. Outcomes per quote: `verbatim-match`,
  `drift` (with exact diff), or `page-unreachable`/`page-changed` (with evidence). Drift is
  corrected by an appended, dated erratum section in `VALIDATION_REPORT.md` - never by silent
  edit - executed only after owner sign-off (§5, checkpoint C3).
- **S9 - Consolidation, audit, tag** (exit for all tasks). A single writer agent merges all
  provenance rows into `data/PROVENANCE.md`; the adversarial provenance auditor (§5) then attempts
  to refute the record; on pass and owner sign-off, commit ("P1.1-P1.5 complete") and tag
  `data-v1`. Later phases cite the tag.

## 4. Academic-integrity protocol

- **Provenance and checksums.** Every artifact: URL, UTC access date, byte count, SHA-256,
  retrieving agent, and every verification performed. Dual-fetch by independent agents guards
  against truncation and silent corruption. Nothing enters `data/` without a provenance row;
  nothing in later phases may cite a file without one (roadmap exit criterion).
- **Verbatim quotation.** This phase adds no new quotations. S8 audits existing ones against live
  pages, preserving the fetched page bytes so the audit itself is reproducible. The register in
  `VALIDATION_REPORT.md` §8 remains the only citation pool; any source this plan marks
  "[to be located and verified during execution]" may be cited only after it is fetched,
  checksummed, and quoted verbatim with URL and access date.
- **Pre-registration discipline.** The expected-property table (S3) is committed before any
  download. A download that violates its pre-registered property is recorded as a discrepancy and
  investigated; the table is never edited to fit the data (amendments append, per the P3.5
  pattern).
- **Blinding and confirmation-bias controls.** Duplicate fetchers do not see each other's
  checksums. Quote-audit agents receive only (quote text, URL) - not the surrounding argument or
  the finding the quote supports - so a fuzzy match cannot be rationalized as "close enough."
  The provenance auditor is prompted to refute, not confirm.
- **AI-assistance disclosure.** This plan and all execution agents are claude-fable-5 instances;
  `data/PROVENANCE.md` opens with a disclosure block naming the model, orchestration tool, and
  the human owner as approver of record. This mirrors the P0.1 lesson: AI involvement is labeled,
  never laundered.
- **Error-correction and retraction.** Quote drift found in S8 produces a dated erratum appended
  to `VALIDATION_REPORT.md`; a provenance row later found wrong is struck through with a dated
  correction row, never deleted.
- **Null results are published.** "No archived DTM exists" (S6) and "quote could not be verified
  because the page changed" (S8) are committed findings with the same formality as successes.

## 5. Agent fan-out design

Orchestration: Claude Code Workflow tool (`agent()`/`parallel()`/`pipeline()`); all agents inherit
claude-fable-5.

| Role | Count | Task IDs | Independence / blinding |
|---|---|---|---|
| Fetcher-A / Fetcher-B (duplicate downloaders) | 2 per binary artifact (S4, S6; PDS frames in S5 dual-fetched likewise) | P1.1-P1.3 | Separate agents, separate local paths and times; neither sees the other's checksum or output |
| PDS navigator | 1 | P1.2 | Identifies frame IDs from index + User's Guide only; forbidden to consult the repo's interpretive documents |
| DTM searcher | 1 | P1.3 | Reports found/not-found with evidence; prompted that "not found" is a fully acceptable answer |
| Literature retriever | 1 | P1.4 | Resolves DOIs; records access route and license status |
| Quote auditors | 1 per quotation in the S8 enumeration, in parallel | P1.5 | Each receives only (quote, URL); blind to findings F1-F9 and to other auditors |
| Adversarial provenance auditor | 3 | S9 gate | Each independently prompted to REFUTE `data/PROVENANCE.md`: recompute every checksum from disk, re-verify sizes/dimensions, hunt for uncited files in `data/` |
| Consolidation writer | 1 | S9 | The only agent that writes `data/PROVENANCE.md`; performs no fetches itself |

**Pattern.** `parallel()` fan-out across S4-S8 (the five acquisition streams are independent),
inside each stream a `pipeline()` where order matters (S5: index -> frame identification -> frame
fetches). **The one genuine barrier** is before S9: consolidation requires every stream's JSON to
be final, because the auditors must attack a complete record and the single writer must not race
partial results. Everything upstream of that barrier is free-running.

**Structured-output contracts.** Fetchers return
`{task_id, artifact, source_url, access_datetime_utc, http_status, bytes, sha256, local_path,
anomalies[]}`. Quote auditors return
`{quote_id, url, access_datetime_utc, verdict: "verbatim-match"|"drift"|"page-unreachable"|"page-changed",
diff, saved_page_sha256}`. The DTM searcher returns
`{observation_pair, dtm_found: bool, evidence_url, access_datetime_utc, notes}`. Auditors return
`{verdict: "record-holds"|"record-refuted", defects: [{row, defect, evidence}]}`.

**Acceptance thresholds.** (i) Duplicate fetches: SHA-256 **exactly equal**; on mismatch a third
independent fetch runs and 2-of-3 agreement accepts, else the artifact is quarantined and
escalated. (ii) Pre-registered properties (S3): all pass, or the discrepancy is logged and
escalated - never waved through. (iii) Quote audit: `verbatim-match` closes a quote; anything else
goes to checkpoint C3. (iv) Adversarial audit: **any one** auditor's confirmed defect blocks the
tag (unanimity required to pass - stricter than majority, appropriate for a provenance record).

**Correlated-error limitation.** Duplicate agents are instances of the same model
(claude-fable-5); procedural isolation prevents information leakage but not shared
model-systematic priors, so duplicate agreement bounds procedural/transcription error only, not
model-systematic error. Where the protocol supports it, duplicates must take methodologically
distinct routes (named in the relevant step); a human spot-check of a randomized sample of
duplicate outputs is a standing checkpoint before phase close.

**Human-in-the-loop checkpoints.** C1: owner approves the S3 expected-property commit before
downloads begin. C2: owner resolves any quarantined artifact, paywall access route, or ambiguous
PDS frame identification. C3: owner approves each erratum text before `VALIDATION_REPORT.md` is
touched. C4: owner signs off on the audited `data/PROVENANCE.md` before the `data-v1` tag - the
tag is the phase's point of no return, since later phases build on it.

## 6. Quality gates and exit criteria

Measurable, mapped to the roadmap's exit criteria:

1. **Coverage:** provenance rows exist for both Photojournal TIFFs (P1.1); the identified EDR
   frames, their labels, and the User's Guide (P1.2); both HiRISE observations plus a positive or
   negative DTM row (P1.3); all five papers' bibliographic/checksum records (P1.4); and one
   closed verdict per enumerated quote (P1.5).
2. **Integrity:** every binary artifact dual-fetch-verified; every S3 pre-registered property
   checked with outcome logged.
3. **Adversarial audit:** three auditors, zero unresolved defects.
4. **Roadmap exit criterion, verbatim:** "all five items checksummed and provenance-logged"; and
   the standing prohibition is operative - no later-phase document may cite a file absent from
   `data/PROVENANCE.md`.
5. `data-v1` tag exists and points at the commit containing the audited record.

## 7. Failure modes and stopping rules

- **Host unreachable:** 3 retries spaced >=1 hour; then record the failure with status codes and
  stop that stream. Only institutional mirrors already named in the source register may be
  substituted; anything else requires owner approval at C2. A stream stopped this way blocks the
  phase (partial acquisition cannot satisfy the exit criterion) but its negative log is committed.
- **Checksum non-reproducibility** (2-of-3 fails): artifact quarantined outside `data/`, phase
  blocked on that item, owner escalation. No quarantined file is ever cited.
- **Pre-registered property violated** (e.g. TIFF dimensions differ from 7238x3135 / 7296x3135):
  recorded as a discrepancy finding, investigated as possibly a repo-document error or a changed
  archive product - but per the standing no-post-hoc-rescue rule, the S3 table itself is not
  edited; an appended amendment with owner sign-off documents the resolution.
- **PDS frame identification ambiguous:** hard stop; escalate with the candidate list. Guessing
  frame IDs would poison Phases 2 and 5.
- **No archived DTM (S6)** and **quote drift (S8)** are *not* failures - they are pre-anticipated
  findings with defined handling (record; erratum via C3). Recording them as anything other than
  what they are would itself violate the program's rules.
- **Phase failure** is declared if any of P1.1-P1.5 cannot be completed and its blocker cannot be
  resolved by the owner; the failure state, evidence, and partial provenance are committed as the
  phase's (null) result. Later phases do not proceed on partial data without an owner-approved,
  committed scope amendment.

## 8. Deliverables

- `data/PROVENANCE.md` - the audited provenance register (with AI-disclosure block).
- `data/photojournal/`, `data/pds/`, `data/hirise/` - acquired products and labels;
  `data/papers/` - bibliographic records and checksums (copyrighted PDFs held locally,
  uncommitted); `data/quote-audit/` - saved pages and per-quote verdict JSONs.
- Fetch/verify scripts used (committed under `analysis/` or `tools/`, so a stranger can re-run).
- Errata appended to `VALIDATION_REPORT.md` if S8 found drift (owner-approved).
- Commits: "P1: provenance scaffold" (S2), "P1: pre-registered expected properties" (S3, before
  any download), per-stream acquisition commits referencing P1.1-P1.5, and the consolidation
  commit; git tag **`data-v1`** on the audited final state.
