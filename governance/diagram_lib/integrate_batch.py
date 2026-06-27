import sys,json,re,os
sys.path.insert(0,'governance/diagram_lib'); import sp_diagrams as D
OUT="/sessions/charming-jolly-goodall/mnt/outputs"; F="Desk_Bible_v2.md"
DESK="Bank Lens (Desk Economics)"; CTRL="Bank Lens (Controls & 2nd Line of Defence)"
def payoff_img(abbr,A,m):
    if m.get("legs"):
        lg=m["legs"]; f=f"{A}/legs_{abbr}_01.svg"; D.swap_legs(f,client_pays=lg["client_pays"],client_receives=lg["client_receives"],client_label="Investor",title=lg["title"]); return f'![{lg["title"]} — Investor Lens]({f})'
    p=m.get("payoff")
    if not p: return ""
    k=p.get("kind"); f=f"{A}/payoff_{abbr}_01.svg"
    if k=="ppn": D.payoff_ppn(f,floor_pct=p.get("floor_pct",100),participation=p["participation"],cap_pct=p.get("cap_pct"),title=p["title"])
    elif k=="option": D.payoff_option(f,option=p.get("option","call"),strike_pct=p.get("strike_pct",100),premium_pct=p.get("premium_pct",5),title=p["title"])
    elif k=="forward": D.payoff_forward(f,direction=p.get("direction","long"),strike_pct=p.get("strike_pct",100),title=p["title"])
    elif k=="correlation": D.payoff_correlation(f,direction=p["direction"],title=p["title"])
    elif k=="range_accrual": D.payoff_range_accrual(f,max_coupon=p["max_coupon"],title=p["title"])
    elif k=="steepener": D.payoff_steepener(f,leverage=p["leverage"],floor_coupon=p.get("floor_coupon",0),cap_coupon=p.get("cap_coupon"),strike_spread=p.get("strike_spread",0),title=p["title"])
    elif k=="digital": D.payoff_digital(f,strike_pct=p["strike_pct"],coupon_pct=p["coupon_pct"],capital_barrier_pct=p.get("capital_barrier_pct"),title=p["title"])
    elif k=="digital_rate": D.payoff_digital_rate(f,strike_rate=p["strike_rate"],high_coupon=p["high_coupon"],low_coupon=p.get("low_coupon",0),title=p["title"])
    elif k=="varswap": D.payoff_varswap(f,strike_vol=p["strike_vol"],title=p["title"])
    elif k=="geared": D.payoff_geared_note(f,barrier_pct=p["barrier_pct"],coupon_pct=p["coupon_pct"],gearing=p.get("gearing",1.33),title=p["title"])
    elif k=="participation": D.payoff_participation(f,bonus_pct=p["bonus_pct"],participation=p["participation"],barrier_pct=p["barrier_pct"],title=p["title"])
    elif k=="barrier_note": D.payoff_barrier_note(f,barrier_pct=p["barrier_pct"],coupon_pct=p["coupon_pct"],title=p["title"])
    elif k=="sharkfin": D.payoff_sharkfin(f,participation=p.get("participation",1.0),ko_barrier_pct=p["ko_barrier_pct"],rebate_pct=p.get("rebate_pct",2),floor_pct=p.get("floor_pct",100),title=p["title"])
    else: return ""
    return f'![{p["title"]} — Investor Lens]({f})'
def build(abbr):
    m=json.load(open(f"{OUT}/{abbr}_manifest.json")); A=f"assets/{abbr}"; os.makedirs(A,exist_ok=True); E={}
    E["payoff"]=payoff_img(abbr,A,m)
    if m.get("gamma"):
        g=m["gamma"]; gf=f"{A}/desk_{abbr}_gamma_07.svg"; D.desk_gamma_profile(gf,barrier_pct=g["barrier_pct"],title=g["title"]); E["gamma"]=f'![{g["title"]} — {DESK}]({gf})'
    else: E["gamma"]=""
    w=m["waterfall"]; wf=f"{A}/waterfall_{abbr}_09.svg"; D.coupon_waterfall(wf,components=[(c[0],c[1]) for c in w["components"]],net_label=w.get("net_label","Net"),title=w["title"]); E["waterfall"]=f'![{w["title"]} — {DESK}]({wf})'
    r=m["recon"]; rf=f"{A}/controls_{abbr}_recon_08.svg"; D.reconciliation_flow(rf,product=abbr.upper(),bor_system="Murex",risk_system="Risk",points=[(p[0],p[1]) for p in r["points"]],flagged_index=r["flagged_index"],flag_tag=r["flag_tag"]); E["recon"]=f'![{abbr.upper()} Reconciliation Flow — {CTRL}]({rf})'
    core=open(f"{OUT}/{abbr}_core_new.md").read().rstrip("\n")
    for k in ["payoff","gamma","waterfall","recon"]: core=core.replace(f"<!--IMG:{k}-->",E[k])
    core=re.sub(r"\n{3,}","\n\n",core); assert not re.findall(r"<!--IMG:\w+-->",core),(abbr,re.findall(r"<!--IMG:\w+-->",core))
    return core.split("\n")
def splice(core):
    lines=open(F,encoding="utf-8").read().split("\n"); head=core[0].strip()
    s=[i for i,l in enumerate(lines) if l.strip()==head]; assert len(s)==1,(head,len(s)); s=s[0]
    nxt=next(i for i in range(s+1,len(lines)) if re.match(r"^### 5\.",lines[i]) or lines[i].startswith("## 5.") or lines[i].startswith("## 6"))
    kc=next((i for i in range(s+1,nxt) if lines[i].strip()=="### Knowledge Check"),nxt)
    open(F,"w",encoding="utf-8").write("\n".join(lines[:s]+core+lines[kc:])); return s,len(core)
import sys as S
for abbr in S.argv[1:]:
    core=build(abbr); s,n=splice(core); print(f"{abbr}: imgs {sum(1 for l in core if l.startswith('!['))}, you {sum(1 for l in core if ' you ' in l.lower() or ' your ' in l.lower())}")
