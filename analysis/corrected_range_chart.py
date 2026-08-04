#!/usr/bin/env python3
"""The corrected replacement for the print's range scale ("fixing the nose").

The original scale system placed range zero at the print's bottom edge (the
"43 inch mark", point D) and assumed range grows linearly upward. This script
computes what the geometry actually requires, and shows why the original
scheme cannot be repaired by relocating its origin.

Three results:

  1. THE TRUE ORIGIN IS THE HORIZON, NOT THE BOTTOM EDGE. For a camera at
     height h over locally level ground, a point at range Z appears at
     depression angle theta = atan(h/Z) BELOW the horizon. The reference line
     is therefore the horizon row, and range is read downward from it. The
     horizon is not a zero: it is a singularity (Z -> infinity).

  2. NO ORIGIN MAKES A LINEAR MODEL CORRECT. Z = h/tan(theta) is hyperbolic.
     Relocating the origin changes the derived scale factors but cannot change
     the functional form; a linear print-position-to-range map is wrong at
     every origin.

  3. THE TWO CALIBRATION ANCHORS ARE, GEOMETRICALLY, ON TOP OF EACH OTHER.
     North Twin (860 m) and South Twin (1006 m) differ in depression angle by
     ~0.25 mrad = ~0.018 print inches. The annotation separates them by
     0.375 in -- about 21x too far. Their apparent separation on the print is
     occluding terrain, not range, so no range scale can be calibrated from it.

What replaces it: for TRANSVERSE size the angular relation needs no origin at
all (size = Z * N * IFOV), which is why the corrected pipeline works. For
NEAR-FIELD range the chart below is the honest ruler -- valid only on locally
level ground and only where the flat-ground assumption holds (see
SIZE_VERIFICATION_METHODOLOGY.md Step 3c: use below ~50 m).

Run: python3 analysis/corrected_range_chart.py
"""
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

IFOV = 0.98e-3          # rad per native px (Smith et al. 1997)
ENLARGE = 5.0           # catalog: "enlarged by 500%"
PRODUCT_H = 3135
RULER_IN = 43.0         # annotation ruler span over the product height
MRAD_PER_IN = PRODUCT_H / RULER_IN / ENLARGE * IFOV * 1e3   # 14.29
H_NOM, H_DEP = 1.5, 1.85        # camera height: nominal / as-deployed
USER_FACTOR = 2800.0 / (43.0 - 4.875)   # 73.44 ft/in, the original model
FT = 3.280839895


def horizon_print_inch(path="preview.webp", x0=80, x1=600):
    """Locate the far skyline (horizon proxy) and return its print-inch position."""
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(float).mean(axis=2)
    rows = []
    for x in range(x0, min(x1, a.shape[1])):
        col = a[:, x]
        thr = col[:40].mean() * 0.94
        idx = np.where((col[:-2] < thr) & (col[1:-1] < thr) & (col[2:] < thr))[0]
        if len(idx):
            rows.append(idx[0])
    return float(np.median(rows)) / im.size[1] * RULER_IN


def range_from_depression(d_in, h):
    """Ground range for a point d_in print-inches below the horizon."""
    theta = d_in * MRAD_PER_IN * 1e-3
    return h / np.tan(theta) if theta > 0 else np.inf


def inches_below_horizon(Z, h):
    """Inverse: where a given range plots, in print inches below the horizon."""
    return np.arctan(h / Z) * 1e3 / MRAD_PER_IN


def main():
    hor = horizon_print_inch()
    print(f"angular scale        : {MRAD_PER_IN:.3f} mrad per print inch")
    print(f"horizon located at   : print inch {hor:.2f} from the top edge")
    print(f"original 'zero' (D)  : print inch {RULER_IN:.1f} (the bottom edge)")
    print(f"bottom edge is       : {RULER_IN - hor:.2f} in below the horizon\n")

    print("CORRECTED NEAR-FIELD RANGE CHART (read DOWN from the horizon)")
    print(f"{'in below horizon':>16} {'depression':>12} {'Z, h=1.5 m':>12} "
          f"{'Z, h=1.85 m':>12} {'original model':>15}")
    for d in (0.25, 0.5, 1, 2, 4, 8, 16, 24, RULER_IN - hor):
        p = hor + d                       # absolute print inch
        lin = (RULER_IN - p) * USER_FACTOR / FT     # original linear model, metres
        print(f"{d:>16.2f} {d*MRAD_PER_IN:>9.1f} mr {range_from_depression(d, H_NOM):>12.1f} "
              f"{range_from_depression(d, H_DEP):>12.1f} {lin:>15.1f}")

    print("\nWHY RELOCATING THE ZERO CANNOT FIX IT")
    for Z, name in ((860.0, "North Twin"), (1005.8, "South Twin")):
        print(f"  {name:11s} ({Z:6.1f} m): {inches_below_horizon(Z, H_NOM):.4f} in below horizon")
    sep = abs(inches_below_horizon(860.0, H_NOM) - inches_below_horizon(1005.8, H_NOM))
    annot = 5.25 - 4.875
    print(f"  geometric separation of the two anchors : {sep:.4f} in ({sep*1000:.1f} thou)")
    print(f"  separation used by the annotation       : {annot:.3f} in")
    print(f"  overstatement                           : x{annot/sep:.0f}")
    print("  => the anchors' apparent separation is occluding terrain, not range;")
    print("     a range scale cannot be calibrated from it at any origin.")

    print("\nWHAT REPLACES IT")
    print("  transverse size : s = Z * N * IFOV   (no origin required)")
    print("  near-field range: the chart above, valid on level ground below ~50 m")
    print("  far-field range : from orbital cartography, never from print position")


if __name__ == "__main__":
    main()
