---
categories:
- Uncategorized
category_ids: []
collection: Deutscher Support
collection_id: 60c7b284fa6e7d669e9d5f8e
created_at: '2025-05-07T20:14:45Z'
created_by: 560533
helpful_count: null
id: 681bbf355531c754b139ebc3
keywords: []
not_helpful_count: null
popularity: 0.0
site: DialogShift Support Deutsch
slug: warnung-bei-moglicherweise-falsch-konfigurierter-weiterleitung-zur-phone-ai
status: published
title: Warnung bei möglicherweise falsch konfigurierter Weiterleitung zur Phone AI
updated_at: '2025-05-08T08:17:50Z'
updated_by: 560533
view_count: 1
---

[English Article](<https://dialogshift.helpscoutdocs.com/article/171-warning-for-possibly-incorrectly-configured-forwarding-to-phone-ai>) 🇬🇧

  


 **Was bedeutet diese Warnung?**

Über 20 % der Anrufe bei der Phone-AI stammen von derselben Nummer – ein Hinweis darauf, dass die Weiterleitung der Anrufe zur Phone AI **nicht die Nummer des Gastes mitliefert**.

  


 **Hintergrund der Warnung:**

Damit die Phone AI die Nummer des anrufenden Gastes erkennen kann, muss die eingerichtete Weiterleitung zur Phone AI die Nummer des Gastes mitliefern. Die notwendige Konfiguration dazu lautet: **Blind Transfer with CLI (Caller Line Identification) - no screening**

  


 **Was ist zu tun?**

  1. Überprüfe, welche Nummern bei Deinen Anrufen angezeigt werden:



In der DialogShift App öffne die Live Chat Ansicht:

![](https://s3.amazonaws.com/helpscout.net/docs/assets/60c74eabb899954cddd470ce/images/681bc2ca44b3a84c1aacd8db/file-uHdr8yVZvd.png)

![](https://s3.amazonaws.com/helpscout.net/docs/assets/60c74eabb899954cddd470ce/images/681c4c686e5d0e3e66f7bd01/file-ydB1rwS6pE.gif)

  


In den Telefonnummern der Konversationen sollten die Nummern der anrufenden Gäste stehen.

Wenn Du hier die Nummer Deines Hotels siehst, ist vermutlich die Weiterleitung nicht richtig konfiguriert oder es gibt ein Problem mit der Telefongesellschaft.

  


 **Es gibt zwei Möglichkeiten, das Problem zu lösen:**

Kontaktiere Deinen Telefon-Diensteister und vergewissere Dich, dass **Blind Transfer with CLI (Caller Line Identification) - no screening** aktiv ist.

Nutze die neue Fähigkeit (ab 15. Mai 2025) der DialogShift Phone AI, sich als SIP-Telefon direkt in die Telefonanlage des Hotels anzumelden. 

Dies sind dann die Voraussetzungen, die Du mit dem Telefon-Dienstleister abklären müsstest:

  * Die Phone AI benötigt einen zusätzlichen SIP-Zugang in Deiner Telefonanlage – also einen eigenen „Telefonanschluss“. Das ist im Prinzip dasselbe wie ein weiteres Telefon im Haus.
  * Dieser SIP Zugang muss über das Internet erreichbar sein