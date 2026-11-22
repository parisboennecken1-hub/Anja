#!/usr/bin/env python3
"""Positionsrechner im Modus MAXIMALES RISIKO (config.json): voller Kapitaleinsatz, beliebiger Hebel,
keine Limits und keine Pflicht-Checks. Ausgegeben werden nur Kennzahlen und der Knock-out-/Liquidationspreis.

Beispiel: python3 sizing.py --einstieg 54677 --stop 48000 --ziel 70000 --hebel 10
"""
import argparse, json, os
cfg = json.load(open(os.path.join(os.path.dirname(__file__), "config.json")))
p = argparse.ArgumentParser()
p.add_argument("--einstieg", type=float, required=True)
p.add_argument("--stop", type=float, help="optional")
p.add_argument("--ziel", type=float, help="optional")
p.add_argument("--klasse", default="beliebig")
p.add_argument("--hebel", type=float, default=1.0)
p.add_argument("--kapital", type=float, default=cfg["startkapital_eur"])
p.add_argument("--short", action="store_true")
a = p.parse_args()

sgn = -1 if a.short else 1
einsatz = a.kapital * cfg["einsatz_pro_trade_pct"] / 100 - cfg["gebuehr_pro_order_eur"]
exposure = einsatz * a.hebel
print(f"Kapitaleinsatz: {einsatz:.2f} EUR | Hebel {a.hebel:g}x | Exposure {exposure:.2f} EUR")
if a.hebel > 1:
    ko = a.einstieg * (1 - sgn / a.hebel)
    print(f"Knock-out-/Liquidationspreis ca.: {ko:.6g} ({(ko / a.einstieg - 1):+.2%}) -> dort Totalverlust des Einsatzes")
    if a.stop is not None and ((not a.short and ko >= a.stop) or (a.short and ko <= a.stop)):
        print("Hinweis: Knock-out liegt vor dem Stop.")
for name, kurs in (("Stop", a.stop), ("Ziel", a.ziel)):
    if kurs is not None:
        r = sgn * (kurs - a.einstieg) / a.einstieg
        pnl = max(-einsatz, exposure * r - exposure * 2 * cfg["spread_annahme_pct"] / 100 - cfg["gebuehr_pro_order_eur"])
        print(f"{name} {kurs:g}: Kursbewegung {r:+.2%} -> Ergebnis {pnl:+.2f} EUR ({pnl / a.kapital:+.1%} des Kapitals)")
if a.stop is not None and a.ziel is not None:
    print(f"CRV 1:{abs(a.ziel - a.einstieg) / abs(a.einstieg - a.stop):.2f}")
