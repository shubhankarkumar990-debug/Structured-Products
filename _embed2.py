import re
from pathlib import Path
B=Path("Desk_Bible_v2.md"); t=B.read_text(encoding="utf-8")
JOBS=[("TRADE ENTRY","assets/foundations/concept_systems_flow_01.svg","How a trade flows through the systems"),
      ("Trade Date  →  +Settlement Lag","assets/foundations/concept_settlement_timeline_01.svg","Settlement workflow (DvP)")]
fre=re.compile(r"```[^\n]*\n(.*?)\n```",re.S)
for anc,svg,cap in JOBS:
    for m in fre.finditer(t):
        if anc in m.group(1):
            t=t[:m.start()]+f"![{cap}]({svg})\n\n*{cap}.*"+t[m.end():]; print("OK",anc[:30]); break
B.write_text(t,encoding="utf-8")
