---
name: news-analysis
description: |
  Analyze recent news, filings, announcements, corporate actions, and event impact for NSE/BSE
  stocks. Use when the user asks what changed recently, whether news is positive or negative,
  or how events affect a stock thesis.
---

# News Analysis

News should explain what changed, not just list headlines.

## Tools

USE these tools in this order:

1. **NSE/BSE exchange announcements** — primary source for confirmed filings, corporate actions, regulatory disclosures. These are the most reliable.
2. **Company investor relations page** — press releases, investor presentations, earnings transcripts. High quality and forward-looking.
3. **Annual reports and quarterly result notes** — for management commentary context.
4. **Business news** (Mint, Economic Times, Bloomberg Quint, CNBCTV18) — for general market context and media interpretation of events.
5. **Web search** — for breaking news only. Clearly separate unconfirmed reports from confirmed filings.
6. **Social media** — weak sentiment signal only, never as fact.

When using news sources, always distinguish between: confirmed exchange filing vs. media report vs. unverified social comment.

## Source Priority

1. NSE/BSE exchange announcements and filings
2. Company investor-relations updates, press releases, presentations, transcripts
3. Annual reports and quarterly result notes
4. Reputed business news sources
5. Social media only as weak sentiment

## What To Capture

- Quarterly results and management commentary
- Order wins, capex, acquisitions, divestments
- Regulatory actions, litigation, tax, penalties
- Product launches, pricing changes, market-share updates
- Corporate actions: dividend, bonus, split, rights issue, buyback, merger/demerger
- Promoter or institutional stake changes, pledging, large block deals
- Credit-rating changes and debt refinancing

## Classify Each Event

| Classification | Meaning |
|----------------|---------|
| Positive | Improves earnings, balance sheet, moat, sentiment, or valuation case |
| Negative | Weakens earnings, governance, balance sheet, sentiment, or technicals |
| Neutral | Relevant but unlikely to change thesis materially |
| Uncertain | Potentially important but needs confirmation or numbers |

## Output

```markdown
## News & Events
| Event | Source Type | Classification | Expected Impact | What To Watch |
|-------|-------------|----------------|-----------------|---------------|

Summary: [3-5 sentence narrative of what changed and why it matters]
```

Always separate confirmed filings from unverified media reports.
