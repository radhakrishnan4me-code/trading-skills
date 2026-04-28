---
name: technical-analysis
description: |
  Technical analysis module for NSE/BSE stock reports. Use for weekly/daily trend, support and
  resistance, moving averages, RSI, MACD, ADX, Bollinger Bands, volume, breakouts, breakdowns,
  risk levels, and timing context.
---

# Technical Analysis

Use technicals as timing and risk context. Do not let chart signals override weak fundamentals without saying so.

## Tools

USE these tools in this order for chart and price data:

1. **Groww MCP candles and indicators** — primary tool. Fetch daily candles (200+ sessions) and weekly candles (2+ years) directly. Get RSI, MACD, Bollinger Bands, SMA/EMA values from the indicators tool.
2. **yfinance** — fallback if Groww MCP is unavailable. Get OHLCV history, then calculate indicators manually.
3. **NSE/BSE chart pages** — for 52-week range, recent price context if both tools above are unavailable.
4. **Web search** — only for sector index data or relative strength comparison when tools above cannot provide it.

Do not rely on web search for price data. If chart tools are unavailable, state this clearly and reduce confidence.

## Tool Setup

If Groww MCP is not installed:

```
npx @anthropic-ai/claude-code@latest config add --mcp-server groww-mcp
```

Or add via Claude Code settings → MCP Servers → Add. Restart Claude Code after installation.

If Groww MCP is unavailable, **USE yfinance immediately** to get OHLCV data, then calculate indicators manually. Do not skip to web search for price data. Only use web search for sector index data or relative strength when yfinance also fails.

## Data Needed

- Current price, 52-week range, volume
- Daily candles for at least 200 sessions
- Weekly candles for at least 2 years when available
- SMA/EMA 20, 50, 100, 200
- RSI(14), MACD, ADX, Bollinger Bands
- Recent swing highs/lows and volume spikes

## Framework

- **Weekly trend:** higher highs/lows, lower highs/lows, trend vs 50W/200W averages.
- **Daily trend:** price structure, pullback, breakout, breakdown, consolidation.
- **Moving averages:** price above/below 20/50/200 DMA and slope.
- **Momentum:** RSI zones, MACD cross/histogram, ADX trend strength.
- **Volume:** breakout volume, distribution, accumulation, dry-up near support. Also check VWAP — in Indian equities, intraday VWAP is a critical reference level that many tools provide and the 200-DMA alone misses.
- **Levels:** support, resistance, gap zones, round numbers, invalidation level.
- **Relative strength:** Compare the stock's performance vs Nifty 50 and vs its sector index over 1-month, 3-month, and 1-year windows. Leadership relative to the index tells you if the stock is a outperformer or laggard independent of the chart. A stock in a strong sector that is underperforming its sector index is a warning sign even if the chart looks bullish.
- **Sector rotation context:** Note whether the stock's sector is currently in favor or out of favor. A technically strong stock in a dying sector may rally but fail to sustain. Conversely, a technically weak stock in a strong sector sector may be worth accumulating on weakness.
- **Market breadth:** If analyzing a Nifty-level or sector-level view, check advance/decline ratio and new highs vs new lows. A bullish chart in a market where most stocks are declining is less reliable.

## Output

```markdown
## Technical View
- Weekly trend: ...
- Daily trend: ...
- Support zones: ...
- Resistance zones: ...
- Indicators: ...
- Volume read: ...
- Relative strength (vs Nifty / sector): ...
- Sector rotation view: ...
- Key trigger: ...
- Invalidation level: ...
- Technical verdict: [Bullish / Neutral / Weak / Bearish]
```

For long-term investors, emphasize major trend and risk levels. For traders, include entry zone, stop, target, and risk-reward only if useful.
