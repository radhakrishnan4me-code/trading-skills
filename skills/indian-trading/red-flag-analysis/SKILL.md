---
name: red-flag-analysis
description: |
  Identify and score red flags in NSE/BSE stock analysis: governance, debt, valuation, earnings
  quality, sector, liquidity, regulatory, promoter, technical, and news-related risks.
---

# Red Flag Analysis

A good stock report must say what can go wrong.

## Tools

USE these tools in this order:

1. **NSE/BSE exchange filings** — primary source for regulatory actions, auditor changes, pledge disclosures, and related-party transaction details.
2. **Groww MCP holdings tool** — for promoter pledge status and shareholding pattern changes quarter-on-quarter.
3. **Company annual report** — for auditor's report, related-party transactions, contingent liabilities, and CFO/comparator notes.
4. **Finance portals** (Screener, Trendlyne) — for multi-year debt ratios, interest coverage, and CFO vs PAT trends. Use these to verify quantitative triggers.
5. **Business news** (Mint, ET) — for regulatory actions, management exits, and litigation updates.
6. **Web search** — only for unresolved legal cases or SEBI/RBI actions not yet on exchange filings.

## Risk Areas

- **Governance:** promoter pledge, auditor issues, related-party transactions, regulatory actions, repeated dilution.
- **Debt:** high leverage, weak interest coverage, refinancing pressure, falling credit rating.
- **Earnings quality:** cash flow weaker than profit, receivables spike, inventory build-up, one-time gains.
- **Valuation:** priced for perfection, premium unsupported by growth, peak-cycle earnings.
- **Business:** customer concentration, commodity exposure, disruption, weak market share, execution risk.
- **Sector/macro:** rates, currency, crude, policy, regulation, demand cycle.
- **Liquidity:** low volume, wide spreads, small free float.
- **Technical:** major support breakdown, distribution volume, long-term moving average weakness.
- **News:** unresolved litigation, penalties, management exits, adverse filings.

## India-Specific Hard Triggers

These are binary disqualifiers regardless of other scores. If any trigger is active, the stock should be rated at least "High risk":

| Trigger | Threshold | Why It Matters |
|---------|-----------|----------------|
| Promoter pledge | >20% of promoter holdings pledged | Governance and margin-call risk |
| Auditor qualification | Any qualified audit or emphasis of matter | Earnings may be materially misstated |
| Auditor change without explanation | Sudden change in auditor | Possible disagreement on accounting |
| Related-party transaction growth | RPTs growing faster than revenue | Potential tunneling |
| CFO resignation | CFO leaves within 12 months of results | Usually signals internal concern |
| Debt/EBITDA | >4x for non-financial companies | Stressed balance sheet, refinancing risk |
| Interest coverage | ICR < 1.5x | Cannot service debt from operations |
| CFO vs PAT ratio | CFO/PAT < 0.7 for two consecutive years | Earnings are not cash-backed |
| Promoter pledged shares increase | Any material increase quarter-on-quarter | Margin call risk, governance signal |
| SEBI action / regulatory scrutiny | Any SEBI or RBI enforcement action | Binary regulatory risk |

## Score

Use a 0-10 red flag score:

- 0-2: Low visible red flags
- 3-5: Moderate risk; monitor closely
- 6-8: High risk; position sizing or avoidance needed
- 9-10: Severe red flags; avoid unless special situation is clearly understood

## Output

```markdown
## Risks & Red Flags
- Red Flag Score: X/10
- Governance risk: ...
- Financial risk: ...
- Valuation risk: ...
- Business/sector risk: ...
- Technical risk: ...
- Thesis breakers: ...
```

Be direct. Do not soften serious governance, debt, or earnings-quality issues.
