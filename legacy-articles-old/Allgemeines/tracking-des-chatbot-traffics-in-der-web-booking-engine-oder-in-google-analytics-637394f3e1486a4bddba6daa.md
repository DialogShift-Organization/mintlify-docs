---
categories:
- Allgemeines
category_ids: []
collection: Deutscher Support
collection_id: 60c7b284fa6e7d669e9d5f8e
created_at: '2022-11-15T13:32:35Z'
created_by: 632219
helpful_count: null
id: 637394f3e1486a4bddba6daa
keywords: []
not_helpful_count: null
popularity: 0.8
site: DialogShift Support Deutsch
slug: tracking-des-chatbot-traffics-in-der-web-booking-engine-oder-in-google-analytics
status: published
title: Tracking des Chatbot Traffics in der Web Booking Engine, Google Analytics oder
  mittels eines Tracking Pixels
updated_at: '2024-07-10T18:48:28Z'
updated_by: 754830
view_count: 101
---

## Booking Engine Statistik

Die meisten Anbieter von Web Booking Engines (WBE) bieten auch das Tracking der Umsätze, die in der Booking Engine getätigt wurde, an.

Z.B. in einer Statistik.

Diese Statistik enthält die üblichen Zahlen: gebuchte Nächte, Umsätze, Conversion Rates, usw. In der Regeln erlaubt die Statistik diese Zahlen nach der **Herkunft des Traffics** aufzuschlüsseln. Standardmäßig kommt der Traffic von der Hotel-Website, oder aus Werbe-Mailings, oder von Anzeigen im Web.

Nun kann die Herkunft des Buchenden ja auch vom Chatbot kommen. Daher markieren wir den von uns zur WBE weiterleiteten Traffic mit Markierungen:

  1. Mit URL Parametern
  2. Alternativ, mit qualitativen Abstrichen kann auch die "Referrer-Domain" genutzt werden: Dies ist "[dialogshift.com](<http://dialogshift.com>)"



Beide Markierungen erlauben es, später die WBE-Zahlen nach Herkunft des Buchenden vom Chatbot aufzuschlüsseln.

Es lohnt sich also mit dem WBE Anbieter zu sprechen und mit dem Dienstleister, der das Website-Tracking verantwortet.

## Google Analytics E-Commerce Tracking

Es gibt es keine allgemeingültige Lösung, da ein E-Commerce Tracking in Google Analytics unterschiedlich aufgesetzt sein kann.

Die generelle Vorgehensweise bleibt jedoch identisch:

  * Erstelle einen Custom Report
  * Filtere die Umsätze nach der Existenz des URL Parameters `ref=dialogshift`



## Tracking Pixel

Tracking Pixel sind für das Hotel sehr transparent, weil Umsatzzahlen bei uns in der DialogShift Statistik einsehbar sind. 

Leider werden aus technischen Gründen und Limitationen keine Umsätze aus den Kanälen Instagram, Facebook, Google's Business Messages oder WhatsApp eingerechnet. 

Diese Lösung liefert eher indikative Zahlen.