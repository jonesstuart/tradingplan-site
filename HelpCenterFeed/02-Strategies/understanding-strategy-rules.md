# Understanding Strategy Rules

**Category:** Strategies  
**Helpful for:** Users unsure how to structure rules, users wanting to get more out of the strategy builder

---

## How Rules Are Structured

Each strategy section (Analysis, Entry, Stop-Loss, etc.) contains **rule groups**, and each group contains individual **rules**.

Think of it as:

```
Section (e.g. Entry)
  └── Rule Group (e.g. "Primary Entry Trigger")
        └── Rule: "Break and close above H4 resistance"
        └── Rule: "Volume must be above 20-period average"
  └── Rule Group (e.g. "Confirmation")
        └── Rule: "Stochastic must be below 80 and rising"
```

This structure lets you organise your rules logically — keeping related conditions together — rather than having one long, unstructured list.

---

## Rule Groups

A rule group is a named cluster of related rules. You can label a group anything you like. For example:
- "Market Context"
- "Primary Entry Trigger"
- "Confirmation Conditions"
- "Invalidation"

Groups are purely for your own clarity. They don't affect how the strategy flow works — every rule in every group is displayed during the flow for you to check off.

---

## Writing Good Rules

The best rules are **specific, objective, and unambiguous**. A good rule is one you can look at a chart and say with certainty: "yes" or "no."

**Too vague:**
> "Market must look bullish"

**Specific and testable:**
> "Price must be above the 50 EMA on the 4H chart and the 200 EMA on the daily chart"

**Too vague:**
> "Good risk/reward"

**Specific:**
> "Minimum 2:1 risk-reward ratio to target. Stop no wider than 1.5% of account"

The more specific your rules, the more honest the strategy flow checklist becomes.

---

## Conditions and Opposites

Within a rule, you can specify **conditions** — structured criteria using the built-in condition picker. The condition picker gives you a set of common technical and market-structure conditions (e.g. "price above X moving average", "RSI above 50", "breakout of level") that you can select and configure.

Each condition also has an **opposite** — which is automatically available to flip the condition. This is useful when you want the same condition checked in reverse for short trades.

You don't have to use the condition picker. You can write rules entirely in free text if you prefer — most traders do.

---

## Enabling and Disabling Rules

Any individual rule can be toggled off without deleting it. This is useful when:
- You're testing a variation of your strategy without a particular rule
- A rule only applies to certain market conditions
- You're iterating on your rules over time

Disabled rules are greyed out in the editor and are skipped during the strategy flow.

---

## Reordering Rules

Long-press any rule to enter reorder mode, then drag it to the position you want. The order of rules in the editor is the order they appear in the strategy flow — so organise them in the logical sequence you want to check them.

---

## How Many Rules Is Too Many?

There's no hard limit, but be practical. The strategy flow is a checklist you'll run before every trade. If your strategy has 40 rules, you may find yourself skimming rather than genuinely checking each one.

A good target is **5–15 rules per strategy**, covering the most important conditions. You can always add notes and context inside individual rules rather than creating a separate rule for every nuance.

---

## The Direction Block

At the top of each strategy is a **Trade Direction** setting: Long, Short, or Both. This affects:
- How the strategy is labelled in the list
- Whether a Directional Bias section appears in the flow

Set this to match how you actually trade the setup. If you take both long and short trades with the same entry logic (just mirrored), choose "Both."

---

## Copying a Strategy

There is no one-tap duplicate feature, but you can use an **example strategy** as a reference and build your own version manually. Many traders start by reviewing an example strategy and then building a personalised version with their own conditions.
