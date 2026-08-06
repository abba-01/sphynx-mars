# Provenance Log

Acquisition and verification records for primary data (roadmap Phase 1). Every
analysis input must have a row here before later phases may cite it.

## 2026-08-02 — `intake/official/` acquisition (owner browser session)

**Acquisition method.** Repository owner's browser session against
`science.nasa.gov` on 2026-08-02 (evidence: MHTML snapshot header
`Date: Sun, 2 Aug 2026 08:05:36 -0700`, `Snapshot-Content-Location:
https://science.nasa.gov/photojournal/twin-peaks-in-super-resolution-right-eye/`;
saved pages carry science.nasa.gov photojournal asset URLs). Owner-mediated, not an
automated institutional fetch — but the saved pages themselves document the session,
and the hash results below are independent of trust in the transfer.

### Product TIFF verification (closes the P1.1 hash check)

| File | SHA-256 | Verification |
|---|---|---|
| `intake/official/PIA02405.tif` | `d32ee9af29b6505e7377bf8dd3fadde2554d510d09ab68459a6d9ea1cc2c69d6` | **Byte-identical** to `intake/00/PIA02405.tif` (the P2 analysis input); 65,926,165 bytes = catalog's stated 65.93 MB; 7238×3135 = catalog dimensions |
| `intake/official/PIA02406.tif` | `49de98486fbfc1836e2feb26aecc7589bddad2de437bf706e64e5ba4df484199` | **Byte-identical** to `intake/00/PIA02406.tif`; 7296×3135 = catalog dimensions |

Consequence: the full-resolution re-run's inputs (`analysis/FULLRES_RERUN.md` §1)
are confirmed against copies acquired in a documented NASA session. Remaining
residual (minor): both acquisitions were owner-mediated; an automated fetch with
transport logs would be the belt-and-suspenders close-out and stays on
`data/SOURCING_LIST.md` A1–A2 as a low-priority item.

### Caption-page quote verification (Tier C, partial P1.5)

Verified verbatim against saved pages in `intake/official/` (source URLs embedded
in the saves):

1. **"Twin Peaks in Super Resolution - Left Eye"**
   (science.nasa.gov/photojournal/twin-peaks-in-super-resolution-left-eye/):
   - Processing quote — "enlarged by 500% and then co-added using Adobe Photoshop to
     produce, in effect, a super-resolution panchromatic frame … color balance was
     adjusted to approximate the true color of Mars." **Matches** `VALIDATION_REPORT.md` §2. ✔
   - Distance/height quote — "The peaks are approximately 30-35 meters (~100 feet)
     tall. North Twin is approximately 860 meters (2800 feet) from the lander, and
     South Twin is about a kilometer away (3300 feet). The scene includes bouldery
     ridges and swales or 'hummocks' of flood debris that range from a few tens of
     meters away from the lander to the distance of the South Twin Peak." **Matches** §2. ✔
2. **"Big Crater as Viewed by Pathfinder Lander"** (PIA01008;
   science.nasa.gov/photojournal/big-crater-as-viewed-by-pathfinder-lander/):
   - "'Far Knob.' This mountain is over 450 meters (1480 feet) tall, and is over 30
     kilometers (19 miles) from the spacecraft." **Verifies** `data/P1_4_RETRIEVAL.md`
     §2's search-rendered quote, now from an in-repo NASA page save. ✔
   - "Another, smaller and closer knob, nicknamed 'Southeast Knob' can be seen as a
     triangular peak to the left of the flanks of the Big Crater rim. This knob is 21
     kilometers (13 miles) southeast from the spacecraft." **Resolves** the retrieval
     log's open question (the sentence the intake framework quoted is genuine NASA
     text) and adds a datum: SE Knob ≈ 21 km SE. ✔
   - New near-field control datum: "The largest rock in the nearfield, just left of
     center in the foreground, nicknamed 'Otter,' is about 1.5 meters (4.9 feet) long
     and 10 meters (33 feet) from the spacecraft." — a published size-and-distance
     known-answer target inside the IMP stereo validity envelope (feeds Phase 5's
     P5.1 disparity-pipeline validation).

### Inventory note

`intake/official/` holds 103 files: JPG/TIF pairs for ~35 PIA products (PIA00613 …
PIA02406, including PIA01008 Big Crater, PIA01466, PIA01120/49/51/52/53 panoramas,
topographic/coordinate maps) plus 32 saved NASA Science pages and 1 MHTML snapshot.
Duplicate: `PIA00965 (1).jpg/.tif` are byte-size-identical twins of `PIA00965.jpg/.tif`.
Per-file hashing of the full set is deferred until a file is actually used as an
analysis input — at that moment its row is added here first (Phase 1 exit rule).
