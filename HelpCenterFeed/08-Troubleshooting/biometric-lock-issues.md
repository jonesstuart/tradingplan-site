# Biometric Lock Issues

**Category:** Troubleshooting  
**Helpful for:** Users having trouble with Face ID or Touch ID, users who are locked out

---

## What is the App Lock?

TradingPlan includes an optional biometric lock that requires Face ID or Touch ID to open the app. This prevents anyone who picks up your device from seeing your trading plan without your authentication.

The lock is optional — it's not enabled by default. You enable it in **Profile → Security**.

---

## I'm Locked Out of the App

If biometric authentication is failing and you can't get into the app:

### Try Your Device Passcode First
Some devices fall back to your device passcode if Face ID or Touch ID fails enough times. When prompted for biometrics, look for a "Use Passcode" or "Enter Passcode" option.

### Check Face ID / Touch ID Is Working Generally
1. Open the **Settings** app — if Face ID unlocks Settings, it should work in TradingPlan too
2. Go to **Settings → Face ID & Passcode** (or Touch ID & Passcode)
3. Check that TradingPlan is listed and enabled under "Use Face ID For"

### Re-enrol Your Biometrics
If your Face ID or Touch ID isn't working in general:
1. Go to **Settings → Face ID & Passcode**
2. Tap **Set Up Face ID** (or add a fingerprint)
3. Follow the prompts
4. Try unlocking TradingPlan again

---

## Disabling the App Lock

If you want to turn off the biometric lock:

1. Open TradingPlan (authenticate first)
2. Go to **Profile → Security**
3. Toggle **App Lock** off
4. Confirm with Face ID, Touch ID, or your device passcode

---

## Face ID Not Working in TradingPlan Specifically

If Face ID works elsewhere but not in TradingPlan:

1. Go to **Settings → Face ID & Passcode**
2. Enter your passcode
3. Look for TradingPlan in the list under "Use Face ID For" and confirm it's enabled
4. If TradingPlan isn't listed, try toggling App Lock off and on again within the app

---

## App Lock Keeps Re-Enabling Itself

App Lock settings sync across your devices via iCloud. If you've enabled App Lock on one device, the setting will be active on all devices signed in with your Apple ID. To disable it everywhere, disable it on each device individually.

---

## I Never Set Up App Lock But It's Asking for Biometrics

This could happen if:
- You enabled it on another device and it synced
- You enabled it previously and forgot

Go through the lock screen normally (use your device passcode as a fallback if needed) and then disable App Lock in Profile → Security if you don't want it.

---

## Can I Reset the Lock Without Getting In?

If you're genuinely unable to authenticate (device biometrics completely unavailable, no passcode fallback working), reinstalling TradingPlan will remove the lock. Your data is safe in iCloud and will sync back when you sign in again.

1. Delete TradingPlan from your device
2. Reinstall from the App Store
3. Sign in with Apple
4. Wait for data to sync
5. Do not re-enable App Lock unless you've resolved the biometric issue
