#!/usr/bin/env python3
"""Build the linked HTML edition: Bible + companions + landing page, cross-linked,
with sidebar TOC, callout styling, and a contents filter. Outputs to html_edition/site/."""
import re, subprocess, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HD = ROOT / "governance" / "html_edition"
SITE = HD / "site"
SITE.mkdir(parents=True, exist_ok=True)

# files: (source, output html, title)
FILES = [
    ("START_HERE.md", "index.html", "Structured Products — Library Home"),
    ("Desk_Bible_v2.md", "Desk_Bible_v2.html", "The Structured Products Desk Bible"),
    ("production/solutions_manual.md", "solutions_manual.html", "Solutions Manual"),
    ("production/product_comparison_matrix.md", "product_comparison_matrix.html", "Product Comparison Matrices"),
    ("production/product_dna_atlas.md", "product_dna_atlas.html", "Product DNA Atlas"),
    ("production/interview_system_v2_2.md", "interview_system_v2_2.html", "Interview System"),
    ("production/infrastructure_encyclopedia_v1.md", "infrastructure_encyclopedia_v1.html", "Market Infrastructure Encyclopedia"),
]
# map source .md (any path) -> output html name for link rewriting
MDMAP = {Path(s).name: o for s, o, _ in FILES}

def rewrite_links(text):
    # [..](production/foo.md#x) or (foo.md#x) or (foo.md)  ->  (foo.html#x)/(foo.html)
    def repl(m):
        label, target = m.group(1), m.group(2)
        if target.startswith(("http", "#", "mailto:")):
            return m.group(0)
        frag = ""
        if "#" in target:
            target, frag = target.split("#", 1); frag = "#" + frag
        fn = target.split("/")[-1]
        if fn in MDMAP:
            return f"[{label}]({MDMAP[fn]}{frag})"
        if fn.endswith(".md"):  # unknown md -> keep name but .html
            return f"[{label}]({fn[:-3]}.html{frag})"
        return m.group(0)
    return re.sub(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)', repl, text)

def main():
    # copy assets + css + mind map
    if (ROOT / "assets").exists():
        shutil.copytree(ROOT / "assets", SITE / "assets", dirs_exist_ok=True)
    shutil.copy(HD / "style.css", SITE / "style.css")
    mm = ROOT / "NotebookLM Mind Map.png"
    if mm.exists(): shutil.copy(mm, SITE / "NotebookLM Mind Map.png")
    built = []
    for src, out, title in FILES:
        sp = ROOT / src
        if not sp.exists():
            print("SKIP missing", src); continue
        md = rewrite_links(sp.read_text(encoding="utf-8"))
        tmp = Path("/tmp") / ("_tmp_" + Path(out).stem + ".md")
        tmp.write_text(md, encoding="utf-8")
        cmd = ["pandoc", str(tmp), "-f", "markdown-tex_math_dollars-tex_math_single_backslash",
               "-s", "--toc", "--toc-depth=3", "--css", "style.css",
               "-A", str(HD / "nav_include.html"),
               "--metadata", f"title={title}", "--resource-path", str(ROOT),
               "-o", str(SITE / out)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        try: tmp.unlink(missing_ok=True)
        except OSError: pass
        ok = (SITE / out).exists()
        built.append((out, ok, (r.stderr.strip().splitlines() or [""])[-1]))
        print(("OK  " if ok else "FAIL") + f" {out}")
        if not ok: print("   ", r.stderr[-300:])
    print(f"\nbuilt {sum(1 for _,ok,_ in built if ok)}/{len(FILES)} pages -> {SITE}")

if __name__ == "__main__":
    main()
