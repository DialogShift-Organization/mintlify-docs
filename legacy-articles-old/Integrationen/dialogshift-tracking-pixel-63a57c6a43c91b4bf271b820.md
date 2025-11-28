---
categories:
- Integrationen
category_ids: []
collection: Deutscher Support
collection_id: 60c7b284fa6e7d669e9d5f8e
created_at: '2022-12-23T10:01:14Z'
created_by: 560533
helpful_count: null
id: 63a57c6a43c91b4bf271b820
keywords: []
not_helpful_count: null
popularity: 1.9
site: DialogShift Support Deutsch
slug: dialogshift-tracking-pixel
status: published
title: DialogShift Tracking Pixel (EN)
updated_at: '2025-05-30T07:29:43Z'
updated_by: 560533
view_count: 246
---

# DialogShift Tracking Pixel

Implementation guidelines for the DialogShift Tracking Pixel on the booking confirmation page.

The raw version:
    
    
    <img href="https://ibe.prod.co25.net/pixel?clientid=${clientid}&conversionType=${conversionType}&amount=${amount}&currency=${currency}&rooms=${rooms}&nights=${nights}">
    

### Parameters:

clientid  |  (mandatory) Client ID provided by DialogShift   
---|---  
conversionType  |  (mandatory) During beta period always `ibe`  
amount  |  (mandatory) Numeric amount without thousands separators (e.g. `234,56`)   
currency  |  (mandatory) Currency code in [ISO 4217](<https://en.wikipedia.org/wiki/ISO_4217>) (e.g. `EUR`)   
rooms  |  (optional) Number of rooms booked (integer)   
nights  |  (optional) Number of nights booked (integer)   
url  |  (optional) Host and URL of IBE page   
custid  |  (optional) custid is provided as a GET parameter in the redirect to the booking engine. Send back this value for increased accuracy.   
  
### Google Tag Manager (GTM) Example integration

 _Prerequisite_ : Clientid provided by DialogShift in this example is `pro123`

_Prerequisite_ : A working E-Commerce tracking with GTM/GA & Data Layer

Add this snippet as a “Custom HTML” tag and trigger it on the booking confirmation page.

Example:
    
    
    <script>var pixel = document.createElement("img"); 	pixel.src = "https://ibe.prod.co25.net/pixel?clientid=pro123&conversionType=ibe&amount={{TotalCost}}&currency={{SelectedCurrCode}}&rooms={{RmQty}}&nights={{nights}}"; 	pixel.style = "display: none;"; document.body.appendChild(pixel);</script>
    

### IBE integration - Server Side Rendering (PHP, Python, Ruby on Rails):

Replace the '${VARIABLE}' with the corresponding variables from your system.
    
    
    <script> var pixel = document.createElement("img"); 	pixel.src = "https://ibe.prod.co25.net/pixel?clientid=${clientid}&conversionType=ibe&amount=${amount}&currency=${currency}&rooms=${rooms}&nights=${nights}"; pixel.style = "display: none;"; document.body.appendChild(pixel); </script>
    

### IBE Integration - JavaScript Rendering

Add the tracking pixel via JavaScript using booking values from the IBE namespace.

Example:
    
    
    <script>
    var pixel = document.createElement("img");
    pixel.src = "https://ibe.prod.co25.net/pixel?clientid=${clientid}&conversionType=ibe&amount=${amount}&currency=${currency}&rooms=${rooms}&nights=${nights}";
    pixel.style = "display: none;";document.body.appendChild(pixel);</script>