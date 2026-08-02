#!/usr/bin/env python3
"""Independent re-measurement of the Twin Peaks in PIA02405/PIA02406.

Reproducible check of the ruler-based scale system in this repository,
using only the repo's own preview images (verified to be exact-aspect
downscales of the NASA Photojournal products) and NASA-published camera
constants.

Camera constants (Smith et al. 1997, JGR 102(E2), doi:10.1029/96JE03568):
  - IFOV: 0.98 mrad/pixel (native IMP pixel)
  - FOV per eye: 14.4 x 14.0 deg; frame 256 x 256 px; f/18
  - stereo baseline: 15.0 cm; focal length 23 mm / 23 um pixels -> f = 1000 px
  - deployed camera height: 1.5 m above the surface (nominal; mission
    reports give 1.75-1.85 m achieved) [mars.nasa.gov/MPF/mpf/sci_desc.html]

Product constants (NASA Photojournal catalog pages PIA02405/PIA02406):
  - left eye 7238 x 3135 px, right eye 7296 x 3135 px
  - frames "enlarged by 500% and then co-added using Adobe Photoshop"
    -> 1 product px = 1/5 native px = 0.196 mrad
  - caption distances: North Twin ~860 m (2800 ft), South Twin ~1 km (3300 ft)
  - caption heights: "approximately 30-35 meters (~100 feet) tall"

Usage: python3 analysis/measure_twin_peaks.py   (from the repo root;
requires Pillow and numpy)
"""
import numpy as np
from PIL import Image, ImageDraw

IFOV_NATIVE = 0.98e-3        # rad per native IMP pixel (Smith et al. 1997)
ENLARGE = 5.0                # Photojournal caption: "enlarged by 500%"
PRODUCT_W = 7238             # PIA02405 (left eye) width, catalog page
PRODUCT_H = 3135
D_NORTH_M = 860.0            # caption distance to North Twin
D_SOUTH_M = 1005.8           # 3300 ft (caption "about a kilometer / 3300 ft")
FT = 3.280839895

# --- the user's scale system, transcribed from the annotated image -------
RULER_SPAN_IN = 43.0         # "0 inches" top edge -> "43 inch mark" (D) bottom
USER_SCALES = {              # per-anchor ft/inch factors from the annotation
    "B (North Twin, 2800 ft)": 2800.0 / (43.0 - 4.875),   # 73.44 ft/in
    "C (South Twin, 3300 ft)": 3300.0 / (43.0 - 5.25),    # 87.42 ft/in
}
USER_HEIGHTS_FT = {"F North Twin": 188 + 12/61, "G South Twin": 174 + 126/151}
USER_EXTENTS_IN = {"F North Twin": 2 + 9/16, "G South Twin": 2.0}


def skyline(path):
    """First row (per column) where luminance departs >6% from the sky."""
    im = np.asarray(Image.open(path).convert("RGB")).astype(float)
    lum = im.mean(axis=2)
    ys = np.zeros(im.shape[1], int)
    for x in range(im.shape[1]):
        col = lum[:, x]
        thr = col[:40].mean() * 0.94
        idx = np.where((col[:-2] < thr) & (col[1:-1] < thr) & (col[2:] < thr))[0]
        ys[x] = idx[0] if len(idx) else -1
    return ys


def main():
    L = skyline("preview.webp")            # downscaled PIA02405
    W = len(L)
    sc_prod = PRODUCT_W / W                # preview px -> product px
    mrad_per_preview_px = sc_prod / ENLARGE * IFOV_NATIVE * 1e3

    print(f"preview width {W}, scale to product {sc_prod:.3f}, "
          f"{mrad_per_preview_px:.3f} mrad/preview px")

    def apex(a, b):
        i = int(np.argmin(L[a:b])); return a + i, int(L[a + i])

    nx, ny = apex(800, 1050)               # North Twin
    sx, sy = apex(1120, 1420)              # South Twin
    n_base = float(np.median(np.r_[L[700:790], L[1040:1100]]))
    s_base = float(np.median(np.r_[L[1060:1110], L[1430:1520]]))

    rows = []
    for name, (ax, ay, base, Z) in {
        "North Twin": (nx, ny, n_base, D_NORTH_M),
        "South Twin": (sx, sy, s_base, D_SOUTH_M),
    }.items():
        ext_px = base - ay
        ang = ext_px * mrad_per_preview_px * 1e-3          # rad
        h = Z * ang
        rows.append((name, ax, ay, base, ext_px, ang * 1e3, h))
        print(f"{name}: apex=({ax},{ay}) visible base y={base:.1f} "
              f"extent={ext_px:.1f} preview px = {ang*1e3:.1f} mrad "
              f"-> apparent height {h:.1f} m at {Z:.0f} m "
              f"(lower bound; base partly occluded by ridges)")

    # --- print-scale reconstruction and correction factor ----------------
    prod_px_per_inch = PRODUCT_H / RULER_SPAN_IN           # 72.9
    rad_per_inch = prod_px_per_inch / ENLARGE * IFOV_NATIVE
    print(f"\nprint scale: {prod_px_per_inch:.1f} product px/inch "
          f"= {rad_per_inch*1e3:.2f} mrad/inch")
    for anchor, s_user in USER_SCALES.items():
        Z_ft = 2800.0 if "North" in anchor else 3300.0
        s_true = Z_ft * rad_per_inch                       # true transverse ft/in
        print(f"{anchor}: user scale {s_user:.2f} ft/in, "
              f"true transverse scale {s_true:.2f} ft/in, "
              f"overestimate x{s_user/s_true:.2f}")

    print()
    for k in USER_HEIGHTS_FT:
        Z_m = D_NORTH_M if "North" in k else D_SOUTH_M
        h_corr = USER_EXTENTS_IN[k] * rad_per_inch * Z_m * FT
        print(f"{k}: user height {USER_HEIGHTS_FT[k]:.1f} ft; corrected with "
              f"angular scale: {h_corr:.1f} ft = {h_corr/FT:.1f} m "
              f"(NASA caption: 30-35 m)")

    # --- stereo geometry --------------------------------------------------
    f_px, B = 1000.0, 0.15
    for Z in (D_NORTH_M, D_SOUTH_M):
        d = f_px * B / Z
        sigZ = Z**2 * 0.2 / (f_px * B)
        print(f"\nZ={Z:.0f} m: stereo disparity {d:.3f} native px "
              f"({d*ENLARGE:.2f} product px = "
              f"{d*ENLARGE/prod_px_per_inch:.4f} print inches); "
              f"range error for 0.2 px matching: +/-{sigZ:.0f} m "
              f"({100*sigZ/Z:.0f}% of distance)")

    # --- near-field / horizon mapping ------------------------------------
    for h_cam in (1.5, 1.85):
        horizon_km = np.sqrt(2 * 3_389_500 * h_cam) / 1e3
        y_h = float(np.median(L[80:600]))                  # far skyline row
        below = (PRODUCT_H - y_h * sc_prod) / ENLARGE * IFOV_NATIVE
        z_bottom = h_cam / np.tan(below)
        print(f"\ncamera height {h_cam} m: flat-ground horizon {horizon_km:.2f} km; "
              f"bottom edge of frame is ground at ~{z_bottom:.1f} m "
              f"(the '43-inch mark' is NOT range zero)")

    # --- overlay ----------------------------------------------------------
    im = Image.open("preview.webp").convert("RGB")
    d = ImageDraw.Draw(im)
    for x in range(0, W, 2):
        if L[x] >= 0:
            d.point((x, int(L[x])), fill=(0, 255, 0))
    for name, ax, ay, base, *_ in rows:
        d.line([(ax, ay), (ax, int(base))], fill=(255, 0, 0), width=2)
        d.text((ax + 5, ay), name, fill=(255, 255, 0))
    im.save("analysis/skyline_overlay.png")
    print("\nwrote analysis/skyline_overlay.png")


if __name__ == "__main__":
    main()
