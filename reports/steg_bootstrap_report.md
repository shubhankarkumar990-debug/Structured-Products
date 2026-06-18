# STEG Bootstrap Report

**Date:** 2026-06-19  
**Bootstrap product:** VSTEG001 — Vanilla Steepener Note  
**Pipeline:** v2.1 (stable)

---

## Result

**VSTEG001 COMPLETE. STEG family bootstrapped. All memory artifacts validated.**

| Gate | Result | Issues |
|------|--------|--------|
| QA | PASS | 1 MAJOR advisory (CMS decomposition format) |
| Style | PASS | Zero violations |
| CrossRef | PASS | 3 cross-family refs, 2 forward refs |
| Publishing | READY | Zero blocking issues |

## Memory artifact validation

| Artifact | Used | Reuses | Issues |
|----------|------|--------|--------|
| memory/terminology/STEG.yaml | Yes | CMS spread notation, convexity adjustment, leverage, floor, cap | None |
| memory/booking-maps/STEG_system_mapping.yaml | Yes | Murex four-leg, CMS-specific booking items | None |
| memory/style-patterns/STEG.yaml | Yes | 3 known FPs suppressed, 4 conventions applied | None |

All 3 STEG memory artifacts worked correctly on first use. No updates required.

## New family-level conventions discovered

### 1. CMS spread decomposition format

**Convention:** Unlike fixed-rate or equity products where decomposition components sum directly to the headline coupon, CMS spread products decompose into cost components that sum to a total cost (5.0%), while the expected coupon (4.0%) is determined by the underlying spread level. The difference (1.0%) represents the net cost of leverage, embedded options, and convexity adjustment.

**Action:** Defer adding to STEG style-patterns until validated against RASTEG001. If the pattern holds across two products, add as an accepted convention.

**Rationale:** Adding a convention based on a single product is premature. The CMS decomposition format may vary for range-accrual steepeners or TARNs.

## Cross-family reference analysis

VSTEG001 established 3 cross-family references to SRT products:

| From | To | Type | Rationale |
|------|----|------|-----------|
| VSTEG001 | NCRA001 | Concept parallel | Both are rate-contingent coupon products |
| VSTEG001 | CRASRT001 | Concept parallel | Callable vs non-callable comparison |
| VSTEG001 | IRCFRN001 | System parallel | Both use Murex four-leg framework |

These references validate the bible's cross-family consistency. STEG products share the Murex four-leg system with SRT, and CMS-linked coupons share structural parallels with range accrual products.

## STEG family readiness for remaining products

| Product | Key difference from VSTEG001 | Memory ready |
|---------|------------------------------|:------------:|
| RASTEG001 | Adds range accrual to CMS spread | Yes |
| CSTEG001 | Adds Bermudan call | Yes |
| TARN001 | Adds target redemption (path-dependent) | Partial — may need target-level convention |

**Assessment:** STEG memory artifacts are production-ready for RASTEG001 and CSTEG001. TARN001 may require 1 new accepted convention for target-level/auto-redemption terminology.

## Bootstrap quality comparison

| Metric | ELN bootstrap (PHX001) | SRT bootstrap (IRCFRN001) | CLN bootstrap (VCLN001) | STEG bootstrap (VSTEG001) |
|--------|:----------------------:|:-------------------------:|:-----------------------:|:-------------------------:|
| Memory artifacts created | 3 | 3 | 3 | 3 |
| Pipeline retries | 0 | 0 | 0 | 0 |
| QA BLOCKERs | 0 | 0 | 0 | 0 |
| New conventions found | 12 | 3 | 2 | 1 |
| Cross-family refs | 0 | 0 | 1 | 3 |

VSTEG001 is the cleanest bootstrap yet — 1 new convention (deferred), zero blocking issues, and the highest cross-family reference count (benefiting from 20 existing products to reference).

## Verdict

**STEG bootstrap: COMPLETE. Memory validated. Ready for Batch 4 (RASTEG001, CSTEG001, TARN001).**
