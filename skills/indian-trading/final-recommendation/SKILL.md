---
name: final-recommendation
description: |
  Produce the final AI view for NSE/BSE stock analysis: rating, confidence, thesis, action zone,
  1-year scenario view, invalidation, top risks, educational caveat, and investor-style one-liner.
---

# Final Recommendation

The final view should synthesize evidence, not repeat every section.

> **Data dependency:** This skill requires outputs from all other analysis skills. If used standalone, gather inputs from `stock-profile`, `financial-report-analysis`, `valuation-analysis`, `technical-analysis`, `scenario-forecasting`, `investor-checklist`, and `red-flag-analysis` first.

## Rating Scale

- **Strong Buy:** quality business, attractive valuation, clean financials, favorable technicals, strong upside skew.
- **Buy on Dips:** good business but current price leaves limited margin of safety.
- **Accumulate:** suitable for gradual buying at or below stated zones.
- **Hold:** existing holders can continue, but fresh entry is not compelling.
- **Watchlist:** interesting, but wait for trigger, better valuation, or clearer data.
- **Avoid:** risk/reward is unattractive.
- **Reduce / Exit:** thesis has weakened or downside risk dominates.

## Required Elements

- Rating
- Confidence: High / Medium / Low
- Suitable horizon: swing / 1-year / long-term / avoid
- 1-year bull/base/bear summary
- Action zone: buy/add/hold/watch/avoid level or condition
- Invalidation: what would prove the thesis wrong
- Top 3 risks
- Educational caveat
- Investor-style one-liner

## Investor-Style One-Liner Rules

- Do not present it as an exact quote.
- Use "In a Jhunjhunwala-style view..." when growth, opportunity size, sector tailwind, and conviction are the main story.
- Use "In a Damani-style view..." when valuation discipline, business simplicity, cash generation, patience, and downside protection are the main story.
- Keep it to one sentence.

## Output

```markdown
## Final AI View
- Rating: ...
- Confidence: ...
- Suitable horizon: ...
- Thesis: ...
- Action zone: ...
- Invalidation: ...
- Top risks: ...
- Educational caveat: This is stock-analysis support, not financial advice.

> Investor-style one-liner: In a [Jhunjhunwala/Damani]-style view, ...
```
