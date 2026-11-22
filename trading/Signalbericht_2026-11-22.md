# Signalbericht nach Multi-Asset-Framework, Stand 22.11.2026

**Erstellt:** 22.11.2026, ca. 11 Uhr UTC · **Modus:** Papierhandel (Woche 1 von 4–8) · **Startkapital:** 1.000 EUR
**Kurse:** Schlusskurse Freitag, 20.11.2026 (USA), historisch und verzögert · **EUR/USD:** 1,0970 (20.11.2026)

> Keine Anlageberatung, keine Gewinngarantie. Alle Signale sind **Papier-Trades**. Echtgeld ist laut Framework erst zulässig, wenn der Erwartungswert positiv ist und den MSCI World schlägt.

---

## 0. Kurzfazit

1. **Es gibt 3 Papier-Signale, alle Aktien long:** Accenture (ACN), AutoNation (AN), LKQ (LKQ). Grundlage sind Cluster-Käufe von Insidern mit eigenem Geld (SEC Form 4) plus laufende Aktienrückkäufe. **Keines davon erreicht „Handeln“.** Beide Quellen stammen vom selben Akteur (dem Management) und sind daher nur eingeschränkt unabhängig.
2. **Krypto, Rohstoffe, Forex, Memecoins: kein Signal.** On-Chain- und Optionsdaten sind nicht verfügbar. Das COT-Signal hatte in meinem Backtest 2010–2026 bei Gold, Silber und Öl **keinen Vorteil**.
3. **Strukturproblem:** Deine Regeln (1 % Risiko, max. 5 % je Einzelwert) erlauben bei 1.000 € nur Positionen von **≤ 50 €**. 1 € Ordergebühr kostet dann **4 % pro Runde**. Einzeltitel-Trading ist so im Echtgeld nicht wirtschaftlich. Lösungsvorschläge stehen in Abschnitt 6.

---

## 1. Datenzugriff und Zuverlässigkeits-Scores der Quellen

| Quelle | Zugriff | Score (0–100) | Begründung |
|---|---|---|---|
| **SEC Form 4: Insiderkäufe (Code P)** | ✓ direkt, alle 26.800 Meldungen vom 27.10.–20.11.2026 gescannt | **55** | Primärquelle, meldepflichtig innerhalb von 2 Geschäftstagen. Die Forschung findet für Insider-*Käufe* (v. a. Cluster, CEO/CFO) überdurchschnittliche Folgerenditen, mit Abschwächung in den letzten Jahrzehnten. **Hier nicht selbst nachgetestet.** Störfaktoren: IPO-Käufe, Mitarbeiter-Kaufpläne. |
| **Aktienrückkäufe (SEC-XBRL)** | ✓ direkt | **45** | belegt, aber quartalsweise verzögert. Kommt vom selben Akteur wie die Insiderkäufe und ist daher **nicht voll unabhängig**. |
| **Makro: VIX-Regime** | ✓ direkt (Yahoo, Fed, EZB) | **60** | 36 Jahre Daten. Bei VIX ≥ 30 lagen S&P 500 und Nasdaq-100 nach 6 Monaten in 82–89 % der Fälle im Plus (siehe Analyse 2). Aber nur ~25 unabhängige Episoden. Aktueller VIX (20.11.): **35,89**. |
| **COT-Report (CFTC)** | ✓ direkt, Stichtag 17.11.2026 (veröffentlicht 20.11.) | **20** | eigener Backtest 2010–2026 (Tabelle in Abschnitt 2): Extreme Commercials-Positionen hatten bei Gold, Silber und Öl **keinen** Vorhersagewert, bei Silber sogar einen negativen. |
| 13F großer Fonds | möglich, nicht ausgewertet | 15 | bis zu 45 Tage verzögert, nur Long-Positionen. Für 3–6 Monate kaum verwertbar. |
| Optionsflow (Volumen ≫ OI, Blocktrades) | **NICHT VERFÜGBAR** | — | keine Datenquelle zugänglich |
| On-Chain-Wallets (≥ 50 Trades/90 T, realisierter Gewinn) | **NICHT VERFÜGBAR** | — | bräuchte Explorer-API mit Schlüssel und Wallet-Labeling (z. B. Arkham/Nansen); nicht reproduzierbar ohne Kosten |
| BaFin Directors' Dealings | **NICHT VERFÜGBAR** (Host blockiert) | — | kann freigeschaltet werden |
| Wirtschaftskalender | teilweise | 70 | bestätigt: FOMC 08./09.12.2026, EZB 16./17.12.2026. CPI-Termine **nicht** verifiziert. |

---

## 2. Ergebnisse je Anlageklasse

### 2.1 COT-Positionierung (CFTC, Stichtag 17.11.2026)

Der COT-Index ist der 3-Jahres-Perzentilwert der Nettoposition: 0 = so bärisch wie nie in 3 Jahren, 100 = so bullisch wie nie.

| Markt | Leveraged Funds / Managed Money | Asset Manager | Dealer / Commercials | Deutung |
|---|---|---|---|---|
| E-mini S&P 500 | 86 | 52 | 32 | neutral |
| Nasdaq-100 | 73 | 74 | 18 | neutral |
| Euro FX | **1** | **1** | 98 | Spekulanten extrem bärisch auf den Euro |
| 10Y T-Note | 4 | **100** | 10 | Basis-Trade (Arbitrage), **nicht** richtungsweisend |
| Bitcoin (CME) | 100 | 2 | 30 | Leveraged Funds so wenig short wie nie (Basis-Trade wird aufgelöst), mehrdeutig |
| Gold | 37 | — | **100** | Commercials so wenig short wie nie |
| Silber | 18 | — | **97** | ebenso |
| WTI-Öl | 18 | — | **96** | ebenso |

**Backtest 2010–2026** (eigene Berechnung; Einstieg am Montag nach der Veröffentlichung; Futures-Kurse über Yahoo):

| Signal | 3 M: P(+) | 3 M: Median | 6 M: P(+) | 6 M: Median | Basisrate 6 M |
|---|---|---|---|---|---|
| Gold, Commercials-Index ≥ 90 | 51 % | +0,2 % | 50 % | −0,1 % | 64 % / +4,1 % |
| Silber, Commercials-Index ≥ 90 | 51 % | +0,5 % | **36 %** | −4,7 % | 53 % / +1,3 % |
| WTI, Commercials-Index ≥ 90 | 57 % | +1,3 % | 46 % | −1,5 % | 51 % / +0,7 % |
| EUR/USD, Lev-Funds-Index ≤ 10 (~5 Episoden) | 37 % | −1,4 % | 65 % | +1,9 % | 47 % / −0,5 % |

→ **Kein Rohstoff- und kein Forex-Signal.** Das klassische Lehrbuchsignal hat in diesem Zeitraum nicht funktioniert.

### 2.2 Insiderkäufe (SEC Form 4, 27.10.–20.11.2026)

- Ausgangsmenge: 4.885 Kaufzeilen. Davon 98 Cluster mit mindestens 2 Organmitgliedern und mindestens 200.000 USD. Davon bestanden 31 den Liquiditätsfilter (Ø Tagesumsatz ≥ 20 Mio. USD, Kurs ≥ 5 USD, ≥ 120 Handelstage Historie).
- Manuell aussortiert:
  - **TSM:** ~30 Käufe zu identischen 70,50 $, typisch für einen Mitarbeiter-Kaufplan
  - **UPBD:** Kurs seit dem ersten Insiderkauf schon +50 % → „zu spät“
  - **DOX:** XBRL-Fundamentaldaten veraltet (20-F 2025)
  - **CAT:** XBRL-Gewinndaten fehlerhaft, außerdem Kurs am 52-Wochen-Tief, −52 % vom Hoch
  - **BA, COHR:** kein laufender Rückkauf, damit nur eine Quelle
  - **DKNG, MTDR:** Gewinn- bzw. FCF-Daten unklar, Rückkauf gering
  - **IPO-Käufe:** z. B. WWB, ASPE, BBTX, alle ohnehin durch den Liquiditäts- und Historienfilter gefallen

---

## 3. Signale im geforderten Format

| Produkt | Klasse | Quellen + Score | Check | Einstieg / Stop / Ziel (USD) | CRV | Hebel / KO | Risiken | Empfehlung |
|---|---|---|---|---|---|---|---|---|
| **Accenture (ACN, NYSE)** | Aktie | Form 4: CEO Julie Sweet kaufte am 26.10.2026 12.200 Aktien für ~3,0 Mio. USD, dazu Director P. Price 0,2 Mio. USD (55). Rückkäufe 7,52 Mrd. USD im GJ bis 31.08.2026, ~5 % der Marktkapitalisierung (45). | ✓ Liquidität (ADV ~1,3 Mrd. USD). KGV ~17 (XBRL-Näherung). FCF-Rendite ~8 %. Cash 12,8 Mrd. vs. Schulden 10,0 Mrd. USD. ⚠ Q1-Zahlen vermutlich Mitte/Ende Dezember (**nicht bestätigt**). | 221,17 / **196,87** (−11,0 %; 2,5 × ATR) / **269,78** (+22,0 %), unter dem 52-W-Hoch von 288,54 | **1 : 2,0** | 1× / – | KI-Disruption bei IT-Dienstleistern; Kursreaktion auf Zahlen; USD-Risiko. **„Zu spät“?** Nein: Kurs liegt 10,5 % *unter* dem Insider-Kaufkurs. | **Beobachten / Papierhandel** |
| **AutoNation (AN, NYSE)** | Aktie | Form 4: CEO M. Manley ~1,03 Mio., CFO T. Szlosek 4 × 100.000, General Counsel und Director, 02.–06.11.2026 (55). Rückkauf 0,63 Mrd. USD in 9 M 2026, ~11 % der Marktkapitalisierung (45). | ✓ Liquidität (ADV ~99 Mio. USD). KGV ~8,6. ⚠ ausgewiesener FCF negativ (Händler-Fahrzeugfinanzierung verzerrt). ⚠ Schulden 1,5 Mrd. USD ohne Floorplan. | 175,48 / **159,24** (−9,3 %) / **207,96** (+18,5 %), unter dem 52-W-Hoch von 229,98 | **1 : 2,0** | 1× / – | Zinsen und Autokredite; Konsumschwäche; der Stop liegt nahe am 52-W-Tief (153,01). Gelaufen: −4,4 % seit den Insiderkäufen. | **Beobachten / Papierhandel** |
| **LKQ Corp (LKQ, Nasdaq)** | Aktie | Form 4: 4 Directors, ~1,29 Mio. USD, 30.10.–18.11.2026 (50). Rückkauf 0,08 Mrd. USD in 9 M 2026, ~1,7 % der Marktkapitalisierung (30). | ✓ Liquidität (ADV ~96 Mio. USD). KGV ~7,7. FCF-Rendite ~23 % (XBRL-Näherung). ⚠ Kurs unter SMA50 und SMA200, klarer Abwärtstrend. | 18,51 / **16,52** (−10,8 %, unter dem 52-W-Tief von 17,10) / **22,50** (+21,5 %) | **1 : 2,0** | 1× / – | fallendes Messer; kein CEO/CFO unter den Käufern. Gelaufen: −4,0 %. | **Beobachten** (schwächstes Signal) |
| Gold / Silber / Öl | Rohstoffe | nur COT (20) | ✗ nur 1 Quelle; Backtest ohne Vorteil | — | — | — | — | **Meiden** (kein Signal) |
| EUR/USD long | Forex | nur COT (20) | ✗ nur 1 Quelle; n ≈ 5 Episoden | — | — | — | — | **Kein Signal** |
| Bitcoin / Ether | Krypto | CME-COT mehrdeutig; On-Chain **nicht verfügbar** | ✗ | — | — | — | — | **Kein Signal** |
| Memecoins | Krypto | keine | ✗ Mint/Freeze, Liquiditätssperre, Honeypot ohne On-Chain-Zugang nicht prüfbar; Hebel laut Regel verboten | — | — | — | — | **Meiden** |
| MSCI World ETF | ETF | VIX-Regime (60); sonst keine zweite Quelle (COT neutral) | ✓ | — | — | — | — | **Kein Trading-Signal.** Bleibt als langfristiger Kern aus Analyse 2 sinnvoll (Benchmark). |

**Positionsgröße nach deinen Regeln** (Ergebnis von `sizing.py`):
- ACN: Das Risikobudget von 10 € würde 86 € Einsatz erlauben, das Einzelwertlimit kappt auf **50 €**, also ≈ 0,25 Aktien (Bruchteilsaktien nötig).
- Die Gebühren betragen dann 4 % pro Runde. Das Tool meldet deshalb für Echtgeld „Trade wirtschaftlich fragwürdig“. Im Papierhandel wird das so mitgerechnet.

---

## 4. Ablauf Papierhandel (Woche 1–8)

1. **Montag, 23.11.2026:** Papier-Einstieg zum Eröffnungskurs für S001–S003 in `journal.csv` eintragen (`einstieg_datum`, `einstieg_kurs`).
2. **Täglich:** Prüfen, ob Stop oder Ziel *auf Schlusskursbasis* erreicht wurden. Bei Ziel die Hälfte schließen und für den Rest einen Trailing Stop auf Einstand setzen.
3. **Wöchentlich (freitags):**
   - `python3 insider_scan.py <Datum−7> <Datum>`, dann `python3 insider_cluster.py`
   - `python3 cot_positionierung.py`
   - neue Signale nur nach Check und Regeln
   - `python3 auswertung.py` (Trefferquote, Ø Gewinn/Verlust, Erwartungswert, Drawdown, Benchmark)
4. **Termine:** FOMC 08./09.12.; EZB 16./17.12.; Accenture-Zahlen (Termin selbst prüfen). Vor den Zahlen entscheiden: Position halten oder nicht. Gaps können den Stop überspringen.
5. **Abbruchregeln:** Nach 50 Signalen mit Erwartungswert ≤ 0 gilt die Strategie als gescheitert (`auswertung.py` meldet das automatisch). Tages- und Monatslimits (3 % / 10 %) gelten auch im Papierhandel.

---

## 5. Was dieses Framework nicht leisten kann (ehrliche Grenzen)

- **Zwei Quellen sind hier faktisch eine:** Insiderkauf und Rückkauf gehen beide vom Management aus. Echte Unabhängigkeit hätten Optionsflow oder 13F, aber diese Daten fehlen bzw. sind zu verzögert.
- **Die Insider-Wirkung ist hier nicht selbst getestet.** Ein sauberer Backtest bräuchte mehrere Jahre Form-4-Historie, also Hunderttausende Abrufe. Das ist machbar, aber aufwendig.
- **Stops und Ziele** sind regelbasiert (2,5 × ATR, CRV 2) und keine Prognose von Kurszielen.
- **Krypto-Smart-Money (Wallet-Tracking)** ist ohne kostenpflichtige Daten nicht seriös umsetzbar. Gratis-„Copy-Wallet“-Listen in sozialen Medien sind oft selbst Teil von Pump-Schemata.

---

## 6. Empfohlene Anpassungen der Platzhalter

| Parameter | Dein Rahmen | Problem bei 1.000 € | Vorschlag |
|---|---|---|---|
| Risiko pro Trade | 1–2 % | 10–20 € Risiko | 1 % beibehalten |
| Max. je Einzelwert | 5 % | ≤ 50 € Position, 4 % Gebühren pro Runde | **15 %** (150 €; Gebühren ~1,3 %) oder Broker ohne Ordergebühr bzw. Sparplan-Ausführung nutzen |
| Max. je Anlageklasse | 20 % | Aktien max. 200 € | Cash/Geldmarkt ausnehmen (so in `config.json` gesetzt) |
| Hebel | 2–5× | — | **max. 3×** und nur auf Indizes, Large Caps, Hauptwährungen (gesetzt) |
| Mindestvolumen | offen | — | Aktien ≥ 20 Mio. USD/Tag, ETFs ≥ 1 Mio. €/Tag, Krypto ≥ 50 Mio. USD/Tag (gesetzt) |

Alle Werte stehen in `trading/config.json` und lassen sich dort ändern.

---

## 7. Quellen (alle am 22.11.2026 abgerufen)

- **SEC EDGAR:** tägliche Form-Indizes (`/Archives/edgar/daily-index/2026/QTR4/form.YYYYMMDD.idx`; 11.11.2026 Feiertag, kein Index) und die einzelnen Form-4-XML-Dateien.
  - Beispiel ACN, CEO-Kauf: https://www.sec.gov/Archives/edgar/data/1467373/000148763026000022/
  - Beispiel AN, CEO-Kauf: https://www.sec.gov/Archives/edgar/data/350698/000151899226000004/
  - Beispiel LKQ, Director-Kauf: https://www.sec.gov/Archives/edgar/data/1065696/000121465926014549/
- **SEC XBRL companyfacts** (data.sec.gov): Rückkäufe (`PaymentsForRepurchaseOfCommonStock`), Gewinn, Cashflow, Schulden, Aktienzahl
- **CFTC Public Reporting:** Traders in Financial Futures (gpe5-46if) und Disaggregated (72hh-3qpy), Stichtag 17.11.2026; Wochenbericht https://www.cftc.gov/dea/newcot/FinFutWk.txt
- **Yahoo-Finance-Chart-Endpunkt:** Kurse, Volumen, ATR, Futures-Historie (GC=F, SI=F, CL=F, EURUSD=X, ^GSPC, ^VIX)
- **Federal Reserve und EZB:** Sitzungskalender (abgerufen 20.11.2026)
