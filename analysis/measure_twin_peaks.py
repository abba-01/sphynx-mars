#!/usr/bin/env python3
"""Independent re-measurement of the Twin Peaks in PIA02405/PIA02406.

Reproducible check of the ruler-based scale system in this repository,
using the repo's preview images (verified to be exact-aspect downscales
of the NASA Photojournal products) or the full-resolution TIFF products
in intake/, and NASA-published camera constants. One code path serves
both resolutions (roadmap P2.1): analysis windows are defined once in
reference left-preview coordinates (1568 x 679) and scaled to the input
image, so the default invocation reproduces the preview-based numbers in
VALIDATION_REPORT.md exactly.

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

Usage (from the repo root; requires Pillow and numpy):
  python3 analysis/measure_twin_peaks.py                       # preview, left eye
  python3 analysis/measure_twin_peaks.py --image intake/PIA02405.tif
  python3 analysis/measure_twin_peaks.py --image intake/PIA02406.tif --eye right
"""
import argparse
import os

import numpy as np
from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None  # the full-res products exceed Pillow's default cap

IFOV_NATIVE = 0.98e-3        # rad per native IMP pixel (Smith et al. 1997)
ENLARGE = 5.0                # Photojournal caption: "enlarged by 500%"
PRODUCT_W = {"left": 7238, "right": 7296}   # catalog pages
PRODUCT_H = 3135
D_NORTH_M = 860.0            # caption distance to North Twin
D_SOUTH_M = 1005.8           # 3300 ft (caption "about a kilometer / 3300 ft")
FT = 3.280839895

# Reference geometry all analysis windows are defined in: the left-eye
# preview (preview.webp), 1568 x 679. Windows scale linearly with the
# input image's width/height, so preview and full-res runs share one path.
REF_W, REF_H = 1568, 679
APEX_WIN = {"North Twin": (800, 1050), "South Twin": (1120, 1420)}
BASE_WIN = {"North Twin": ((700, 790), (1040, 1100)),
            "South Twin": ((1060, 1110), (1430, 1520))}
FAR_SKY_WIN = (80, 600)
SKY_ROWS_REF = 40            # rows sampled per column for the sky level
PERSIST_REF = 3              # consecutive below-threshold rows = skyline
# The two eyes' mosaics are offset ~175 product px by framing alone
# (VALIDATION_REPORT.md section 5.1) = ~38 reference px; widen the apex
# search for the right eye so the summits stay inside the windows.
RIGHT_EYE_PAD = 45

# --- the user's scale system, transcribed from the annotated image -------
RULER_SPAN_IN = 43.0         # "0 inches" top edge -> "43 inch mark" (D) bottom
USER_SCALES = {              # per-anchor ft/inch factors from the annotation
    "B (North Twin, 2800 ft)": 2800.0 / (43.0 - 4.875),   # 73.44 ft/in
    "C (South Twin, 3300 ft)": 3300.0 / (43.0 - 5.25),    # 87.42 ft/in
}
USER_HEIGHTS_FT = {"F North Twin": 188 + 12/61, "G South Twin": 174 + 126/151}
USER_EXTENTS_IN = {"F North Twin": 2 + 9/16, "G South Twin": 2.0}


def skyline(path, sy):
    """First row (per column) where luminance departs >6% from the sky.

    sy scales the row-count parameters (sky sample depth, persistence run)
    from reference-preview rows to the input image's rows; at sy = 1 this
    is bit-identical to the original preview-only implementation.
    """
    arr = np.asarray(Image.open(path).convert("RGB"))
    lum = arr.mean(axis=2, dtype=np.float32)
    sky_rows = max(1, int(round(SKY_ROWS_REF * sy)))
    n = max(1, int(round(PERSIST_REF * sy)))
    ys = np.zeros(lum.shape[1], int)
    kernel = np.ones(n, int)
    for x in range(lum.shape[1]):
        col = lum[:, x]
        thr = col[:sky_rows].mean() * 0.94
        runs = np.convolve((col < thr).astype(int), kernel, "valid") == n
        idx = np.where(runs)[0]
        ys[x] = idx[0] if len(idx) else -1
    return ys


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--image", default="preview.webp",
                    help="input image (preview or full-res product)")
    ap.add_argument("--eye", choices=("left", "right"), default="left",
                    help="which product the image is (sets catalog width)")
    ap.add_argument("--overlay", default=None,
                    help="overlay output path (default: derived from input)")
    args = ap.parse_args()

    with Image.open(args.image) as im0:
        W, H = im0.size
    sx, sy = W / REF_W, H / REF_H
    pad = int(round(RIGHT_EYE_PAD * sx)) if args.eye == "right" else 0

    L = skyline(args.image, sy)
    sc_prod = PRODUCT_W[args.eye] / W      # image px -> product px
    mrad_per_px = sc_prod / ENLARGE * IFOV_NATIVE * 1e3

    print(f"image {args.image} ({args.eye} eye), width {W}, "
          f"scale to product {sc_prod:.3f}, {mrad_per_px:.3f} mrad/image px")

    def win(a, b, p=0):
        return max(0, int(round(a * sx)) - p), min(W, int(round(b * sx)) + p)

    def apex(a, b):
        i = int(np.argmin(L[a:b])); return a + i, int(L[a + i])

    def base_of(name):
        (a1, b1), (a2, b2) = BASE_WIN[name]
        return float(np.median(np.r_[L[slice(*win(a1, b1))],
                                     L[slice(*win(a2, b2))]]))

    rows = []
    for name, Z in (("North Twin", D_NORTH_M), ("South Twin", D_SOUTH_M)):
        ax, ay = apex(*win(*APEX_WIN[name], pad))
        base = base_of(name)
        ext_px = base - ay
        ang = ext_px * mrad_per_px * 1e-3          # rad
        h = Z * ang
        rows.append((name, ax, ay, base, ext_px, ang * 1e3, h))
        print(f"{name}: apex=({ax},{ay}) visible base y={base:.1f} "
              f"extent={ext_px:.1f} image px = {ang*1e3:.1f} mrad "
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
        y_h = float(np.median(L[slice(*win(*FAR_SKY_WIN))]))   # far skyline row
        below = (PRODUCT_H - y_h * sc_prod) / ENLARGE * IFOV_NATIVE
        z_bottom = h_cam / np.tan(below)
        print(f"\ncamera height {h_cam} m: flat-ground horizon {horizon_km:.2f} km; "
              f"bottom edge of frame is ground at ~{z_bottom:.1f} m "
              f"(the '43-inch mark' is NOT range zero)")

    # --- overlay ----------------------------------------------------------
    if args.overlay is None:
        if args.image == "preview.webp":
            overlay = "analysis/skyline_overlay.png"
        else:
            stem = os.path.splitext(os.path.basename(args.image))[0]
            overlay = f"analysis/skyline_overlay_{stem}_{args.eye}.png"
    else:
        overlay = args.overlay
    im = Image.open(args.image).convert("RGB")
    d = ImageDraw.Draw(im)
    lw = max(2, int(round(2 * sx)))
    for x in range(0, W, 2):
        if L[x] >= 0:
            d.point((x, int(L[x])), fill=(0, 255, 0))
    for name, ax, ay, base, *_ in rows:
        d.line([(ax, ay), (ax, int(base))], fill=(255, 0, 0), width=lw)
        d.text((ax + 5 * lw // 2, ay), name, fill=(255, 255, 0))
    im.save(overlay)
    print(f"\nwrote {overlay}")


if __name__ == "__main__":
    main()
