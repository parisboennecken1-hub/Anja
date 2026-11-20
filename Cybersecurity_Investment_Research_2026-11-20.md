# Cybersecurity-Investment-Research: 1.000 EUR, Horizont 3 und 6 Monate

**Erstellt:** Freitag, 20. November 2026, ca. 11–12 Uhr UTC (12–13 Uhr MEZ)
**Datenstichtag Kurse:** Schlusskurse vom 19.11.2026, US-Börsen (Ausnahme: Kurse europäischer und asiatischer Titel vom 20.11.2026, intraday und verzögert)
**Datenstichtag Fundamentaldaten:** jeweils letzter veröffentlichter Quartalsbericht (Zeiträume siehe Tabellen)

> Dies ist Research und keine individuelle Anlageberatung. Es gibt keine Garantie, dass irgendein Szenario eintritt. Alle Wahrscheinlichkeiten sind ausdrücklich Schätzungen.

---

## 1. Kurzfazit

**Empfehlung: Vorerst überwiegend Cash halten. Höchstens ein kleiner Teil (≤ 30–40 %) wird investiert, und zwar gestaffelt und erst nach den Quartalszahlen Anfang Dezember.**

Begründung in fünf Punkten:

1. **Es gibt keinen belastbaren Renditevorteil.** In meinen offengelegten Szenarien liegt die erwartete Nettorendite (nach ~1,5 % Kosten) der fünf Finalisten bei **−5,8 % bis +1,2 % für 3 Monate** und **−1,8 % bis +3,5 % für 6 Monate**. Dem stehen Verlustbandbreiten von −20 % bis −40 % im Bear-Fall gegenüber. Cash (Einlagezins der EZB: 2,50 %) bringt risikolos etwa +0,5 % bzw. +1,1 % (vor Steuern; die Konditionen der Banken sind nicht geprüft).
2. **Eine Wahrscheinlichkeit von mehr als 50 % für einen Gewinn ist bei Einzelaktien nicht erreichbar.** Die realisierte Volatilität der Finalisten liegt bei 55–64 % p.a. (120 Handelstage). Bei einer Annahme ohne Kursdrift liegt die modellierte Wahrscheinlichkeit einer positiven Nettorendite bei **etwa 40–46 %**. Grund sind der Volatilitätsabschlag und die Kosten. Das zweite Ziel des Auftrags („möglichst hohe Wahrscheinlichkeit positiver Gesamtrendite“) spricht also gegen Einzelaktien in diesem Zeitfenster.
3. **Das Makroumfeld ist risikoavers.** Am 20.11.2026 stand der VIX bei 28,85. Der S&P 500 (SPY) hat in einem Monat −7,4 % verloren, der Nasdaq-100 (QQQ) −11,1 %. Die Rendite 10-jähriger US-Staatsanleihen liegt bei 5,05 %. Laut Sekundärquelle hat die Fed im September 2026 die Zinsen *erhöht*. Im Oktober stimmten zwei Mitglieder für eine weitere Erhöhung. Die nächste Sitzung ist am 8./9.12.2026.
4. **Der Sektor ist gelaufen und gilt als „crowded“.** Seit Jahresbeginn: CrowdStrike +115 %, Okta +147 %, Palo Alto +102 %. Die Bewertungen preisen bei mehreren Titeln viel ein, CrowdStrike etwa mit ~41× EV/Umsatz und ~194× bereinigtem KGV. Die Kursreaktionen auf Zahlen sind extrem: Fortinet fiel am 29.10. trotz „Beat & Raise“ um rund 20 %, Zscaler hatte im Beobachtungszeitraum einen schlechtesten Tag von −31,5 %.
5. **Zwischen 24.11. und 3.12. kommen gebündelt Zahlen**, mindestens CrowdStrike, Okta, SentinelOne und vermutlich Zscaler. Danach folgt die Fed-Entscheidung. Wer vorher kauft, setzt auf Kurslücken, deren Richtung ich nicht verlässlich vorhersagen kann. Abwarten kostet wenig: etwa zwei Wochen Opportunität.

Falls trotzdem investiert werden soll: Das relativ beste Chance-Risiko-Profil haben nach meiner Einschätzung **Zscaler** (stark abgestraft, ~8× EV/Umsatz, Katalysator im Zeitfenster) und **Fortinet** (GAAP-profitabel, ~37× KGV nach dem Kurssturz, hoher Free Cashflow). Beide Einschätzungen sind ausdrücklich keine starke Überzeugung. Details zu den Modellen A/B/C stehen in Abschnitt 9. Alle drei Modelle halten viel Cash. Keines ist „ausführungsfertig“ (Begründung in Abschnitt 9).

---

## 2. Datenstand und Recherchegrenzen

### 2.1 Tatsächlich verfügbare Werkzeuge und Daten

| Quelle / Werkzeug | Status | Art der Daten |
|---|---|---|
| Websuche (Suchmaschine mit Zusammenfassungen) | verfügbar | nur zum **Finden** von Quellen; Snippets sind keine Belege |
| SEC EDGAR (8-K/6-K-Exhibits, XBRL) | **direkt geöffnet und ausgewertet** | Primärquelle, historisch (letzte Quartale) |
| Yahoo-Finance-Chart-Endpunkt (Tagesschlusskurse, 1 Jahr) | direkt abgerufen | **historisch/verzögert**, keine Echtzeitkurse |
| EZB-Referenzkurse (eurofxref-daily.xml) | direkt abgerufen | amtlich, Stand 19.11.2026 |
| EZB-Leitzinsen und Sitzungskalender | direkt abgerufen | amtlich |
| Federal Reserve: FOMC-Statement 28.10.2026 und Kalender | direkt abgerufen | amtlich |
| Investor-Relations-Seiten (CrowdStrike, Zscaler, Okta, SentinelOne, Fortinet) | **blockiert (HTTP 403)** | Termine nur über Suchergebnisse, d. h. **nicht direkt verifiziert** |
| Optionsdaten (Volumen, Open Interest, implizite Volatilität) | **NICHT VERFÜGBAR** | — |
| Short Interest (FINRA/Börse) | **NICHT VERFÜGBAR** | — |
| 13F/13D/G-Auswertung | **nicht durchgeführt** | — |
| Kostenpflichtige Datenbanken, Echtzeitkurse, Dark Pool, Market-Maker-Positionen | **nicht genutzt / nicht verfügbar** | — |
| Broker-Kosten, Spreads, Verfügbarkeit von Bruchteilsaktien | **nicht geprüft** | nur Annahmen |

Hinweis zur Arbeitsumgebung: Zu Beginn waren Originalquellen gesperrt. Für diese Recherche habe ich deshalb eine Umgebung mit freigegebenen Hosts angelegt (SEC, EZB, Fed, Kursdaten, IR-Seiten). Die IR-Seiten der Unternehmen verweigern automatisierte Abrufe trotzdem.

### 2.2 Was daraus folgt
- **Fundamentaldaten der Finalisten** stammen direkt aus den Pressemitteilungen, die als Exhibit 99.1 bei der SEC eingereicht wurden. Das ist die höchste Datenqualität in diesem Bericht.
- **Kurse** sind Schlusskurse vom 19.11.2026 (US) und damit **nicht live**. Zum Ausführungszeitpunkt weichen sie ab.
- **Termine** (Quartalszahlen) sind teils nur über Suchergebnisse belegt. Wo die Quellen sich widersprechen, steht „Termin nicht bestätigt“.
- **Kapitalfluss, Optionen, Short Interest:** Daraus lassen sich **keine** Aussagen ableiten. Ich treffe auch keine.
- **Nicht-US-Titel** (secunet, Trend Micro, AhnLab, Yubico, Wallix) habe ich nur mit Kursdaten und Sekundärquellen geprüft. Sie kommen deshalb nicht in die Finalrunde.

---

## 3. Marktüberblick

**Treiber 2026**
- **KI als Angriffs- und Verteidigungsthema.** Im März 2026 lösten Berichte über Anthropics Modell „Claude Mythos“ einen sektorweiten Ausverkauf aus. Die Angst war, KI könne Sicherheitsplattformen entwerten. Danach drehte die Erzählung: „KI-Adoption braucht Sicherheit“. CrowdStrike spricht im Q2-Bericht wörtlich vom „Mythos moment“ als Nachfragetreiber ([CRWD 8-K, 26.08.2026](https://www.sec.gov/Archives/edgar/data/1535527/000153552726000029/crwd-20260826xex991.htm)). Die Sekundärberichterstattung zum Ausverkauf habe ich nur über Suchergebnisse gesehen (z. B. [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/software-cybersecurity-stocks-tank-anthropic-121840002.html)).
- **Plattformkonsolidierung.** Palo Alto hat CyberArk übernommen (Abschluss am 11.02.2026 laut [PANW-Pressemitteilung](https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-completes-acquisition-cyberark-secure--ai-era), über Suchergebnis). Proofpoint/Thoma Bravo will Varonis übernehmen ([Varonis Q3, laut Sekundärquelle](https://finviz.com/news/414720/varonis-announces-third-quarter-2026-financial-results)).
- **Starke Fundamentaldaten bei den Marktführern:** Palo Alto meldet +39 % Umsatz im Q1 FY27, wesentlich anorganisch durch CyberArk. CrowdStrike meldet einen Rekord beim Net New ARR (+51 %), Cloudflare +39 % Umsatz.

**Risiken**
- **Bewertung und Positionierung:** extremer Kursanstieg seit dem Tief im April, sehr hohe Multiples.
- **Kurslücken bei Zahlen:** Selbst gute Zahlen werden abgestraft (Fortinet −20 % am 29.10.2026; Check Point −9 % am 02.11.2026 laut Suchergebnis).
- **Zinsen:** Fed und EZB erhöhen. EZB-Einlagesatz 2,50 % seit 16.09.2026, nach 2,25 % ab 17.06.2026 ([EZB](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html)). Fed-Zielband 3,75–4,00 % ([Fed, 28.10.2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm)). Wachstumsaktien mit langer Duration reagieren besonders empfindlich auf Zinsen.
- **Hohe Korrelation innerhalb des Sektors** (siehe Abschnitt 9). Diversifikation über mehrere Cybersecurity-Aktien reduziert das Risiko nur wenig.

---

## 4. Kandidatenuniversum (22 Titel)

Kurse: Schluss 19.11.2026 (US) bzw. 20.11.2026 intraday (Nicht-US), Quelle Yahoo-Chart-Daten. „YTD“ = seit 01.01.2026. „Vol“ = realisierte Volatilität p.a. über 120 Tage.

| # | Unternehmen (Ticker, Börse) | Segment | Kurs | YTD | Vol | Grund für Aufnahme | Erster Ausschluss-/Prüfpunkt |
|---|---|---|---|---|---|---|---|
| 1 | CrowdStrike (CRWD, Nasdaq) | Endpoint/XDR, SIEM, Cloud | 243,46 USD | +115 % | 64 % | Marktführer, Net New ARR +51 % | extreme Bewertung (~41× EV/Umsatz) → **Finalist (Kontrollfall)** |
| 2 | Palo Alto Networks (PANW, Nasdaq) | Netzwerk, SASE, Cloud, Identity | 361,73 USD | +102 % | 60 % | Q1-Beat, Guidance deutlich erhöht (18.11.) | Wachstum anorganisch aufgebläht → **Finalist** |
| 3 | Zscaler (ZS, Nasdaq) | SASE/Zero Trust | 205,71 USD | −7 % | 61 % | einziger großer Wert mit Kursrückgang, Zahlen im Zeitfenster | Wachstumsverlangsamung → **Finalist** |
| 4 | Fortinet (FTNT, Nasdaq) | Firewall/SASE | 131,46 USD | +69 % | 55 % | −24 % in 1 Monat nach Zahlen, GAAP-profitabel | Service-Wachstum schwächer → **Finalist** |
| 5 | SentinelOne (S, NYSE) | Endpoint/XDR | 24,01 USD | +64 % | 62 % | niedrigstes EV/Umsatz der Wachstumswerte, Zahlen am 03.12. | GAAP-Verluste, negativer FCF im Q2 → **Finalist** |
| 6 | Okta (OKTA, Nasdaq) | Identity | 206,85 USD | +147 % | 72 % | Narrativ „KI-Agenten-Identität“, Zahlen am 01.12. | nur ~10 % Wachstum bei ~11× EV/Umsatz; Kurs > Fundament → Ersatzkandidat |
| 7 | Cloudflare (NET, NYSE) | Edge/Zero Trust | 303,68 USD | +55 % | 62 % | +39 % Umsatz Q3 | Security nur Teil des Geschäfts; sehr hohe Bewertung |
| 8 | Check Point (CHKP, Nasdaq) | Firewall | 155,50 USD | −14 % | 39 % | günstig, Rückkäufe | Umsatz Q3 −1 % (laut Suchergebnis) |
| 9 | Rubrik (RBRK, NYSE) | Data Security/Recovery | 114,56 USD | +52 % | 67 % | Subscription-ARR +33 % (Q2 FY27, SEC) | Bewertung, Verwässerung |
| 10 | Netskope (NTSK, Nasdaq) | SASE | 24,80 USD | +47 % | 78 % | ARR +27 % (Q2 FY27, SEC) | +71 % in 3 Monaten; IPO-Lock-up-/Datenhistorie kurz |
| 11 | SailPoint (SAIL, Nasdaq) | Identity Governance | 22,04 USD | +16 % | 67 % | ARR +25 % (Q2 FY27, SEC) | PE-Eigentümer-Überhang (nicht geprüft) |
| 12 | Tenable (TENB, Nasdaq) | Vulnerability/Exposure | 44,09 USD | +94 % | 73 % | Q3 Beat & Raise (SEC) | nur ~9,5 % Wachstum |
| 13 | Qualys (QLYS, Nasdaq) | Vulnerability | 192,43 USD | +47 % | 67 % | profitabel, +11 % Wachstum (SEC) | Kursrückgang nach Q3 trotz Erhöhung |
| 14 | Rapid7 (RPD, Nasdaq) | SecOps/MDR | 15,33 USD | +7 % | 89 % | Turnaround/M&A-Fantasie | Umsatz stagniert, Datenlage schwach |
| 15 | Radware (RDWR, Nasdaq; Israel) | Application Security | 33,74 USD | +42 % | 55 % | +12 % Umsatz, Cloud-ARR +21 % (SEC 6-K) | geringe Liquidität (~19 Mio. USD/Tag) |
| 16 | Varonis (VRNS, Nasdaq) | Data Security | 49,14 USD | +53 % | 46 % | — | **Übernahmesituation** (Proofpoint) → Merger-Arbitrage, kein Sektor-Investment |
| 17 | Gen Digital (GEN, Nasdaq) | Consumer Security | 30,15 USD | +16 % | 47 % | niedrigere Bewertung | hohe Verschuldung (~8,1 Mrd. USD langfristige Schulden lt. XBRL) |
| 18 | Akamai (AKAM, Nasdaq) | Edge/App Security | 91,71 USD | +8 % | 58 % | Value | Security nur Teilsegment, −17 % in 3 Monaten |
| 19 | secunet (YSN, Xetra; DE) | Behörden-/Hochsicherheit | 186,40 EUR | +2 % | 58 % | EUR-Titel ohne FX-Risiko, öffentliche Aufträge | Q3-EBIT −19 %, Kurs −21 % in 1 Monat (Sekundärquellen); geringe Liquidität |
| 20 | Trend Micro (4704, Tokio; JP) | Endpoint/Cloud | 7.583 JPY | +18 % | 54 % | Bewertung, Rückkaufprogramm | operativer Gewinn rückläufig (Sekundärquelle); Primärquelle nicht geöffnet |
| 21 | AhnLab (053800, KOSDAQ; KR) | Endpoint (Korea) | 111.100 KRW | +84 % | 73 % | Heimatmarkt-Führer | für EU-Privatanleger schwer handelbar; Daten nicht geprüft |
| 22 | Yubico (YUBICO, Stockholm; SE) | Hardware-Authentisierung | 180,40 SEK | +147 % | 77 % | Identity-/Passkey-Thema | +100 % in 3 Monaten; nur Kursdaten geprüft |

Nicht aufgenommen: CyberArk (seit 11.02.2026 Teil von Palo Alto) und Darktrace (privat).

**Filterkriterien für die Finalisten (transparent):**
1. Liquidität: durchschnittlicher Tagesumsatz > 200 Mio. USD, damit ein Handel über deutsche Plattformen mit engen Spreads plausibel ist.
2. Vollständige Primärdaten (SEC-Exhibit) verfügbar.
3. Kein Sondersituations-Charakter (Übernahme, Delisting).
4. Mindestens ein überprüfbarer Katalysator in 0–6 Monaten.
5. Mischung aus „Momentum/Qualität“ (PANW, CRWD) und „abgestraft/Bewertung“ (ZS, FTNT, S), damit die These nicht einseitig bestätigt wird.

Okta erfüllt alle Kriterien. Ich habe es trotzdem gegen SentinelOne getauscht, weil Okta bei einem Kursplus von 147 % und nur ~10 % Umsatzwachstum stärker vom Narrativ abhängt. Das ist eine Ermessensentscheidung.

---

## 5. Vergleich der Finalisten

### 5.1 Fundamentaldaten (Primärquelle: SEC-Exhibit 99.1)

Alle Beträge in USD. „NG“ = Non-GAAP (bereinigt). GAAP- und Non-GAAP-Werte stehen getrennt.

| Kennzahl | CrowdStrike | Palo Alto | Zscaler | Fortinet | SentinelOne |
|---|---|---|---|---|---|
| Berichtszeitraum | Q2 FY27 (bis 31.07.2026) | Q1 FY27 (bis 31.10.2026) | Q4 FY26 (bis 31.07.2026) | Q3 2026 (bis 30.09.2026) | Q2 FY27 (bis 31.07.2026) |
| Veröffentlicht | 26.08.2026 | 18.11.2026 | 03.09.2026 | 28.10.2026 | 27.08.2026 |
| Umsatz Quartal | 1,47 Mrd. (+26 %) | 3,44 Mrd. (+39 %, inkl. CyberArk) | 898,2 Mio. (+25 %; ohne Red Canary ~+20 %) | 2,078 Mrd. (+20 %) | 292 Mio. (+21 %) |
| ARR / wiederkehrend | ARR 5,84 Mrd. (+25 %), Net New ARR 333 Mio. (+51 %) | NGS-ARR 9,73 Mrd. (+66 %); RPO 21,0 Mrd. (+35 %) | ARR 3,771 Mrd. (+25 %; organisch +20 %) | Billings 2,34 Mrd. (+29 %); Service +13 %, Produkt +37 % | ARR 1,218 Mrd. (+22 %) |
| Bruttomarge | Subscription GAAP 78 % / NG 81 % | NICHT EXTRAHIERT | NG-Guidance ~80 % | NG-Guidance 78–80 % (Q4) | GAAP 72 % / NG 77 % |
| Operatives Ergebnis GAAP | −33,2 Mio. | +96 Mio. (2,8 %) | −15,5 Mio. (−2 %) | Marge 34 % | Marge −31 % |
| Operatives Ergebnis NG | 371,6 Mio. (~25 %) | 1,1 Mrd. (~32 %) | 218,4 Mio. (24 %) | Marge 38 % | Marge 10 % |
| Free Cashflow | Q2: 377,4 Mio.; H1: 845,9 Mio. | Q1 bereinigt: 1,9 Mrd. (56,2 %) | Q4: 60,8 Mio. (7 %); FY26: 779,1 Mio. (23 %) | Q3: 864,8 Mio. (41,6 %) | Q2: −13,2 Mio.; H1: +17,5 Mio. |
| Cash / Investments | Cash 5,01 Mrd. | 2,594 Cash + 0,461 kurzfristig + 6,08 langfristig (XBRL, 31.10.) | 0,928 Cash + 2,546 kurzfristig | Cash 3,75 Mrd. + 0,519 langfristig (kurzfristige Investments: NICHT EXTRAHIERT) | 813 Mio. |
| Schulden | 746 Mio. langfristig | Wandelanleihe kurzfristig 1,93 Mrd. (XBRL) | Wandelanleihen 1,696 Mrd. | 497 Mio. langfristig | keine Finanzschulden ausgewiesen |
| Aktienvergütung (SBC) | H1: 674,6 Mio. = **23,6 % vom Umsatz** | Q1 SBC-bezogen: 622 Mio. = **18,1 %** | FY26: 821,9 Mio. = **24,5 %** | 9M: 231,9 Mio. = **3,9 %** | H1: 167,0 Mio. (≈ 28–30 % vom Umsatz, H1-Umsatz nicht extrahiert) |
| NRR / Retention | „gestiegen“, ohne Zahl | NICHT VERFÜGBAR | NICHT VERFÜGBAR | NICHT VERFÜGBAR | NICHT VERFÜGBAR |
| Guidance | FY27 (bis 31.01.2027): Umsatz 5,991–6,011 Mrd.; NG-EPS 1,25–1,26; Net-New-ARR-Wachstum auf ~34 % **erhöht** | FY27: Umsatz 14,52–14,57 Mrd. (+26–27 %); NG-EPS 4,26–4,30; FCF-Marge 38 %; „materiell erhöht“ | FY27: Umsatz 3,908–3,938 Mrd. (+16,6–17,5 %); ARR +16,6–17,4 %; NG-EPS 4,86–4,90; FCF-Marge 23–23,5 % | FY26 Umsatz 8,125–8,215 Mrd. (+~20 %), **erhöht**; Q4 NG-Op-Marge 35,5–37,5 % | FY27 Umsatz 1,202–1,207 Mrd., NG-EPS 0,30–0,32, **erhöht** |

Quellen: [CRWD](https://www.sec.gov/Archives/edgar/data/1535527/000153552726000029/crwd-20260826xex991.htm) · [PANW](https://www.sec.gov/Archives/edgar/data/1327567/000132756726000030/ex991q127earningsrelease.htm) · [ZS](https://www.sec.gov/Archives/edgar/data/1713683/000171368326000156/zs-07312026_991.htm) · [FTNT](https://www.sec.gov/Archives/edgar/data/1262039/000126203926000024/ftntq3-2026ex991.htm) · [S](https://www.sec.gov/Archives/edgar/data/1583708/000158370826000052/sentineloneq227exhibit991.htm). Bilanzwerte teils aus SEC-XBRL (companyfacts).

### 5.2 Bewertung (eigene Berechnung, Kurs 19.11.2026)

Methode: Marktkapitalisierung = Aktienzahl × Kurs. Als Aktienzahl dient für CRWD, PANW, ZS und FTNT die Cover-Page-Angabe des letzten 10-Q/10-K, für S die verwässerte Guidance-Aktienzahl (370 Mio.). EV = Marktkapitalisierung − Cash/Investments + Finanzschulden. Umsatz und EPS sind die Mittelwerte der Unternehmens-Guidance für das jeweils laufende Geschäftsjahr. Leasing und Minderheiten sind ignoriert.

| | CRWD | PANW | ZS | FTNT | S | (OKTA) |
|---|---|---|---|---|---|---|
| Marktkap. (Mrd. USD) | 249,3 | 297,0 | 33,5 | 96,6 | 8,9 | ~38,1 |
| EV (Mrd. USD) | 245,0 | 289,8 | 31,8 | ~92,8* | 8,1 | ~35,8 |
| EV / Umsatz lfd. GJ | **40,8×** | 19,9× | **8,1×** | 11,4× | **6,7×** | ~11,1× |
| KGV auf NG-EPS-Guidance | **~194×** | ~85× | ~42× | **~37×** | ~77× | — |
| FCF-Rendite (Guidance) | NICHT BERECHNET (keine FCF-Guidance gefunden) | ~1,9 % | ~2,7 % | NICHT BERECHNET | <1 % | — |
| Kurs in EUR (EZB 1,0992) | 221,49 € | 329,08 € | 187,15 € | 119,60 € | 21,84 € | 188,18 € |

\* Für FTNT ohne kurzfristige Investments, die ich nicht extrahiert habe. Das EV ist daher eher zu hoch angesetzt.

Wichtig: Die Non-GAAP-Multiples schließen die Aktienvergütung aus. Bei CRWD, ZS und S entspricht sie rund einem Viertel des Umsatzes oder mehr. Die „echte“ Profitabilität für Aktionäre ist dort deutlich niedriger, als die NG-KGVs nahelegen. Fortinet ist hier mit SBC ≈ 4 % klar am saubersten.

### 5.3 Kurzbeurteilung und Datenqualität

| | These pro | Stärkstes Gegenargument | Was die These widerlegt | Datenqualität |
|---|---|---|---|---|
| **CRWD** | beschleunigendes Net New ARR, Falcon-Flex-ARR +101 %, Rekord-Pipeline | ~41× EV/Umsatz und ~194× KGV preisen Perfektion ein; SBC 23,6 % | Net New ARR Q3 unter Guidance-Pfad, nachlassende Flex-Dynamik | hoch (SEC) |
| **PANW** | breite Plattform, Guidance klar erhöht, FCF-Marge 38 % | +39 % Umsatz ist größtenteils CyberArk; FY-Guidance für NGS-ARR nur +26–27 %, RPO +19–20 % → deutliche Verlangsamung ab dem Jahrestag der Übernahme (Feb. 2027); GAAP-Op-Marge 2,8 %; neue All-Stock-Akquisition (Applied Compute) verwässert | Integrationsprobleme, NGS-ARR-Ziel verfehlt | hoch (SEC, 2 Tage alt) |
| **ZS** | Bewertung im Sektorvergleich niedrig (8,1×), Kurs −27 % in 1 J., Katalysator im Zeitfenster | organisches Wachstum fällt (FY27-Guidance ~17 %); FCF-Marge Q4 nur 7 % wegen hoher Investitionen; SBC 24,5 %; schlechtester Tag im Beobachtungszeitraum −31,5 % | Q1-ARR-Wachstum < 17 % oder Senkung der FY-Guidance | hoch (SEC; Q1-Termin unbestätigt) |
| **FTNT** | GAAP-Marge 34 %, SBC niedrig, Guidance erhöht, Rückkaufprogramm 2 Mrd., Kurs −32 % vom 52-Wochen-Hoch | Service-Umsatz nur +13 %; Analysten vermuten vorgezogene Produktdeals (Firewall-Refresh-Zyklus) → Q4/2027 könnten schwächer werden | Q4-Billings unter 2,775 Mrd. oder schwache Guidance 2027 | hoch (SEC) |
| **S** | niedrigste Bewertung, +21 % Wachstum, steigende NG-Marge, mögliches M&A-Ziel (Spekulation, **nicht belegt**) | GAAP-Op-Marge −31 %, FCF im Q2 negativ, starker Wettbewerb durch CRWD/Microsoft | ARR-Wachstum < 20 % oder weitere FCF-Verluste | hoch (SEC) |

---

## 6. Kapitalfluss, Optionen und Marktstruktur

| Bereich | Status | Was sich daraus **nicht** ableiten lässt |
|---|---|---|
| Institutionelle Beteiligungen (13F/13D/G) | **NICHT AUSGEWERTET.** 13F-Meldungen sind ohnehin bis zu 45 Tage nach Quartalsende verzögert, decken nur Long-Positionen in US-Wertpapieren ab und sind keine Echtzeit-Gesamtpositionen. | keine Aussage über „Smart Money“-Zu- oder -Abflüsse |
| Short Interest | **NICHT VERFÜGBAR** (FINRA-Daten nicht abrufbar) | keine Aussage über Squeeze-Potenzial; eine hohe Short-Quote allein wäre ohnehin kein Squeeze-Signal |
| Short Volume | **NICHT VERFÜGBAR** | — |
| Optionen (Volumen, OI, implizite Volatilität) | **NICHT VERFÜGBAR** | keine Aussage über erwartete Kursbewegung bei Zahlen; keine GEX-/Dealer-Aussagen |
| Dark Pools / Orderflow | **NICHT VERFÜGBAR** | keine Aussage über Akkumulation |
| Ersatzweise beobachtet: realisierte Volatilität und Tagesumsatz | verfügbar (Yahoo, historisch) | Die realisierte Volatilität beschreibt die Vergangenheit, nicht die erwartete Bewegung. |

Liquidität (Ø Handelsvolumen der letzten 20 Tage in USD, Yahoo): CRWD ~2,2 Mrd., PANW ~2,6 Mrd., FTNT ~0,9 Mrd., ZS ~0,5 Mrd., S ~0,25 Mrd. pro Tag. Für eine Order von 1.000 EUR ist die Liquidität kein Engpass. Relevant sind die Spreads auf dem deutschen Handelsplatz außerhalb der US-Handelszeit (nicht geprüft).

---

## 7. Makro, Regulierung und Katalysatoren

### 7.1 Makro (amtliche Quellen, direkt geprüft)
- **Fed:** Zielband 3,75–4,00 %. Am 28.10.2026 wurde es gehalten (10:2; Cook und Hammack wollten +0,25 Pp.). Im Statement: „Inflation remains elevated.“ Nächste Sitzung **8./9.12.2026** mit Projektionen ([Statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm), [Kalender](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)). Laut Sekundärquelle wurde im September um 0,25 Pp. erhöht. Der Kalender bestätigt die Sitzung am 15./16.09.; den Inhalt dieser Entscheidung habe ich nicht direkt geöffnet.
- **EZB:** Einlagesatz 2,50 % seit 16.09.2026. Nächste geldpolitische Sitzung **16./17.12.2026**, danach 03./04.02.2027 und 18.03.2027 ([EZB-Kalender](https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html)).
- **EUR/USD:** EZB-Referenzkurs 1,0992 am 19.11.2026. Am 02.11. lag er noch bei 1,1216 (laut EZB-Tabelle in den Suchergebnissen). Der USD hat sich also zuletzt gegenüber dem EUR gefestigt. Für einen EUR-Anleger heißt das: Ein schwächerer Dollar würde die USD-Renditen direkt mindern. ±5 % FX in 3–6 Monaten sind ein realistischer Bereich (Annahme).
- **Marktstress:** VIX 28,85 (20.11.2026), 10-jährige US-Rendite 5,05 % (19.11.2026).

### 7.2 Regulierung und öffentliche Ausgaben
Regulierungsquellen (NIS2-Umsetzung, US-Budget für CISA, EU-Vergaben) habe ich in dieser Sitzung **nicht in Originalquellen geprüft**. Ich rechne deshalb **keinen** regulatorischen Katalysator in die Szenarien ein. Die im Auftrag geforderte Stufenunterscheidung (Ankündigung → Entwurf → Beschluss → Auftrag → Umsatz) kann ich hier nicht belegt liefern. Das einzige belegte Unternehmensbeispiel: Fortinet wurde in Microsofts „Sovereign Partner Ecosystem“ aufgenommen ([FTNT 8-K](https://www.sec.gov/Archives/edgar/data/1262039/000126203926000024/ftntq3-2026ex991.htm)). Das ist eine Partnerschaftsankündigung, kein Umsatznachweis.

### 7.3 Katalysatorenkalender (bis ca. Mai 2027)

| Datum | Ereignis | Status / Quelle | Positiv möglich | Negativ möglich | Unsicherheit |
|---|---|---|---|---|---|
| 24.11.–02.12.2026 | **Zscaler Q1 FY27** | **Termin nicht bestätigt.** Drittquellen nennen 24.11., 27.11. oder 02.12. ([Suchergebnis](https://www.globalbankingandfinance.com/markets/zs/)) | ARR-Beschleunigung, Guidance-Erhöhung | Wachstum < 17 %, FCF-Marge | hoch; Gap-Risiko (−31,5 % an einem Tag im Beobachtungszeitraum) |
| 01.12.2026, nach US-Börsenschluss | **CrowdStrike Q3 FY27** | IR-Eventseite laut Suchergebnis; Pressemitteilung vom 04.11.2026 ([IR](https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-announces-date-fiscal-third-quarter-2027-financial)), nicht direkt geöffnet | Net New ARR über Plan | jede Enttäuschung bei 41× EV/Umsatz | hoch |
| 01.12.2026, nach US-Börsenschluss | **Okta Q3 FY27** | Pressemitteilung 02.11.2026 ([über Suchergebnis](https://investingnews.com/okta-to-announce-third-quarter-fiscal-year-2027-financial-results-on-december-1-2026/)) | cRPO-Beschleunigung | Wachstum ~10 % rechtfertigt Kurs nicht | hoch |
| 03.12.2026, nach US-Börsenschluss | **SentinelOne Q3 FY27** | Pressemitteilung laut Suchergebnis ([Finviz](https://finviz.com/news/422106/sentinelone-announces-date-of-fiscal-third-quarter-2027-financial-results-conference-call-and-participation-in-upcoming-investor-conference)) | ARR/Margen über Guidance (Q3: Umsatz 309–311 Mio.) | FCF negativ, ARR-Verlangsamung | hoch |
| 08./09.12.2026 | **FOMC** mit Projektionen | **bestätigt** (Fed) | Signal „Pause“ | weitere Zinserhöhung | hoch |
| 16./17.12.2026 | **EZB-Ratssitzung** | **bestätigt** (EZB) | — | Zinserhöhung → stärkerer EUR → USD-Aktien in EUR schwächer | mittel |
| ca. Anfang Feb. 2027 | **Fortinet Q4 2026 und Ausblick 2027** | Termin nicht bestätigt (Vorjahresmuster) | Billings ≥ 2,775 Mrd., solide Guidance 2027 | Bestätigung vorgezogener Deals | hoch |
| ca. Mitte/Ende Feb. 2027 | **Palo Alto Q2 FY27** | Termin nicht bestätigt | NGS-ARR ≥ 10,20 Mrd. (Guidance) | Integrationskosten, Verwässerung durch Applied Compute | mittel |
| Feb.–Apr. 2027 | Abschluss Applied Compute (PANW) | laut Sekundärquelle „im Fiskal-Q3“, nicht in Primärquelle bestätigt | — | All-Stock = Verwässerung | mittel |
| ca. Anfang März 2027 | CrowdStrike Q4 FY27 und FY28-Guidance | Termin nicht bestätigt | — | — | hoch |
| ca. Ende Feb./Anfang März 2027 | Zscaler Q2 FY27, SentinelOne/Okta Q4 | Termin nicht bestätigt | — | — | hoch |

---

## 8. Bear-/Base-/Bull-Szenarien

### 8.1 Methode und Vorbehalte
- Die Szenariorenditen beziehen sich auf den **Aktienkurs in USD**. Die Gewichte sind **meine subjektive Einschätzung**, abgeleitet aus Bewertung, Katalysatoren, Makro und der realisierten Volatilität. Sie sind **nicht** statistisch geschätzt und **nicht** aus Optionspreisen abgeleitet (diese Daten fehlen).
- Erwartungsrendite = Σ (Szenariogewicht × Szenariorendite). Netto = abzüglich ~1,5 % Kosten für Kauf und Verkauf bei kleinen Ordergrößen (Annahme: 1 € Gebühr je Order und ~0,3 % Spread je Richtung).
- FX ist **nicht** enthalten. Zusätzlich gilt: ±5 % EUR/USD verschiebt die EUR-Rendite um rund ∓5 Pp.

### 8.2 Szenarien je Finalist

| Titel | Horizont | Bear (Gewicht) | Base (Gewicht) | Bull (Gewicht) | E[R] brutto | E[R] netto |
|---|---|---|---|---|---|---|
| CRWD | 3 M | −30 % (35 %) | 0 % (40 %) | +25 % (25 %) | −4,3 % | **−5,8 %** |
| CRWD | 6 M | −40 % (35 %) | +5 % (35 %) | +40 % (30 %) | −0,3 % | **−1,8 %** |
| PANW | 3 M | −20 % (30 %) | +3 % (45 %) | +20 % (25 %) | +0,4 % | **−1,2 %** |
| PANW | 6 M | −30 % (30 %) | +5 % (40 %) | +35 % (30 %) | +3,5 % | **+2,0 %** |
| ZS | 3 M | −25 % (30 %) | +3 % (40 %) | +30 % (30 %) | +2,7 % | **+1,2 %** |
| ZS | 6 M | −35 % (30 %) | +5 % (40 %) | +45 % (30 %) | +5,0 % | **+3,5 %** |
| FTNT | 3 M | −20 % (30 %) | +4 % (45 %) | +22 % (25 %) | +1,3 % | **−0,2 %** |
| FTNT | 6 M | −28 % (30 %) | +6 % (40 %) | +35 % (30 %) | +4,5 % | **+3,0 %** |
| S | 3 M | −30 % (35 %) | +2 % (40 %) | +35 % (25 %) | −1,0 % | **−2,5 %** |
| S | 6 M | −40 % (35 %) | +5 % (35 %) | +50 % (30 %) | +2,8 % | **+1,3 %** |
| *Cash (Referenz)* | 3 / 6 M | — | — | — | — | *ca. +0,5 % / +1,1 % (Annahme, vor Steuern)* |

Annahmen hinter den Szenarien:
- **Bear:** enttäuschende Zahlen oder Guidance, kombiniert mit weiterem Zins- und Bewertungsdruck. Die Spannweite orientiert sich an den realen Einbrüchen der letzten 12 Monate (max. Drawdown: ZS −59 %, FTNT −39 %, CRWD −33 %, PANW −29 %, S −30 %).
- **Base:** Zahlen im Rahmen der Guidance, der Markt bleibt seitwärts.
- **Bull:** „Beat & Raise“ plus Entspannung bei Zinsen und Sektor-Rotation. Bei S und ZS gehört auch eine Neubewertung dazu, bei S zusätzlich M&A-Fantasie (unbelegt).
- CRWD erhält wegen der Bewertung die schiefste Verteilung nach unten.

### 8.3 Wahrscheinlichkeitsbandbreiten

Referenzmodell: lognormal, Volatilität = realisierte 120-Tage-Volatilität, Kursdrift 0 % bis +10 % p.a., Kosten 1,5 %, ohne FX. Die Bandbreiten unten verbinden das Modell mit den Szenarien und sind bewusst grob gehalten.

| Titel | Horizont | P(Rendite > 0, netto) | P(≥ +20 %) | P(≥ +50 %) | P(≤ −20 %) |
|---|---|---|---|---|---|
| CRWD | 3 M | 38–45 % | 18–25 % | 5–8 % | 28–35 % |
| CRWD | 6 M | 37–44 % | 22–29 % | 10–15 % | 36–43 % |
| PANW | 3 M | 40–46 % | 18–24 % | 4–7 % | 25–30 % |
| PANW | 6 M | 40–46 % | 22–29 % | 9–14 % | 33–40 % |
| ZS | 3 M | 40–46 % | 20–26 % | 5–8 % | 26–32 % |
| ZS | 6 M | 40–46 % | 24–30 % | 10–14 % | 34–40 % |
| FTNT | 3 M | 41–47 % | 18–23 % | 4–6 % | 23–28 % |
| FTNT | 6 M | 41–47 % | 22–28 % | 9–13 % | 31–37 % |
| S | 3 M | 39–45 % | 19–25 % | 5–8 % | 27–33 % |
| S | 6 M | 38–45 % | 23–29 % | 10–14 % | 35–41 % |
| ETF L&G Cyber (USPY, Xetra) | 3 M | 43–50 % | 11–17 % | ~1 % | 11–15 % |
| ETF L&G Cyber (USPY, Xetra) | 6 M | 43–51 % | 18–26 % | 3–7 % | 19–24 % |

Warum die Bandbreiten unsicher sind: Die Volatilität ist nicht stabil. Kurslücken bei Zahlen machen die Verteilung „fat-tailed“, sodass extreme Bewegungen häufiger sind, als das Modell annimmt. Die Kursdrift ist unbekannt. Es gibt keine Optionsdaten. Und die Volatilität des Wechselkurses fehlt im Modell. **Kernaussage:** Bei ~60 % Volatilität ist ein Gewinn mit mehr als 50 % Wahrscheinlichkeit über 3–6 Monate nur mit einer klar positiven Drift zu erreichen. Eine solche Drift kann ich nicht belegen.

---

## 9. Drei Portfoliomodelle für 1.000 EUR

### Status: **NICHT AUSFÜHRUNGSFERTIG**
Gründe:
1. Die Kurse sind historische Schlusskurse (19.11.2026, USD) und keine handelbaren EUR-Quotes deutscher Handelsplätze.
2. Die Verfügbarkeit von Bruchteilsaktien beim jeweiligen Broker ist nicht geprüft.
3. Gebühren und Spreads sind Annahmen: 1 € je Order, ~0,3 % Spread je Richtung.

Die Stückzahlen unten sind daher **indikativ**: Betrag ÷ (USD-Schlusskurs ÷ 1,0992). Ganze Stücke sind nur bei FTNT (119,60 €) und S (21,84 €) bei den gewählten Beträgen sinnvoll möglich.

**Gemeinsame Ausführungsbedingung:** Nicht vor dem 03.12.2026 (nach den Zahlen von ZS, CRWD, OKTA und S) und möglichst nach der Fed-Sitzung am 09.12.2026 kaufen. Bei US-Titeln über deutsche Plätze möglichst während der US-Handelszeit (15:30–22:00 MEZ) handeln, weil die Spreads dann typischerweise enger sind. Das ist eine allgemeine Erfahrung, für den einzelnen Broker nicht geprüft.

### Modell A – Aggressiv, Fokus auf höhere Gewinnwahrscheinlichkeit
| Position | Ticker / Börse | Kurs (19.11., USD → EUR) | Indikative Stückzahl | Betrag | Gewicht |
|---|---|---|---|---|---|
| Fortinet | FTNT, Nasdaq (oder dt. Handelsplatz) | 131,46 USD → 119,60 € | ≈ 1,672 (Bruchteil) bzw. 1 ganzes Stück + Rest Cash | 200,00 € | 20,0 % |
| Palo Alto Networks | PANW, Nasdaq | 361,73 USD → 329,08 € | ≈ 0,608 (nur mit Bruchteilsaktien) | 200,00 € | 20,0 % |
| Kaufgebühren (Annahme) | | | | 2,00 € | 0,2 % |
| **Cash** | | | | **598,00 €** | 59,8 % |
| **Summe** | | | | **1.000,00 €** | 100 % |

Begründung: die beiden Titel mit der höchsten GAAP- bzw. FCF-Qualität und der geringsten Volatilität unter den Finalisten. Fortinet ist der am wenigsten mit den übrigen Finalisten korrelierte Titel (0,61–0,71). Die Korrelation FTNT–PANW liegt bei 0,71. Ihre Termine liegen außerhalb des Dezember-Clusters.

### Modell B – Höchste plausible erwartete Rendite
| Position | Ticker / Börse | Kurs → EUR | Indikative Stückzahl | Betrag | Gewicht |
|---|---|---|---|---|---|
| Zscaler | ZS, Nasdaq | 205,71 USD → 187,15 € | ≈ 1,603 | 300,00 € | 30,0 % |
| Fortinet | FTNT, Nasdaq | 131,46 USD → 119,60 € | ≈ 2,090 | 250,00 € | 25,0 % |
| SentinelOne | S, NYSE | 24,01 USD → 21,84 € | ≈ 6,868 (6 ganze Stücke = 131,04 €) | 150,00 € | 15,0 % |
| Kaufgebühren (Annahme) | | | | 3,00 € | 0,3 % |
| **Cash** | | | | **297,00 €** | 29,7 % |
| **Summe** | | | | **1.000,00 €** | 100 % |

### Modell C – Konzentriert, höchste (relative) Überzeugung
| Position | Ticker / Börse | Kurs → EUR | Indikative Stückzahl | Betrag | Gewicht |
|---|---|---|---|---|---|
| Zscaler | ZS, Nasdaq | 205,71 USD → 187,15 € | ≈ 2,137 (2 ganze Stücke = 374,30 €) | 400,00 € | 40,0 % |
| Kaufgebühr (Annahme) | | | | 1,00 € | 0,1 % |
| **Cash** | | | | **599,00 €** | 59,9 % |
| **Summe** | | | | **1.000,00 €** | 100 % |

„Höchste Überzeugung“ ist hier relativ gemeint. Zscaler hat in meinen Szenarien den höchsten Erwartungswert, aber die Überzeugung ist **gering**. Deshalb bleibt der Cash-Anteil hoch.

### Gewinn- und Verlustszenarien in EUR (einschließlich Gebühren und Spreads; FX neutral; Cash ohne Zinsen)

Annahme: Alle Positionen eines Portfolios landen im selben Szenario. Bei Korrelationen von 0,6–0,9 ist das realistisch.

| Portfolio | 3 M Bear | 3 M Base | 3 M Bull | E[3 M] | 6 M Bear | 6 M Base | 6 M Bull | E[6 M] |
|---|---|---|---|---|---|---|---|---|
| A | −86 € | +8 € | +77 € | −3 € | −122 € | +15 € | +133 € | +10 € |
| B | −179 € | +12 € | +186 € | ±0 € | −244 € | +27 € | +286 € | +20 € |
| C | −104 € | +8 € | +115 € | +6 € | −144 € | +15 € | +175 € | +15 € |
| *Nur Cash* | 0 € | ~+5 € | — | ~+5 € | 0 € | ~+11 € | — | ~+11 € |

**Stresstests** (alle Aktienpositionen gleichzeitig):

| Portfolio | −20 % | −40 % | −60 % | −40 % und EUR +5 % ggü. USD |
|---|---|---|---|---|
| A | −86 € | −165 € | −245 € | −177 € |
| B | −149 € | −289 € | −428 € | −309 € |
| C | −84 € | −163 € | −243 € | −175 € |

Die Erwartungswerte der Portfolios liegen bei −3 € bis +20 € über 6 Monate. Das ist **kaum mehr als Cash (~+11 €)**, bei Verlustrisiken von über −100 € bis −300 €.

### Korrelationen und Konzentration
Realisierte Korrelation der täglichen Log-Renditen, 01.06.–19.11.2026 (eigene Berechnung aus Yahoo-Kursdaten):

| | CRWD | PANW | ZS | FTNT | S | OKTA | BUG (ETF) | SPY |
|---|---|---|---|---|---|---|---|---|
| CRWD | 1 | 0,90 | 0,77 | 0,68 | 0,81 | 0,86 | 0,91 | 0,42 |
| PANW | | 1 | 0,76 | 0,71 | 0,82 | 0,79 | 0,89 | 0,38 |
| ZS | | | 1 | 0,61 | 0,79 | 0,79 | 0,86 | 0,29 |
| FTNT | | | | 1 | 0,63 | 0,64 | 0,71 | 0,33 |
| S | | | | | 1 | 0,81 | 0,92 | 0,38 |

Folgerungen: ein starker Sektorfaktor und eine hohe USD-Konzentration in allen Modellen. Fortinet ist der am wenigsten mit dem Sektor korrelierte Finalist.

### ETF als Alternative (nur teilweise geprüft)
- **L&G Cyber Security UCITS ETF**, Xetra-Ticker USPY: Kurs 42,60 € (20.11.2026, Yahoo), YTD +65 %, Volatilität 37 %.
- **iShares Digital Security UCITS ETF**, Xetra-Ticker L0CK: Kurs 11,24 €, YTD +32 %, Volatilität 26 %.
- **TER, ISIN-Zuordnung, Zusammensetzung und Replikation habe ich NICHT in Originalquellen geprüft.**
- Ein ETF senkt das Einzeltitelrisiko (Gap-Risiko bei Zahlen) deutlich, nicht aber das Sektor- und Bewertungsrisiko: BUG korreliert zu 0,86–0,92 mit den Einzeltiteln. Für das Ziel „Gewinnwahrscheinlichkeit“ ist ein ETF der Einzelaktie überlegen (Abschnitt 8.3), für das Ziel „maximale Rendite“ unterlegen.

### Steuern (separat, ohne persönliche Annahmen)
Für in Deutschland steuerpflichtige Privatanleger gilt grundsätzlich die Abgeltungsteuer: 25 % zzgl. Solidaritätszuschlag und ggf. Kirchensteuer, auf realisierte Gewinne nach Sparer-Pauschbetrag. Verluste aus Aktien sind nur mit Aktiengewinnen verrechenbar. Bei ETFs gelten die Regeln des Investmentsteuergesetzes (Teilfreistellung, Vorabpauschale). Bei US-Dividenden fällt Quellensteuer an (bei diesen Titeln kaum relevant, weil sie keine oder geringe Dividenden zahlen). Das ist eine allgemeine Darstellung und nicht in Gesetzestexten verifiziert. Die individuelle Situation bitte mit Steuerberatung klären.

---

## 10. Gegenargumente und Alternativen

**Gründe, gar nicht zu investieren**
- Der Erwartungswert ist kaum höher als bei Cash, die Verlustrisiken sind aber hoch (Abschnitte 8–9).
- Das Makroumfeld ist ungünstig: steigende Leitzinsen bei Fed und EZB, 10-jährige US-Rendite über 5 %, VIX nahe 29, Nasdaq −11 % in einem Monat.
- Zahlen werden asymmetrisch bestraft (Fortinet, Check Point, Qualys fielen trotz Guidance-Erhöhung bzw. Beat).
- Der Sektor ist nach Bernstein-Aussage „crowded“ (laut Sekundärquelle, nicht geprüft).
- Der Gewinner ist schwer zu bestimmen: Die Korrelationen sind hoch, der Ertrag hängt vom Sektor- und Makrotiming ab, nicht von der Titelauswahl.

**Stärkste Gegenargumente gegen meine eigene Vorsicht**
- Die Fundamentaldaten sind tatsächlich stark (Rekord-ARR bei CRWD, Guidance-Erhöhungen bei PANW, FTNT, S, ZS, NET). Ein Mitte Dezember beginnender Sektor-Rebound würde verpasst.
- Nach dem Ausverkauf bei ZS und FTNT könnte die schlechte Nachricht bereits im Kurs sein.

**Alternativen**
1. **Cash bzw. Tagesgeld** bis nach den Dezember-Terminen, dann neu bewerten (empfohlen).
2. **Breiter Cybersecurity-ETF** (nach Prüfung von TER und Index) statt Einzeltiteln, wenn die Gewinnwahrscheinlichkeit im Vordergrund steht.
3. **Gestaffelter Einstieg:** ein Drittel nach den Zahlen, ein Drittel nach der Fed, ein Drittel nach den Februar-Zahlen. Keine automatischen Nachkäufe bei fallenden Kursen.

---

## 11. Ein- und Ausstiegsregeln und Neubewertung

Ich nenne bewusst keine Kursziele. Belastbare Echtzeitkurse und Optionsdaten fehlen.

| | Zscaler | Fortinet | Palo Alto | SentinelOne |
|---|---|---|---|---|
| **Einstieg stützen würde** | Q1-ARR-Wachstum ≥ 17 % organisch, FY-Guidance bestätigt oder erhöht, FCF-Marge-Ziel gehalten; kein Kurssturz > 10 % nach Zahlen | Kursstabilisierung über mehrere Wochen ohne neue Tiefs; Bestätigung, dass die Q4-Billings im Rahmen liegen (vorab nur indirekt möglich) | Kurs hält das Niveau nach den Zahlen; keine negativen Integrationsmeldungen | Q3-ARR-Wachstum ≥ 20 %, positiver FCF |
| **Nicht einsteigen, wenn** | Guidance gesenkt; FCF-Marge-Ziel aufgegeben | Senkung der Billings-Guidance; Management bestätigt vorgezogene Deals | All-Stock-Akquisitionen erhöhen die Verwässerung deutlich | ARR-Wachstum < 18 % oder Barmittel sinken deutlich |
| **Neubewertung erforderlich bei** | jedem Quartalsbericht; Wechsel im Management oder Vertrieb | Q4-Zahlen (Feb. 2027) | Q2-Zahlen (Feb. 2027), Abschluss Applied Compute | Q3/Q4-Zahlen; Übernahmegerüchte |
| **Fundamentaler Ausstieg (These widerlegt)** | ARR-Wachstum < 15 % | Service-Umsatzwachstum < 10 % | NGS-ARR-Guidance gesenkt | zwei Quartale negativer FCF in Folge |
| **Technischer Stop (Vorschlag)** | Schlusskurs ≥ 25 % unter dem Einstieg | ≥ 20 % unter dem Einstieg | ≥ 20 % unter dem Einstieg | ≥ 25 % unter dem Einstieg |
| **Zeitliche Überprüfung** | spätestens nach 3 Monaten (ca. Ende Feb. 2027) und nach jedem Quartalsbericht | ebenso | ebenso | ebenso |
| **Teilgewinnmitnahme (Vorschlag)** | bei +25 %: ⅓ verkaufen; bei +40 %: weiteres ⅓ | ebenso | ebenso | ebenso |

Wichtig:
- **Stop-Orders schützen nicht vor Kurslücken.** Fällt ein Titel nachbörslich um 20–30 % (wie Fortinet am 29.10. oder Zscaler mit −31,5 % an einem Tag), wird die Stop-Order zum nächsten verfügbaren, deutlich schlechteren Kurs ausgeführt.
- **Keine automatischen Nachkäufe** bei fallenden Kursen.
- Die Stop-Abstände orientieren sich an der Volatilität der Titel. Engere Stops würden bei ~60 % Volatilität häufig ohne fundamentalen Grund auslösen.

---

## 12. Abschließende Beurteilung

**Gesamturteil: Vorerst Cash.** Zum Recherchezeitpunkt gibt es keinen überzeugenden, belegbaren Investmentvorteil in Cybersecurity-Einzelaktien für 3–6 Monate. Die Fundamentaldaten sind gut, aber weitgehend eingepreist. Das Makro- und Terminumfeld spricht eher für Abwarten. Wer trotzdem investieren will, sollte höchstens 30–40 % einsetzen (Modell A oder C), gestaffelt und erst nach dem 9.12.2026.

**Neue Informationen, die eine Neubewertung auslösen würden**
1. Zahlen von Zscaler, CrowdStrike, Okta und SentinelOne (24.11.–03.12.2026), vor allem ARR-Wachstum und FCF.
2. Die Fed-Entscheidung und die Projektionen am 09.12.2026 sowie die EZB am 17.12.2026.
3. Ein Rückgang des VIX unter ~20 und eine Stabilisierung des Nasdaq.
4. Eine deutliche Kurskorrektur des Sektors (z. B. −15–20 %) ohne fundamentale Verschlechterung: Das würde die Bewertungsfrage verändern.
5. Verfügbare Daten zu Optionen (implizite Volatilität vor den Zahlen) und Short Interest. Damit ließen sich die Wahrscheinlichkeitsbandbreiten besser kalibrieren.
6. Belegte Übernahmeangebote (z. B. für SentinelOne, Rapid7 oder Tenable). Eine Spekulation darauf habe ich bewusst nicht eingepreist.

---

## 13. Qualitätskontrolle

| Prüfpunkt | Ergebnis |
|---|---|
| Datum, Geschäftsjahr, Berichtszeitraum | geprüft; abweichende Geschäftsjahre (CRWD/S/OKTA bis 31.01., PANW bis 31.07., ZS bis 31.07.) sind je Kennzahl angegeben |
| Unternehmensangaben aus Originalquellen | ja, für alle fünf Finalisten (SEC-Exhibits); Universumsdaten teils sekundär (gekennzeichnet) |
| Kurse gekennzeichnet | ja, historische Schlusskurse vom 19.11.2026, keine Echtzeitkurse |
| EUR-Umrechnung | EZB-Referenzkurs 1,0992 (19.11.2026) |
| 13F | nicht ausgewertet, Verzögerung erläutert |
| Short Interest und Short Volume getrennt | ja, beides NICHT VERFÜGBAR |
| Optionen und Market Maker nicht überinterpretiert | ja, keine Aussagen |
| Politische Vorschläge vs. geltende Regeln | Regulierung nicht geprüft, daher kein Katalysator eingerechnet |
| Gegenargumente sichtbar | ja (Abschnitte 5.3 und 10) |
| Portfolios exakt 1.000 € | A: 200+200+2+598; B: 300+250+150+3+297; C: 400+1+599 → jeweils 1.000,00 € |
| Erfundene Zahlen? | Nein. Szenariogewichte und Kostenannahmen sind als Annahmen gekennzeichnet. |

---

## 14. Quellenregister

### Primärquellen (direkt geöffnet)
| Quelle | Veröffentlicht | Daten-/Berichtsstichtag |
|---|---|---|
| [Palo Alto Networks, Exhibit 99.1 zum 8-K: Q1 FY2027](https://www.sec.gov/Archives/edgar/data/1327567/000132756726000030/ex991q127earningsrelease.htm) | 18.11.2026 | 31.10.2026 |
| [CrowdStrike, Exhibit 99.1 zum 8-K: Q2 FY2027](https://www.sec.gov/Archives/edgar/data/1535527/000153552726000029/crwd-20260826xex991.htm) | 26.08.2026 | 31.07.2026 |
| [Zscaler, Exhibit 99.1 zum 8-K: Q4/FY2026](https://www.sec.gov/Archives/edgar/data/1713683/000171368326000156/zs-07312026_991.htm) | 03.09.2026 | 31.07.2026 |
| [Fortinet, Exhibit 99.1 zum 8-K: Q3 2026](https://www.sec.gov/Archives/edgar/data/1262039/000126203926000024/ftntq3-2026ex991.htm) | 28.10.2026 | 30.09.2026 |
| [SentinelOne, Exhibit 99.1 zum 8-K: Q2 FY2027](https://www.sec.gov/Archives/edgar/data/1583708/000158370826000052/sentineloneq227exhibit991.htm) | 27.08.2026 | 31.07.2026 |
| [Okta, Exhibit 99.1 zum 8-K: Q2 FY2027](https://www.sec.gov/Archives/edgar/data/1660134/000166013426000068/okta-7312026_ex991.htm) | 26.08.2026 | 31.07.2026 |
| [Cloudflare, Exhibit 99.1 zum 8-K: Q3 2026](https://www.sec.gov/Archives/edgar/data/1477333/000147733326000060/q326exhibit991.htm) | 05.11.2026 | 30.09.2026 |
| SEC-8-K/6-K-Exhibits Rubrik (27.08.), Netskope (02.09.), SailPoint (09.09.), Tenable (28.10.), Radware (28.10.), Qualys (09.11.), Check Point (02.11.), über [EDGAR](https://www.sec.gov/edgar/search/) | wie angegeben | jeweils letztes Quartal |
| SEC XBRL companyfacts (Aktienzahlen, Cash, Schulden) über [data.sec.gov](https://data.sec.gov/api/xbrl/companyfacts/) | abgerufen 20.11.2026 | letztes 10-Q/10-K |
| [Federal Reserve: FOMC-Statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm) | 28.10.2026 | — |
| [Federal Reserve: FOMC-Kalender](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) | abgerufen 20.11.2026 | — |
| [EZB: Referenzkurse (täglich)](https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml) | 19.11.2026 | 19.11.2026 |
| [EZB: Leitzinsen](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html) | abgerufen 20.11.2026 | gültig seit 16.09.2026 |
| [EZB: Sitzungskalender](https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html) | abgerufen 20.11.2026 | — |

### Markt- und Kursdaten (historisch, direkt abgerufen)
| Quelle | Stichtag |
|---|---|
| Yahoo-Finance-Chart-Endpunkt (`query1.finance.yahoo.com/v8/finance/chart`), Tagesschlusskurse 1 Jahr: Grundlage für Kurse, Renditen, Volatilität, Korrelationen, Drawdowns, Ø-Umsatz, VIX, 10-jährige Rendite | 19.11.2026 (US-Schluss) bzw. 20.11.2026 (Europa/Asien intraday, verzögert) |

### Sekundärquellen (nur über Suchergebnisse, **nicht** direkt geöffnet; nur ergänzend verwendet)
| Quelle | Datum | Verwendet für |
|---|---|---|
| [CrowdStrike IR: Termin Q3 FY27](https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-announces-date-fiscal-third-quarter-2027-financial) | 04.11.2026 | Termin 01.12.2026 |
| [Investing News: Okta-Termin Q3 FY27](https://investingnews.com/okta-to-announce-third-quarter-fiscal-year-2027-financial-results-on-december-1-2026/) | 02.11.2026 | Termin 01.12.2026 |
| [Finviz: SentinelOne-Termin Q3 FY27](https://finviz.com/news/422106/sentinelone-announces-date-of-fiscal-third-quarter-2027-financial-results-conference-call-and-participation-in-upcoming-investor-conference) | Nov. 2026 | Termin 03.12.2026 |
| [Global Banking & Finance: ZS](https://www.globalbankingandfinance.com/markets/zs/) | Nov. 2026 | ZS-Termin (unbestätigt) |
| [Trefis: Fortinet −20,1 % am 29.10.2026](https://www.trefis.com/stock/ftnt/articles/621368/what-just-happened-to-fortinet-stock/2026-10-29) | 29.10.2026 | Kursreaktion und Begründung |
| [Finviz: Fortinet-Aktie −25 % nachbörslich](https://finviz.com/news/411709/fortinet-shares-fall-more-than-25-as-product-revenue-growth-slows-to-37) | 28./29.10.2026 | Kursreaktion |
| [Palo Alto: Abschluss der CyberArk-Übernahme](https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-completes-acquisition-cyberark-secure--ai-era) | 11.02.2026 | CyberArk-Status |
| [Yahoo Finance: Software-/Cyber-Ausverkauf wegen KI-Sorgen](https://finance.yahoo.com/sectors/technology/articles/software-cybersecurity-stocks-tank-anthropic-121840002.html) | März 2026 | Marktüberblick |
| [Barchart: Okta-Rally](https://www.barchart.com/story/news/4396475/okta-stock-has-more-than-doubled-in-2026-ai-agents-could-drive-the-next-leg-higher) | 2026 | Okta-Kontext |
| [Finviz: Varonis Q3 2026 / Proofpoint-Übernahme](https://finviz.com/news/414720/varonis-announces-third-quarter-2026-financial-results) | 03.11.2026 | Ausschluss Varonis |
| [Morningstar/PR Newswire: Check Point Q3 2026](https://www.morningstar.com/news/pr-newswire/20261102dc86338/check-point-software-reports-2026-third-quarter-financial-results) und [StockTwits](https://stocktwits.com/news-articles/markets/equity/chkp-stock-tanks-as-q3-revenue-misses-estimates-ceo-says-recovery-is-taking-longer-than-anticipated/cNG9DdBR9PR) | 02.11.2026 | Universum |
| [goldesel.de: secunet Q3 2026](https://goldesel.de/aktien/news/secunet-sec-networks-aktie-umsatz-wachst-quartalsgewinn-sinkt-ausblick-bestatigt) | 12.11.2026 | Universum |
| [uanalyze.com.tw: Trend Micro Q3 2026](https://uanalyze.com.tw/articles/4081759238) | 12.11.2026 | Universum |
| [Axios: KI-Sorgen treiben Cyber-Aktien](https://www.axios.com/2026/09/15/ai-cybersecurity-stocks) | 15.09.2026 | Marktüberblick |
| [Yahoo Finance: Cyber-Aktien steigen nach PANW-Prognose](https://finance.yahoo.com/markets/stocks/articles/cybersecurity-stocks-rise-investors-bet-215200509.html) | 19.11.2026 | Marktkontext |
