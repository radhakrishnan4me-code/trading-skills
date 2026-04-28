---
name: investor-checklist
description: |
  Apply quality + value investor mental models to stock analysis. Use for long-term investor
  assessment inspired by public principles associated with Rakesh Jhunjhunwala, Radhakishan
  Damani, Warren Buffett, Charlie Munger, Peter Lynch, Benjamin Graham, and Howard Marks.
---

# Investor Quality Checklist

Apply public investing principles as a checklist. Do not claim to quote or represent any investor.

> **Data dependency:** This skill synthesizes from the outputs of `stock-profile`, `financial-report-analysis`, `valuation-analysis`, `red-flag-analysis`, and `technical-analysis`. If used standalone, gather those inputs first.

## Mental Models

- **Jhunjhunwala-style:** big opportunity size, earnings growth, promoter quality, sector tailwind, long-term conviction.
- **Damani-style:** simple business, cash generation, valuation comfort, downside protection, patience.
- **Buffett/Munger-style:** durable moat, honest management, pricing power, high ROE/ROCE, low debt.
- **Peter Lynch-style:** understandable story, visible growth runway, reasonable price for growth.
- **Graham-style:** margin of safety, balance-sheet protection, avoid overpaying.
- **Howard Marks-style:** cycle awareness, sentiment, risk compensation, probability-weighted downside.

## When To Use Which Model

Do not blend all six. Default to one primary model based on the stock type:

| Stock Type | Primary Model | Skip |
|------------|--------------|------|
| Large-cap quality compounder (Nifty 50 / Nifty 100) | Buffett/Munger | Graham, Marks |
| High-growth midcap / smallcap with visible runway | Peter Lynch | Graham |
| Turnaround or deep-value situation | Graham | Lynch |
| Sector-thematic bet with large opportunity | Jhunjhunwala | Graham |
| Stable business with cash-generous management | Damani | Marks |
| Cyclical at trough / early recovery | Howard Marks | Buffett |

Pick one primary. Note 1-2 secondary overlays if genuinely relevant. Do not apply Buffett's moat standard to a smallcap turnaround — it will always fail and produce misleading output.

## Checklist

Score each item as Strong / Acceptable / Weak / Unknown:

- Business is understandable
- Earnings can grow for 3-5 years
- Moat or competitive edge exists
- Management/promoter quality is acceptable
- Capital allocation is sensible
- ROE/ROCE and cash flows are strong
- Debt is manageable
- Valuation is reasonable versus growth
- Margin of safety exists
- There is a credible multibagger or compounding path
- Thesis breakers are visible and monitorable

## India-Specific Checks

Apply these additionally for NSE/BSE stocks:

- **Working capital cycle:** Are debtor days expanding while creditors are shrinking? This is the most common Indian midcap cash trap. Investigate if DIO + DSO > 180 combined.
- **Promoter pledge:** Anything above 20% of promoter holdings is a governance risk. Watch for sudden increases.
- **Related-party transactions:** Flag if RPTs with promoter entities are growing faster than revenue.
- **Auditor qualification:** Any qualified report, emphasis of matter, or auditor change is a red flag. Do not ignore it.
- **Subsidiary leakage:** Check if subsidiaries are burning cash that the parent is funding. Holding company discount and cross-holding structures are common in India.
- **Brand vs. generic:** In pharma and FMCG, understand whether revenue is brand premium or commodity-priced. Brand moat is more durable.
- **Execution track record:** Promoter track record across cycles matters more in India than in developed markets because institutional governance is weaker.

## Factor Weighting

Not all checklist items are equally important. Weight the verdict accordingly:

| Tier | Factors | Weight |
|------|---------|--------|
| **Tier 1 — Disqualifiers** | Management quality, earnings quality, debt sustainability | If any Tier 1 factor is Weak, downgrade the verdict significantly regardless of other scores |
| **Tier 2 — Core quality** | Moat, ROE/ROCE, cash flow, growth runway | Core compounders need most of these strong |
| **Tier 3 — Valuation** | Margin of safety, valuation vs growth | Important but less disqualifying than Tier 1 |

A fraud company with perfect margins is still a fraud. A Weak on management quality or earnings quality should never be rated "High-quality compounder."

## Output

```markdown
## Investor Quality Checklist
| Factor | Assessment | Comment |
|--------|------------|---------|

Investor lens verdict: [High-quality compounder / Good but expensive / Cyclical opportunity / Turnaround / Speculative / Weak]
```

Use this section to sharpen the final recommendation, not to romanticize the stock.

> **Attribution note:** These mental models are public summaries of well-known investing principles. They are educational shorthand, not personal endorsements or quotes from any investor.
