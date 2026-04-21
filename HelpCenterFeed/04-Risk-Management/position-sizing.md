# Position Sizing

**Category:** Risk Management  
**Helpful for:** Users setting up position sizing for the first time, users wanting to understand the different methods

---

## What is Position Sizing?

Position sizing is how you determine how large a trade is relative to your account. It's not just about picking a number — it's about ensuring that no single trade can seriously damage your account, while still making the expected return worthwhile.

Getting this right is arguably more important than your entry strategy. A trader with an average entry strategy and excellent position sizing will outperform a trader with a great entry strategy and poor position sizing over any meaningful sample size.

---

## The Four Methods

### Fixed Percentage (Recommended for most traders)

You risk a fixed percentage of your account on every trade.

**How it works:** If your account is £10,000 and you risk 1%, you risk £100 per trade. If your stop is 50 pips, you size your position so that 50 pips of movement = £100 loss.

**Why it works:** Your position size automatically scales with your account. As you win, you trade bigger. As you lose, you trade smaller. This compounds gains and limits drawdown naturally.

**Common risk percentages:**
- Conservative: 0.5%–1%
- Moderate: 1%–2%
- Aggressive: 2%+ (not recommended unless your strategy has been thoroughly tested)

**Setting it up:** Go to Risk Management → Position Sizing, select **Fixed %**, and enter your risk percentage. Use the stepper to adjust in 0.1% increments.

---

### Fixed Lot

You trade the same position size every time, regardless of stop distance or account size.

**How it works:** You decide on a fixed number of lots (or contracts, or shares) and trade that amount every time.

**When it's used:** Some prop firm traders or systematic traders use this where position size is dictated externally. It's less adaptive than fixed percentage but simpler to calculate in real time.

**Setting it up:** Select **Fixed Lot** and enter your lot size. Adjust in 0.01 increments.

---

### Fixed Amount

You risk a fixed cash amount per trade regardless of account size.

**How it works:** If you've decided to risk £200 per trade, every trade risks £200 — whether your account is £5,000 or £50,000.

**When it's used:** Some traders prefer this when building a trading account from scratch with a fixed monthly funding contribution, or when their strategy has a very wide range of stop distances and they want consistent cash exposure.

**Setting it up:** Select **Fixed Amount**, choose your currency, and enter the amount.

---

### Custom

Your position sizing method doesn't fit any of the above — describe it in your own words.

**Examples of custom methods:**
- "1% of max drawdown remaining — risk reduces as I approach my drawdown limit"
- "Tiered approach: 1% for A-grade setups, 0.5% for B-grade setups"
- "Kelly Criterion adjusted for win rate and average R"

**Setting it up:** Select **Other** and type your method description.

---

## Drawdown Limits and Position Sizing Work Together

Position sizing alone doesn't protect you from a catastrophic session. You also need drawdown limits. Even with 1% risk per trade, five losing trades in a row during one session is a 5% drawdown in a day.

Set your drawdown limits in the section directly below Position Sizing. See [Risk Management Overview](risk-management-overview.md) for more.

---

## Common Mistakes

**Risking too much per trade** — The emotional pull to "make it back quickly" after a loss leads many traders to increase position size at the worst possible time. Fix your percentage and don't deviate.

**Not adjusting for stop width** — Fixed lot traders often don't account for the fact that a wide stop requires a smaller position to risk the same amount. If your stop is twice as wide as usual, your position should be half the size.

**Changing your method too often** — Pick one approach, stick with it long enough to evaluate it, then update deliberately. Chopping and changing destroys the ability to know what's actually working.
