#!/usr/bin/env python3
"""Backtest: Haben COT-Extreme (Index >=90 / <=10) die 3-/6-Monats-Rendite vorhergesagt? (2010-heute)"""
import json,urllib.request,urllib.parse,datetime,statistics as st,bisect
def q(ds,where):
    u=f"https://publicreporting.cftc.gov/resource/{ds}.json?"+urllib.parse.urlencode({'$where':where,'$order':'report_date_as_yyyy_mm_dd','$limit':'50000'})
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=120))
def px(t):
    j=json.load(urllib.request.urlopen(urllib.request.Request(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=1104537600&period2=1800000000&interval=1d",headers={'User-Agent':'Mozilla/5.0'}),timeout=60))['chart']['result'][0]
    return [(datetime.datetime.fromtimestamp(a,datetime.UTC).date(),b) for a,b in zip(j['timestamp'],j['indicators']['quote'][0]['close']) if b]
def fwd(prices,d,days):
    ds=[p[0] for p in prices];i=bisect.bisect_left(ds,d+datetime.timedelta(days=3))  # entry after Friday release
    j=bisect.bisect_left(ds,ds[i]+datetime.timedelta(days=days)) if i<len(ds) else None
    if i>=len(ds) or j>=len(ds): return None
    return prices[j][1]/prices[i][1]-1
def run(name,ds,where,lk,sk,ticker,sign=+1):
    r=q(ds,where+" AND report_date_as_yyyy_mm_dd >= '2007-01-01'")
    dates=[datetime.date.fromisoformat(x['report_date_as_yyyy_mm_dd'][:10]) for x in r]
    net=[float(x[lk])-float(x[sk]) for x in r]
    P=px(ticker);W=156
    res={'hi':{91:[],182:[]},'lo':{91:[],182:[]},'all':{91:[],182:[]}}
    for i in range(W,len(r)):
        win=net[i-W:i+1];lo,hi=min(win),max(win);ix=100*(net[i]-lo)/(hi-lo) if hi>lo else 50
        for h in (91,182):
            f=fwd(P,dates[i],h)
            if f is None: continue
            res['all'][h].append(f)
            if ix>=90: res['hi'][h].append(f)
            if ix<=10: res['lo'][h].append(f)
    def s(a): return f"n={len(a)} P>0 {sum(x>0 for x in a)/len(a):.0%} med {st.median(a):+.1%}" if a else 'n=0'
    print(f"{name}: Basis 3M {s(res['all'][91])} | 6M {s(res['all'][182])}")
    print(f"   Idx>=90: 3M {s(res['hi'][91])} | 6M {s(res['hi'][182])}")
    print(f"   Idx<=10: 3M {s(res['lo'][91])} | 6M {s(res['lo'][182])}")
run('GOLD Commercials','72hh-3qpy',"market_and_exchange_names like 'GOLD - COMMODITY EXCHANGE%'",'prod_merc_positions_long','prod_merc_positions_short','GC=F')
run('SILVER Commercials','72hh-3qpy',"market_and_exchange_names like 'SILVER - COMMODITY EXCHANGE%'",'prod_merc_positions_long','prod_merc_positions_short','SI=F')
run('WTI Commercials','72hh-3qpy',"market_and_exchange_names like 'WTI-PHYSICAL - NEW YORK%' OR market_and_exchange_names like 'CRUDE OIL, LIGHT SWEET - NEW YORK%'",'prod_merc_positions_long','prod_merc_positions_short','CL=F')
run('EURO FX LevFunds','gpe5-46if',"market_and_exchange_names like 'EURO FX - CHICAGO%'",'lev_money_positions_long','lev_money_positions_short','EURUSD=X')
run('S&P LevFunds','gpe5-46if',"market_and_exchange_names like 'E-MINI S&P 500 -%'",'lev_money_positions_long','lev_money_positions_short','^GSPC')
