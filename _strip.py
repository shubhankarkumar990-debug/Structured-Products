import re
from pathlib import Path
B=Path("Desk_Bible_v2.md"); lines=B.read_text(encoding="utf-8").split("\n")
emb=re.compile(r'!\[.*\]\(assets/foundations/.*\.svg\)')
cap=re.compile(r'^\*.*\*$')
out=[]; i=0; removed=0
while i<len(lines):
    out.append(lines[i])
    if emb.search(lines[i]):
        j=i+1
        while j<len(lines) and lines[j].strip()=="": j+=1
        if j<len(lines) and cap.match(lines[j].strip()):
            out.append("")            # normalize one blank line
            removed+=1; i=j+1; continue
    i+=1
B.write_text("\n".join(out),encoding="utf-8")
print("caption lines removed:",removed)
