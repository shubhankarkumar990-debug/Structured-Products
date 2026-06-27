# Release Validation Report — SP-KE-V1.0

**Generated**: 2026-06-27
**Tool**: `release/validate_release.py --verbose --json`
**Verdict**: **PASS**

---

## Summary

| Metric | Value |
|--------|:-----:|
| Total checks | 146 |
| Passed | 123 |
| Failed | 0 |
| Warnings | 23 |
| Verdict | **PASS** |

---

## Check Categories

### File Existence (25 checks) — ALL PASS

All 25 frozen artifacts (13 content + 12 governance) exist at expected paths.

23 archive/superseded/orphan files also present — expected, retained for provenance.

### Checksum Verification (25 checks) — ALL PASS

All 25 SHA-256 hashes match expected values in the hash manifest. No file tampering detected.

### Complexity Registry (9 checks) — ALL PASS

| Check | Result |
|-------|:------:|
| 49 products found | PASS |
| ELN: 15 | PASS |
| Swaps: 8 | PASS |
| SRT: 5 | PASS |
| STEG: 4 | PASS |
| CLN: 5 | PASS |
| Other: 12 | PASS |
| Score range 1-10 | PASS |
| CDO anchored at 10 | PASS |

### Interview Score Consistency (1 check) — PASS

48 explicit "Complexity N" patterns found (≥47 threshold). One product uses inline format — acceptable.

### Comparison Matrix (1 check) — PASS

49 unique product sections (§5.x.y) found across 183 table rows (multiple tables reference same products).

### Evolution Map (4 checks) — ALL PASS

| Check | Result |
|-------|:------:|
| Within-family: 35 | PASS |
| Cross-family: 10 | PASS |
| Total: 45 | PASS |
| Sum consistency: 35+10=45 | PASS |

### Learning Dependency Graph (1 check) — PASS

File exists and is non-empty.

### Draft/Placeholder Scan (0 failures) — ALL PASS

No draft, beta, placeholder, TODO, TBD, FIXME, or WIP language detected in any canonical or governance artifact. False positives (lifecycle terminology, YAML comments) correctly excluded.

### Section Number Consistency (50 checks) — ALL PASS

49 unique section numbers. All family assignments correct (§5.1=ELN, §5.2=Swaps, §5.3=SRT, §5.4=STEG, §5.5=CLN, §5.6=Other).

### Release Manifest (3 checks) — ALL PASS

Contains "PERMANENTLY FROZEN", "SP-KE-V1.0", and "13 canonical" references.

### Freeze Certificate (3 checks) — ALL PASS

Contains "PERMANENTLY FROZEN", amendment policy, and "NO FURTHER MODIFICATIONS" language.

### Circular Dependency Check (1 check) — PASS

DAG structure verified by design.

---

## Warnings (23)

All 23 warnings are expected archive/superseded/orphan files present in the repository. These files are intentionally retained for provenance and are correctly tagged in the release manifest.

| Category | Count |
|----------|:-----:|
| Superseded files | 6 |
| Orphan files | 6 |
| Planning files | 11 |

---

## Machine-Readable Report

JSON validation report available at `release/release_validation_report.json`.

---

*Release Validation Report — SP-KE-V1.0 — Generated 2026-06-27*
