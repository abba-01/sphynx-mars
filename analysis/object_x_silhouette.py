#!/usr/bin/env python3
"""Silhouette characterization of the annotated feature "Object X" in
PIA02406 (Mars Pathfinder IMP Twin Peaks super-resolution, right eye).

Measures the neutral geometry of the feature — cluster envelope, width
profile ("neck" test), constituent sub-feature decomposition, angular
size, absolute size as a function of assumed range, and the resolution
floor — WITHOUT assigning any interpretation. The measurement is
reproducible; the naming ("head", "neck", "monument") is not in the math
and is discussed only as a conferred semantic layer in the report
(analysis/OBJECT_X_SILHOUETTE_REPORT.md).

Object X location is taken from intake/INTAKE_REVIEW.md: the intake markup
family calibrates it to PIA02406 product px ~x 4312-4500, y 522-635.

Camera/product constants: 0.98 mrad/native px (Smith et al. 1997);
"enlarged by 500%" (catalog) -> 1 product px = 1/5 native px = 0.196 mrad.

Requires Pillow + numpy (no scipy). Run from repo root:
  python3 analysis/object_x_silhouette.py
"""
import numpy as np
from collections import deque
from PIL import Image, ImageDraw, ImageFilter

Image.MAX_IMAGE_PIXELS = None
IFOV = 0.98e-3            # rad / native IMP px (Smith et al. 1997)
ENLARGE = 5.0            # catalog: "enlarged by 500%"
MRAD_PPX = IFOV / ENLARGE * 1e3      # 0.196 mrad per product px
WIN = (4285, 4530, 505, 665)         # measurement window (x0,x1,y0,y1)
IMG = "intake/00/PIA02406.tif"
FIG = "analysis/object_x_silhouette.png"


def dilate(m, r):
    for _ in range(r):
        m = (m | np.roll(m, 1, 0) | np.roll(m, -1, 0)
             | np.roll(m, 1, 1) | np.roll(m, -1, 1))
    return m


def close(m, r):
    return ~dilate(~dilate(m, r), r)


def components(mask, minsz=1):
    seen = np.zeros_like(mask); out = []
    for y0 in range(mask.shape[0]):
        for x0 in range(mask.shape[1]):
            if mask[y0, x0] and not seen[y0, x0]:
                q = deque([(y0, x0)]); seen[y0, x0] = True; pts = [(y0, x0)]
                while q:
                    y, x = q.popleft()
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            ny, nx = y + dy, x + dx
                            if (0 <= ny < mask.shape[0] and 0 <= nx < mask.shape[1]
                                    and mask[ny, nx] and not seen[ny, nx]):
                                seen[ny, nx] = True; q.append((ny, nx)); pts.append((ny, nx))
                if len(pts) >= minsz:
                    out.append(pts)
    return out


def main():
    x0, x1, y0, y1 = WIN
    sub = Image.open(IMG).convert("L").crop((x0, y0, x1, y1))
    a = np.asarray(sub).astype(float); h, w = a.shape
    bg = np.asarray(sub.filter(ImageFilter.GaussianBlur(30))).astype(float)
    res = np.clip(bg - a, 0, None)            # dark features positive

    env = max(components(close(res >= np.percentile(res, 80), 3), minsz=30), key=len)
    em = np.zeros((h, w), bool)
    for y, x in env:
        em[y, x] = True
    ys = np.array([p[0] for p in env]); xs = np.array([p[1] for p in env])
    bw, bh = xs.max() - xs.min() + 1, ys.max() - ys.min() + 1
    print(f"cluster envelope {bw}x{bh} product px = {bw*MRAD_PPX:.1f} x "
          f"{bh*MRAD_PPX:.1f} mrad; aspect H/W {bh/bw:.2f}")
    print(f"annotator ruler silhouette 191x55 px = {191*MRAD_PPX:.1f} x "
          f"{55*MRAD_PPX:.1f} mrad (length 2-5/8 in, height 3/4 in)")

    widths = np.array([ (xs[ys == r].max() - xs[ys == r].min() + 1) if (ys == r).any() else 0
                        for r in range(ys.min(), ys.max() + 1)])
    print("width profile top->down (px): " + " ".join(map(str, widths.astype(int))))

    subf = sorted((len(p) for p in components(res >= np.percentile(res, 88), minsz=4)),
                  reverse=True)
    print(f"{len(subf)} constituent dark blobs; largest {subf[0]} px = "
          f"{subf[0]/25:.0f} native px; median {int(np.median(subf))} px")

    Wm, Hm = bw * MRAD_PPX, bh * MRAD_PPX
    print("\nabsolute envelope size vs assumed range (range INDETERMINATE):")
    for Z in (30, 100, 300, 860, 1006):
        print(f"  Z={Z:>4} m: {Z*Wm*1e-3:5.1f} x {Z*Hm*1e-3:5.1f} m; "
              f"resolution floor 2px = {2*Z*IFOV:.2f} m")

    lo, hi = np.percentile(a, 2), np.percentile(a, 98)
    ov = np.clip((np.asarray(sub.convert("RGB")).astype(float) - lo) / (hi - lo) * 255,
                 0, 255).astype(np.uint8)
    S = 4; fig = Image.fromarray(ov).resize((w * S, h * S), Image.NEAREST)
    dr = ImageDraw.Draw(fig)
    edge = em & ~(np.roll(em, 1, 0) & np.roll(em, -1, 0) & np.roll(em, 1, 1) & np.roll(em, -1, 1))
    for y, x in zip(*np.where(edge)):
        dr.rectangle([x*S, y*S, x*S+S-1, y*S+S-1], fill=(255, 220, 0))
    dr.rectangle([xs.min()*S, ys.min()*S, (xs.max()+1)*S, (ys.max()+1)*S],
                 outline=(255, 120, 0), width=2)
    fig.save(FIG)
    print(f"\nwrote {FIG}")


if __name__ == "__main__":
    main()
