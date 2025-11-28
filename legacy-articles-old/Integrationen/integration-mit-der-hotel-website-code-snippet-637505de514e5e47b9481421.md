---
categories:
- Integrationen
category_ids: []
collection: Deutscher Support
collection_id: 60c7b284fa6e7d669e9d5f8e
created_at: '2022-11-16T15:46:38Z'
created_by: 560533
helpful_count: null
id: 637505de514e5e47b9481421
keywords: []
not_helpful_count: null
popularity: 0.7
site: DialogShift Support Deutsch
slug: integration-mit-der-hotel-website-code-snippet
status: published
title: Integration/Einbindung mit der Hotel Website - Demo Code Snippet
updated_at: '2023-12-06T09:24:20Z'
updated_by: 560533
view_count: 95
---

Der DialogShift Chat kann leicht in die Hotelwebsite integriert werden.

## Direktes Einfügen des Code Snippets in die Website

Im Rahmen des Setup stellt Dir DialogShift ein Code Snippet zur Einbindung auf Deiner Website zur Verfügung.

Nachfolgend findest Du ein Beispiel des Snippets. **Dieses hier gezeigte Demo-Snippet kann testweise eingebunden werden.**
    
    
    <script>
      ;(function() {
        var script = document.createElement('script');
        script.src = 'https://assets.dialogshift.com/code/pro12bd.js';
        document.getElementsByTagName('head')[0].appendChild(script);
      })()
    
    </script>

Die Positionierung des Chat-Buttons kann dann in der Live-Chat-App unter 

**Einstellungen - > Chatbot-Einstellungen -> Chat-Design **

angepasst werden. 

Alternativ können auch die folgenden CSS-Variablen überschrieben werden, wir empfehlen aber, die Einstellungen in der Live-Chat-App zu benutzen. Bitte keine CSS-Werte direkt überschreiben.
    
    
    --base-margin-left/--base-margin-left-mobile: Abstand zum linken Bildschirmrand (wirksam, wenn Chat-Button links)
    
    --base-margin-right/--base-margin-right-mobile: Abstand zum rechten Bildschirmrand (wirksam, wenn Chat-Button rechts)
    
    --base-margin-bottom/--base-margin-bottom-mobile: Abstand zum unteren Bildschirmrand

## Einfügen des Code-Snippets via Google Tag Manager (GTM)

Alternativ kann das Snippet per GTM wie hier beschrieben eingebunden werden: <https://support.google.com/tagmanager/answer/6107167?hl=en>

##