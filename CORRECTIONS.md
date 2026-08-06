# Corrections Log

Errors found in this repository's own work, with the correction and how each was caught.
Kept permanently and append-only: the project's standing rules require error correction to
be visible rather than silent, and a repository that criticises other documents for
fabricated numbers must hold its own to the same standard.

---

## 2026-08-04 — Systematic numerical audit (25 confirmed errors)

**How found.** A factor-of-1000 error (entry 1 below) surfaced during manuscript
preparation. Because one confirmed error invalidates the assumption that the rest is
sound, a full audit was run: six independent auditors recomputed every numeric claim
across all authored documents against canonical verified values, and each flagged
discrepancy was then passed to an adversarial verifier whose default posture was
refutation. 32 candidate errors were flagged; **7 were refuted as false positives**
(rounding, misread context) and **25 were confirmed** and are corrected below.

### Blocking

1. **Resolution comparison wrong by ~10³.** "HiRISE offers a ~3400× finer ground sample
   than the IMP view" → the correct comparison is 0.25 m/px vs 0.98 mrad × 860 m =
   0.84 m/px, i.e. **3.4× finer linearly (11.4× by area)**. Affected
   `VALIDATION_REPORT.md` §7, `analysis/OBJECT_X_SILHOUETTE_REPORT.md` §6,
   `FINDINGS.md` §8. *No conclusion changes*: the decisive advantage of orbital data is
   the elimination of range ambiguity, not sampling density.

2. **Unsupported number producing a fabricated agreement.** `VALIDATION_REPORT.md` §4.1
   and `paper/manuscript.md` §3.1 both claimed the North Twin extent "re-measured in
   pixels (≈194 product px)" gave 75.7 px/in, "agreeing within 4 %" with the print scale
   of 72.9 px/in, and that this "confirms" a ~99-inch print. **The figure 194 appears in
   no measurement anywhere in this repository.** The actual measurements are 155 product
   px (full-res left), 164 px (right), 157 px preview-equivalent — giving 60.5–64.0
   px/in, i.e. 12–17 % *below* the print scale, not 4 % above. The claimed independent
   confirmation did not exist. Corrected: both passages now state that the print scale is
   a *definition* taken from the annotation's own ruler, not an independently confirmed
   quantity, and explain the 12–17 % deficit as the expected apex-to-*visible-base*
   occlusion effect already carried in the error budget. **This is the most serious
   error found** — it is the same failure mode (a number with no provenance supporting a
   satisfying conclusion) that this project documents in the earlier AI-generated
   material. Nothing in §5.3–§5.5 or §4.2–§4.3 of the manuscript depended on it.

3. **"A thousand times the signal"** (`book/the-sphinx-on-mars.md` §IV) → the mosaic
   framing offset (~175 px) is **~200×** the stereo disparity (0.87 product px), not 1000×.

4. **Mars moon torque overstated by ~75×.** `models/CATACLYSM_MODEL.md` Test C and
   `models/cataclysm_stress.py` claimed Mars' moons contribute "~1000× less" spin-axis
   torque than the Sun. Recomputation of the model's own proxy: **Phobos ~13× less**
   (0.077), Deimos ~1500× less (0.00068), both combined ~13× less. The qualitative
   conclusion (Mars' moons cannot stabilise obliquity; Earth's Moon at ~2× the Sun's
   torque can) is unaffected, but the stated factor was wrong.

5. **P1.4 scope understated.** `plans/PHASE_1_PLAN.md` scoped and gated P1.4 as "three
   governing papers"; the roadmap task lists **five** (Smith 1997, Kirk 1999, Parker 1997,
   Golombek 1997, Oberst 1999). Gate updated accordingly.

### Measurement description errors

6. **The "neck" was in the wrong place — and the correction weakens the artificial
   reading.** `analysis/OBJECT_X_SILHOUETTE_REPORT.md` and `paper/manuscript.md` §4.6
   described "a real mid-height constriction," which the semantic discussion then treated
   as the geometry the word *neck* names. Re-examination of the width profile shows the
   apex-to-body transition is a **monotone widening** — there is no constriction between
   "head" and "body" at all. The sole interior width collapse is at **row 56 of 72
   (78 % down, near the base)**, separating the basal mass from a small lower lobe: a
   position consistent with a shadow or talus boundary, not anatomy. Corrected in both
   documents, with the discussion rewritten to state that the geometry does not support
   the conferral. *This correction makes the null result stronger, not weaker.*

7. **Area reported as if linear.** "largest sub-feature 82 native px (8.9 mrad)" conflated
   an **area** (2062 product px² = 82 native px²) with a linear extent. Corrected to give
   the bounding box (99 × 54 product px = 19.4 × 10.6 mrad) and label the 8.9 mrad figure
   explicitly as an equivalent-square side. Median blob likewise is ~1 native px² of area.

8. **Undocumented threshold.** The sub-feature decomposition uses the 88th percentile,
   while the method section documented only the 80th percentile used for the envelope.
   At 80 % the same code gives 61 blobs, largest 143 native px² — so the documented
   method did not reproduce the reported numbers. Both thresholds are now stated.

### Arithmetic and consistency

9. Error-budget total: **−2.1/+8.5 m → −2.1/+8.1 m** (quadrature sum; upper bound 34.2 m).
   `analysis/FULLRES_RERUN.md` §4 and `paper/manuscript.md` Appendix A. Conclusion
   ("consistent with 30–35 m") unchanged.
10. Cross-eye agreement stated as 1.7 / 0.5 mrad → **1.76 / 0.59 mrad** (9 and 3 product
    px). Still inside the ±1.96 mrad tolerance; gate verdict PASS unchanged.
11. Horizon-error threshold: "±2 native px moves Z by >100 % beyond ~150 m" → the
    threshold is Z = h/(2δ) = **~380 m** (h = 1.5 m) / **~470 m** (h = 1.85 m); at 150 m
    the excursion is −16 %/+24 %. `SIZE_VERIFICATION_METHODOLOGY.md` Step 3c. The
    operational guidance ("use only below ~50 m") is unaffected.
12. Range/size ambiguity stated as "factor-of-~20" → **factor-of-~33** (30 m to 1006 m),
    matching the silhouette report's own table. `VALIDATION_REPORT.md` §5.5,
    `FINDINGS.md` §4, `plans/PHASE_3_PLAN.md` §1.
13. Cydonia–Pathfinder separation "3,000 km" → **~1,750 km**. `FINDINGS.md` §6.
14. "57.4 m — half again too tall" → **nearly twice** (the ratio is ×1.84).
    `book/the-sphinx-on-mars.md` §IV.
15. Cydonia Face "a mile across" → **~2 miles (about 3 km)**, matching the sourced mesa
    length in the same paragraph. `book/the-sphinx-on-mars.md` §VI.
16. Stale cross-reference "(see §5.2)" → **§5.1**. `VALIDATION_REPORT.md` §2.
17. Stale cross-reference for the 31.9 m corrected ruler length: `analysis/FULLRES_RERUN.md`
    → **`VALIDATION_REPORT.md` §5.5**. (Value 31.9 m is correct and unchanged.)
18. Stale cross-reference "Phase 1 plan §6 no-DTM row" → **§3 step S6**.
    `plans/PHASE_3_PLAN.md`.
19. Methodology Step 7 cited a pre-registered hypothesis as "73 ft × 193 ft sphinx-scale
    object" — an *uncorrected* figure from the invalidated ruler system. Replaced with the
    repo's actual pre-registered H1 (plan length 73 m ± 15 % = 62.05–83.95 m; relief 20 m
    ± 25 % = 15.0–25.0 m).
20. `plans/PHASE_0_PLAN.md` header-drafter count "6" matched neither the class-(iv)-excluded
    count (5) nor the included count (9) → **9**.
21. `plans/PHASE_3_PLAN.md` claimed two "methodologically distinct" print-to-pixel routes
    (horizontal via width, vertical via 43-in/3135-px). These are **algebraically the same
    relation**; the duplicates provide procedural independence only. The claim is now
    stated as the limitation it is, and the expected x-range corrected from 4386–4605 to
    **4374–4593** product px.

---

## 2026-08-04 (later) — Self-correction found within one turn of publication

**26. The anchor-separation argument in `analysis/FIXING_THE_ZERO_POINT.md` §3 was
wrong.** As first published, that section claimed the two calibration anchors were
"0.0177 in apart geometrically versus 0.375 in as annotated — ×21 too far," concluding
the calibration baseline carried no range information. The error: it applied the
*ground-range* depression relation Z = h_cam/tan θ to marks that are not ground points.
The annotation's own table (`B. 4 7/8 TO F. 7 7/16 = 2 9/16`) identifies **B as the North
Twin summit and F as its visible base**, so B and C are summit marks, whose elevation
above the horizon is h_peak/Z.

Read correctly they are a *successful* measurement: 34.4 mrad × 860 m = **29.6 m** and
29.0 mrad × 1006 m = **29.2 m** — agreeing with each other to 1 % and consistent with
NASA's published 30–35 m; the predicted mark separation for ~30 m peaks is 0.354 in
against 0.375 in annotated (6 %). The marks also land within **1 product pixel** of the
pipeline's independently measured apex rows.

The section's *conclusion* survives — the linear model is still invalid — but now for the
correct reason: Z × (inches above horizon) is constant (2068 vs 2042, 1.3 %), confirming
the hyperbolic law, while propagating North's factor to South mispredicts by −16 %, which
is exactly why two inconsistent ft/in factors were needed.

**Found:** while building the corrected overlay, by checking what the anchor marks
physically are before drawing them. **Elapsed:** under one turn from publication.
**Net effect:** the correction is favourable to the original annotation — the hand
measurement was better than the previous analysis credited.

---

## 2026-08-02 — Corrections made during ordinary work

- `analysis/FULLRES_RERUN.md`: provenance caveat updated when owner-supplied TIFFs were
  confirmed byte-identical to an independent NASA-session download (P1.1 hash check
  satisfied).
- `data/P1_4_RETRIEVAL.md`: the open question of whether the "Southeast Knob" sentence was
  genuine NASA text was resolved affirmatively against a saved NASA caption page.

---

## Standing policy

1. Errors are corrected **in place** with a dated, visible note, never silently.
2. The correction states what changes downstream and what does not.
3. Corrections that *strengthen* a null result (e.g. entry 6) are reported with the same
   prominence as those that weaken it.
4. A correction is not complete until every document repeating the error is fixed —
   `grep` the whole repository for the erroneous figure before closing.
