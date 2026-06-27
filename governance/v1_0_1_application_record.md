# V1.0.1 ERRATA APPLICATION RECORD

**Date:** 2026-06-27
**Action:** Errata corrections applied directly into source artifacts (not as a companion addendum). The frozen V1.0 copies under `release/desk-bible-v1/` are untouched and remain the historical record.

---

## 1. Original 9 errata applied (15 line corrections)

| Erratum | File | Status |
|:-------:|------|:------:|
| E-01a | Desk_Bible_v2.md §1 ELI5 | ✅ short→long credit correlation |
| E-01b | Desk_Bible_v2.md §11 key insight | ✅ short→long, structural note added |
| E-01c | Desk_Bible_v2.md NTD coupon table (FTD row) | ✅ short→long (MTM) |
| E-02 | Desk_Bible_v2.md worst-of parallel | ✅ short→long (MTM) |
| E-03 | production/part6_sections_10_11.md:102 | ✅ ownership + raw/hedged fixed |
| E-04a | production/part6_sections_10_11.md:110 | ✅ net/hedged qualifier added |
| E-04b | production/infrastructure_encyclopedia_v1.md:4290 | ✅ raw/unhedged qualifier added |
| E-05 | Desk_Bible_v2.md WOAC 65% | ✅ above→below strike, physical delivery math |
| E-06 | Desk_Bible_v2.md dispersion diagram | ✅ long→short correlation |
| E-07 | Desk_Bible_v2.md gamma sign | ✅ 3×(−2) intermediate sign fixed |
| E-08 | production/interview_system_v2_2.md:356 | ✅ SHORT→long (line 358 desk Greek kept) |
| E-09 | Desk_Bible_v2.md NTD table (2TD–5TD) | ✅ all relabeled short (MTM) |

## 2. Additional defects found by the semantic linter (NOT in the original audit)

The linter, run over the full corpus after the 9 errata, surfaced four more
instances of the same error classes. All were corrected:

| ID | File / Line | Defect | Fix |
|:--:|-------------|--------|-----|
| E-10 | Desk_Bible_v2.md §4.8 cross-family table | "Short correlation (profit from high correlation)" listing FTD/worst-of — self-contradiction | → "Long correlation (MTM)" |
| E-11 | Desk_Bible_v2.md §Phoenix key takeaways | "short correlation products — lower correlation increases risk" — self-contradiction | → "investor long correlation (MTM)" |
| E-12 | production/interview_system_v2_2.md:976 | WOAC "→ short correlation" (contradicts the E-08 fix in the same file) | → "investor long correlation (MTM)" |
| E-13 | Desk_Bible_v2.md NTD common-mistakes | "high-N NTDs (4TD,5TD) are reliably long correlation" — contradicts E-09 | → all NTD N≥2 short under MTM |

Two further single-line precision improvements (a stale review question now
referencing the structural/MTM distinction; one desk raw-position statement
given an explicit "raw" qualifier) were also applied.

Merged-content note: `Desk_Bible_v2.md` contains a copy of the Part 6 §10–11
material, so the E-03 and E-04a corrections were applied in BOTH the production
file and the Bible's merged copy.

## 3. Verification

- **Regression suite:** 21/21 pass (`governance/linter/regression_tests.py`)
- **Semantic linter:** 0 findings across the 9 canonical artifacts (S1:0 S2:0 S3:0 S4:0)
- **Self-test:** all 8 original defect classes are still detected by the linter (it passes by correctness, not blindness).

## 4. Canonical convention (enforced)

Under the MTM sensitivity convention adopted in V1.0.1:
- **FTD investor / worst-of investor:** long correlation (structurally short — sold the premium).
- **NTD (N≥2) investor:** short correlation (risk rises with ρ).
- **Desk raw (unhedged) position from selling these:** short correlation.
- **Desk net (hedged, post-dispersion) position:** long correlation.

*V1.0.1 Application Record | 2026-06-27*
