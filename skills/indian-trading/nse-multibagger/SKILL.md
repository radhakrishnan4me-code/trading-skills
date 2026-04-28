---
name: nse-multibagger
description: |
  Screen and deeply analyze potential NSE multibagger stocks using a Peter Lynch-style quality,
  growth, valuation, and technical framework. Use when the user asks for multibagger stocks,
  undervalued high-growth NSE stocks, Peter Lynch-style analysis, top NSE multibagger candidates,
  smallcap/midcap compounders, value traps, or worst-case scenarios for high-potential stocks.
---

# NSE Multibagger

Use this skill to find and analyze potential 3-5 year multibagger candidates in Indian equities. The default universe is NSE 500 plus smaller midcap/smallcap candidates that pass liquidity, governance, and data-quality filters.

This is an educational research framework. Never promise multibagger returns.

## Default Workflow

1. **Define universe:** Start with NSE 500, then include smaller midcap/smallcap names only if liquidity and disclosure quality are acceptable.
2. **Collect data:** Price, market cap, volume, 3-5 year sales/profit growth, margins, ROE/ROCE, debt, cash flow, promoter holding/pledge, valuation, peers, news, and technical trend.
3. **Apply hard filters:** Remove names with serious governance issues, dangerous debt, poor liquidity, weak disclosures, or unsustainable peak-cycle earnings.
4. **Score candidates:** Rank growth, quality, valuation, technicals, and risk.
5. **Classify with Peter Lynch lens:** Fast grower, stalwart, turnaround, cyclical, asset play, or slow grower.
6. **Deep dive strongest ideas:** Explain why the stock can grow multifold, what must go right, and what can go wrong.
7. **Output top 10 plus deep dives:** Include avoid/watchlist names and thesis breakers.

## Tools

USE these tools in this order. Web search is not sufficient for a broad screen — these tools are required.

1. **Groww MCP** — symbol lookup, live quote, holdings, indicators, candles. Primary tool for price, volume, and chart data.
2. **yfinance** — historical OHLCV, multi-year price history for long-term charts and relative strength calculations.
3. **Finance portals** (Screener, Trendlyne, Tickertape) — multi-year financial ratios, peer comparison, promoter holdings, shareholding pattern. These are critical for the screening phase — use these before any web search.
4. **NSE/BSE exchange filings** — shareholding pattern, corporate actions, director dealings.
5. **Company annual reports / investor presentations** — for business model, growth runway, and segment details on deep-dive candidates.
6. **Business news** (Mint, ET, Bloomberg Quint) — recent developments on candidates.
7. **Web search** — only for breaking news or context when the above tools are unavailable.

## Tool Setup

If Groww MCP is not installed, set it up first:

```
npx @anthropic-ai/claude-code@latest config add --mcp-server groww-mcp
```

Or add via Claude Code settings → MCP Servers → Add. Restart Claude Code after installation.

## Fallback: When Groww MCP Is Unavailable

If Groww MCP is not available or returns no data:

1. **USE yfinance immediately.** Import and call yfinance to get historical OHLCV, current price, and basic financials. Do not skip to web search.
2. For price and volume: `yfinance.Ticker(symbol).history(period="2y")`
3. For current quote: `yfinance.Ticker(symbol).info`
4. For financials: `yfinance.Ticker(symbol).financials` and `.balance_sheet`
5. Only use web search after yfinance has been attempted and still returns insufficient data.

The AI must explicitly try yfinance before falling back to web search. Web search alone is not sufficient for a broad multibagger screen.

## Hard Rejection Filters

Reject or mark as Avoid if any of these are material:

- Promoter pledge is high or rising without a credible explanation
- Auditor resignation, qualified audit, serious regulatory action, or repeated related-party concerns
- Debt/equity and interest coverage indicate stress
- Operating cash flow is persistently far weaker than reported profit
- Sales/profit growth is collapsing while valuation still assumes growth
- Stock is cheap only because the business is structurally declining
- Liquidity is too poor for realistic entry and exit
- Cyclical company appears cheap only on peak earnings

## Peter Lynch Lens

Classify each candidate:

| Type | What To Look For | Multibagger Relevance |
|------|------------------|-----------------------|
| Fast Grower | High sales/profit growth, long runway, reinvestment opportunity | Best hunting ground if valuation is not excessive |
| Stalwart | Large high-quality company, steady growth | Lower multibagger odds, better compounding quality |
| Turnaround | Bad period improving due to balance-sheet/business repair | High upside, high execution risk |
| Cyclical | Earnings tied to commodity/capex/industry cycle | Buy near trough, avoid peak-earnings traps |
| Asset Play | Hidden land, investments, cash, brands, subsidiaries | Upside depends on value unlocking |
| Slow Grower | Low growth, dividend-heavy | Usually not a multibagger candidate |

## Scoring Model

Score 1-5 for each factor:

- **Growth Score:** sales/profit CAGR, runway, market share, sector tailwind
- **Quality Score:** ROE/ROCE, margins, cash conversion, debt, capital allocation
- **Valuation Score:** P/E, PEG, P/B, EV/EBITDA, peer discount, historical range
- **Technical Score:** long base, accumulation, relative strength, breakout, support
- **Risk Score:** governance, liquidity, debt, cyclicality, valuation, thesis fragility

Higher Risk Score means higher risk. A strong candidate usually has:

- Growth Score: 4-5
- Quality Score: 4-5
- Valuation Score: 3-5
- Technical Score: 3-5
- Risk Score: 1-3

## Multibagger Thesis Checklist

For each deep dive, answer:

- Is the business simple enough to understand?
- Can sales and earnings compound for 3-5 years?
- Is the market opportunity much larger than the current revenue base?
- Does the company have a moat, niche, brand, cost edge, distribution edge, or execution edge?
- Is management allocating capital sensibly?
- Does profit convert into operating cash flow?
- Is debt manageable even in a bad year?
- Is valuation reasonable relative to growth?
- What temporary issue or market neglect creates undervaluation?
- What technical pattern supports accumulation or trend reversal?
- What would prove the thesis wrong?

## Technical Confirmation

Use technicals to time risk, not to justify weak fundamentals.

Look for:

- Long consolidation base after earnings improvement
- Price reclaiming 50/200 DMA
- Higher highs and higher lows on weekly chart
- Volume expansion on breakout days
- Relative strength versus Nifty Midcap/Smallcap indices
- Clear support and invalidation levels

Avoid technically strong stocks if valuation is euphoric and fundamentals cannot support the move.

## Worst-Case Scenario

Always include a worst-case section:

- Earnings fail to grow or reverse
- Margin pressure destroys expected operating leverage
- Debt or working capital stress appears
- Promoter/governance concern emerges
- Valuation de-rates despite growth
- Technical breakdown below long-term support
- Expected 3-5 year upside becomes dead money or permanent capital loss

## Position Risk Labels

| Label | Meaning |
|-------|---------|
| Core | High quality, liquid, lower red flags, suitable for larger long-term allocation |
| Satellite | Good upside but higher volatility, valuation, or execution risk |
| Speculative | High upside but high uncertainty, low allocation only |
| Avoid | Risk/reward, governance, debt, liquidity, or value-trap risk is unacceptable |

## Output Format

```markdown
# NSE Multibagger Screen - [Date]

## Screening Universe
- Universe: [NSE 500 + qualified small/midcaps, or user-provided list]
- Data sources: [...]
- Exclusions: [...]
- Missing data: [...]

## Top 10 Candidates
| Rank | Stock | Market Cap | Lynch Type | Growth Score | Quality Score | Valuation Score | Technical Score | Risk Score | Verdict |
|------|-------|------------|------------|--------------|---------------|-----------------|-----------------|------------|---------|

## Deep Dive: [Best Candidate]
- Business story:
- Why it can grow multifold:
- Peter Lynch classification:
- Financial strength:
- Valuation comfort:
- Technical setup:
- 3-5 year bull/base/bear scenarios:
- Worst-case scenario:
- Thesis breakers:
- Position risk label: [Core / Satellite / Speculative / Avoid]
- Final view:

## Avoid / Watchlist Names
[Stocks rejected or kept on watchlist and why]

> Lynch-style one-liner: [simple one-line explanation without claiming to quote Peter Lynch]
```

## Guardrails

- Do not promise 2x, 5x, or 10x returns.
- Do not claim Peter Lynch would buy, sell, or endorse any stock.
- Use "Lynch-style" only as a public investing-principle shorthand.
- State when screening is incomplete because full NSE financial data was unavailable.
- Prefer "potential multibagger candidate" over "multibagger stock."
