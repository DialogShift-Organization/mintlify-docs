---
categories:
- GPT Chatbot
category_ids: []
collection: Deutscher Support
collection_id: 60c7b284fa6e7d669e9d5f8e
created_at: '2023-07-18T15:25:16Z'
created_by: 560533
helpful_count: null
id: 64b6aedc2af2e15078a7d4f2
keywords: []
not_helpful_count: null
popularity: 0.2
site: DialogShift Support Deutsch
slug: gpt-allgemeine-informationen-beta-phase
status: published
title: 'GPT: Allgemeine Informationen / Beta Phase'
updated_at: '2023-07-18T16:49:33Z'
updated_by: 560533
view_count: 28
---

Folgende Informationen beziehen sich nur auf die GPT Version des DialogShift Chatbots:

  


  * Dem Chatbot stehen die **Informationen über das Hotel aus dem Fragenkatalog** zur Verfügung
    * Das Wissen des GPT Chatbots kann leicht über das Chatbot Editing erweitert werden
    * Tutorial: [Weiteres Wissen hinzufügen](<https://dialogshift.helpscoutdocs.com/article/106-gpt-dem-chatbot-weiteres-wissen-hinzufugen?preview=649e945fa15a23231a649a81>)
  * Die **Quick Reply-Buttons** unter den Antworten im Chat werden ebenfalls von der KI ausgewählt und dem Nutzer angeboten. Im Rahmen der Beta-Phase arbeiten wir daran, die Treffsicherheit hier weiter zu steigern.
  *  **Bilder und Videos** werden aktuell von einem Algorithmus ausgewählt. Es ist hier geplant, auch diese Auswahl der KI zu übergeben.
  * Der Chatbot ist optimiert für **Anfragen von Gästen** , die man üblicherweise erwarten kann. Anfragen zur Betriebsgesellschaft, Eigentumsverhältnissen und leitenden Personen werden wir im Laufe der Beta-Phase hinzufügen.
  *  **Was der Chatbot nicht beantworten kann** : Fragen zum Hotel, die nicht dem Wissen des Chatbots hinzugefügt wurden. Der Chatbot nutzt keine Suchmaschine, um Informationen zu einer Frage des Gastes selber in Erfahrung zu bringen. Der aktuelle Stand der Technik erlaubt dies nicht. Wir können aber erwarten, dass im Laufe der weiteren Entwicklung dieser recht jungen Technologie solche Angebote realisierbar werden.
  * Warum kann der Chatbot dann bestimmte Fragen zur Umgebung von Hotels beantworten, Entfernungen abschätzen oder die Höhe des Eiffelturms wissen?

Das hängt damit zusammen, dass wir standardmäßig dem Chatbot erlauben auf seine eigenen Trainingsdaten von OpenAI zuzugreifen. Diese sind mal mehr oder weniger vollständig, manchmal unterschiedlicher Qualität. Wir können aber immer dieses GPT eigene Wissen für den Hotel Chatbot auch deaktivieren. Damit erhält man die Kontrolle über die möglichen Antworten.


  
  


Wichtig zu wissen:

 **1\. Gelegentliche Überlastung der API:** Leider hat aktuell die Microsoft API von OpenAI Modellen gelegentliche Überlastungen. Wir versuchen diese abzufedern, aber mittelfristig werden sie auch von vom Anbieter beseitigt.

 **2\. Kann der Chatbot nun alle Fragen zum Hotel und zur Umgebung des Hotels beantworten?**

Nein, der Wissensumfang zum Hotel bleibt bei den Chatbots in etwa gleich. Denn der Chatbot greift auf den Fragenkatalog als Wissensquelle für spezifische Hotelinformationen zurück. Er ist jedoch durch das umfassende Sprachmodell und seine Trainingsdaten auch in der Lage, weitere Fragen, wie z.B. zur Höhe des Eiffelturms, zu beantworten. Der Chatbot greift aktuell nicht standardmässig auf die Inhalte der Website zurück. Er nutzt die hinterlegten Inhalte (Fragenkatalog) des bisherigen Chatbots.

 **3\. Wie kann man den GPT Wissensumfang erweitern?**

Möchte man dem Chatbot weitere Informationen hinzufügen, so kann eine neue Antwort im DialogShift Backend erstellt werden (Kategorie: “Eigene Antworten”) und dort die Informationen eingetragen werden. Z. B. Anbindung Nahverkehr, Name Hoteldirektor, usw.