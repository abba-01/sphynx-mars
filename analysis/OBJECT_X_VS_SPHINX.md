# Object X vs the Great Sphinx of Giza — Scale Comparison, Including a Range-Free Upper Bound

**What this adds.** Every earlier comparison in this repository (`VALIDATION_REPORT.md`
§5.5, `book/the-sphinx-on-mars.md`, `paper/manuscript.md`) computed Object X's size at an
*assumed* range and compared that single figure to the Sphinx. This document does one new
thing: it uses NASA's own stated **upper bound** on the hummock field's range to compute
an upper bound on Object X's size that requires **no range assumption at all** — and asks,
in reverse, how far away Object X would have to be to actually match the Sphinx.

## 1. Inputs (all previously established, sourced)

- Object X's measured angular envelope: **33.5 × 14.1 mrad** (cluster envelope,
  `analysis/object_x_silhouette.py`, run on full-resolution PIA02406).
- NASA's caption bound on the hummock field's range: "a few tens of meters away from the
  lander **to the distance of the South Twin Peak**" — i.e. **≤ 1005.8 m**
  (`VALIDATION_REPORT.md` §2). This is a stated maximum, not an assumption.
- Great Sphinx of Giza: **73 m long, 20 m high** (*Encyclopædia Britannica*, "Great Sphinx
  of Giza").

## 2. Size at each candidate range

| Assumed range | Object X | % of Sphinx length | % of Sphinx height |
|---|---|---|---|
| 30 m | 1.0 × 0.4 m | 1% | 2% |
| 100 m | 3.4 × 1.4 m | 5% | 7% |
| 300 m | 10.1 × 4.2 m | 14% | 21% |
| 860 m (North Twin) | 28.8 × 12.1 m | 39% | 61% |
| **1006 m (NASA's stated maximum)** | **33.7 × 14.2 m** | **46%** | **71%** |

(For comparison, the corrected *ruler* estimate at 860 m — `VALIDATION_REPORT.md` §5.5 —
is 31.9 × 9.1 m: 44% / 45% of the Sphinx, consistent with the independent pixel envelope.)

## 3. The range-free result

**Object X cannot equal the Sphinx's size anywhere inside NASA's stated field.** Inverting
the angular relation (Z = size ÷ angle) gives the range at which each dimension would
match:

- Length match (73 m): requires Z = 73 / 0.0335 = **2179 m**
- Height match (20 m): requires Z = 20 / 0.0141 = **1418 m**

Both exceed NASA's stated maximum range for the hummock field (1006 m) — by **×2.2** and
**×1.4** respectively. This conclusion does not depend on which range within the caption's
own stated bound is assumed; it holds at the bound itself, which is the most generous
reading available.

**The firm upper bound, therefore:** at the absolute maximum range the caption allows,
Object X is at most **46% of the Sphinx's length and 71% of its height** — under half the
Sphinx by length in every case the source data permit, and reaching most-but-not-all of
its height only at the single most extreme (and least likely) range in the caption's
range.

## 4. What does not survive: the aspect ratio

The one quantity immune to the range ambiguity is the aspect ratio, since range cancels:

- Object X: 14.1/33.5 = **0.421**
- Sphinx: 20/73 = **0.274**

These do not match (Object X is proportionally taller/stubbier), and in any case, per
`VALIDATION_REPORT.md` §5.5, a height-to-length ratio in this range is common to most
elongated natural mounds and has no discriminating power for artificiality.

## 5. Verdict

Combining §3 and §4: there is no range inside NASA's own stated bound on the hummock
field at which Object X matches the Sphinx in absolute size, and its proportions do not
match either. The strongest statement the data support in the Sphinx's favor is the
already-published caveat (`VALIDATION_REPORT.md` §5.5) that at one particular assumed
range (860 m) the uncorrected ruler figures come within 80–83% before correction — a
number this document's §2 table also reports as the *ceiling* case, and which falls to
44–45% once the ×1.84 scale correction is applied. The range-free bound in §3 confirms that
ceiling was never reachable in the first place: even at the most generous range NASA's
caption allows, the match tops out at 46%/71%, and reaching it requires trusting the very
extreme edge of a caption phrase that was never meant as a precise distance measurement.

Figure: `analysis/objectx_vs_sphinx_scale.png` (both objects drawn to the same metre
scale, generated inline; not a separate script — see the commit that added this file for
the generating code, or regenerate from the numbers in §2–§3).

*This document extends, and does not supersede, `analysis/OBJECT_X_SILHOUETTE_REPORT.md`
§5 (where naming enters) and `VALIDATION_REPORT.md` §5.5. Object X's identity remains
undetermined by these images regardless of size; this document addresses size alone.*
