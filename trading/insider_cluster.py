#!/usr/bin/env python3
"""Verdichtet form4_purchases.jsonl zu Cluster-Kaeufen (>=2 Insider = Director/Officer, >=200k USD)
und prueft Liquiditaet/Historie ueber Yahoo-Kursdaten. Fonds/BDCs/SPACs, 10%-Eigner ohne Organfunktion,
Kurse < 3 USD und Kaeufe < 10k USD werden ausgeschlossen. Achtung: Mitarbeiter-Kaufplaene (viele Kaeufe
zum identischen Preis) und Kaeufe zum IPO-Preis manuell aussortieren."""
import json,collections,re,urllib.request,datetime,statistics as st,sys
f=sys.argv[1] if len(sys.argv)>1 else 'form4_purchases.jsonl'
R=[json.loads(l) for l in open(f)]
fund=re.compile(r'\b(FUND|TRUST|BDC|INCOME|PRIVATE|CREDIT|LENDING|CAPITAL CORP|REIT|FINANCE CORP|PARTNERS LP|HOLDINGS LP|ACQUISITION)\b',re.I)
agg=collections.defaultdict(lambda:{'owners':set(),'value':0,'issuer':'','first':'9999','px':[]});seen=set()
for r in R:
    k=(r['owner'],r['tdate'],r['shares'],r['price'],r['ticker'])
    if k in seen or not r['ticker'] or fund.search(r['issuer']): continue
    seen.add(k)
    if not (set(r['role'])&{'Director','Officer'}) or r['price']<3 or r['value']<10000: continue
    a=agg[r['ticker']];a['owners'].add(r['owner']);a['value']+=r['value'];a['issuer']=r['issuer'];a['first']=min(a['first'],r['tdate']);a['px'].append(r['price'])
for t,a in sorted(agg.items(),key=lambda kv:(-len(kv[1]['owners']),-kv[1]['value'])):
    if len(a['owners'])<2 or a['value']<2e5: continue
    try:
        j=json.load(urllib.request.urlopen(urllib.request.Request(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d",headers={'User-Agent':'Mozilla/5.0'}),timeout=20))['chart']['result'][0]
        q=j['indicators']['quote'][0];p=[(c,v or 0) for c,v in zip(q['close'],q['volume']) if c]
        adv=st.mean([c*v for c,v in p[-20:]]);last=p[-1][0];ok=len(p)>=120 and adv>=20e6 and last>=5
        print(f"{'OK ' if ok else 'xx '}{t:6s} {a['issuer'][:30]:30s} Insider={len(a['owners'])} ${a['value']/1e6:6.2f}M ab {a['first']} OKaufkurs {sum(a['px'])/len(a['px']):8.2f} jetzt {last:8.2f} ({last/(sum(a['px'])/len(a['px']))-1:+.0%}) ADV ${adv/1e6:.0f}M Historie {len(p)}T")
    except Exception as e: print('?? ',t,e)
