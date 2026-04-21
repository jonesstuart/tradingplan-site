# Creating Your First Strategy

**Category:** Strategies  
**Helpful for:** Users creating a strategy for the first time, users unsure what to put in each section

---

## What is a Strategy?

A strategy in TradingPlan is a precise set of rules for one specific trading setup. It answers the question: "Under exactly what conditions do I enter this trade, where is my stop, and where is my target?"

You might have one strategy or several — each one represents a different setup you trade. For example:
- A trend-following strategy on the daily chart
- A breakout strategy for the London open
- A mean-reversion strategy at major support/resistance

---

## Starting From Scratch vs. Using a Template

### Create From Scratch
Go to **Strategies** and tap **Create New Strategy**. An empty strategy opens immediately — give it a name and start adding rules.

### Start From an Example
Scroll down in the Strategies tab to the **Example Strategies** section. These are real, documented trading approaches built into the app. You can't edit them directly, but they're an excellent reference for how a well-structured strategy looks.

> **Important:** Example strategies are for educational purposes only. They are not financial advice and carry no guarantee of profitability. Always test any strategy thoroughly before trading it live.

---

## Naming Your Strategy

Give your strategy a name that immediately tells you what it is. Good names:
- "EUR/USD Daily Trend Follow"
- "London Breakout"
- "SPX Mean Reversion"
- "Momentum Swing — Equities"

Vague names like "Strategy 1" make it harder to remember what the strategy is when you're about to trade.

---

## The Six Strategy Sections

Each strategy is divided into six sections. You don't have to fill them all in, but the more complete your rules, the more useful the strategy flow becomes.

### 1. Analysis
The market conditions that must be present before you'll consider this setup. This is your "big picture" context. Examples:
- "Daily trend must be bullish (price above 200 EMA)"
- "Market must be in a range, between defined S/R levels"
- "RSI must be above 50 on the 4H timeframe"

### 2. Directional Bias
How you determine trade direction. This is your filter for whether you're looking long, short, or both. Examples:
- "Only trade in direction of daily trend"
- "Long above the weekly pivot, short below"
- "Direction set by the opening range break"

### 3. Entry
The specific trigger that gets you into the trade. This is the most precise section — your entry conditions should be unambiguous. Examples:
- "Break and close above the H4 resistance on increased volume"
- "Pin bar reversal at key support level with bullish close"
- "Price pulls back to the 50 EMA, then forms a bullish engulfing candle"

### 4. Stop-Loss
Where your stop goes and why. Includes conditions for initial placement and any rules about moving the stop. Examples:
- "Stop placed 10 pips below the entry candle low"
- "Stop below the most recent swing low, minimum 1.5x ATR"
- "No stop wider than 2% of account risk"

### 5. Target
Your profit target logic. This could be a fixed R-multiple, a price level, or a structure-based target. Examples:
- "Target is 2R minimum. Close 50% at 1R, move stop to breakeven"
- "Target the next significant resistance level on the H4 chart"
- "Trail stop using a 20 EMA once 1R is reached"

### 6. Active Management
Rules for managing the trade once it's open. How do you react if price stalls? Do you add to winners? What triggers early exit? Examples:
- "If price consolidates for more than 3 candles without momentum, close 50%"
- "Do not move stop to breakeven until 1R profit achieved"
- "Add to position on pullback to entry if original conditions still valid"

---

## Adding Rules

Inside each section, tap **Add Rule** to add a new rule. Rules are written in plain text — just type what the condition is. You can:
- Add as many rules as you need
- Reorder rules by dragging
- Group related rules together using the group feature
- Enable or disable individual rules without deleting them

---

## Including Your Strategy in Your Plan

Once your strategy has at least a basic set of rules, tap the **star icon** next to its name in the Strategies list. This marks it as "included in your plan." Included strategies:
- Appear on the Strategies dashboard widget
- Are available when you run a strategy flow
- Show in the sidebar (on iPad and Mac)

Strategies without a star are still saved, but they're excluded from your active plan. This is useful for strategies you're still developing or have retired.

---

## Free Plan Limit

On the free plan, you can have **one strategy**. If you need more, upgrade to Pro. See [Free Plan vs Pro](../06-Account-and-Subscription/free-vs-pro.md) for full details.
