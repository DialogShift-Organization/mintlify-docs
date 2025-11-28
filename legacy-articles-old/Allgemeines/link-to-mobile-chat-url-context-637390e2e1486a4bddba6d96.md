---
categories:
- Allgemeines
category_ids: []
collection: Deutscher Support
collection_id: 60c7b284fa6e7d669e9d5f8e
created_at: '2022-11-15T13:15:14Z'
created_by: 632219
helpful_count: null
id: 637390e2e1486a4bddba6d96
keywords: []
not_helpful_count: null
popularity: 0.0
site: DialogShift Support Deutsch
slug: link-to-mobile-chat-url-context
status: notpublished
title: Link to mobile Chat URL & Context
updated_at: '2022-11-15T17:13:40Z'
updated_by: 560533
view_count: 1
---

#### Base URL & Hotel-ID

`https://livechat.dialogshift.com?cid=pro12bd`

#### Set Customer Context:

  * URL encode the context : <https://www.urlencoder.org/>
  * Example context: `{"channel":"pwa-guestapp"}`
  * URL parameter: `&context=%7B%22channel%22%3A%22pwa-mailing%22%7D`
  * Full URL: `https://webchat.dialogshift.com/?clid=pro12bd&context=%7B%22channel%22%3A%22pwa-guestapp%22%7D`



#### Reserved context keys:

`channel` : Name of currently used channel in webchat apps. Must be approved by DialogShift. Free to use: `pwa-guestapp` (hotel's own guest app) or `pwa-mailing` (in email) or `pwa-qr` (scanned QR code).

`email` : Email address of guest. Used to notify guest if a new message has arrived (not used in channels WhatsApp, Facebook Mesenger).

`guestName` : Name of the guest. Displayed in Live Chat Chat App.

`space` : Current room/space of guest. Displayed in Live Chat Chat App.