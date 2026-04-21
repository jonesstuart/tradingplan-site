# Advanced Risk Features (Pro)

**Category:** Risk Management  
**Helpful for:** Pro subscribers setting up advanced risk rules, users considering upgrading

---

## Overview

Pro subscribers unlock eight additional risk categories in the Risk Management section. These cover the scenarios that catch intermediate and advanced traders out — the ones that don't show up on a beginner's radar but become increasingly important as account size and strategy complexity grows.

All advanced sections follow the same pattern: toggle the section on, configure your rules, and save.

---

## Concurrent Trade Risk

**The problem it solves:** Running multiple positions simultaneously means your total live risk is the sum of all open trades — not just the last one you entered.

**What you configure:**
- **Max Open Trades** — the maximum number of simultaneous open positions. When this limit is reached, no new trades until one is closed
- **Max Live Risk Cap** — a percentage cap on total risk across all open positions simultaneously. For example, if you risk 1% per trade but cap live risk at 3%, you can have at most 3 full-risk trades open at once

**Example:**
> "Maximum 3 open trades at once. Maximum combined live risk of 3% of account."

---

## Asset Correlation Risk

**The problem it solves:** Trading correlated instruments simultaneously multiplies your actual exposure. Long EURUSD, GBPUSD, and AUDUSD at the same time is effectively a 3x USD short — not three independent trades.

**What you configure:**
- Define the affected markets (e.g. "All USD pairs", "Gold and Silver", "US Equities and US Indices")
- Choose a limit method: maximum number of correlated positions, or maximum combined risk percentage
- Add notes for context (e.g. "Max 2 USD positions at once, max 4% combined risk on yen pairs")

You can add multiple correlation rules for different market groups.

---

## Spread Risk

**The problem it solves:** Entering a trade when the spread is unusually wide — during news, low liquidity periods, or with certain brokers — eats into your expected return and makes your risk:reward worse than planned.

**What you configure:**
- Maximum acceptable spread in pips before you'll enter a trade
- Notes for any instrument-specific rules (e.g. "Never enter GBPJPY if spread exceeds 4 pips")

---

## News Risk

**The problem it solves:** High-impact news events create erratic, often random price movements. Positions held through these events are exposed to large, fast moves that can trigger stops or cause significant slippage.

**What you configure:**
- Which events the rule applies to (e.g. "FOMC, NFP, CPI, Interest Rate Decisions")
- Action during news: avoid new entries, close existing positions, reduce position size, or monitor only
- Whether to skip the whole day (useful for particularly volatile events)
- Buffer in minutes — how long before and after the event to observe the rule (e.g. 30 minutes)

You can add multiple news risk rules for different event types with different protocols.

---

## Slippage Risk

**The problem it solves:** When your order is filled at a significantly worse price than intended — due to fast markets, low liquidity, or requotes — the trade's actual risk is different from what you calculated.

**What you configure:**
- Maximum acceptable slippage in pips
- Notes for your protocol (e.g. "Cancel and re-evaluate if filled more than 3 pips from intended entry")

---

## Overnight / Weekend Risk

**The problem it solves:** Holding positions when markets close exposes you to gap risk — price can open significantly above or below where it closed, jumping straight through your stop.

**What you configure:**
- Overnight rule: whether you hold positions overnight or close before session end
- Weekend rule: whether you hold positions over the weekend
- Position size rules for any positions you do hold (e.g. reduce size to 50% if holding overnight)
- Notes for specific markets or conditions

---

## Execution Error Risk

**The problem it solves:** Everyone makes execution mistakes at some point — wrong size, wrong direction, wrong instrument. Without a pre-planned protocol, panic often makes it worse.

**What you configure:**
- Your immediate action protocol (e.g. "Close the position immediately, regardless of price. Do not try to average out of a mistake")
- Maximum time to correct the error
- Whether you log it in your business notes
- Whether you stop trading for the session after an execution error

Having this written in advance means you respond calmly and correctly, not reactively.

---

## Conditions to Trade

**The problem it solves:** You're not a machine. Your decision-making quality varies with sleep, stress, emotional state, and preparation. Trading when you're not fit to trade is as risky as having no strategy at all.

**What you configure:**
- A personal checklist of conditions that must be true before you'll trade
- Examples: "I've had at least 7 hours of sleep", "I've reviewed the economic calendar", "I'm not under unusual personal stress", "I've completed my pre-market routine"

This section turns the subjective "am I ready?" question into an objective, checkable list.

---

## Technology Risk

**The problem it solves:** Platform failures, internet outages, and hardware problems happen. Without a plan, they can result in positions you can't manage or close.

**What you configure:**
- Backup platform or broker contact details
- Protocol if your primary platform goes down (e.g. "Call broker immediately to close all positions")
- Backup internet method (e.g. mobile hotspot)
- Conditions under which you simply won't trade (e.g. "Do not trade if primary connection is unavailable")

---

## Tips

**Start with the sections most relevant to your trading.** If you're a day trader who never holds overnight, skip Overnight Risk for now and focus on News Risk and Concurrent Trade Risk.

**Be specific.** Vague rules are ignored under pressure. "Be careful around news" is not a rule. "No new entries 30 minutes before or after FOMC, CPI, or NFP. Close any open positions 60 minutes before FOMC" is a rule.

**Review these after a bad experience.** The advanced risk rules are best written when you've lived through the problem they're designed to prevent.
