# iCloud Sync Explained

**Category:** Data & Sync  
**Helpful for:** Users wanting to understand how sync works, users experiencing sync issues

---

## How TradingPlan Uses iCloud

All your TradingPlan data is stored in iCloud's private database, associated with your Apple ID. This means:

- Your data syncs automatically across all your devices logged in with the same Apple ID
- No separate TradingPlan account or password is needed
- Your data is private — only your devices can access it
- Even if you delete and reinstall the app, your data returns when you sign back in

---

## What Syncs

Everything in TradingPlan syncs via iCloud:
- All strategies and their rules
- Philosophy, mindset, your why, business notes
- Risk management settings
- Routines and their steps
- Flow history (strategy flows and routine flows)
- Dashboard widget preferences and layout

**App preferences** (notification settings, app lock settings, biometric preferences) sync separately via iCloud Key-Value Storage — also automatically.

---

## What Doesn't Sync

- **Local app settings** tied to a specific device (like whether a particular sheet is open)
- **Profile photo** syncs as part of your user profile data, but large images may take slightly longer

---

## When Does Sync Happen?

Sync happens automatically in the background. There's no manual sync button. Changes you make on one device typically appear on your other devices within a few seconds to a few minutes, depending on:

- Internet connectivity on both devices
- Whether iCloud is experiencing any delays
- Whether the app is open in the background on the receiving device

---

## Why Sync Might Be Slow

Sync works via Apple's CloudKit infrastructure. Occasional delays are normal and usually resolve themselves within minutes. Sync can be slower when:

- Either device has a poor internet connection
- The receiving device hasn't been opened recently (changes will appear next time it's opened)
- iCloud is experiencing a service disruption (rare — check [Apple System Status](https://www.apple.com/support/systemstatus/))

---

## How to Check Sync Is Working

1. Make a small change on one device (e.g. update a business note)
2. Open the app on another device
3. The change should appear within a few minutes

If it doesn't, see [Data Not Syncing](../08-Troubleshooting/data-not-syncing.md).

---

## iCloud Storage

TradingPlan data is small and won't meaningfully impact your iCloud storage. Even a complete plan with many strategies and routines takes up only a few megabytes.

---

## Privacy

Your data is stored in iCloud's private database — it's encrypted and only accessible to your devices via your Apple ID. TradingPlan cannot access your iCloud data; only you can.

---

## Simulator / No iCloud Account

If you're running TradingPlan on a device that isn't signed in to iCloud, or in certain test environments, the app will store data locally only (no sync). A sign-in prompt will appear if you haven't signed in with Apple yet.
