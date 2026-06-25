# Struktur-Guide für Supportartikel

Verbindliche Vorgabe, was in einen DialogShift-Supportartikel gehört. Die Bausteinlisten sind **abschließend**: Was nicht aufgeführt ist, gehört nicht hinein.

## Grundprinzipien

- **Du-Form**, knapp, auf den Punkt.
- **Eine Sache pro Artikel** – nur das, was der Leser zum Erledigen braucht.
- **Ziel ist Selbsthilfe.** Kein Aufruf, sich an uns oder den Support zu wenden. Kein Anbieten von Hilfe.
- Kein Marketing und kein Anbieterporträt ("Über das Unternehmen", Gründungsjahr, Produktwerbung).
- Keine Zukunftsversprechen ("coming soon", "ab Q1 ...").
- Keine externen Link-Sammlungen / "weiterführenden" Links.
- Fakten müssen stimmen (gegen Produkt/Code/interne Doku geprüft).

## Bausteine eines Supportartikels (abschließend)

1. **Frontmatter** – `title` und `description` (ein Satz: was der Leser erreicht).
2. **Einleitung** – 1–2 Sätze: worum es geht und für wen.
3. **Inhaltliche Abschnitte** – fokussiert auf das Thema: Schritte, Felder oder Anleitung.
4. **Voraussetzungen** – optional, nur wenn es echte gibt.

How-to- und Checklisten-Artikel folgen derselben Struktur; die "Inhaltlichen Abschnitte" sind dann die einzelnen Schritte.

## Zusätzliche Bausteine eines Integrationsartikels (abschließend)

1. **Einleitung** – was die Integration leistet (Datenfluss und welche Funktionen/Agenten sie ermöglicht).
2. **Voraussetzungen** – z. B. Kunde des Anbieters, Beauftragung, Client-ID.
3. **Buchungsfunktionen** – nur bei Booking-Engine-Integrationen: eine kurze Tabelle mit Checkout, Zahlungslink, Zahlungsvarianten, Rabattcodes und benötigten Gastdaten.
4. **Integration aktivieren** – wer initiiert, ob das Hotel die Integration selbst in der DialogShift App aktivieren kann oder Customer Success die Engine aktivieren muss, welche Credentials wo eingetragen werden.
5. **Konfiguration** – nur falls es Felder/Einstellungen gibt: die konkreten Felder.

## Komponenten

- Erlaubt: `<Note>` und `<Info>` sparsam; Tabellen oder Listen für Felder und Werte.
- Nicht erwünscht: dekorative `<Card>`, `<CardGroup>`, `<Tip>` und `<Steps>` als Schmuck.
