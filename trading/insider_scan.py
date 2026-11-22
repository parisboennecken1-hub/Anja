#!/usr/bin/env python3
"""SEC-Form-4-Scan: findet Insider-KAEUFE mit eigenem Geld (Transaktionscode P) in einem Datumsfenster.
Aufruf: python3 insider_scan.py 2026-10-27 2026-11-20   -> schreibt form4_purchases.jsonl
Hinweis: ~8 Abrufe/s (SEC-Limit 10/s); ein Monat (~20.000 Meldungen) dauert ca. 40 Min.
Danach: python3 insider_cluster.py
"""
# Scan SEC daily form indexes for Form 4 filings in a date window, parse open-market purchases (code P)
import urllib.request,time,re,json,sys,datetime,xml.etree.ElementTree as ET
UA={'User-Agent':'ResearchClient research@example.org'}
def get(u,retry=3):
    for k in range(retry):
        try:
            time.sleep(0.11);return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read()
        except Exception as e:
            if k==retry-1: raise
            time.sleep(2)
start=datetime.date.fromisoformat(sys.argv[1]);end=datetime.date.fromisoformat(sys.argv[2])
filings=[]
d=start
while d<=end:
    if d.weekday()<5:
        q=(d.month-1)//3+1
        u=f"https://www.sec.gov/Archives/edgar/daily-index/{d.year}/QTR{q}/form.{d.strftime('%Y%m%d')}.idx"
        try:
            t=get(u).decode('latin1')
            for line in t.splitlines():
                if line.startswith('4 ') :
                    m=re.search(r'(edgar/data/\S+\.txt)',line)
                    if m: filings.append((str(d),m.group(1)))
        except Exception as e: print('noidx',d,e,file=sys.stderr)
    d+=datetime.timedelta(days=1)
print('form4 filings',len(filings),file=sys.stderr)
out=open('form4_purchases.jsonl','w');import threading,concurrent.futures as cf
lock=threading.Lock();cnt=[0]
_last=[0.0]
def rl():
    with lock:
        now=time.time();w=max(0,_last[0]+0.115-now);_last[0]=now+w
    time.sleep(w)
def work(item):
    fd,path=item;rl()
    try: raw=urllib.request.urlopen(urllib.request.Request('https://www.sec.gov/Archives/'+path,headers=UA),timeout=30).read().decode('utf-8','ignore')
    except Exception: return
    with lock:
        cnt[0]+=1
        if cnt[0]%500==0: print('progress',cnt[0],file=sys.stderr,flush=True)
    proc(fd,path,raw)
def proc(fd,path,raw):
    m=re.search(r'<ownershipDocument>.*?</ownershipDocument>',raw,re.S)
    if not m or '<transactionCode>P</transactionCode>' not in raw: return
    try: x=ET.fromstring(m.group(0))
    except Exception: return
    g=lambda e,p: (e.findtext(p) or '').strip()
    issuer=g(x,'issuer/issuerName');tick=g(x,'issuer/issuerTradingSymbol');icik=g(x,'issuer/issuerCik')
    owner=g(x,'reportingOwner/reportingOwnerId/rptOwnerName')
    rel=x.find('reportingOwner/reportingOwnerRelationship')
    role=[]
    if rel is not None:
        for k in ('isDirector','isOfficer','isTenPercentOwner','isOther'):
            if (rel.findtext(k) or '').strip() in('1','true'): role.append(k[2:])
        ot=(rel.findtext('officerTitle') or '').strip()
        if ot: role.append(ot)
    for tr in x.findall('nonDerivativeTable/nonDerivativeTransaction'):
        if g(tr,'transactionCoding/transactionCode')!='P': continue
        try:
            sh=float(g(tr,'transactionAmounts/transactionShares/value') or 0);px=float(g(tr,'transactionAmounts/transactionPricePerShare/value') or 0)
        except: continue
        rec=dict(filed=fd,tdate=g(tr,'transactionDate/value'),issuer=issuer,ticker=tick.upper(),cik=icik,owner=owner,role=role,shares=sh,price=px,value=sh*px,url='https://www.sec.gov/Archives/'+path)
        with lock: out.write(json.dumps(rec)+'\n');out.flush()
with cf.ThreadPoolExecutor(24) as ex: list(ex.map(work,filings))
print('done',file=sys.stderr)
