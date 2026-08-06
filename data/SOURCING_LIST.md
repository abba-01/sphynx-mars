# Master Sourcing List — Documents to Acquire Directly

Consolidated acquisition checklist for everything the program needs fetched from
institutional sources (roadmap P1.1–P1.5 plus items surfaced by
`intake/INTAKE_REVIEW.md` and `data/P1_4_RETRIEVAL.md`). The analysis sandbox's
egress proxy returns HTTP 403 for all of these hosts — **every item below must be
fetched from a machine with normal network access.** For each acquisition: record
URL, access date, file size, and SHA-256 into `data/PROVENANCE.md`; nothing absent
from that file may be cited by later phases (Phase 1 exit criterion).

## Tier A — Primary data (blocking; closes P1.1–P1.3)

| # | Item | Source | Verify on receipt | Closes |
|---|---|---|---|---|
| A1 | `PIA02405.tif` (left eye, full-res) | https://photojournal.jpl.nasa.gov/catalog/PIA02405 | 7238×3135 px; catalog states 65.93 MB; SHA-256 vs repo copy `d32ee9af…c69d6` — match confirms the intake copy's integrity, mismatch is a finding | P1.1 |
| A2 | `PIA02406.tif` (right eye, full-res) | https://photojournal.jpl.nasa.gov/catalog/PIA02406 | 7296×3135 px; SHA-256 vs repo copy `49de984…84199` | P1.1 |
| A3 | `PIA02406_modest.jpg` (NASA web derivative) | same catalog page | md5 vs repo copy `f7c883c3fe0b90239103f7f948751192` — independent lineage check that the repo's PIA02406 chain traces to NASA servers | P1.1 |
| A4 | Live catalog pages PIA02405 + PIA02406 (HTML or print-to-PDF) | photojournal.jpl.nasa.gov | Verbatim match against the two saved catalog-page PDFs in `intake/00/` and repo root (processing description, product sizes, distances/heights caption) | P1.1, P1.5 |
| A5 | IMP EDR dataset `MPFL-M-IMP-2-EDR-V1.0` — at minimum the left/right frames composing the Twin Peaks super-resolution sequence | https://pds-imaging.jpl.nasa.gov (PDS Imaging Node) | PDS labels intact; 256×256 px native frames; frame IDs logged | P1.2 (unblocks P2.4) |
| A6 | *The Imager for Mars Pathfinder User's Guide* (from the dataset's `document/` directory) | PDS Imaging Node, same dataset | — | P1.2 |
| A7 | HiRISE `PSP_001890_1995` map-projected product (JP2 + label) | https://www.uahirise.org/PSP_001890_1995 | 25 cm/px map-projected (28.5 cm/px native); lander visible per caption | P1.3 |
| A8 | HiRISE `PSP_002391_1995` stereo observation | https://www.uahirise.org/PSP_002391_1995 | Stereo companion of A7 | P1.3 |
| A9 | HiRISE DTM for the PSP_001890_1995 / PSP_002391_1995 pair **if archived** | HiRISE DTM archive, https://www.uahirise.org/dtm/ | If none exists, record the negative result + search route in the P1.3 provenance row — that record arms the pre-registered no-DTM stereo fallback branch (Phase 1 plan §S6) | P1.3 |

## Tier B — Governing papers (closes P1.4)

| # | Item | DOI / locator | Role |
|---|---|---|---|
| B1 | Smith, P. H., et al. (1997), "The imager for Mars Pathfinder experiment," *JGR* 102(E2), 4003–4025 | doi:10.1029/96JE03568 | Camera constants authority (15.0 cm baseline, 14.4°×14.0°, 0.98 mrad/px, f/18) |
| B2 | Kirk, R. L., et al. (1999), "Digital photogrammetric analysis of the IMP camera images…," *JGR* 104(E4) | doi:10.1029/1998JE900012 | Site DTM/control-network prior art; external control for Phase 5 |
| B3 | Parker sight-line localization, *Science* 278, 1746 (1997) | via https://www.science.org (same issue as B4) | How NASA actually got the distances (VALIDATION_REPORT §5.1) |
| B4 | Golombek, M. P., et al. (1997), "Overview of the Mars Pathfinder Mission and Assessment of Landing Site Predictions," *Science* 278(5344), 1743–1748 | doi:10.1126/science.278.5344.1743 (records: ADS 1997Sci...278.1743G; USGS pubs 70246335) | Mission overview; candidate source of horizon-landmark text |
| B5 | Oberst, J., et al. (1999), "Photogrammetric analysis of horizon panoramas: The Pathfinder landing site in Viking orbiter images," *JGR Planets* | doi:10.1029/98JE01429; ISPRS companions: https://www.isprs.org/proceedings/XXXII/part4/oberst139.pdf and …/oberst31neu.pdf | **P4.1 prior art.** Verify the provisional azimuth table in `data/P1_4_RETRIEVAL.md` §3 (South Twin 242°, North Twin 259–262°, knobs/crater) against the actual text; record volume/pages |
| B6 | *(secondary)* Golombek, M. P., et al. (1999), "Overview of the Mars Pathfinder Mission: Launch through landing…," *JGR* 104 | doi:10.1029/98JE02554 | Alternate candidate source for the azimuth values; fetch if B5 does not contain them |

## Tier C — NASA caption & instrument pages (verbatim-quote verification; closes P1.5 and the knob verification)

| # | Page | Quote to verify |
|---|---|---|
| C1 | PIA01447 (Pathfinder first-anniversary refined landing site) — https://www.jpl.nasa.gov/images/pia01447-mars-pathfinder-first-anniversary-special-refined-landing-site-location/ | "Sight lines to various landmarks … matched to features seen in Viking Orbiter images by T. Parker … to within a few hundred meters" (VALIDATION_REPORT §5.1) |
| C2 | PIA01124 "Mars Pathfinder Landing Site" — https://www.jpl.nasa.gov/images/pia01124-mars-pathfinder-landing-site/ and https://photojournal.jpl.nasa.gov/catalog/PIA01124 | "Only the tip of North Knob, which appears larger in the Viking orbiter images than the Twin Peaks, projects above the local horizon"; five-features list; Little/Rimshot Crater sentence |
| C3 | PIA09105 "Mars Pathfinder Landing Site and Surroundings" — https://photojournal.jpl.nasa.gov/catalog/PIA09105 | Same knob lineage at HiRISE era; cross-check against C2 |
| C4 | PIA01008 "Big Crater as Viewed by Pathfinder Lander" — https://www.jpl.nasa.gov/images/pia01008-big-crater-as-viewed-by-pathfinder-lander/ | "Far Knob is a large streamlined mountain over 450 meters (1480 feet) tall, located over 30 kilometers (19 miles) from the Pathfinder spacecraft"; "discovered on the first panoramas taken … July 4, 1997"; locate the "Southeast Knob … triangular peak" sentence (not yet found in a rendering) |
| C5 | Mars Pathfinder Instrument Descriptions — https://mars.nasa.gov/MPF/mpf/sci_desc.html | "The imager rests on a pop-up mast 80 cm above the lander and 1.5 m above the surface" (VALIDATION_REPORT §3) |
| C6 | PIA03225 "Highest-Resolution View of 'Face on Mars'" — https://science.nasa.gov/resource/highest-resolution-view-of-face-on-mars/ | "shown in the higher-resolution image to be a natural feature similar to a butte or mesa on Earth" (VALIDATION_REPORT §7) |
| C7 | HiRISE caption pages PSP_001890_1995 / PSP_002391_1995 — uahirise.org | "the image scale is 28.5 cm/pixel … map-projected to 25 cm/pixel"; "The white feature at center is the Pathfinder lander" (VALIDATION_REPORT §7) |

## Tier D — Secondary/context sources (cited in VALIDATION_REPORT §8; verify while at it)

| # | Item | Locator | Cited for |
|---|---|---|---|
| D1 | *Encyclopædia Britannica*, "Great Sphinx of Giza" — https://www.britannica.com/topic/Great-Sphinx | — | 240 ft (73 m) long, 66 ft (20 m) high |
| D2 | *Britannica*, "Mars Global Surveyor" | britannica.com | Cydonia mesa ~3 km × 250 m |
| D3 | Musselwhite/… (1991), "Early outgassing of Mars supported by differential water solubility of iodine and xenon," *Nature* 352, 697–699 | https://www.nature.com/articles/352697a0 | Mainstream ¹²⁹Xe account (contra the "nuclear event" material) |
| D4 | "Xenon isotope constraints on ancient Martian atmospheric escape," *EPSL* (2021) | via journal search | Same |
| D5 | "Impact sculpting of the early martian atmosphere," *Science Advances* (2024) | via journal search | Same |

## Acquisition protocol (applies to every tier)

1. Fetch from the listed institutional host only; no mirrors or aggregator re-uploads.
2. Record in `data/PROVENANCE.md`: URL, access date (UTC), bytes, SHA-256, and the
   verification outcome from the "verify on receipt" column.
3. Where a repo copy already exists (A1–A4), a hash **match** upgrades the existing
   analyses' provenance in place; a **mismatch** is a finding to investigate, not to
   silently overwrite.
4. Quote verifications (Tier C) are pass/fail per quote; any drift is corrected in
   the citing document with a dated note (P1.5).
5. Paywalled papers (Tier B): institutional access or author-archived copies
   (NASA/USGS technical-report servers often host G97/O99 lineage); record which
   route was used.
