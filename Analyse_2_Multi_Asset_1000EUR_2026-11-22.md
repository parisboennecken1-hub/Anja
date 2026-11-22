# Analyse 2: Multi-Asset-Strategien für 1.000 EUR (Krypto, Memecoins, Aktien, ETFs, Hebel, Derivate)

**Erstellt:** 22.11.2026 (Sonntag), ca. 10 Uhr UTC
**Datenstichtag:** Krypto 22.11.2026, ca. 09:34 UTC (24/7-Handel, verzögert); Aktien/ETFs/VIX Schlusskurse Freitag, 20.11.2026
**Horizont:** 3 und 6 Monate · **Startkapital:** 1.000 EUR · **Ziel:** möglichst hohe Gewinnwahrscheinlichkeit, in der Realität umsetzbar

> Research, keine Anlageberatung. Alle Wahrscheinlichkeiten sind **historische Häufigkeiten**, keine Prognosen. Die Vergangenheit kann sich anders wiederholen oder gar nicht.

---

## 1. Kernaussage vorab

**„Hohe Gewinnwahrscheinlichkeit“ und „schnell viel Geld“ schließen sich aus.** Das zeigen die Daten klar. Je mehr Hebel oder je spekulativer der Coin, desto *niedriger* ist die Wahrscheinlichkeit, nach 3–6 Monaten im Plus zu sein. Die Chance auf einen großen Gewinn steigt dabei, das Risiko eines Totalverlusts aber auch.

Historische Wahrscheinlichkeit, nach **6 Monaten im Plus** zu sein (eigene Auswertung der Kursdaten, Details in Abschnitt 4):

| Rang | Umsetzung | P(Gewinn) 6 M | typischer Ausgang (Median) | schlechte 5 % der Fälle |
|---|---|---|---|---|
| 1 | Geldmarkt-ETF / Tagesgeld | ~100 % (bei positivem Zins) | +1 % | ~0 % |
| 2 | **Breiter Aktien-ETF, gekauft bei VIX ≥ 30** (heute 35,9) | **82–91 %** | +12 bis +23 % | −10 bis −12 % |
| 3 | Nasdaq-100 mit 2× Hebel (ETF, täglich angepasst), gekauft bei VIX ≥ 30 | 76–85 % | +25 bis +41 % | −24 bis −30 % |
| 4 | Bitcoin nach Crash (−40 % vom Hoch und −20 % im Monat; das ist heute der Fall) | 3 M: 66 % · 6 M: 50 % | 3 M: +11 % · 6 M: −1 % | 3 M: −18 % (p10) · 6 M: −38 % (p10) |
| 5 | Krypto-Knock-out 5×–10× | 31–50 % | — | Knock-out (Totalverlust) in 37–66 % der Fälle |
| 6 | Memecoins (DOGE, SHIB, PEPE, BONK, WIF) | **29–47 %** | −4 % bis −42 % | −59 % bis −78 % |

**Mein Vorschlag:** Plan A (Abschnitt 5). Kern ist ein breiter Aktien-ETF, gestaffelt gekauft, während der VIX erhöht ist, dazu ein Cash-Puffer und ein kleiner gehebelter Teil. Memecoins und hoch gehebelte Krypto-Produkte haben die *schlechteste* Gewinnwahrscheinlichkeit aller geprüften Optionen.

---

## 2. Marktlage am Stichtag (Daten direkt abgerufen)

| Markt | Stand | 1 Monat | 3 Monate | 1 Jahr | Abstand zum Allzeithoch |
|---|---|---|---|---|---|
| VIX (Angstindex) | **35,89** (20.11.) | +89 % | +132 % | | |
| MSCI World ETF (EUNL, EUR) | 122,72 € | −5,6 % | −3,0 % | +12,3 % | −7,2 % |
| S&P 500 ETF (SXR8, EUR) | 694,06 € | −6,0 % | −2,0 % | +12,0 % | −8,0 % |
| Nasdaq-100 ETF (EXXT, EUR) | 227,05 € | −10,2 % | −6,6 % | +9,5 % | −16,0 % |
| Nasdaq-100 2× (LQQ, Paris, EUR) | 7,41 € | −21,9 % | −20,0 % | +3,1 % | −32,5 % |
| Bitcoin (EUR) | 54.677 € | −24,5 % | −17,9 % | −25,6 % | **−48,7 %** |
| Ethereum (EUR) | 1.541 € | −27,6 % | −26,9 % | −35,9 % | −62,9 % |
| Solana (EUR) | 63,66 € | −30,6 % | −22,1 % | −42,5 % | −75,0 % |
| Dogecoin (EUR) | 0,0500 € | −28,6 % | −37,4 % | −58,9 % | −91,1 % |
| PEPE / BONK / WIF / TRUMP (USD) | | −31 % bis −48 % | | −16 % bis −86 % | **−87 % bis −98 %** |
| Gold ETC (4GLD, EUR) | 103,78 € | −10,8 % | −19,0 % | −8,4 % | −28,7 % |
| Geldmarkt (XEON, €STR) | 150,85 € | +0,2 % | +0,6 % | +2,1 % | Allzeithoch |
| EUR/USD | 1,0970 | −2,2 % | −4,4 % | −5,5 % | |

Quelle: Yahoo-Finance-Chart-Daten, abgerufen am 22.11.2026.

Leitzinsen (amtliche Quellen, am 20.11.2026 geprüft): Die Fed hält 3,75–4,00 % (nächste Sitzung 8./9.12.). Der EZB-Einlagesatz liegt bei 2,50 % (nächste Sitzung 16./17.12.).

Hintergrund laut Sekundärquellen (nicht in Originalquellen geprüft):
- Starker Rückgang bei KI- und Chip-Aktien im November ([Kitco, 05.11.2026](https://www.kitco.com/news/off-the-wire/2026-11-05/wall-street-fear-gauge-jumps-most-liberation-day-ai-trade-stumbles); [24/7 Wall St, 06.11.2026](https://247wallst.com/investing/2026/11/06/wall-streets-fear-gauge-just-had-its-third-biggest-jump-since-1990/)).
- Krypto: ETF-Abflüsse und Liquidationen gehebelter Positionen ([Crypto Briefing](https://cryptobriefing.com/bitcoin-falls-23-november-2026-bear-market/)).

---

## 3. Methode (damit alles nachbaubar ist)

1. **Daten:** tägliche Schlusskurse über den Yahoo-Finance-Chart-Endpunkt. Zeiträume: 10 Jahre (Krypto ab Verfügbarkeit, Memecoins ab 2021–2025) und für S&P 500, Nasdaq-100 und VIX seit 1990.
2. **Rollierende Renditen:** Für jeden Handelstag wird die Rendite 3 Monate (63 Handelstage bzw. 91 Kalendertage bei Krypto) und 6 Monate später berechnet. Daraus ergeben sich der Anteil positiver Fälle, der Median sowie das 5- und 10-%-Quantil.
3. **Bedingte Auswertung („Regime“):**
   - Aktien: nur Tage mit VIX ≥ 30.
   - Krypto: nur Tage mit einem Abstand von mindestens −40 % zum bisherigen Hoch und einem 30-Tage-Verlust von mindestens −20 %.
4. **Hebel-Simulation:** Täglich angepasster Hebel (wie bei Hebel-ETFs/Faktor-Zertifikaten) mit Finanzierungskosten von 5 % p.a. auf den Hebelanteil plus 0,6 % Produktkosten.
5. **Knock-out-Simulation:** Die Knock-out-Schwelle liegt bei Einstieg × (1 − 1/Hebel). Gezählt wird, wie oft der Kurs sie innerhalb des Horizonts berührt.

**Grenzen:**
- Überlappende Zeitfenster: 736 VIX-Tage seit 1990 entsprechen nur rund 25 unabhängigen Episoden.
- Indexdaten ohne Dividenden, in USD und ohne Wechselkurseffekt.
- **Survivorship Bias bei Memecoins:** Ausgewertet sind nur Coins, die noch existieren. Tausende tote Coins fehlen, die echten Werte sind schlechter.
- Krypto-Historie ist kurz.
- Keine Optionsdaten, keine Funding-Rates, kein Orderbuch.

---

## 4. Ergebnisse im Detail

### 4.1 Ohne Bedingung (gesamte verfügbare Historie, ohne Kosten)

| Anlage | 3 M: P(+) | 3 M: Median | 3 M: p5 | 6 M: P(+) | 6 M: Median | 6 M: p5 | 6 M: P(≤ −50 %) |
|---|---|---|---|---|---|---|---|
| MSCI World (EUR, 2016–26) | 74 % | +4 % | −8 % | 77 % | +7 % | −8 % | 0 % |
| Nasdaq-100 (EUR, 2016–26) | 73 % | +6 % | −11 % | 79 % | +11 % | −10 % | 0 % |
| Nasdaq-100 2× (LQQ, real) | 71 % | +10 % | −24 % | 77 % | +19 % | −24 % | 0 % |
| Gold (EUR) | 66 % | +3 % | −7 % | 70 % | +6 % | −9 % | 0 % |
| Bitcoin | 58 % | +7 % | −40 % | 61 % | +16 % | −46 % | 3 % |
| Ethereum | 53 % | +5 % | −51 % | 56 % | +8 % | −65 % | 13 % |
| Solana | 54 % | +5 % | −57 % | 55 % | +19 % | −68 % | 16 % |
| XRP | 48 % | −2 % | −46 % | 46 % | −4 % | −54 % | 8 % |
| Dogecoin | 43 % | −6 % | −50 % | 47 % | −4 % | −59 % | 11 % |
| Shiba Inu | 34 % | −10 % | −52 % | 29 % | −20 % | −59 % | 14 % |
| PEPE | 36 % | ±0 % | −60 % | 41 % | ±0 % | −64 % | 22 % |
| BONK | 41 % | ±0 % | −65 % | 41 % | −25 % | −71 % | 32 % |
| WIF | 38 % | −16 % | −78 % | 29 % | −42 % | −78 % | 45 % |
| Bitcoin 2× (simuliert) | 52 % | +3 % | −69 % | 51 % | +2 % | −77 % | 23 % |
| Bitcoin 3× (simuliert) | 49 % | −4 % | −91 % | 47 % | −14 % | −100 % | 40 % |
| Bitcoin 5× (simuliert) | 44 % | −16 % | −99 % | 43 % | −41 % | −100 % | 48 % |

### 4.2 Bedingt auf die heutige Lage

**Aktien bei VIX ≥ 30** (S&P 500 und Nasdaq-100, 1990–2026, 736 Tage, ~25 Episoden u. a. 2001/02, 2008/09, 2011, 2020, 2022, 2025):

| Anlage | 3 M: P(+) | 3 M: Median | 3 M: p5 | 6 M: P(+) | 6 M: Median | 6 M: p5 | 6 M: p1 |
|---|---|---|---|---|---|---|---|
| S&P 500 1× | 77 % | +8 % | −14 % | **82 %** | +15 % | −10 % | −32 % |
| Nasdaq-100 1× | 82 % | +12 % | −11 % | **89 %** | +23 % | −12 % | −27 % |
| S&P 500 2× (sim.) | 73 % | +13 % | −31 % | 76 % | +25 % | −24 % | −62 % |
| Nasdaq-100 2× (sim.) | 78 % | +21 % | −25 % | 85 % | +41 % | −30 % | −56 % |
| Nasdaq-100 3× (sim.) | 74 % | +26 % | −41 % | 79 % | +57 % | −49 % | −78 % |
| MSCI World in EUR (2016–26) | 85 % | +7 % | p10 −2 % | **91 %** | +12 % | p10 ±0 % | |

**Krypto nach Crash** (−40 % vom Hoch und −20 % in 30 Tagen; das trifft am Stichtag auf BTC, ETH und SOL zu):

| Anlage | 3 M: P(+) | 3 M: Median | 3 M: p10 | 6 M: P(+) | 6 M: Median | 6 M: p10 |
|---|---|---|---|---|---|---|
| Bitcoin (~15 Episoden) | 66 % | +11 % | −18 % | 50 % | −1 % | −38 % |
| Ethereum (~19) | 61 % | +11 % | −51 % | 52 % | +5 % | −58 % |
| Solana (~20) | 63 % | +13 % | −42 % | 57 % | +23 % | −65 % |

**Knock-out-Zertifikate long** (Anteil Ausknockungen = Totalverlust):

| Basiswert | Hebel 3× | Hebel 5× | Hebel 10× |
|---|---|---|---|
| Bitcoin, 3 M / 6 M | 14 % / 28 % | 37 % / 50 % | 57 % / 66 % |
| Nasdaq-100, 3 M / 6 M | 0 % / 0 % | 4 % / 8 % | 18 % / 25 % |
| S&P 500, 3 M / 6 M | 0 % / 0 % | 4 % / 8 % | 10 % / 19 % |

**Interpretation:**
1. Die höchste belegte Gewinnwahrscheinlichkeit *mit nennenswertem Ertrag* hat ein **breiter Aktien-ETF, gekauft in Phasen hoher Angst**: 82–91 % nach 6 Monaten. Selbst dort lagen die schlechtesten 1 % der Fälle bei rund −30 %, etwa in Phasen wie 2008.
2. Moderater Hebel (2×) auf den Nasdaq hob historisch den Median deutlich bei nur leicht geringerer Gewinnwahrscheinlichkeit, aber mit doppelt so tiefen Verlusten im Ernstfall.
3. **Bitcoin nach einem Crash** ist auf 3 Monate leicht positiv (66 %), auf 6 Monate ein Münzwurf.
4. **Memecoins und Krypto-Hebel verlieren meistens.** Das ist kein Zufall: Hoher Hebel bei sehr volatilen Werten frisst die Rendite auf (Volatilitätsabschlag).

### 4.3 Weitere Optionen, geprüft und verworfen

| Idee | Warum nicht (oder nur bedingt) |
|---|---|
| CFDs | Anbieter müssen in der EU ausweisen, wie viele Privatkunden Geld verlieren; typischerweise sind das deutlich über 50 %. Die Zahl habe ich in dieser Sitzung nicht verifiziert. Hebel plus Finanzierungskosten plus Spread sind bei 3–6 Monaten strukturell ungünstig. |
| Optionen verkaufen (z. B. Puts) | hohe *Trefferquote*, aber seltene große Verluste (negativer Schiefe-Effekt). Mit 1.000 € kaum umsetzbar (Margin, Kontraktgrößen, Termingeschäftsfähigkeit). Keine Optionsdaten verfügbar. |
| Krypto-Futures/Perpetuals (Binance, Bybit u. Ä.) | Funding-Kosten, Liquidationsrisiko wie beim Knock-out; Plattform- und Regulierungsrisiko für EU-Kunden |
| Neue Memecoins / Presales / „Pump“-Coins | keine verwertbaren Daten; Betrugsquote hoch; Survivorship Bias macht selbst die obigen Zahlen zu optimistisch |
| Krypto-Staking / „Yield“ | Rendite meist in Coins, also Kursrisiko; Plattform-Pleiten (2022) als Warnsignal |
| Gold | P(+) 70 % historisch, aktuell im Abwärtstrend (−19 % in 3 M); mögliche Beimischung, kein Renditetreiber |
| Einzelaktien Cybersecurity | siehe Analyse 1: P(+) ~40–46 % wegen hoher Volatilität |

---

## 5. Konkrete Umsetzungspläne mit 1.000 EUR

**Für alle Pläne gilt:**
- Die Kurse sind Schlusskurse vom 20.11.2026 und nicht live. Vor dem Kauf aktuellen Kurs, ISIN und Handelsplatz beim eigenen Broker prüfen.
- Die ISINs stammen aus meinem Wissen und sind **nicht** in dieser Sitzung verifiziert. Bitte vor jeder Order im Broker abgleichen.
- Gebührenannahme: 1 € pro Order (typisch für Neobroker). Spreads je nach Handelszeit 0,05–0,5 %.

### Plan A: „Hohe Gewinnwahrscheinlichkeit“ (empfohlen)

| Baustein | Produkt (Ticker, ISIN, Börse) | Betrag | Wann kaufen |
|---|---|---|---|
| Kern | iShares Core MSCI World (EUNL, IE00B4L5Y983, Xetra/Tradegate) | 500 € | 3 Tranchen à ~166 €: (1) jetzt bei VIX > 30, (2) nach FOMC am 09.12., (3) Anfang Januar |
| Rendite-Satellit | Amundi Nasdaq-100 Daily 2× Leveraged (LQQ, FR0010342592, Euronext Paris; deutsche Handelbarkeit prüfen) | 150 € | 2 Tranchen: jetzt und nach dem 09.12. |
| Puffer | Xtrackers EUR Overnight Rate Swap (XEON, LU0290358497) oder Tagesgeld | 345 € | sofort; dient als Reserve, *nicht* für Nachkäufe in fallende Kurse |
| Ordergebühren | 5 Kauforders à 1 € | 5 € | |
| **Summe** | | **1.000 €** | |

Erwartbare Bandbreite nach 6 Monaten. Das sind grobe Werte aus den historischen Verteilungen (Abschnitt 4.2), keine Prognose. Der Median ist mit Abschlägen gegenüber den historischen Werten konservativ angesetzt:

| Szenario | MSCI World 500 € | Nasdaq 2× 150 € | Puffer 345 € | Gebühren | **Gesamt** |
|---|---|---|---|---|---|
| Typisch (Median, konservativ) | +60 € (+12 %) | +30 € (+20 %) | +4 € | −5 € | **≈ +90 €** |
| Schlecht (schlechteste 5 %) | −50 € (−10 %) | −45 € (−30 %) | +4 € | −5 € | **≈ −95 €** |
| Extrem (Crash wie 2008, schlechteste 1 %) | −160 € (−32 %) | −85 € (−56 %) | +4 € | −5 € | **≈ −245 €** |

Historische Gewinnwahrscheinlichkeit des Gesamtplans: grob **75–85 %** nach 6 Monaten (geschätzt aus den Einzelwerten bei hoher Korrelation von Kern und Satellit). Ein zusätzliches Wechselkursrisiko entsteht durch den hohen USD-Anteil im MSCI World und Nasdaq.

### Plan B: „Mehr Rendite, mittlere Wahrscheinlichkeit“

| Baustein | Produkt | Betrag |
|---|---|---|
| Nasdaq-100 1× | iShares Nasdaq-100 (EXXT, DE000A0F5UF5) | 450 € |
| Nasdaq-100 2× | LQQ (FR0010342592) | 300 € |
| Bitcoin | Spot über eine regulierte Börse bzw. Broker (MiCA-lizenziert) oder physisch besichertes BTC-ETP; Produkt selbst wählen und prüfen | 150 € |
| Puffer | Geldmarkt/Tagesgeld | 96 € |
| Gebühren | 4 Orders | 4 € |
| **Summe** | | **1.000 €** |

Grobe Bandbreite nach 6 Monaten: typisch **≈ +100 bis +130 €**, schlechteste 5 % **≈ −190 €**, Extremfall **≈ −360 €**. Historische Gewinnwahrscheinlichkeit grob **65–80 %**.

### Plan C: „Spekulation / Lotterie“ (nicht empfohlen)

Falls unbedingt Memecoins oder Hebel gewünscht sind: **maximal 50 €** und gedanklich sofort abschreiben. Historisch verlor ein Memecoin-Kauf in 53–71 % der Fälle Geld (6 M); bei 11–45 % der Startzeitpunkte halbierte sich der Wert mindestens. Ein 10×-Krypto-Knock-out wurde in 57–66 % der Fälle ausgeknockt. Ein Plan aus 1.000 € Memecoins hätte im Median Verlust gemacht.

---

## 6. Regeln für die Umsetzung

**Einstieg**
- Gestaffelt kaufen (Tranchen wie oben), keine Market-Order außerhalb der Haupthandelszeit. Limit-Orders etwa 0,3 % über dem Briefkurs setzen.
- Bei Krypto: nur über in der EU lizenzierte Anbieter (MiCA). Keine Kredit- oder Hebelfunktion aktivieren.

**Was die Strategie widerlegt (dann neu bewerten)**
- Der VIX bleibt über mehrere Wochen über 40 und die Indizes fallen weiter (Muster 2008). Ab −20 % auf den Kern-ETF: anhalten, neu analysieren, **nicht** blind nachkaufen.
- Die Fed erhöht am 09.12. die Zinsen kräftig und signalisiert weitere Erhöhungen.

**Ausstieg / Gewinnmitnahme**
- Nasdaq-2×-Satellit: bei +30 % die Hälfte verkaufen. Bei −30 % vom Einstieg aussteigen (technischer Stop). Achtung: Kurslücken können zu deutlich schlechteren Ausführungen führen.
- Kern-ETF: kein Stop (bei breiten ETFs lösen Stops historisch oft unnötig aus); Überprüfung nach 3 und 6 Monaten.
- Bitcoin-Anteil: Überprüfung nach 3 Monaten. Historisch war das 3-Monats-Fenster nach Crashs besser als das 6-Monats-Fenster.

**Zeitliche Überprüfung:** 09.12.2026 (Fed), 17.12.2026 (EZB), ~22.02.2027 (3 Monate), ~22.05.2027 (6 Monate).

---

## 7. Steuern und Recht (allgemein, nicht in dieser Sitzung verifiziert)

- **ETFs/Aktien:** Abgeltungsteuer 25 % plus Solidaritätszuschlag (ggf. Kirchensteuer) nach Sparer-Pauschbetrag; Teilfreistellung bei Aktien-ETFs.
- **Krypto (Privatvermögen):** Gewinne sind bei Haltedauer **unter 1 Jahr** mit dem persönlichen Steuersatz steuerpflichtig (Freigrenze für private Veräußerungsgeschäfte; aktuelle Höhe prüfen). Nach über 1 Jahr Haltedauer sind sie in Deutschland grundsätzlich steuerfrei. Bei einem Horizont von 3–6 Monaten greift die Steuerfreiheit **nicht**.
- **Hebelprodukte/Derivate:** Sonderregeln für Termingeschäfte möglich; Broker verlangt ggf. eine Erklärung zur Termingeschäftsfähigkeit.
- Individuelle Situation mit Steuerberatung klären.

---

## 8. Ehrliche Grenzen dieser Analyse

- Historische Häufigkeiten aus rund 25 Angst-Episoden sind keine Garantie. Ein Szenario wie 2008 (der VIX blieb monatelang über 40) liegt in den schlechtesten 1–5 % der Fälle und wäre heute ebenso möglich.
- Nicht verfügbar bzw. nicht geprüft: Live-Kurse, Optionsdaten, Krypto-Funding-Rates, Gebührenmodell und Produktangebot des konkreten Brokers, ISINs, TER/Kosten der Produkte.
- Hintergründe zur Marktlage stammen aus Sekundärquellen.
- Daten: Yahoo-Finance-Chart-Endpunkt (abgerufen 22.11.2026); Fed- und EZB-Webseiten (abgerufen 20.11.2026).
