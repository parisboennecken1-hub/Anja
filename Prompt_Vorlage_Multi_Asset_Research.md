# Prompt-Vorlage: Multi-Asset-Research für [KAPITAL] EUR

Kopiere alles zwischen den Linien in eine neue Sitzung. Passe nur die Werte in [ECKIGEN KLAMMERN] an.
Tipp: In Claude Code die Umgebung **„Anja Finanzrecherche“** wählen. Dort sind SEC, EZB, Fed und Kursdaten freigeschaltet.

---

# MULTI-ASSET-RESEARCH: [KAPITAL, z. B. 1.000] EUR · HORIZONT 3 UND 6 MONATE

## Auftrag
Finde mit **aktuellen Daten zum heutigen Datum** die Umsetzungen mit der höchsten belegbaren Wahrscheinlichkeit, nach 3 bzw. 6 Monaten im Gewinn zu sein. Gesucht ist ein sinnvoller, nachvollziehbarer Ertrag. Erlaubt sind alle Anlageklassen: Geldmarkt/Tagesgeld, Anleihen, Aktien-ETFs, Einzelaktien, Gold, Bitcoin und andere Kryptowährungen, Memecoins, Hebel-ETFs/Faktor-Zertifikate, Knock-outs, Optionen, Futures, CFDs. Cash ist zulässig. Ich lebe in [LAND, z. B. Deutschland] und handle über [BROKER, z. B. Trade Republic / Scalable / unbekannt]. Risikobereitschaft: [z. B. hoch, aber Totalverlust des Gesamtkapitals vermeiden].

Arbeite ergebnisoffen. Bestätige keine Wunschthese. Wenn die Daten sagen „Hebel oder Memecoins senken die Gewinnwahrscheinlichkeit“, dann schreib genau das.

## 1. Datenregeln (verbindlich)
1. Nenne zu Beginn: heutiges Datum mit Zeitzone, Datenstichtag je Anlageklasse (Krypto 24/7, Börsen letzter Schlusskurs), welche Werkzeuge und Datenquellen tatsächlich funktionieren und welche nicht.
2. Lade Kursdaten selbst (z. B. Yahoo-Finance-Chart-Endpunkt, EZB-Referenzkurse, Fed/EZB-Webseiten, SEC EDGAR). Kennzeichne jede Zahl als live, verzögert oder historisch.
3. Suchmaschinen-Snippets sind keine Belege. Prüfe Originalquellen, sonst kennzeichne die Angabe als „Sekundärquelle, nicht verifiziert“.
4. Erfinde nichts: keine ISINs, Gebühren, Kurse, Wahrscheinlichkeiten oder Datenzugriffe. Fehlt etwas, schreibe „NICHT VERFÜGBAR“.
5. Wenn Originalquellen blockiert sind, sag es sofort und schlage vor, welche Hosts freigeschaltet werden müssen.

## 2. Pflicht-Analysen (mit Code nachrechnen, Skript-Logik offenlegen)
A. **Marktlage am Stichtag:** VIX, MSCI World, S&P 500, Nasdaq-100, EUR/USD, Leitzinsen (Fed, EZB) mit nächsten Sitzungsterminen, Gold, Bitcoin, Ethereum, Solana, 5 große Memecoins. Je Wert: 1 M, 3 M, 1 J, Abstand zum Allzeithoch.

B. **Historische Basisraten** (rollierend, möglichst lange Historie, für Indizes ab 1990): für jede Anlage P(Rendite > 0), Median, 5-%- und 1-%-Quantil, P(≤ −20 %), P(≤ −50 %), P(≥ +50 %) für 3 und 6 Monate. Kosten und Wechselkurseffekt berücksichtigen.

C. **Regime-Analyse:** Welche historischen Situationen ähneln der heutigen (z. B. VIX-Niveau, Drawdown vom Hoch, 30-Tage-Momentum, Zinsumfeld)? Berechne die Basisraten nur für diese Situationen. Nenne die Zahl der unabhängigen Episoden, nicht nur die Zahl der Tage.

D. **Hebel und Derivate simulieren:** täglich angepasster Hebel (2×, 3×, 5×) mit Finanzierungskosten; Knock-out-Wahrscheinlichkeit (3×, 5×, 10×) für Indizes und Bitcoin. Optionen und CFDs nur bewerten, wenn Daten vorliegen; sonst begründet einordnen.

E. **Memecoins/Altcoins:** Basisraten berechnen und den Survivorship Bias ausdrücklich benennen.

F. **Rangliste:** alle Optionen nach P(Gewinn) **und** Median **und** Verlust im schlechten Fall (p5/p1) sortieren. Erkläre den Zielkonflikt zwischen Trefferquote und Ertrag.

## 3. Umsetzungspläne (realitätsnah, exakt [KAPITAL] EUR)
Erstelle 2–3 Pläne: (A) höchste Gewinnwahrscheinlichkeit, (B) mehr Rendite bei mittlerer Wahrscheinlichkeit, (C) optional Spekulation mit kleinem Maximalbetrag.

Je Plan:
- Produkt mit Name, Ticker, **ISIN** (als „verifiziert“ oder „bitte im Broker prüfen“ markieren), Handelsplatz, Betrag in EUR. Gebühren einrechnen; die Summe muss exakt [KAPITAL] EUR ergeben.
- Kaufzeitpunkte und Tranchen, gekoppelt an konkrete Termine (Fed, EZB, Quartalszahlen) und Bedingungen (z. B. VIX-Niveau).
- Ordertyp (Limit/Market), sinnvolle Handelszeit.
- Szenario-Tabelle in EUR für 3 und 6 Monate: typisch (Median), schlecht (p5), extrem (p1/Crash). Dazu die geschätzte Gesamt-Gewinnwahrscheinlichkeit mit Herleitung.
- Ausstiegsregeln: Gewinnmitnahme, technischer Stop (mit Hinweis auf Kurslücken), fundamentale Widerlegung, zeitliche Überprüfung. Keine automatischen Nachkäufe in fallende Kurse.
- Wechselkursrisiko und Korrelation zwischen den Bausteinen.

## 4. Steuern und Recht (separat, allgemein)
Steuerliche Behandlung je Produktklasse in [LAND] (ETFs, Krypto mit Haltefrist, Termingeschäfte/Derivate), Anforderungen des Brokers (z. B. Termingeschäftsfähigkeit), Anbieterregulierung (bei Krypto z. B. MiCA). Keine persönliche Steuersituation unterstellen.

## 5. Vergleich mit dem Vorbericht (falls vorhanden)
Lies die Dateien im Repository (z. B. `Analyse_2_Multi_Asset_1000EUR_*.md`). Zeige, was sich seit dem letzten Stichtag geändert hat (Kurse, VIX, Zinsen, Regime) und ob die Pläne angepasst werden müssen.

## 6. Ausgabe
- Bericht auf Deutsch als Markdown-Datei im Repository, Dateiname mit Datum. Committen und auf den Arbeits-Branch pushen.
- Struktur: 1) Kurzfazit mit Empfehlung, 2) Datenstand und Grenzen, 3) Marktlage, 4) Basisraten, 5) Regime-Analyse, 6) Hebel/Derivate, 7) Rangliste, 8) Umsetzungspläne, 9) Regeln, 10) Steuern/Recht, 11) Quellen mit Datum.
- Schlusskontrolle: Summen exakt, keine erfundenen Zahlen, Prognosen klar von historischen Häufigkeiten getrennt.

Dies ist Research, keine Anlageberatung. Ehrliche Unsicherheit ist wichtiger als scheinbare Präzision.

---
