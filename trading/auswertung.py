#!/usr/bin/env python3
"""Wertet journal.csv aus: Trefferquote, Durchschnittsgewinn/-verlust, Erwartungswert, max. Drawdown,
getrennt nach Anlageklasse und Quelle, Vergleich mit MSCI World (EUNL.DE) ueber denselben Zeitraum.
Steuer: vereinfachte Abgeltungsteuer auf positive Jahressumme (ohne Pauschbetrag/Verlusttoepfe - nur Naeherung)."""
import csv, json, os, datetime, urllib.request, collections
D = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(os.path.join(D, "config.json")))
rows = [r for r in csv.DictReader(open(os.path.join(D, "journal.csv"))) if r.get("ausstieg_datum")]
def netto(r): return float(r["ergebnis_brutto_eur"] or 0) - float(r["gebuehren_eur"] or 0)
def stats(rs):
    if not rs: return None
    n = [netto(r) for r in rs]; w = [x for x in n if x > 0]; l = [x for x in n if x <= 0]
    eq, peak, mdd = 0, 0, 0
    for x in n: eq += x; peak = max(peak, eq); mdd = min(mdd, eq - peak)
    return dict(n=len(n), treffer=len(w)/len(n), avg_gewinn=sum(w)/len(w) if w else 0, avg_verlust=sum(l)/len(l) if l else 0,
                erwartungswert=sum(n)/len(n), summe=sum(n), max_drawdown_eur=mdd)
def show(t, s):
    if s: print(f"{t:35s} n={s['n']:3d} Treffer {s['treffer']:.0%} OGewinn {s['avg_gewinn']:+.2f} OVerlust {s['avg_verlust']:+.2f} EV/Trade {s['erwartungswert']:+.2f} Summe {s['summe']:+.2f} MaxDD {s['max_drawdown_eur']:.2f}")
rows.sort(key=lambda r: r["ausstieg_datum"])
for modus in ("papier", "echt"):
    rs = [r for r in rows if r["modus"] == modus]
    if not rs: continue
    print(f"\n=== Modus: {modus} ==="); show("GESAMT", stats(rs))
    for k in sorted(set(r["anlageklasse"] for r in rs)): show("Klasse " + k, stats([r for r in rs if r["anlageklasse"] == k]))
    by_src = collections.defaultdict(list)
    for r in rs:
        for s in r["quellen"].split(";"): by_src[s.strip()].append(r)
    for k, v in sorted(by_src.items()): show("Quelle " + k, stats(v))
    s = stats(rs)
    steuer = max(0, s["summe"]) * cfg["abgeltungsteuer_pct"] / 100
    print(f"Naeherung nach Steuer: {s['summe'] - steuer:+.2f} EUR (Steuer ~{steuer:.2f})")
    start = min(r["einstieg_datum"] for r in rs); end = max(r["ausstieg_datum"] for r in rs)
    try:
        j = json.load(urllib.request.urlopen(urllib.request.Request(f"https://query1.finance.yahoo.com/v8/finance/chart/{cfg['benchmark_yahoo']}?range=5y&interval=1d", headers={"User-Agent": "Mozilla/5.0"}), timeout=30))["chart"]["result"][0]
        px = [(datetime.datetime.fromtimestamp(t, datetime.UTC).strftime("%Y-%m-%d"), c) for t, c in zip(j["timestamp"], j["indicators"]["quote"][0]["close"]) if c]
        a = [c for d, c in px if d >= start][0]; b = [c for d, c in px if d <= end][-1]
        print(f"Benchmark {cfg['benchmark_yahoo']} {start}..{end}: {b/a-1:+.2%} -> auf {cfg['startkapital_eur']} EUR: {cfg['startkapital_eur']*(b/a-1):+.2f} EUR vs. Strategie {s['summe']:+.2f} EUR")
    except Exception as e:
        print("Benchmark nicht abrufbar:", e)
