#!/usr/bin/env python3
"""COT-Positionierung (CFTC, 3-Jahres-COT-Index) fuer Index-, Waehrungs-, Anleihe-, Krypto- und Rohstoff-Futures."""
import json,urllib.request,urllib.parse
def q(ds,where):
    u=f"https://publicreporting.cftc.gov/resource/{ds}.json?"+urllib.parse.urlencode({'$where':where,'$order':'report_date_as_yyyy_mm_dd','$limit':'5000'})
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
since="report_date_as_yyyy_mm_dd >= '2023-11-01'"
TFF={'E-MINI S&P 500':"market_and_exchange_names like 'E-MINI S&P 500 -%'",'NASDAQ-100 E-MINI':"market_and_exchange_names like 'NASDAQ MINI%'",
 'EURO FX':"market_and_exchange_names like 'EURO FX - CHICAGO%'",'JAPANESE YEN':"market_and_exchange_names like 'JAPANESE YEN - CHICAGO%'",
 '10Y T-NOTE':"market_and_exchange_names like 'UST 10Y NOTE%'",'BITCOIN (CME)':"market_and_exchange_names like 'BITCOIN - CHICAGO%'",'ETHER (CME)':"market_and_exchange_names like 'ETHER CASH SETTLED%'",'VIX':"market_and_exchange_names like 'VIX FUTURES%'"}
DIS={'GOLD':"market_and_exchange_names like 'GOLD - COMMODITY EXCHANGE%'",'WTI CRUDE':"market_and_exchange_names like 'WTI-PHYSICAL - NEW YORK%'",'SILVER':"market_and_exchange_names like 'SILVER - COMMODITY EXCHANGE%'",'COPPER':"market_and_exchange_names like 'COPPER- #1 - COMMODITY EXCHANGE%'"}
def idx(series):
    lo,hi=min(series),max(series);return 100*(series[-1]-lo)/(hi-lo) if hi>lo else 50
res={}
for k,w in TFF.items():
    try: r=q('gpe5-46if',w+' AND '+since)
    except Exception as e: print(k,'ERR',e);continue
    if not r: print(k,'no data');continue
    names=set(x['market_and_exchange_names'] for x in r)
    lev=[int(float(x['lev_money_positions_long']))-int(float(x['lev_money_positions_short'])) for x in r]
    am=[int(float(x['asset_mgr_positions_long']))-int(float(x['asset_mgr_positions_short'])) for x in r]
    dl=[int(float(x['dealer_positions_long_all']))-int(float(x['dealer_positions_short_all'])) for x in r]
    oi=int(float(r[-1]['open_interest_all']))
    print(f"{k:18s} {r[-1]['report_date_as_yyyy_mm_dd'][:10]} n={len(r)} OI={oi} | LevFunds net {lev[-1]:+} (Δ1w {lev[-1]-lev[-2]:+}, COT-Idx3J {idx(lev):.0f}) | AssetMgr net {am[-1]:+} (Idx {idx(am):.0f}) | Dealer net {dl[-1]:+} (Idx {idx(dl):.0f}) {list(names)[:2]}")
for k,w in DIS.items():
    try: r=q('72hh-3qpy',w+' AND '+since)
    except Exception as e: print(k,'ERR',e);continue
    if not r: print(k,'no data');continue
    mm=[int(float(x['m_money_positions_long_all']))-int(float(x['m_money_positions_short_all'])) for x in r]
    pr=[int(float(x['prod_merc_positions_long']))-int(float(x['prod_merc_positions_short'])) for x in r]
    print(f"{k:18s} {r[-1]['report_date_as_yyyy_mm_dd'][:10]} n={len(r)} | ManagedMoney net {mm[-1]:+} (Δ1w {mm[-1]-mm[-2]:+}, Idx3J {idx(mm):.0f}) | Producer/Commercial net {pr[-1]:+} (Idx {idx(pr):.0f})")
