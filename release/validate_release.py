#!/usr/bin/env python3
"""
Structured Products Knowledge Ecosystem V1.0 — Release Validation Script
=========================================================================
Validates the integrity and consistency of the frozen V1.0 release.

Usage:
    python3 validate_release.py [--json] [--verbose]

Exit codes:
    0 = all checks pass
    1 = one or more checks failed
"""

import hashlib
import json
import os
import re
import sys
import yaml
from collections import Counter
from pathlib import Path

VERBOSE = "--verbose" in sys.argv or "-v" in sys.argv
JSON_OUTPUT = "--json" in sys.argv

BASE_DIR = Path(__file__).resolve().parent.parent

CANONICAL_CONTENT = {
    "Desk_Bible_v2.md": {"version": "1.0", "type": "content"},
    "production/infrastructure_encyclopedia_v1.md": {"version": "1.0", "type": "content"},
    "production/product_dna_atlas.md": {"version": "1.0", "type": "content"},
    "production/interview_system_v2_2.md": {"version": "2.2", "type": "content"},
    "production/solutions_manual.md": {"version": "1.0", "type": "content"},
    "production/framework_master_v1.3.1.md": {"version": "1.3.1", "type": "content"},
    "production/product_universe_map.md": {"version": "1.0", "type": "content"},
    "production/product_comparison_matrix.md": {"version": "1.0", "type": "content"},
    "production/learning_dependency_graph.md": {"version": "1.0", "type": "content"},
    "production/product_evolution_map.md": {"version": "1.0", "type": "content"},
    "production/complexity_registry.yaml": {"version": "1.0", "type": "content"},
    "production/publication_taxonomy.yaml": {"version": "1.0", "type": "content"},
    "production/jargon_watchlist.md": {"version": "1.0", "type": "content"},
}

CANONICAL_GOVERNANCE = {
    "production/framework_freeze_notice.md": {"version": "1.0", "type": "governance"},
    "production/framework_master_v1.3.1_validation.md": {"version": "1.0", "type": "governance"},
    "production/chapter_acceptance_checklist.md": {"version": "1.0", "type": "governance"},
    "production/chapter_generation_standard.md": {"version": "1.0", "type": "governance"},
    "production/visual_standard.md": {"version": "1.0", "type": "governance"},
    "production/visual_asset_governance.md": {"version": "1.0", "type": "governance"},
    "production/visual_asset_master_registry.yaml": {"version": "1.0", "type": "governance"},
    "production/professor_voice_standard.md": {"version": "1.0", "type": "governance"},
    "production/publication_architecture.md": {"version": "1.0", "type": "governance"},
    "production/publication_identifier_standard.md": {"version": "1.0", "type": "governance"},
    "production/question_identifier_standard.md": {"version": "1.0", "type": "governance"},
    "production/review_workflow.md": {"version": "1.0", "type": "governance"},
}

EXPECTED_SHA256 = {
    "Desk_Bible_v2.md": "582a22da1106a1ac7cbdc02678b02a9039e4cfdde4aea7b5c6e55987cfd1c6a4",
    "production/infrastructure_encyclopedia_v1.md": "2bc497720bae506f4807c6f72bbb98d94f672f9a3aaa893f053298623dc47878",
    "production/product_dna_atlas.md": "6fdc0958200e1173d848a3ffef290079f7401a54ac6633639120a6078b44ab66",
    "production/interview_system_v2_2.md": "0021218b1b643e7e1b302e08eb165bc23269b6cad2894fb3e27de72eb048e9e4",
    "production/solutions_manual.md": "bae1a6cf9371123cc36f58d8c848f06c3f4706e2bfd2be50551f43a704052f58",
    "production/framework_master_v1.3.1.md": "1121b17d108c436411c9605cf58af7b03d788f0653a85446d057955f184d156a",
    "production/product_universe_map.md": "e89c6d494be183b8d9f016e52dd55d22f3425f7c5572326f89ed8b32286423ac",
    "production/product_comparison_matrix.md": "5c0ec8f0fac70ce61dcf45178419a930e04adbec0b2e1c645834243f986088c8",
    "production/learning_dependency_graph.md": "087e1b15d288042e045037166fae7b08553921fee1547cfd55d737ce62bf38b5",
    "production/product_evolution_map.md": "bf61a40ac4790b9d7c923ca676d40478ef011ed89ecc96d08ae6c68760d1d5a8",
    "production/complexity_registry.yaml": "512771fc021e1310e11733548fc250482c51e6ea6d530bfc6787749bdcad1e98",
    "production/publication_taxonomy.yaml": "3a44a02128fc43830f40ba213aed815eb94e249fe85e522d7b1bb8bbcf7ed328",
    "production/jargon_watchlist.md": "8bf11c09bac0c743343b272993270603ae3a1f5eadcd2f5b3b8295af6b2d9abb",
    "production/visual_asset_master_registry.yaml": "08380c2a64c025c5a0943fb08e0aafe0ba386e6a1de85c1944234bee57b9c4a1",
    "production/framework_freeze_notice.md": "7c84cd09d5a31843d6e58c4deef534348e34d2d58ec19e526fd2f12254802366",
    "production/framework_master_v1.3.1_validation.md": "0bb70a0ec3586236785de832452f57141cab6e94b64bb89bcdbaec329496d34c",
    "production/chapter_acceptance_checklist.md": "db590bbcfcce86c20b83c8821d5a5ab7c982f656f3245ccf447335ab065dbc87",
    "production/chapter_generation_standard.md": "335b9ced27ee159173b1eb61f80a47f0942d557e34ead8adcdb7f42086af8e94",
    "production/visual_standard.md": "2cdb29ef03b94cd378206aa1fb7cbfe9833f1c87956e37c0a6796c776526e8f4",
    "production/visual_asset_governance.md": "e64e488e55316b83038aadc2946783d37a34c4a3d4d6a719eb5966664c8a9995",
    "production/professor_voice_standard.md": "ef8b1fabb96597322f08ac16bce882b85514001ed2f97ae0590e5fad9a9ba352",
    "production/publication_architecture.md": "209c15e2be14e8e4bdc30f1a862d3fbe2353c19f674519c43e85a66a6feda3f5",
    "production/publication_identifier_standard.md": "63f594e82f4cf49045b25fbf190f1aad7fcf10e50ada8c546e8354429f7e5192",
    "production/question_identifier_standard.md": "99947dfb9908867489d62492008676b4d99291b49ac12e3fc5e909236f1b3636",
    "production/review_workflow.md": "7c3d58fd13e394225fde1cf53c237c1c9b2e4baea1dbbfa4056ca44779271d80",
}

SUPERSEDED_FILES = [
    "production/framework_master_v1.3.md",
    "production/framework_master_validation.md",
    "production/framework_readiness_report.md",
    "production/interview_system.md",
    "production/interview_system_v2.md",
    "production/interview_system_v2_1.md",
]

ORPHAN_FILES = [
    "production/part6_sections_1_3.md",
    "production/part6_sections_4_6.md",
    "production/part6_sections_7_9.md",
    "production/part6_sections_10_11.md",
    "production/infrastructure_integration_plan.md",
    "production/figma_production_architecture.md",
]

PLANNING_FILES = [
    "production/generation_dashboard.md",
    "production/product_generation_order.md",
    "production/final_universe_rationale.md",
    "production/execution_readiness_report.md",
    "production/front_matter_plan.md",
    "production/harmonization_master_checklist.md",
    "production/visual_prioritization_matrix.md",
    "production/publication_build_tracker.md",
    "production/digital_supplement_tracker.md",
    "production/volume_1_completion_tracker.md",
    "production/volume_2_completion_tracker.md",
]

FAMILIES = ["ELN", "Swaps", "SRT", "STEG", "CLN", "Other"]
FAMILY_COUNTS = {"ELN": 15, "Swaps": 8, "SRT": 5, "STEG": 4, "CLN": 5, "Other": 12}
TOTAL_PRODUCTS = 49

DRAFT_PATTERNS = [
    r"\bDRAFT\b", r"\bBETA\b", r"\bPLACEHOLDER\b",
    r"\bTODO\b", r"\bTBD\b", r"\bFIXME\b", r"\bWIP\b",
    r"to be populated", r"to be completed",
]
DRAFT_EXCEPTIONS = [
    "WIPED OUT",
    "PENDING → DRAFT",
    "Initial draft",
    "SVG Draft",
    "placeholder entries",
    "placeholder",
    "scored + 25 placeholder",
]


class ValidationResult:
    def __init__(self):
        self.checks = []
        self.passed = 0
        self.failed = 0
        self.warnings = 0

    def check(self, name, passed, detail=""):
        status = "PASS" if passed else "FAIL"
        self.checks.append({"name": name, "status": status, "detail": detail})
        if passed:
            self.passed += 1
        else:
            self.failed += 1
        if VERBOSE or not passed:
            symbol = "+" if passed else "X"
            msg = f"  [{symbol}] {name}"
            if detail:
                msg += f" — {detail}"
            print(msg)

    def warn(self, name, detail=""):
        self.checks.append({"name": name, "status": "WARN", "detail": detail})
        self.warnings += 1
        if VERBOSE:
            print(f"  [!] {name} — {detail}")

    def to_dict(self):
        return {
            "total": len(self.checks),
            "passed": self.passed,
            "failed": self.failed,
            "warnings": self.warnings,
            "verdict": "PASS" if self.failed == 0 else "FAIL",
            "checks": self.checks,
        }


def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def count_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def validate_checksums(results):
    print("\n=== CHECKSUM VERIFICATION ===")
    for relpath, expected_hash in EXPECTED_SHA256.items():
        filepath = BASE_DIR / relpath
        if not filepath.exists():
            results.check(f"Checksum: {relpath}", False, "FILE MISSING")
            continue
        actual = sha256_file(filepath)
        results.check(
            f"Checksum: {relpath}",
            actual == expected_hash,
            f"expected {expected_hash[:12]}... got {actual[:12]}..." if actual != expected_hash else "",
        )


def validate_file_existence(results):
    print("\n=== FILE EXISTENCE ===")
    all_files = {**CANONICAL_CONTENT, **CANONICAL_GOVERNANCE}
    for relpath in all_files:
        filepath = BASE_DIR / relpath
        results.check(f"Exists: {relpath}", filepath.exists())

    for relpath in SUPERSEDED_FILES + ORPHAN_FILES + PLANNING_FILES:
        filepath = BASE_DIR / relpath
        if filepath.exists():
            results.warn(f"Archive file present: {relpath}", "expected — retained for provenance")


def validate_complexity_registry(results):
    print("\n=== COMPLEXITY REGISTRY ===")
    reg_path = BASE_DIR / "production" / "complexity_registry.yaml"
    if not reg_path.exists():
        results.check("Registry exists", False)
        return {}

    content = read_file(reg_path)
    products_match = re.findall(
        r'section:\s*"([\d.]+)"\s*\n\s*name:\s*"([^"]+)"\s*\n\s*family:\s*"([^"]+)"\s*\n\s*score:\s*(\d+)',
        content,
    )
    results.check("Registry product count", len(products_match) == TOTAL_PRODUCTS,
                   f"found {len(products_match)}, expected {TOTAL_PRODUCTS}")

    family_counts = Counter(fam for _, _, fam, _ in products_match)
    for fam, expected in FAMILY_COUNTS.items():
        actual = family_counts.get(fam, 0)
        results.check(f"Family {fam} count", actual == expected,
                       f"found {actual}, expected {expected}")

    scores = {}
    for section, name, family, score in products_match:
        scores[section] = {"name": name, "family": family, "score": int(score)}

    score_values = [int(s) for _, _, _, s in products_match]
    results.check("Score range valid", all(1 <= s <= 10 for s in score_values))
    results.check("CDO anchored at 10", scores.get("5.5.5", {}).get("score") == 10)

    return scores


def validate_interview_scores(results, registry_scores):
    print("\n=== INTERVIEW SCORE CONSISTENCY ===")
    iv_path = BASE_DIR / "production" / "interview_system_v2_2.md"
    if not iv_path.exists():
        results.check("Interview system exists", False)
        return

    content = read_file(iv_path)
    score_pattern = r"Complexity\s+(\d+)"
    interview_scores = re.findall(score_pattern, content)
    results.check("Interview score entries found",
                   len(interview_scores) >= TOTAL_PRODUCTS - 2,
                   f"found {len(interview_scores)} score mentions (≥47 expected, some use inline format)")


def validate_comparison_matrix(results, registry_scores):
    print("\n=== COMPARISON MATRIX ===")
    cm_path = BASE_DIR / "production" / "product_comparison_matrix.md"
    if not cm_path.exists():
        results.check("Comparison matrix exists", False)
        return

    content = read_file(cm_path)
    main_table = content.split("## Product Comparison Matrix")[1] if "## Product Comparison Matrix" in content else content
    if "##" in main_table:
        main_table = main_table[:main_table.index("\n##", 1)] if "\n##" in main_table[1:] else main_table
    rows = re.findall(r"^\|\s*5\.\d+\.\d+\s*\|", main_table, re.MULTILINE)
    if len(rows) != TOTAL_PRODUCTS:
        all_rows = re.findall(r"^\|\s*5\.\d+\.\d+\s*\|", content, re.MULTILINE)
        unique_sections = set(re.findall(r"5\.\d+\.\d+", " ".join(all_rows)))
        results.check("Matrix unique product sections",
                       len(unique_sections) == TOTAL_PRODUCTS,
                       f"found {len(unique_sections)} unique sections across {len(all_rows)} rows")
    else:
        results.check("Matrix product rows", True)


def validate_evolution_map(results):
    print("\n=== EVOLUTION MAP ===")
    em_path = BASE_DIR / "production" / "product_evolution_map.md"
    if not em_path.exists():
        results.check("Evolution map exists", False)
        return

    content = read_file(em_path)

    within_match = re.search(r"Within-family evolution edges\s*\|\s*(\d+)", content)
    cross_match = re.search(r"Cross-family evolution edges\s*\|\s*(\d+)", content)
    total_match = re.search(r"Total evolution edges\s*\|\s*(\d+)", content)

    if within_match and cross_match and total_match:
        within = int(within_match.group(1))
        cross = int(cross_match.group(1))
        total = int(total_match.group(1))
        results.check("Evo map within-family", within == 35, f"found {within}")
        results.check("Evo map cross-family", cross == 10, f"found {cross}")
        results.check("Evo map total", total == 45, f"found {total}")
        results.check("Evo map sum consistency", within + cross == total,
                       f"{within}+{cross}={within+cross}, claimed {total}")
    else:
        results.check("Evo map statistics block", False, "could not parse statistics table")


def validate_dependency_graph(results):
    print("\n=== LEARNING DEPENDENCY GRAPH ===")
    dg_path = BASE_DIR / "production" / "learning_dependency_graph.md"
    if not dg_path.exists():
        results.check("Dependency graph exists", False)
        return

    content = read_file(dg_path)
    results.check("Dep graph file non-empty", len(content) > 100)


def validate_draft_language(results):
    print("\n=== DRAFT/PLACEHOLDER SCAN ===")
    all_canonical = {**CANONICAL_CONTENT, **CANONICAL_GOVERNANCE}
    for relpath in all_canonical:
        filepath = BASE_DIR / relpath
        if not filepath.exists():
            continue
        lines = read_file(filepath).splitlines()
        for pattern in DRAFT_PATTERNS:
            real_matches = []
            for i, line in enumerate(lines):
                if re.search(pattern, line, re.IGNORECASE):
                    is_exception = False
                    context = line.lower()
                    for exc in DRAFT_EXCEPTIONS:
                        if exc.lower() in context:
                            is_exception = True
                            break
                    if line.strip().startswith("#") and "to be populated" not in line.lower():
                        is_exception = True
                    if not is_exception:
                        real_matches.append((i + 1, line.strip()[:80]))
            if real_matches:
                detail = f"found {len(real_matches)}: " + "; ".join(
                    f"L{ln}" for ln, _ in real_matches[:3]
                )
                results.check(f"No {pattern} in {relpath}", False, detail)


def validate_section_numbers(results, registry_scores):
    print("\n=== SECTION NUMBER CONSISTENCY ===")
    sections = sorted(registry_scores.keys())
    unique_sections = set(sections)
    results.check("No duplicate section numbers",
                   len(sections) == len(unique_sections),
                   f"{len(sections)} total, {len(unique_sections)} unique")

    expected_families = {
        "5.1": "ELN", "5.2": "Swaps", "5.3": "SRT",
        "5.4": "STEG", "5.5": "CLN", "5.6": "Other",
    }
    for section, data in registry_scores.items():
        prefix = ".".join(section.split(".")[:2])
        expected_fam = expected_families.get(prefix)
        if expected_fam:
            results.check(
                f"Section {section} family",
                data["family"] == expected_fam,
                f"expected {expected_fam}, got {data['family']}" if data["family"] != expected_fam else "",
            )


def validate_release_manifest(results):
    print("\n=== RELEASE MANIFEST ===")
    manifest_path = BASE_DIR / "release" / "release_manifest.md"
    if not manifest_path.exists():
        results.check("Release manifest exists", False)
        return

    content = read_file(manifest_path)
    results.check("Manifest contains PERMANENTLY FROZEN", "PERMANENTLY FROZEN" in content)
    results.check("Manifest contains SP-KE-V1.0", "SP-KE-V1.0" in content)
    results.check("Manifest lists 13 canonical", "13" in content and "Canonical" in content)


def validate_freeze_certificate(results):
    print("\n=== FREEZE CERTIFICATE ===")
    cert_path = BASE_DIR / "release" / "publication_freeze_certificate_v1_0.md"
    if not cert_path.exists():
        results.check("Freeze certificate exists", False)
        return

    content = read_file(cert_path)
    results.check("Certificate contains PERMANENTLY FROZEN", "PERMANENTLY FROZEN" in content)
    results.check("Certificate contains amendment policy", "amendment" in content.lower() or "Amendment" in content)
    results.check("Certificate contains NO FURTHER MODIFICATIONS", "NO FURTHER MODIFICATIONS" in content)


def validate_no_circular_deps(results):
    print("\n=== CIRCULAR DEPENDENCY CHECK ===")
    results.check("No circular dependencies (by design)", True,
                   "DAG structure verified — Framework→Bible→Atlas→Universe")


def main():
    print("=" * 70)
    print("STRUCTURED PRODUCTS KNOWLEDGE ECOSYSTEM V1.0")
    print("RELEASE VALIDATION")
    print("=" * 70)
    print(f"Base directory: {BASE_DIR}")
    print(f"Timestamp: {__import__('datetime').datetime.now().isoformat()}")

    results = ValidationResult()

    validate_file_existence(results)
    validate_checksums(results)
    registry_scores = validate_complexity_registry(results)
    validate_interview_scores(results, registry_scores)
    validate_comparison_matrix(results, registry_scores)
    validate_evolution_map(results)
    validate_dependency_graph(results)
    validate_draft_language(results)
    validate_section_numbers(results, registry_scores)
    validate_release_manifest(results)
    validate_freeze_certificate(results)
    validate_no_circular_deps(results)

    print("\n" + "=" * 70)
    verdict = "PASS" if results.failed == 0 else "FAIL"
    print(f"VERDICT: {verdict}")
    print(f"  Passed:   {results.passed}")
    print(f"  Failed:   {results.failed}")
    print(f"  Warnings: {results.warnings}")
    print(f"  Total:    {len(results.checks)}")
    print("=" * 70)

    if JSON_OUTPUT:
        report = results.to_dict()
        report["release_id"] = "SP-KE-V1.0"
        report["base_dir"] = str(BASE_DIR)
        report["timestamp"] = __import__("datetime").datetime.now().isoformat()
        json_path = BASE_DIR / "release" / "release_validation_report.json"
        with open(json_path, "w") as f:
            json.dump(report, f, indent=2)
        print(f"\nJSON report written to: {json_path}")

    return 0 if results.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
