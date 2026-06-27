#!/usr/bin/env python3
"""
Query CLI over the populated knowledge graph (knowledge_graph.json).
Implements the example traversals from the ontology design.

Usage:
    python3 governance/knowledge_graph/kg_query.py <command> [arg]

Commands:
    where-corr <PRODUCT>     Where a product's correlation direction is discussed
    by-corr <LONG|SHORT>     All products with a given correlation direction
    tests-for <ERRATUM>      Regression tests that cover an erratum (e.g. E-09)
    rules-for-test <TEST>    Linter rule(s) a regression test validates (e.g. REG-COR-05)
    product <PRODUCT>        Full node + edges for a product (name or id)
    errata                   List all errata and the artifacts they correct
    stats                    Node/edge counts
    neighbors <ID>           All edges touching a node id

Examples:
    kg_query.py by-corr LONG
    kg_query.py tests-for E-09
    kg_query.py where-corr "First-to-Default Note"
"""
from __future__ import annotations
import json, sys
from pathlib import Path

KG = json.loads((Path(__file__).resolve().parent / "knowledge_graph.json").read_text(encoding="utf-8"))
NODES = {n["id"]: n for n in KG["nodes"]}
EDGES = KG["edges"]


def find_product(q):
    q = q.lower()
    for n in KG["nodes"]:
        if n["type"] == "N-PRODUCT" and (q == n["id"].lower() or q in n.get("name", "").lower()):
            return n
    return None


def out_edges(nid):
    return [e for e in EDGES if e["source"] == nid]


def in_edges(nid):
    return [e for e in EDGES if e["target"] == nid]


def cmd_by_corr(direction):
    direction = direction.upper()
    rows = [n for n in KG["nodes"] if n["type"] == "N-PRODUCT"
            and n.get("correlation_direction") == direction]
    print(f"Products with correlation_direction = {direction}  ({len(rows)}):")
    for n in sorted(rows, key=lambda x: x["desk_bible_section"]):
        print(f"  {n['desk_bible_section']:8} {n['name']:32} (Bible lines {n['start_line']}-{n['end_line']})")


def cmd_where_corr(q):
    p = find_product(q)
    if not p:
        print("Product not found:", q); return
    term = next((e["target"] for e in out_edges(p["id"]) if e["type"] == "USES"), None)
    print(f"{p['name']} — correlation_direction = {p['correlation_direction']}")
    print(f"  Desk Bible {p['desk_bible_section']} (lines {p['start_line']}-{p['end_line']})")
    if term:
        t = NODES[term]
        print(f"  Uses term: {t['name']} — {t['canonical_meaning']}")
        if t.get("required_qualifier"):
            print(f"  Required qualifier: {t['required_qualifier']}")
    hedge = [e for e in out_edges(p["id"]) if e["type"] == "HEDGED_BY"]
    for e in hedge:
        print(f"  Hedged by: {NODES[e['target']]['name']} — {e.get('note','')}")


def cmd_tests_for(eid):
    eid = eid.upper()
    tests = [e["source"] for e in in_edges(eid) if e["type"] == "COVERS"]
    er = NODES.get(eid)
    if er:
        print(f"{eid}: {er.get('description','')}  [{er.get('error_type')}, {er.get('severity')}] -> {er.get('artifact_id')}")
    if tests:
        for t in tests:
            print(f"  covered by {t}: {NODES[t].get('objective','')}")
    else:
        print("  (no direct regression-test edge; see the regression suite by category)")


def cmd_rules_for_test(tid):
    tid = tid.upper()
    rules = [e["target"] for e in out_edges(tid) if e["type"] == "VALIDATES"]
    if NODES.get(tid):
        print(f"{tid}: {NODES[tid].get('objective','')}")
    for r in rules:
        print(f"  validates linter rule {r} [{NODES[r].get('severity')}, {NODES[r].get('category')}]")
    if not rules:
        print("  (no linter rule declares this test; cross-artifact/manual test)")


def cmd_product(q):
    p = find_product(q)
    if not p:
        print("Product not found:", q); return
    print(json.dumps(p, indent=2, ensure_ascii=False))
    print("Edges:")
    for e in out_edges(p["id"]):
        print(f"  -{e['type']}-> {e['target']}  {e.get('note','')}")


def cmd_errata():
    for n in sorted([x for x in KG["nodes"] if x["type"] == "N-ERRATUM"], key=lambda x: x["id"]):
        print(f"  {n['id']:5} [{n['severity']}, {n['error_type']:16}] {n['artifact_id']:8} {n['description']}")


def cmd_stats():
    from collections import Counter
    nt = Counter(n["type"] for n in KG["nodes"]); et = Counter(e["type"] for e in EDGES)
    print(f"nodes={len(KG['nodes'])} edges={len(EDGES)}")
    print("node types:", dict(nt)); print("edge types:", dict(et))


def cmd_neighbors(nid):
    print(f"out:"); [print("  ->", e["type"], e["target"]) for e in out_edges(nid)]
    print(f"in:"); [print("  <-", e["type"], e["source"]) for e in in_edges(nid)]


CMDS = {"where-corr": cmd_where_corr, "by-corr": cmd_by_corr, "tests-for": cmd_tests_for,
        "rules-for-test": cmd_rules_for_test, "product": cmd_product, "errata": lambda *_: cmd_errata(),
        "stats": lambda *_: cmd_stats(), "neighbors": cmd_neighbors}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        print(__doc__); sys.exit(0)
    arg = sys.argv[2] if len(sys.argv) > 2 else ""
    CMDS[sys.argv[1]](arg) if arg or sys.argv[1] in ("errata", "stats") else CMDS[sys.argv[1]]()
