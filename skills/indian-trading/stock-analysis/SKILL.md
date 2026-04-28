---
name: stock-analysis
description: |
  Master orchestrator for complete AI NSE/BSE stock analysis. Use this skill whenever the user
  asks to analyze a stock, generate a complete stock profile, assess 1-year upside/downside,
  review fundamentals, news, valuation, technicals, risks, or decide whether to buy, hold,
  accumulate, avoid, reduce, or watchlist an Indian equity. Route broad multibagger,
  undervalued high-potential, top NSE candidates, and Peter Lynch-style screening requests to
  the nse-multibagger skill.
---

# AI NSE Stock Analysis Orchestrator

Use this workflow to produce a complete research-style report for NSE/BSE stocks. The default lens is quality + value investing with an educational caveat.

## Tools

USE these tools in this order. Web search is a last resort.

1. **NSE/BSE filings and corporate actions** — exchange websites or Groww MCP filings tools
2. **Company investor relations** — annual reports, quarterly results, investor presentations, transcripts
3. **Groww MCP** — symbol lookup, live quote, depth, holdings, indicators, candles. This is the primary tool for price, volume, and chart data.
4. **yfinance** — historical OHLCV, long-term price series for multi-year charts
5. **Finance portals** (Screener, Trendlyne, Tickertape) — for multi-year ratios, peer comparison, and screening data
6. **Business news** (Mint, ET, Bloomberg Quint, CNBCTV18) — recent developments and filings
7. **Web search** — only for breaking news, general context, or when the above tools are unavailable
8. **Social media** — weak sentiment signal only, never as fact

## Tool Setup

If Groww MCP is not installed, set it up first:

```
npx @anthropic-ai/claude-code@latest config add --mcp-server groww-mcp
```

Or install via Claude Code settings → MCP Servers → Add. Restart Claude Code after installation.

## Fallback: When Groww MCP Is Unavailable

If Groww MCP is not available or returns no data:

1. **USE yfinance immediately.** Import and call yfinance to get historical OHLCV data, current price, and basic financial data. Do not skip to web search.
2. For price and volume: `yfinance.Ticker(symbol).history(period="2y")`
3. For current quote: `yfinance.Ticker(symbol).info` (may return limited fields)
4. For financials: `yfinance.Ticker(symbol).financials` and `.balance_sheet`
5. Only use web search after yfinance has been attempted and still returns insufficient data.

The AI must explicitly try yfinance before falling back to web search. If yfinance is available in the runtime, the AI should not skip it.

## Master Workflow

If the user asks for "multibagger", "undervalued high-growth", "top NSE candidates", "Peter Lynch", "smallcap/midcap compounders", or broad stock screening, use the **nse-multibagger** skill instead of the standard single-stock report workflow.

1. **Resolve stock identity** using name/symbol, exchange, sector, and market cap.
2. **Check data quality**: sources used, freshness, missing items, confidence.
3. **Build company profile** using the stock-profile skill.
4. **Analyze news and events** using the news-analysis skill.
5. **Analyze financial reports** using the financial-report-analysis skill.
6. **Judge valuation** using the valuation-analysis skill.
7. **Check technical setup** using the technical-analysis skill.
8. **Build 1-year scenarios** using the scenario-forecasting skill.
9. **Apply investor mental models** using the investor-checklist skill.
10. **Assess risks and red flags** using the red-flag-analysis skill.
11. **Give final rating** using the final-recommendation skill.

## Required Report Format

```markdown
# [STOCK] Complete NSE Stock Analysis - [Date]

## Quick View
- Rating: [Strong Buy / Buy on Dips / Accumulate / Hold / Watchlist / Avoid / Reduce]
- Confidence: [High / Medium / Low]
- 1-year view: [Bull/base/bear summary]
- Top reason: [one sentence]
- Top risk: [one sentence]

## Data Quality
- Sources used: [list]
- Freshness: [current/stale/partial]
- Missing data: [none or list]
- Analysis confidence impact: [short note]

## Stock Identity
[Company name, NSE/BSE symbol, sector, industry, market cap, current price, 52-week range, volume, liquidity]

## Business Profile
[Business model, revenue drivers, moat, competition, sector tailwinds, cyclicality]

## News & Events
[Recent filings, news, corporate actions, management commentary, sentiment, expected impact]

## Financial Report Analysis
[Revenue/profit growth, margins, EPS, ROE/ROCE, debt, cash flow, working capital, earnings quality]

## Valuation
[P/E, P/B, EV/EBITDA, dividend yield, peer comparison, historical valuation, margin of safety]

## Technical View
[Weekly/daily trend, support/resistance, moving averages, RSI, MACD, ADX, volume, key levels]

## 1-Year Price Outlook
| Scenario | Price Range | Upside/Downside | Key Assumptions | Trigger | Invalidation |
|----------|-------------|-----------------|-----------------|---------|--------------|
| Bull | Rs.X-Y | +X% to +Y% | ... | ... | ... |
| Base | Rs.X-Y | +X% to +Y% | ... | ... | ... |
| Bear | Rs.X-Y | -X% to -Y% | ... | ... | ... |

## Investor Quality Checklist
[Quality + value investor assessment]

## Risks & Red Flags
[Risk score, top risks, thesis breakers]

## Final AI View
[Rating, thesis, action zone, invalidation, top 3 risks, educational caveat]

> Investor-style one-liner: [one line]
```

## Rating Rules

- **Strong Buy:** quality business, attractive valuation, clean financials, favorable technicals, strong scenario skew.
- **Buy on Dips:** good business but price is stretched or technical entry is not ideal.
- **Accumulate:** suitable for gradual buying when valuation and risk are acceptable.
- **Hold:** acceptable for existing holders, but fresh entry is not compelling.
- **Watchlist:** interesting stock, but wait for data, trigger, valuation, or technical confirmation.
- **Avoid:** weak business quality, poor valuation, red flags, or bad risk/reward.
- **Reduce / Exit:** thesis deterioration, major red flags, broken technicals, or downside risk dominates.

## Guardrails

- Do not present scenario forecasts as guaranteed targets.
- Do not claim to quote or speak for Rakesh Jhunjhunwala, Radhakishan Damani, or any investor.
- Use phrases like "Jhunjhunwala-style" or "Damani-style" only as public investing-principle shorthand.
- Separate confirmed filings from media speculation.
- Always include educational disclaimer language in the final view.
