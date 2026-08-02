# P1.4 Retrieval Log — Governing Papers and the Golombek/Knob Verification

**Task.** Roadmap P1.4 retrieval, executed 2026-08-02, triggered by
`intake/INTAKE_REVIEW.md`'s flag: the intake correlation framework quoted
NASA-attributed "North Knob / Southeast Knob / Far Knob" text with no in-repo source,
with Golombek et al. 1997 the suspected origin. This log records what was verified,
how, and what remains open.

**Retrieval constraint (method disclosure).** Every direct page/PDF fetch attempted
from this sandbox returned HTTP 403 at the egress proxy — including
`ui.adsabs.harvard.edu`, `pubs.usgs.gov`, `science.org`,
`agupubs.onlinelibrary.wiley.com`, `isprs.org`, and `photojournal.jpl.nasa.gov`.
All content below therefore comes from **search-engine renderings of institutional
pages** (the same flagged-and-disclosed method as `VALIDATION_REPORT.md` §8's
secondary sources). Nothing here is a substitute for the full texts; the
outside-sandbox checklist at the end is the actual completion path for P1.4.

---

## 1. Citations verified as real

| Ref | Citation | Status |
|---|---|---|
| G97 | Golombek, M. P., Cook, R. A., Economou, T., Folkner, W. M., Haldemann, A. F. C., Kallemeyn, P. H., Knudsen, J. M., Manning, R. M., Moore, H. J., Parker, T. J., Rieder, R., Schofield, J. T., Smith, P. H., & Vaughan, R. M. (1997), "Overview of the Mars Pathfinder Mission and Assessment of Landing Site Predictions," *Science* 278(5344), 1743–1748, doi:10.1126/science.278.5344.1743 | **Verified real** (ADS record 1997Sci...278.1743G, Science.org DOI page, USGS pubs 70246335, U. Arizona experts page). Author list includes T. J. Parker — consistent with the sight-line work cited in `VALIDATION_REPORT.md` §5.1. |
| O99 | Oberst, J., Jaumann, R., Zeitler, W., Hauber, E., Kuschel, M., Parker, T., Golombek, M., Malin, M., & Soderblom, L. (1999), "Photogrammetric analysis of horizon panoramas: The Pathfinder landing site in Viking orbiter images," *J. Geophys. Res. Planets*, doi:10.1029/98JE01429 | **Verified real** (Wiley DOI page, USGS pubs listing, ISPRS proceedings companion `oberst139.pdf`). **New to the program** — found during this retrieval. |

Abstract of O99 as rendered by search (to be re-verified against the full text):

> "Tiepoint measurements, block adjustment techniques, and sunrise/sunset pictures
> were used to obtain precise pointing data with respect to north for a set of 33 IMP
> horizon images. Azimuth angles for five prominent topographic features seen at the
> horizon were measured and correlated with locations of these features in Viking
> orbiter images. Based on this analysis, the Pathfinder line/sample coordinates in
> two raw Viking images were determined with approximate errors of 1 pixel, or 40 m.
> The precise determination of coordinates in images together with the known
> planet-fixed coordinates of the lander make the Pathfinder landing site the most
> important anchor point in current control point networks of Mars."

**Why O99 matters:** it is the professional execution of exactly the procedure
`plans/PHASE_4_PLAN.md` step P4.1 pre-registers — solving horizon-feature azimuths
from lander images and registering them against orbital imagery. It supplies (a)
methodological prior art the plan should cite and follow, (b) published azimuth
values usable as *known-answer controls* for our registration, and (c) an
independence caveat: our P4.1 solution should be computed blind to O99's values,
then compared.

## 2. The "knob" quotes: genuine NASA caption text, misused downstream

The intake framework's knob sentences trace to NASA Photojournal/JPL caption
lineage (PIA01124 "Mars Pathfinder Landing Site" / PIA09105 "Mars Pathfinder Landing
Site and Surroundings" / PIA01008 "Big Crater as Viewed by Pathfinder Lander"), as
rendered by search:

> "Only the tip of North Knob, which appears larger in the Viking orbiter images
> than the Twin Peaks, projects above the local horizon…"

> "Far Knob is a large streamlined mountain over 450 meters (1480 feet) tall,
> located over 30 kilometers (19 miles) from the Pathfinder spacecraft. The larger
> features visible in this scene — Big Crater, Far Knob, and Southeast Knob — were
> discovered on the first panoramas taken by the IMP camera on July 4, 1997, and
> subsequently identified in Viking Orbiter images taken over 20 years ago."

> "Five prominent features on the horizon … North Knob, Southeast Knob, Far Knob,
> Twin Peaks, and Big Crater. Two small craters visible in the orbiter and lander
> views — Little Crater and Rimshot Crater — lie on the northwest outer flank of the
> rim of Big Crater."

**Verdict:** the intake file's knob text was *genuine NASA material* — not
fabricated — but was misused there (folding Far Knob, a >450 m mountain 30 km away,
into a "985 m pyramid hierarchy"). The quotes themselves are salvageable as
registration-landmark documentation; the use made of them stays invalidated
(`intake/INTAKE_REVIEW.md`, correlation-framework entry).

## 3. Horizon-feature azimuths (provisional — snippet-sourced, unverified)

A search rendering attributed the following to the Oberst horizon-panorama work
(likely the ISPRS proceedings paper, `oberst139.pdf`, which could not be fetched):

| Feature | Azimuth (deg, from north) |
|---|---|
| North Knob | 1–8 |
| Southeast Knob (summit) | 135 |
| Big Crater (rim crest) | 140–168 |
| Far Knob | 176–180 |
| **Twin Peaks, South summit** | **242** |
| **Twin Peaks, North summit** | **259–262** |

**Status: PROVISIONAL.** These numbers could not be verified against the source
document from this sandbox and must not be used as inputs. Their intended role once
verified at full text: *known-answer controls* for the P4.1 azimuth registration
(the P4.1 solution is computed first, blind, then compared — mirroring the plan's
existing known-answer gate). Until verified, they are recorded here and nowhere else.

## 4. Program deltas from this retrieval

1. `ROADMAP.md` P1.4 now lists G97 and O99 alongside Smith 1997, Kirk 1999, and
   Parker (*Science* 278, 1746).
2. The P4.1 executor should read O99 before running registration (prior art +
   controls), and record a blind-then-compare step against §3's values once they are
   verified at full text.
3. Open questions for the full texts: whether the intake "Southeast Knob … triangular
   peak to the left of the flanks of the Big Crater rim" sentence appears verbatim in
   a NASA caption (not yet located in a rendering); the exact JGR volume/pages of O99.

## 5. Outside-sandbox completion checklist (what P1.4 still needs)

With normal network access, fetch and archive (checksums into `data/PROVENANCE.md`):

- [ ] G97 full text: https://www.science.org/doi/10.1126/science.278.5344.1743
      (records: https://ui.adsabs.harvard.edu/abs/1997Sci...278.1743G ,
      https://pubs.usgs.gov/publication/70246335 )
- [ ] O99 full text: https://agupubs.onlinelibrary.wiley.com/doi/10.1029/98JE01429 ;
      ISPRS companions: https://www.isprs.org/proceedings/XXXII/part4/oberst139.pdf ,
      https://www.isprs.org/proceedings/XXXII/part4/oberst31neu.pdf — verify §3's
      azimuth table against the actual text and record volume/pages
- [ ] Smith et al. 1997 (doi:10.1029/96JE03568) and Kirk et al. 1999
      (doi:10.1029/1998JE900012) full texts — the P1.4 originals, still unretrieved
- [ ] Parker sight-line localization, *Science* 278, 1746 (1997)
- [ ] NASA caption pages for the knob quotes: PIA01124, PIA09105, PIA01008 — verify
      §2's quotes verbatim against the live pages
- [ ] Cross-check `VALIDATION_REPORT.md` §8 quotes per P1.5 while at it

**P1.4 checkbox status: OPEN** (citations verified and content salvaged; full texts
not yet in hand — this log is progress, not completion).
