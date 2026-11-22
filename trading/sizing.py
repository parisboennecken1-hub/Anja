#!/usr/bin/env python3
"""Positionsgroesse, Chance-Risiko-Verhaeltnis und Knock-out-/Liquidationspreis nach den Regeln in config.json.

Beispiel (Long, ohne Hebel):
  python3 sizing.py --einstieg 122.7 --stop 113 --ziel 142 --klasse ETF
Beispiel (Long-Knock-out, Hebel 3 auf Index):
  python3 sizing.py --einstieg 7340 --stop 6900 --ziel 8200 --klasse Index --hebel 3
"""
import argparse, json, os
cfg = json.load(open(os.path.join(os.path.dirname(__file__), "config.json")))
p = argparse.ArgumentParser()
p.add_argument("--einstieg", type=float, required=True)
p.add_argument("--stop", type=float, required=True)
p.add_argument("--ziel", type=float, required=True)
p.add_argument("--klasse", required=True, help="z.B. ETF, Index, Large-Cap-Aktie, Nebenwert, Krypto, Memecoin, Hauptwaehrung, Rohstoff")
p.add_argument("--hebel", type=float, default=1.0)
p.add_argument("--kapital", type=float, default=cfg["startkapital_eur"])
p.add_argument("--short", action="store_true")
a = p.parse_args()

sgn = -1 if a.short else 1
risk_pct = abs(a.einstieg - a.stop) / a.einstieg          # Abstand zum Stop in % des Basiswerts
chance_pct = sgn * (a.ziel - a.einstieg) / a.einstieg
crv = chance_pct / risk_pct if risk_pct else float("inf")
risk_eur = a.kapital * cfg["risiko_pro_trade_pct"] / 100
kosten_pct = 2 * cfg["spread_annahme_pct"] / 100
# Positionsgroesse = Exposure im Basiswert; Kapitaleinsatz = Exposure / Hebel
exposure = risk_eur / (risk_pct + kosten_pct)
einsatz = exposure / a.hebel
max_einzel = a.kapital * cfg["max_anteil_einzelwert_pct"] / 100
fehler = []
if crv < cfg["min_crv"]: fehler.append(f"CRV {crv:.2f} < {cfg['min_crv']}")
if a.hebel > 1 and (a.hebel > cfg["max_hebel"] or a.klasse not in cfg["hebel_nur_auf"]):
    fehler.append(f"Hebel {a.hebel}x auf '{a.klasse}' nicht erlaubt (max {cfg['max_hebel']}x, nur {cfg['hebel_nur_auf']})")
if a.klasse in ("ETF", "Index") :
    max_pos = a.kapital * cfg["max_anteil_anlageklasse_pct"] / 100
else:
    max_pos = max_einzel
gekappt = min(einsatz, max_pos)
ko = a.einstieg * (1 - sgn / a.hebel) if a.hebel > 1 else None
if ko is not None and ((not a.short and ko >= a.stop) or (a.short and ko <= a.stop)):
    fehler.append(f"Knock-out ({ko:.2f}) liegt vor dem Stop ({a.stop}) - Stop wird nie erreicht")
gebuehr_anteil = 2 * cfg["gebuehr_pro_order_eur"] / gekappt * 100 if gekappt else 0
print(f"Abstand Stop: {risk_pct:.2%} | Chance bis Ziel: {chance_pct:.2%} | CRV 1:{crv:.2f}")
print(f"Erlaubtes Risiko: {risk_eur:.2f} EUR ({cfg['risiko_pro_trade_pct']}% von {a.kapital:.0f})")
print(f"Kapitaleinsatz rechnerisch: {einsatz:.2f} EUR (Exposure {exposure:.2f} EUR, Hebel {a.hebel}x)")
print(f"Kapitaleinsatz nach Positionslimit ({max_pos:.0f} EUR): {gekappt:.2f} EUR")
if ko is not None: print(f"Knock-out-/Liquidationspreis ca.: {ko:.2f} (ohne Finanzierungskosten/Emittentenpuffer - im Produktblatt pruefen)")
print(f"Ordergebuehren hin+zurueck = {gebuehr_anteil:.1f}% des Einsatzes")
if gebuehr_anteil > 2: fehler.append(f"Gebuehren {gebuehr_anteil:.1f}% des Einsatzes - Trade wirtschaftlich fragwuerdig")
print("ERGEBNIS:", "KEIN SIGNAL -> " + "; ".join(fehler) if fehler else "Regeln eingehalten")
