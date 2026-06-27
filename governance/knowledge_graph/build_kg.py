#!/usr/bin/env python3
"""
Knowledge-graph populator for the Structured Products Knowledge Ecosystem.

Populates the ontology in governance/knowledge_graph_ontology.md with real data:
  - 49 products (family, complexity, system, correlation direction, section)
  - governed correlation terms + conventions
  - the 22 linter rules (parsed from semantic_linter.py)
  - the 21 regression tests (parsed from regression_tests.py)
  - the V1.0.1 errata (E-01 .. E-13)
  - artifacts (Desk Bible + 8 companions) and key sections
  - typed, directional edges between them

Run from the repo root:
    python3 governance/knowledge_graph/build_kg.py

Outputs (in governance/knowledge_graph/):
  - knowledge_graph.json   nodes + edges (canonical machine format)
  - knowledge_graph.graphml  for Gephi / yEd / Neo4j import
  - kg_stats.md            human-readable summary
"""
from __future__ import annotations
import json, os, re, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BIBLE = ROOT / "Desk_Bible_v2.md"

# --------------------------------------------------------------------------- #
# 1. Products (49) — id, name, family, section, correlation_direction
# --------------------------------------------------------------------------- #
FAMILY = {"5.1": "ELN", "5.2": "Swap", "5.3": "SRT", "5.4": "STEG", "5.5": "CLN", "5.6": "Other"}
# (section, name, correlation_direction)  — direction per the V1.0.1 MTM convention
PRODUCTS_RAW = [
    ("5.1.1", "Principal Protected Note", "N_A"), ("5.1.2", "Reverse Convertible", "N_A"),
    ("5.1.3", "Phoenix Autocallable", "LONG"), ("5.1.4", "Discounted Reverse Convertible", "N_A"),
    ("5.1.5", "Knock-Out DRC", "N_A"), ("5.1.6", "Callable RC", "N_A"),
    ("5.1.7", "Airbag / Leveraged RC", "N_A"), ("5.1.8", "Bonus / Participation Note", "N_A"),
    ("5.1.9", "Fixed Coupon Note", "N_A"), ("5.1.10", "Callable Range Accrual ELN", "N_A"),
    ("5.1.11", "Issuer Callable Note", "N_A"), ("5.1.12", "Digital Coupon Note", "N_A"),
    ("5.1.13", "Booster Note", "N_A"), ("5.1.14", "Digital Coupon Knock-In Put", "N_A"),
    ("5.1.15", "Warrant / Turbo", "N_A"),
    ("5.2.1", "Interest Rate Swap", "N_A"), ("5.2.2", "Total Return Swap", "N_A"),
    ("5.2.3", "Equity Swap", "N_A"), ("5.2.4", "Variance Swap", "N_A"),
    ("5.2.5", "Credit Default Swap", "N_A"), ("5.2.6", "Cross-Currency Swap", "N_A"),
    ("5.2.7", "Commodity Swap", "N_A"), ("5.2.8", "Vanilla Swap", "N_A"),
    ("5.3.1", "IR Callable Fixed Swap", "N_A"), ("5.3.2", "Zero-Coupon Linked Note", "N_A"),
    ("5.3.3", "Non-Callable Range Accrual", "N_A"), ("5.3.4", "Callable Range Accrual SRT", "N_A"),
    ("5.3.5", "Digital Cap-Floor Note", "N_A"),
    ("5.4.1", "Vanilla Steepener", "N_A"), ("5.4.2", "Range Accrual Steepener", "N_A"),
    ("5.4.3", "Callable Steepener", "N_A"), ("5.4.4", "TARN Steepener", "N_A"),
    ("5.5.1", "Vanilla Credit-Linked Note", "N_A"), ("5.5.2", "Skew CLN", "N_A"),
    ("5.5.3", "First-to-Default Note", "LONG"), ("5.5.4", "Nth-to-Default Note", "SHORT"),
    ("5.5.5", "Synthetic CDO Tranche", "N_A"),
    ("5.6.1", "Structured Deposit", "N_A"), ("5.6.2", "Forward", "N_A"),
    ("5.6.3", "Vanilla Options", "N_A"), ("5.6.4", "Equity-Linked Option", "N_A"),
    ("5.6.5", "Option on RC", "N_A"), ("5.6.6", "Accumulator", "N_A"),
    ("5.6.7", "Decumulator", "N_A"), ("5.6.8", "Dual Currency Investment", "N_A"),
    ("5.6.9", "Shark Fin Note", "N_A"), ("5.6.10", "Snowball Note", "N_A"),
    ("5.6.11", "Cliquet / Ratchet", "N_A"), ("5.6.12", "Worst-of Autocallable", "LONG"),
]
SYSTEM = {"ELN": "Murex", "Swap": "Murex", "SRT": "Murex", "STEG": "Murex", "CLN": "Murex", "Other": "Murex"}


def section_lines(sec):
    """Return (start,end) line numbers of a 5.x.y chapter in the Bible, else (0,0)."""
    try:
        text = BIBLE.read_text(encoding="utf-8").split("\n")
    except OSError:
        return (0, 0)
    s = next((i + 1 for i, l in enumerate(text) if l.strip().startswith(f"### {sec} ")), 0)
    if not s:
        return (0, 0)
    e = next((i + 1 for i in range(s, len(text)) if re.match(r"^### 5\.|^## [56]", text[i]) and i + 1 > s), len(text))
    return (s, e)


# --------------------------------------------------------------------------- #
# 2. Parse the live linter rules and regression tests (ground truth)
# --------------------------------------------------------------------------- #
def parse_linter_rules():
    src = (ROOT / "governance/linter/semantic_linter.py").read_text(encoding="utf-8")
    rules = []
    for m in re.finditer(r'@line_rule\("([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\)', src):
        rules.append({"id": m.group(1), "severity": m.group(2), "regression_test": m.group(3),
                      "category": m.group(1).split("-")[1]})
    # document-level rules referenced in code
    for rid in ["LNT-XAR-03", "LNT-XAR-01", "LNT-XAR-02"]:
        if not any(r["id"] == rid for r in rules):
            rules.append({"id": rid, "severity": "S1", "regression_test": "", "category": "XAR"})
    return rules


def parse_tests():
    src = (ROOT / "governance/linter/regression_tests.py").read_text(encoding="utf-8")
    tests = []
    for m in re.finditer(r'@test\("([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\)', src):
        tests.append({"id": m.group(1), "severity": m.group(2), "objective": m.group(3)})
    return tests


# --------------------------------------------------------------------------- #
# 3. Errata (E-01 .. E-13) — the canonical V1.0.1 corrections
# --------------------------------------------------------------------------- #
ERRATA = [
    ("E-01", "ART-DB", "Label correction", "P1", "FTD §1/§11/table correlation labels"),
    ("E-02", "ART-DB", "Label correction", "P1", "Worst-of correlation label"),
    ("E-03", "ART-P6", "Factual", "P1", "Part 6 protection ownership"),
    ("E-04", "ART-P6", "Qualifier", "P1", "Part 6 / Encyclopedia raw-vs-hedged"),
    ("E-05", "ART-DB", "Arithmetic", "P1", "WOAC 65% above/below strike"),
    ("E-06", "ART-DB", "Label correction", "P2", "Dispersion = short correlation"),
    ("E-07", "ART-DB", "Arithmetic", "P2", "Gamma sign intermediate step"),
    ("E-08", "ART-IS", "Label correction", "P1", "Interview WOAC self-contradiction (from R-01)"),
    ("E-09", "ART-DB", "Label correction", "P1", "NTD coupon-scaling table labels (from R-02)"),
    ("E-10", "ART-DB", "Label correction", "P1", "Cross-family table FTD/worst-of short→long"),
    ("E-11", "ART-DB", "Label correction", "P1", "Phoenix takeaway short→long"),
    ("E-12", "ART-IS", "Label correction", "P1", "Interview WOAC row short→long"),
    ("E-13", "ART-DB", "Label correction", "P1", "NTD common-mistakes 4TD/5TD long→short"),
]

ARTIFACTS = [
    ("ART-DB", "Desk Bible v2", "Desk_Bible_v2.md"),
    ("ART-IS", "Interview System v2.2", "production/interview_system_v2_2.md"),
    ("ART-ENC", "Infrastructure Encyclopedia v1", "production/infrastructure_encyclopedia_v1.md"),
    ("ART-SOL", "Solutions Manual", "production/solutions_manual.md"),
    ("ART-ATL", "Product DNA Atlas", "production/product_dna_atlas.md"),
    ("ART-P6", "Part 6 Operations Guide", "production/part6_sections_10_11.md"),
]

TERMS = [
    ("TERM-COR-01", "long correlation", "Benefits (MTM) when correlation rises", True, "structurally short (sold the premium)"),
    ("TERM-COR-02", "short correlation", "Risk rises (MTM) when correlation rises", True, "raw desk position; qualify raw/net"),
    ("TERM-COR-03", "structurally short", "Sold the correlation premium at inception (structural convention)", False, ""),
    ("TERM-COR-04", "dispersion trade", "Long single-stock vol + short basket vol = short correlation", False, ""),
]


# --------------------------------------------------------------------------- #
# 4. Build nodes + edges
# --------------------------------------------------------------------------- #
def build():
    nodes, edges = [], []

    def node(nid, ntype, **props):
        nodes.append({"id": nid, "type": ntype, **props})

    def edge(etype, src, tgt, **props):
        edges.append({"type": etype, "source": src, "target": tgt, **props})

    # families as anchor product-group nodes
    for fam in sorted(set(FAMILY.values())):
        node(f"FAM-{fam}", "N-FAMILY", name=fam)

    # products
    for sec, name, corr in PRODUCTS_RAW:
        fam = FAMILY[sec.rsplit(".", 1)[0]]
        s, e = section_lines(sec)
        pid = f"PROD-{fam}-{sec.replace('.', '')}"
        node(pid, "N-PRODUCT", name=name, family=fam, system=SYSTEM[fam],
             correlation_direction=corr, status="CANONICAL", desk_bible_section=sec,
             start_line=s, end_line=e)
        edge("BELONGS_TO", pid, f"FAM-{fam}")
        # section node
        secid = f"SEC-DB-{sec.replace('.', '')}"
        node(secid, "N-SECTION", artifact_id="ART-DB", title=f"{sec} {name}",
             start_line=s, end_line=e)
        edge("CONTAINS", "ART-DB", secid)
        # correlation term usage
        if corr == "LONG":
            edge("USES", pid, "TERM-COR-01", note="investor long correlation (MTM); structurally short")
        elif corr == "SHORT":
            edge("USES", pid, "TERM-COR-02", note="investor short correlation (N>=2)")

    # worst-of long-correlation products hedged by dispersion
    for sec in ["5.1.3", "5.5.3", "5.6.12"]:
        fam = FAMILY[sec.rsplit(".", 1)[0]]
        pid = f"PROD-{fam}-{sec.replace('.', '')}"
        edge("HEDGED_BY", pid, "TERM-COR-04", note="desk raw short correlation hedged via dispersion")

    # artifacts
    for aid, name, path in ARTIFACTS:
        p = ROOT / path
        lc = len(p.read_text(encoding="utf-8").split("\n")) if p.exists() else 0
        node(aid, "N-ARTIFACT", name=name, file_path=path, version="V1.0.1",
             status="CANONICAL", line_count=lc)
    edge("DEPENDS_ON", "ART-IS", "ART-DB")
    edge("DEPENDS_ON", "ART-SOL", "ART-DB")
    edge("DEPENDS_ON", "ART-ATL", "ART-DB")

    # terms + conventions
    for tid, name, mean, alt, qual in TERMS:
        node(tid, "N-TERM", name=name, canonical_meaning=mean, has_alternate=alt,
             required_qualifier=qual, severity="S1")
    node("CON-01", "N-CONVENTION", concept="correlation direction",
         canonical_rule="MTM sensitivity convention (long = benefits from rising rho)",
         alternate_rule="structural convention (short = sold the premium)",
         qualifier="'structurally' + MTM-long clause")
    edge("REQUIRES", "TERM-COR-01", "CON-01")
    edge("REQUIRES", "TERM-COR-02", "CON-01")

    # governance rules (one per correlation term, links to linter)
    node("T-COR-01", "N-GOVERNANCE_RULE", term="long/short correlation", severity="S1",
         canonical_meaning="MTM convention; structural use must be qualified")
    edge("GOVERNS", "T-COR-01", "TERM-COR-01")
    edge("GOVERNS", "T-COR-01", "TERM-COR-02")

    # linter rules + tests
    rules = parse_linter_rules()
    for r in rules:
        node(r["id"], "N-LINTER_RULE", severity=r["severity"], category=r["category"],
             regression_test=r.get("regression_test", ""))
        if r["category"] in ("COR", "POS", "PRO", "QAL", "XAR"):
            edge("DETECTS", r["id"], "T-COR-01")
    tests = parse_tests()
    for t in tests:
        node(t["id"], "N-TEST", objective=t["objective"], severity=t["severity"])
    # VALIDATES: test -> linter rule (by the rule's declared regression_test)
    test_ids = {t["id"] for t in tests}
    for r in rules:
        rt = r.get("regression_test")
        if rt and rt in test_ids:
            edge("VALIDATES", rt, r["id"])

    # errata + CORRECTS edges + COVERS (test -> erratum)
    erratum_to_test = {
        "E-01": "REG-COR-01", "E-02": "REG-COR-04", "E-05": "REG-SGN-01", "E-06": "REG-COR-07",
        "E-07": "REG-SGN-02", "E-08": "REG-COR-08", "E-09": "REG-COR-05", "E-03": "REG-PRO-01",
        "E-04": "REG-POS-03",
    }
    for eid, aid, etype, sev, desc in ERRATA:
        node(eid, "N-ERRATUM", artifact_id=aid, error_type=etype, severity=sev, description=desc)
        edge("CORRECTS", eid, aid)
        if eid in erratum_to_test and erratum_to_test[eid] in test_ids:
            edge("COVERS", erratum_to_test[eid], eid)
    for promoted, src in [("E-08", "R-01"), ("E-09", "R-02")]:
        node(src, "N-REVIEW", type="REVIEW_ONLY", artifact_id="ART-DB",
             description=f"promoted to {promoted}", disposition="PROMOTED")
        edge("PROMOTED_FROM", promoted, src)

    return nodes, edges


# --------------------------------------------------------------------------- #
# 5. Emit JSON, GraphML, stats
# --------------------------------------------------------------------------- #
def emit(nodes, edges):
    (OUT / "knowledge_graph.json").write_text(
        json.dumps({"nodes": nodes, "edges": edges}, indent=2, ensure_ascii=False), encoding="utf-8")

    # GraphML
    g = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">',
         '<key id="type" for="node" attr.name="type" attr.type="string"/>',
         '<key id="name" for="node" attr.name="name" attr.type="string"/>',
         '<key id="etype" for="edge" attr.name="etype" attr.type="string"/>',
         '<graph edgedefault="directed">']
    for n in nodes:
        g.append(f'<node id="{html.escape(n["id"])}">'
                 f'<data key="type">{html.escape(n["type"])}</data>'
                 f'<data key="name">{html.escape(str(n.get("name", n["id"])))}</data></node>')
    for i, e in enumerate(edges):
        g.append(f'<edge id="e{i}" source="{html.escape(e["source"])}" target="{html.escape(e["target"])}">'
                 f'<data key="etype">{html.escape(e["type"])}</data></edge>')
    g += ['</graph>', '</graphml>']
    (OUT / "knowledge_graph.graphml").write_text("\n".join(g), encoding="utf-8")

    # stats
    from collections import Counter
    nt = Counter(n["type"] for n in nodes)
    et = Counter(e["type"] for e in edges)
    corr = Counter(n.get("correlation_direction") for n in nodes if n["type"] == "N-PRODUCT")
    lines = ["# Knowledge Graph — Population Summary", "",
             f"**Nodes:** {len(nodes)}  **Edges:** {len(edges)}", "",
             "## Node types", "", "| Type | Count |", "|------|------:|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(nt.items())]
    lines += ["", "## Edge types", "", "| Type | Count |", "|------|------:|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(et.items())]
    lines += ["", "## Product correlation directions (MTM convention)", "",
              "| Direction | Count |", "|-----------|------:|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(corr.items())]
    lines += ["", "*Generated by build_kg.py from the live linter, tests, errata, and 49 products.*"]
    (OUT / "kg_stats.md").write_text("\n".join(lines), encoding="utf-8")
    return nt, et


if __name__ == "__main__":
    nodes, edges = build()
    nt, et = emit(nodes, edges)
    print(f"Knowledge graph populated: {len(nodes)} nodes, {len(edges)} edges")
    print("Node types:", dict(nt))
    print("Wrote knowledge_graph.json / .graphml / kg_stats.md to", OUT)
