# Full-Resolution Re-Run of the Twin Peaks Measurement Pipeline

**Task.** Roadmap P2.1–P2.3: re-run `analysis/measure_twin_peaks.py` against the
full-resolution Photojournal products and confirm that the preview-based results in
`VALIDATION_REPORT.md` hold at native product scale. Executed 2026-08-02, on the
repository's own copies of the products (added to `intake/` by the repository owner
in commit `dd009f4`).

## 1. Inputs and provenance

| File | Bytes | SHA-256 | Dimensions | Catalog claim |
|---|---|---|---|---|
| `intake/00/PIA02405.tif` (left eye) | 65,926,165 | `d32ee9af29b6505e7377bf8dd3fadde2554d510d09ab68459a6d9ea1cc2c69d6` | 7238 × 3135 RGB | "7238 x 3135 pixels", "65.93 MB" |
| `intake/00/PIA02406.tif` (right eye) | 70,574,265 | `49de98486fbfc1836e2feb26aecc7589bddad2de437bf706e64e5ba4df484199` | 7296 × 3135 RGB | "7296 x 3135 pixels" |

Both files match the catalog pages' stated pixel dimensions exactly, and the left
eye's byte count equals the catalog page's stated 65.93 MB. **Provenance caveat:**
these copies were supplied by the repository owner; the sandbox's egress policy
still blocks `photojournal.jpl.nasa.gov`, so checksum verification against a fresh
institutional download (Phase 1, P1.1) remains open. **[Update, 2026-08-02, later
the same day:** fresh copies acquired in the owner's documented NASA browser
session (`intake/official/`, science.nasa.gov snapshot headers) are **byte-identical**
to both inputs above — the P1.1 hash check is satisfied; see `data/PROVENANCE.md`.**]**
Duplicate note:
`intake/00/PIA02405 - Copy.png` and `intake/00/PIA02406 - Copy.png` are byte-identical
copies of the two TIFFs (TIFF data under a `.png` extension), not PNG conversions.

## 2. Method: single code path, refactor gate first

`measure_twin_peaks.py` was parameterized (P2.1): all analysis windows are defined
once in reference left-preview coordinates (1568 × 679) and scaled linearly to the
input image; `--image` and `--eye` select the input. Per the Phase 2 plan's refactor
gate, the default invocation was re-run first and reproduced the preview baseline
**exactly** (all apex/base coordinates, extents, and derived values identical;
only descriptive labels changed). Commands:

```
python3 analysis/measure_twin_peaks.py                                  # baseline gate
python3 analysis/measure_twin_peaks.py --image intake/00/PIA02405.tif --eye left
python3 analysis/measure_twin_peaks.py --image intake/00/PIA02406.tif --eye right
```

For the right eye, the apex search windows are widened by ±45 reference px because
the two independently assembled mosaics are offset ~175 product px by framing
(`VALIDATION_REPORT.md` §5.1); all other parameters are identical between eyes.

## 3. Results

Angular extents (apex to visible base) and apparent heights:

| Quantity | Preview (left, 0.905 mrad/px) | Full-res left (0.196 mrad/px) | Full-res right | Agreement |
|---|---|---|---|---|
| North Twin extent | 34.0 px = 30.8 mrad | 155.0 px = **30.4 mrad** | 164.0 px = **32.1 mrad** | Δ(preview, full) = 0.4 mrad; Δ(eyes) = 1.7 mrad |
| North Twin apparent height @ 860 m | 26.5 m | **26.1 m** | **27.6 m** | lower bounds; base occluded |
| South Twin extent | 25.0 px = 22.6 mrad | 115.0 px = **22.5 mrad** | 112.0 px = **22.0 mrad** | Δ(preview, full) = 0.1 mrad; Δ(eyes) = 0.5 mrad |
| South Twin apparent height @ 1006 m | 22.7 m | **22.7 m** | **22.1 m** | lower bounds; base occluded |

All scale-system conclusions are unchanged at full resolution (they depend on
catalog constants, not on the raster): per-anchor overestimate ×1.84/×1.85;
corrected user ruler heights 31.5 m / 28.7 m vs NASA's "30–35 meters"; stereo
disparity 0.174/0.149 native px with ±115–134 % range error at 0.2 px matching.

**Mosaic framing offset, re-measured at full resolution:** summit x-positions
differ between the eyes by 172 product px (North: 4447 − 4275) and 161 product px
(South: 5884 − 5723) — consistent with the ~175 px preview-based figure (the
argmin apex on a flat summit carries a few-native-px horizontal uncertainty), and
~200× the 0.87-px geometric stereo disparity, re-confirming that no stereo signal
is recoverable from these products (F2).

## 4. Error budget (full-res North Twin, per methodology Step 5)

| Term | Value | Contribution |
|---|---|---|
| Pixel count 155 product px (±10 product px = ±2 native px, base-median sensitivity) | 30.4 ± 2.0 mrad | ±6 % |
| IFOV 0.98 vs 1.00 mrad/native px | 2 % systematic | ±2 % |
| Range 860 m (caption "approximately") | ±5 % assumed | ±5 % |
| Base occlusion (one-sided) | — | −0 / +30 % |
| **Total** | | **26.1 m, −2.1/+8.5 m** → consistent with NASA's 30–35 m |

## 5. Gate verdicts (methodology Step 6)

1. **Known-answer test — PASS.** The corrected angular pipeline continues to place
   both peaks at/below NASA's published 30–35 m (26.1 m and 22.7 m as occluded
   lower bounds; the corrected user ruler values 31.5/28.7 m inside/just under).
2. **Cross-eye test — PASS.** Extents agree between the eyes within 1.7 mrad
   (North) and 0.5 mrad (South), inside the ±2-native-px pixel-count tolerance
   (±1.96 mrad).
3. **Preview-fidelity check — PASS.** Full-res extents agree with the preview run
   to ≤0.4 mrad, confirming `VALIDATION_REPORT.md` §2's claim that the previews
   (0.905 mrad/px ≈ native IMP resolution) already carry nearly all real
   information in the products.

## 6. What this does and does not establish

- **Done:** P2.1 (parameterized single code path, full-res re-run), the full-res
  known-answer gate of P2.2 with the error budget above, and P2.3 (cross-eye).
- **Open:** P2.4 (empirical quantification of the 500 % Photoshop interpolation
  floor) requires the *native* IMP EDR frames — PDS dataset `MPFL-M-IMP-2-EDR-V1.0`
  (Phase 1, P1.2), still to be acquired outside the sandbox. `pipeline-v1` tagging
  (P2.5) waits on P2.4 per the roadmap.
- These TIFFs remain press-release visualization products ("enlarged by 500% and
  then co-added using Adobe Photoshop", colorized — catalog pages). Nothing here
  upgrades their radiometric or sub-native-pixel reliability; the resolution-floor
  rule (~2 native px) still governs all morphological claims.

Overlay records: `skyline_overlay_fullres_left_crop.png` and
`skyline_overlay_fullres_right_crop.png` (product-px region 3900–6300 × 150–700
covering both peaks; full-frame overlays are regenerable with the commands above).
