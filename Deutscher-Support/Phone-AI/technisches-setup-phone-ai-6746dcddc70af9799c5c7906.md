---
categories:
- Phone AI
category_ids: []
collection: Deutscher Support
collection_id: 60c7b284fa6e7d669e9d5f8e
created_at: '2024-11-27T08:48:29Z'
created_by: 754830
helpful_count: null
id: 6746dcddc70af9799c5c7906
keywords: []
not_helpful_count: null
popularity: 5.0
site: DialogShift Support Deutsch
slug: technisches-setup-phone-ai
status: published
title: Technische Voraussetzungen für das Setup der Phone AI
updated_at: '2025-07-01T11:31:43Z'
updated_by: 560533
view_count: 634
---

Im Folgenden findest du die Voraussetzungen und Anforderungen, die erfüllt sein müssen, um die Phone AI erfolgreich einzurichten:
    
    
    ## Anmeldung als SIP-Telefon
    
    - Nahtlose Integration: Die Phone AI wird wie ein reguläres SIP-Endgerät in die bestehende Telefonanlage eingebunden.
    - Weiterleitungen der Phone AI an das Hotel Team sind kostenfrei
    - beste Sprachqualität
    - Die Telefonanlage muss SIP-fähig sein und erlauben, dass sich die Phone AI über das Internet anmeldet
    - Ein Sip-Konto für die Phone AI muss in der Anlage eingerichtet werden
    
    
    ### Technische Anforderungen für die Einbindung der Phone AI als SIP-Telefon
    
    - **SIP-Account inkl. Zugangsdaten**: 
    Für ein SIP-Telefon (genaue Implementierung anlagenabhängig, ein separater Account für die Phone AI aber notwendig)
    
    Immer:
    - Username (ohne Leerzeichen)
    - Passwort
    - Endpoint (URL/IP), 
    - Port
    
    Falls vorhanden:
    - Proxy (URL/IP) 
    
    - **Interne Kurzwahl(en)** für Weiterleitung an Mitarbeiter / Abteilungen
    - **Bei lokaler Telefonanlage**: Feste IP-Adresse (v4 oder v6) ODER Dynamic DNS (Beim Einsatz von Dynamic DNS kann es beim Wechsel der IP-Adresse zu Verbindungsunterbrechungen von mehreren Minuten kommen. Diese Wechsel finden üblicherweise nachts statt). Der SIP-Endpoint muss aus dem Internet erreichbar sein. Bei einer Cloud-Telefonanlage ist dies durch den Anbieter gegeben.
    - **Routing von Anrufen**: Das Routing von Anrufen ist weiterhin Sache der Telefonanlage bzw. der Konfiguration dieser.
    - **Ausfallsicherheit** Unser Softphone meldet sich immer mit **zwei** Softphones an der Telefonnanlage an.
    
    ## Integration mittels Anruf-Weiterleitung (nur für Standorte innerhalb Deutschalands)
    
    - Das Hotel leitet eingehende Anrufe einfach an eine Telefonnummer von DialogShift weiter. Die Konfiguration heißt: **Blind Transfer with CLI (Caller Line Identification) - no screening**
    
    1. **Blind Transfer**: Weiterleitung eines Anrufs an eine andere Rufnummer, ohne dass der ursprüngliche Anrufer oder der Vermittler (die Person, die den Anruf weiterleitet) überprüft, ob der Anruf von der Zielperson angenommen wird.
    2. **CLI Pass-Through - no screening:** Call Forwarding with Original Caller ID. **Diese ist zwingend notwendig\!**
    
    - Das Hotel muss eine Möglichkeit (weitere Nummer, Durchwahl etc.) bereitstellen, über die die Phone AI an einen Mitarbeiter durchstellen kann, ohne dass der Anruf wieder zur Phone AI zurückgeleitet wird. Die Phone AI benutzt dafür eine Anrufweiterleitung (der Fachbegriff für Betreiber von Telefonanlagen lautet blind transfer mit Original Caller ID). Für den Hotelmitarbeiter sieht es nach der Weiterleitung so aus, als käme der Anruf direkt vom Gast. Die Phone AI gibt vor der Weiterleitung keine bisherige Zusammenfassung oder eine Problembeschreibung weiter.

    ## Nicht kompatible Telefonanlagen
    
    - Avaya IP Office: Diese Telefonanlage verfügt nur über eine sehr eingeschränkte SIP-Implementierung, welche leider nicht mit der Phone AI kompatibel ist. Es ist jedoch möglich, ein SBC-Proxy vor die Telefonanlage zu schalten, um diese SIP-kompatibel zu machen.