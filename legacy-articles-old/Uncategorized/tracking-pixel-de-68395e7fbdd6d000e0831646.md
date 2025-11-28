---
categories:
- Uncategorized
category_ids: []
collection: Deutscher Support
collection_id: 60c7b284fa6e7d669e9d5f8e
created_at: '2025-05-30T07:30:07Z'
created_by: 560533
helpful_count: null
id: 68395e7fbdd6d000e0831646
keywords: []
not_helpful_count: null
popularity: 0.2
site: DialogShift Support Deutsch
slug: tracking-pixel-de
status: published
title: Tracking Pixel (DE)
updated_at: '2025-05-30T07:30:26Z'
updated_by: 560533
view_count: 28
---

# DialogShift Tracking Pixel - Implementierungsanleitung

## Überblick

Das DialogShift Tracking Pixel erfasst Buchungsabschlüsse und muss auf der Buchungsbestätigungsseite implementiert werden.

## Grundlegende Pixel-URL
    
    
    https://ibe.prod.co25.net/pixel?clientid=${clientid}&conversionType=${conversionType}&amount=${amount}&currency=${currency}&rooms=${rooms}&nights=${nights}
    

## Erforderliche Parameter

Parameter| Pflicht| Beschreibung| Beispiel  
---|---|---|---  
`clientid` | ✅| Von DialogShift bereitgestellte Client-ID| `pro123`  
`conversionType` | ✅| Während Beta-Phase immer `ibe` | `ibe`  
`amount` | ✅| Buchungsbetrag ohne Tausendertrennzeichen| `234.56`  
`currency` | ✅| Währungscode (ISO 4217)| `EUR` , `USD`  
`rooms` | ✅| Anzahl gebuchter Zimmer| `2`  
`nights` | ✅| Anzahl Übernachtungen| `3`  
  
* * *

## Google Tag Manager (GTM) Integration

### Voraussetzungen

  1.  **DialogShift Client-ID** (wird von DialogShift bereitgestellt)
  2.  **Funktionierendes E-Commerce Tracking** mit GTM und Google Analytics
  3.  **Data Layer Implementation** auf der Buchungsbestätigungsseite



### Was ist der Data Layer?

Der Data Layer ist ein JavaScript-Array auf Ihrer Webseite, das strukturierte Daten für Tracking-Tools bereitstellt:
    
    
    // Data Layer Beispiel
    window.dataLayer = window.dataLayer || [];
    
    // Daten bei Buchungsabschluss hinzufügen
    dataLayer.push({
        'event': 'booking_complete',
        'TotalCost': '299.50',
        'SelectedCurrCode': 'EUR',
        'RmQty': 2,
        'nights': 3
    });
    

### Erforderliche Data Layer Variablen

Ihr Data Layer muss die Buchungsdaten enthalten. Die Variablennamen können beliebig gewählt werden:

 **Beispiel mit Standard-Namen:**

  * `TotalCost` \- Gesamtbuchungsbetrag
  * `SelectedCurrCode` \- Währungscode
  * `RmQty` \- Anzahl Zimmer
  * `nights` \- Anzahl Nächte



 **Beispiel mit eigenen Namen:**

  * `bookingTotal` \- Gesamtbuchungsbetrag
  * `currency` \- Währungscode
  * `roomCount` \- Anzahl Zimmer
  * `stayNights` \- Anzahl Nächte



### GTM Setup Schritt-für-Schritt

#### 1\. Custom HTML Tag erstellen

  * Gehen Sie zu **Tags** → **Neu**
  * Wählen Sie **Benutzerdefiniertes HTML**
  * Fügen Sie folgenden Code ein:


    
    
    <script>
    var pixel = document.createElement("img"); 
    pixel.src = "https://ibe.prod.co25.net/pixel?clientid=IHRE_CLIENT_ID&conversionType=ibe&amount={{TotalCost}}&currency={{SelectedCurrCode}}&rooms={{RmQty}}&nights={{nights}}"; 
    pixel.style = "display: none;"; 
    document.body.appendChild(pixel);
    </script>
    

#### 2\. Client-ID ersetzen

Ersetzen Sie `IHRE_CLIENT_ID` mit der von DialogShift bereitgestellten ID.

#### 3\. Trigger konfigurieren

  * Erstellen Sie einen Trigger für die **Buchungsbestätigungsseite**
  * Empfohlen: Custom Event Trigger auf `booking_complete` Event



#### 4\. Tag aktivieren

  * Verknüpfen Sie Tag mit Trigger
  * Testen Sie in der GTM Vorschau
  * Veröffentlichen Sie den Container



### Wie GTM die Variablen findet

GTM erkennt automatisch das `dataLayer` Array und ersetzt Variablen in `{{}}` Klammern:

  * `{{TotalCost}}` wird zu dem Wert aus `dataLayer.TotalCost`
  * `{{bookingTotal}}` wird zu dem Wert aus `dataLayer.bookingTotal`
  * **Wichtig** : Die Namen in `{{}}` müssen exakt den Data Layer Variablennamen entsprechen
  * Kein expliziter Verweis auf den Data Layer nötig
  * GTM überwacht Data Layer Änderungen automatisch



### Anpassung der Variablennamen

Falls Ihr Data Layer andere Variablennamen verwendet, passen Sie den Pixel-Code entsprechend an:

 **Beispiel mit eigenen Variablennamen:**
    
    
    <script>
    var pixel = document.createElement("img"); 
    pixel.src = "https://ibe.prod.co25.net/pixel?clientid=IHRE_CLIENT_ID&conversionType=ibe&amount={{bookingTotal}}&currency={{currencyCode}}&rooms={{roomCount}}&nights={{stayNights}}"; 
    pixel.style = "display: none;"; 
    document.body.appendChild(pixel);
    </script>
    

**Zugehöriger Data Layer:**
    
    
    dataLayer.push({
        'event': 'booking_complete',
        'bookingTotal': '299.50',
        'currencyCode': 'EUR',
        'roomCount': 2,
        'stayNights': 3
    });
    

* * *

## Alternative Implementierungen

### Server-Side Rendering (PHP, Python, Ruby)
    
    
    <script>
    var pixel = document.createElement("img"); 
    pixel.src = "https://ibe.prod.co25.net/pixel?clientid=${clientid}&conversionType=ibe&amount=${amount}&currency=${currency}&rooms=${rooms}&nights=${nights}"; 
    pixel.style = "display: none;"; 
    document.body.appendChild(pixel);
    </script>
    

_Ersetzen Sie_` _${VARIABLE}_` _mit entsprechenden Server-Variablen._

### JavaScript Integration
    
    
    <script>
    var pixel = document.createElement("img"); 
    pixel.src = "https://ibe.prod.co25.net/pixel?clientid=" + yourClientId + "&conversionType=ibe&amount=" + bookingAmount + "&currency=" + currencyCode + "&rooms=" + roomCount + "&nights=" + nightCount; 
    pixel.style = "display: none;";
    document.body.appendChild(pixel);
    </script>
    

* * *

## Testen der Implementation

### 1\. GTM Vorschau verwenden

  * Aktivieren Sie GTM Preview Mode
  * Führen Sie eine Testbuchung durch
  * Prüfen Sie, ob das Pixel ausgelöst wird



### 2\. Browser Entwicklertools

  * Öffnen Sie Network Tab
  * Suchen Sie nach Requests an `ibe.prod.co25.net`
  * Überprüfen Sie Parameter-Werte



### 3\. Häufige Probleme

  *  **Pixel feuert nicht** : Prüfen Sie Trigger-Konfiguration
  *  **Falsche Werte** : Überprüfen Sie Data Layer Implementierung
  *  **404 Fehler** : Kontrollieren Sie Client-ID



* * *

## Support

Bei Fragen zur Implementation kontaktieren Sie das DialogShift Support-Team mit:

  * Ihrer Client-ID
  * URL der Buchungsbestätigungsseite
  * Screenshots der GTM Konfiguration (falls relevant)
  *  **Screenshot des Tracking Requests** aus den Browser Developer Tools (Network Tab)