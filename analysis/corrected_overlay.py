#!/usr/bin/env python3
"""Corrected-geometry overlay on the highest-resolution available product.

SOURCE SELECTION (documented, not assumed). Every product in intake/official/
was surveyed by pixel count and angular sampling. The 360-degree panoramas
(PIA00752, PIA00782, PIA00662, PIA00994, PIA01005, PIA01466) are 6222-6283 px
wide, i.e. 6283 mrad / width = ~1.0 mrad per pixel: native IMP sampling.
PIA01149 (24.4 Mpx) is a two-panel near-field figure; PIA01008 is a superpan of
the Big Crater azimuth, not Twin Peaks. The Twin Peaks super-resolution
products PIA02405 (7238x3135) and PIA02406 (7296x3135) are "enlarged by 500%"
per their catalog pages, giving 0.196 mrad per product pixel -- ~5x finer
angular sampling than any other product covering this scene. PIA02405 (left
eye) is used here because it is the substrate the annotation print was made
from (preview.webp is its downscale).

WHAT THE OVERLAY DRAWS (all corrections established in
analysis/FIXING_THE_ZERO_POINT.md and VALIDATION_REPORT.md):

  1. HORIZON (the true reference line) at product row 531, versus the
     annotation's assumed range origin D at the bottom edge -- 2604 px away,
     at the far end of the frame and in the opposite direction of measurement.
  2. The two anchor marks B and C read CORRECTLY as summit elevations above
     the horizon. Solving h = Z * theta gives 29.6 m and 29.2 m, agreeing with
     each other to 1% and consistent with NASA's published 30-35 m. The
     annotation's own marks, read with the right model, measure the peaks.
  3. The annotation marks verified against the pipeline's independently
     measured apex rows: agreement within 1 product px (0.2 native px).
  4. The RESOLUTION FLOOR bar: 2 native px = 10 product px, the smallest
     credible morphological detail.
  5. Object X: the measured cluster envelope, with absolute size shown as a
     function of assumed range (indeterminate; factor-of-33 ambiguity).

Run: python3 analysis/corrected_overlay.py
Outputs: analysis/corrected_overlay_scene.png (full-width, reduced)
         analysis/corrected_overlay_objectx.png (full-resolution detail)
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None

SRC = "intake/00/PIA02405.tif"          # left eye: the annotation substrate
SRC_R = "intake/00/PIA02406.tif"        # right eye: Object X markup calibration
IFOV = 0.98e-3
ENLARGE = 5.0
MRAD_PPX = IFOV / ENLARGE * 1e3          # 0.196 mrad per product px
PH, RULER = 3135, 43.0
PX_PER_IN = PH / RULER                   # 72.907
HORIZON_ROW = 531                        # measured (see FIXING_THE_ZERO_POINT)
ANCHORS = {"B  North Twin summit": (4.875, 860.0), "C  South Twin summit": (5.25, 1005.8)}
MEASURED_APEX = {"B  North Twin summit": 356, "C  South Twin summit": 382}
OBJX_RIGHT = (4312, 4500, 522, 635)      # Object X box, right-eye product px
FRAMING_OFFSET = 172                     # right - left, measured at the summits

WHITE, YEL, CYA, RED, GRN, ORG = ((255,255,255),(255,214,0),(0,229,255),
                                  (255,82,82),(105,240,174),(255,145,0))


def font(sz):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(p, sz)
        except OSError:
            pass
    return ImageFont.load_default()


def label(dr, xy, text, fill, fnt, pad=5):
    x, y = xy
    b = dr.textbbox((x, y), text, font=fnt)
    dr.rectangle([b[0]-pad, b[1]-pad, b[2]+pad, b[3]+pad], fill=(0, 0, 0))
    dr.text((x, y), text, fill=fill, font=fnt)


def scene_overlay(out="analysis/corrected_overlay_scene.png", W=2600):
    im = Image.open(SRC).convert("RGB")
    s = W / im.size[0]
    im = im.resize((W, int(im.size[1] * s)), Image.LANCZOS)
    dr = ImageDraw.Draw(im)
    f, fs = font(30), font(22)

    # --- 1. the true reference: the horizon
    hy = HORIZON_ROW * s
    dr.line([(0, hy), (W, hy)], fill=CYA, width=3)
    label(dr, (18, hy - 42), "TRUE REFERENCE — HORIZON  (θ→0, Z→∞ : a singularity, not a zero)", CYA, f)

    # --- the annotation's assumed origin, at the far edge
    by = PH * s - 4
    dr.line([(0, by), (W, by)], fill=RED, width=4)
    label(dr, (18, by - 40), "ANNOTATION'S ASSUMED RANGE ZERO  \"D\" (43 in) — "
                             f"{PH-HORIZON_ROW} px away, wrong end, wrong direction; true range here ≈ 2.7 m",
          RED, fs)

    # --- 2/3. anchors read correctly
    for i, (name, (inch, Z)) in enumerate(ANCHORS.items()):
        row = inch * PX_PER_IN
        y = row * s
        el_in = HORIZON_ROW / PX_PER_IN - inch
        th = el_in * PX_PER_IN * MRAD_PPX          # mrad above horizon
        h = Z * th * 1e-3
        dr.line([(0, y), (W, y)], fill=YEL, width=2)
        d = MEASURED_APEX[name] - row
        # stagger: first anchor label above-left, second below-left, so the
        # two lines (only ~27 product px apart) never overlap
        ly = y - 34 if i == 0 else y + 8
        label(dr, (18, ly),
              f"{name}   {th:.1f} mrad above horizon × {Z:.0f} m  →  h = {h:.1f} m"
              f"   (apex Δ{d:+.1f} px)", YEL, fs)

    label(dr, (18, 14),
          "PIA02405 left eye, 7238×3135, 0.196 mrad/product px — highest angular sampling "
          "of this scene (360° pans are 1.0 mrad/px)", WHITE, fs)
    label(dr, (18, 48),
          "Both anchors solved independently give 29.6 m and 29.2 m — agreeing to 1% and "
          "consistent with NASA's published 30–35 m", GRN, fs)

    # --- 4. resolution floor bar (2 native px = 10 product px)
    bx, byy, blen = W - 720, im.size[1] - 150, 10 * s
    dr.line([(bx, byy), (bx + max(blen, 2), byy)], fill=ORG, width=8)
    label(dr, (bx, byy - 40), f"resolution floor: 2 native px = 10 product px = 1.96 mrad", ORG, fs)
    dr.line([(bx, byy + 46), (bx + PX_PER_IN * s, byy + 46)], fill=WHITE, width=5)
    label(dr, (bx, byy + 56), "1 print inch = 14.29 mrad", WHITE, fs)

    # --- 5. Object X location (converted from the right-eye markup)
    x0 = (OBJX_RIGHT[0] - FRAMING_OFFSET) * s
    x1 = (OBJX_RIGHT[1] - FRAMING_OFFSET) * s
    y0, y1 = OBJX_RIGHT[2] * s, OBJX_RIGHT[3] * s
    dr.rectangle([x0, y0, x1, y1], outline=GRN, width=3)
    label(dr, (x0 - 250, y1 + 14), "Object X  (size indeterminate: ×33 range ambiguity)", GRN, fs)

    im.save(out)
    print(f"wrote {out}  ({im.size[0]}×{im.size[1]})")


def objectx_detail(out="analysis/corrected_overlay_objectx.png"):
    x0, x1, y0, y1 = 4020, 4560, 470, 700          # left-eye window centred on Object X
    # (markup box maps to left-eye x 4140-4328 after removing the 172 px framing offset)
    im = Image.open(SRC).convert("L").crop((x0, y0, x1, y1))
    a = np.asarray(im).astype(float)
    lo, hi = np.percentile(a, 2), np.percentile(a, 98)
    ov = np.clip((np.asarray(im.convert("RGB")).astype(float) - lo) / (hi - lo) * 255,
                 0, 255).astype(np.uint8)
    S = 3
    fig = Image.fromarray(ov).resize((ov.shape[1]*S, ov.shape[0]*S), Image.NEAREST)
    dr = ImageDraw.Draw(fig)
    fs = font(20)

    bx0 = (OBJX_RIGHT[0] - FRAMING_OFFSET - x0) * S
    bx1 = (OBJX_RIGHT[1] - FRAMING_OFFSET - x0) * S
    by0, by1 = (OBJX_RIGHT[2] - y0) * S, (OBJX_RIGHT[3] - y0) * S
    dr.rectangle([bx0, by0, bx1, by1], outline=GRN, width=3)
    label(dr, (bx0, by1 + 12), "Object X markup box (left-eye equivalent)", GRN, fs)

    # resolution-floor bar, true scale
    fx, fy = 30, fig.size[1] - 60
    dr.line([(fx, fy), (fx + 10 * S, fy)], fill=ORG, width=7)
    label(dr, (fx, fy - 32), "2 native px (1.96 mrad) — nothing smaller is real", ORG, fs)

    # size-vs-range ladder for the measured 33.5 mrad envelope width
    lines = ["measured envelope 33.5 × 14.1 mrad →",
             "   30 m :  1.0 × 0.4 m", "  100 m :  3.4 × 1.4 m",
             "  300 m : 10.1 × 4.2 m", "  860 m : 28.8 × 12.1 m",
             " 1006 m : 33.7 × 14.2 m"]
    for i, t in enumerate(lines):
        label(dr, (fig.size[0] - 420, 24 + i * 28), t, CYA if i else WHITE, fs)

    fig.save(out)
    print(f"wrote {out}  ({fig.size[0]}×{fig.size[1]})")


if __name__ == "__main__":
    scene_overlay()
    objectx_detail()
