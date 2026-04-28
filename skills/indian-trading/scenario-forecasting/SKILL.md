---
name: scenario-forecasting
description: |
  Build 1-year bull/base/bear stock-price scenarios for NSE/BSE equities. Use when the user asks
  about upside, downside, expected growth, target range, good scenario, bad scenario, or 12-month
  price outlook.
---

# Scenario Forecasting

Use ranges, not a single magic target. Tie every price range to business and valuation assumptions.

> **Data dependency:** This skill requires current price, EPS, and a valuation multiple from `valuation-analysis` or `stock-profile`. If used standalone, gather those inputs first.

## Minimum Data Threshold

Do not produce bull/base/bear scenarios unless you have at least:
- Current price and market cap
- At least 2 years of revenue and PAT history (or reasonable proxy)
- Current P/E or EV/EBITDA and a sense of historical range
- One clearly identifiable growth driver or risk factor

If data is below this threshold, state the gap explicitly and issue Low-confidence scenarios only. Do not generate numerically precise ranges when the inputs are too thin to support them.

## Scenario Structure

| Scenario | Basis |
|----------|-------|
| Bull Case | Strong earnings, margin expansion, sector tailwind, market-share gains, valuation re-rating |
| Base Case | Reasonable growth, stable margins, fair valuation, no major surprise |
| Bear Case | Weak earnings, margin pressure, bad news, de-rating, technical breakdown, governance or sector risk |

## Worked Example

Stock: XYZ Ltd | Current price: Rs.500 | Current P/E: 25x | FY25 EPS: Rs.20 | Expected EPS growth: 15%

**Bull case (5x multiple expansion + EPS growth):**
- Year-1 EPS = 20 × 1.15 = Rs.23
- Multiple expands to 30x (justified if ROCE improves and sector re-rates)
- Target = 23 × 30 = Rs.690 | Upside: +38%

**Base case (EPS growth, multiple holds):**
- Year-1 EPS = Rs.23
- Multiple stays at 25x (no change in sentiment)
- Target = 23 × 25 = Rs.575 | Upside: +15%

**Bear case (multiple compresses):**
- Year-1 EPS = 20 × 1.05 = Rs.21 (margin pressure, growth slows)
- Multiple compresses to 20x (sector de-rating or governance concern)
- Target = 21 × 20 = Rs.420 | Downside: −16%

Range: Rs.420–690 | Base: Rs.575

Adjust the assumptions to match the actual stock. Never present the arithmetic as certainty.

## Calculation Steps

1. Start with current price and current multiple.
2. Estimate year-1 EPS using conservative growth (default: street consensus if available; otherwise use 1-year historical growth × 0.8 as a buffer).
3. Choose bull/base/bear multiples based on the scenario definitions.
4. Cross-check implied prices against technical resistance (bull) and support (bear) zones. Flag any significant disagreement.
5. Convert ranges to percentage upside/downside from current price.
6. Assign confidence: High only when data quality is strong and assumptions are conservative; Medium by default; Low when data is incomplete or stock is highly uncertain.

## Output

```markdown
## 1-Year Price Outlook
| Scenario | Price Range | Upside/Downside | Key Assumptions | Trigger | Invalidation |
|----------|-------------|-----------------|-----------------|---------|--------------|
| Bull | Rs.X-Y | +X% to +Y% | ... | ... | ... |
| Base | Rs.X-Y | +X% to +Y% | ... | ... | ... |
| Bear | Rs.X-Y | -X% to -Y% | ... | ... | ... |

Scenario verdict: [short explanation of which case has the highest probability and why]
```

State clearly: these are educational scenario estimates, not guaranteed targets.
