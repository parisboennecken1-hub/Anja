# Trading-Framework: Werkzeuge (Modus maximales Risiko)

| Datei | Zweck |
|---|---|
| `config.json` | Modus **maximales Risiko**: voller Kapitaleinsatz pro Trade, Hebel unbegrenzt, keine Limits; nur Gebühren, Steuer, Benchmark |
| `sizing.py` | Einsatz, Exposure, Knock-out-/Liquidationspreis, Ergebnis bei Stop/Ziel (keine Regel-Checks) |
| `insider_scan.py` | SEC-Form-4-Scan auf Insider-Käufe mit eigenem Geld (Code P) in einem Datumsfenster |
| `insider_cluster.py` | verdichtet den Scan zu Cluster-Käufen und prüft Liquidität und Historie |
| `cot_positionierung.py` | CFTC-COT-Positionierung (3-Jahres-Index) für Index-, FX-, Anleihe-, Krypto- und Rohstoff-Futures |
| `cot_backtest.py` | prüft, ob COT-Extreme historisch einen Vorteil hatten (Ergebnis 2010–2026: nein bei Rohstoffen) |
| `journal.csv` | Journal aller Signale (auch nicht gehandelter), Modus `papier` oder `echt` |
| `auswertung.py` | Trefferquote, Ø Gewinn/Verlust, Erwartungswert, max. Drawdown nach Klasse und Quelle; Benchmark MSCI World |
| `Signalbericht_YYYY-MM-DD.md` | Bericht je Lauf |

**Voraussetzung:** Netzwerkzugriff auf `www.sec.gov`, `data.sec.gov`, `www.cftc.gov`, `publicreporting.cftc.gov` und `query1.finance.yahoo.com`. Die Cloud-Umgebung „Anja Finanzrecherche“ hat diese Hosts freigeschaltet.

**Wöchentlicher Ablauf**
```bash
python3 insider_scan.py 2026-11-23 2026-11-27   # ~10-15 Min pro Woche
python3 insider_cluster.py
python3 cot_positionierung.py
python3 sizing.py --einstieg 54677 --stop 48000 --ziel 70000 --hebel 10
python3 auswertung.py
```
