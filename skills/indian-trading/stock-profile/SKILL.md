---
name: stock-profile
description: |
  Build the company and business profile section for NSE/BSE stock analysis. Use when the user
  asks what a company does, how it makes money, its sector, moat, market position, growth runway,
  cyclicality, or competitive strengths and weaknesses.
---

# Stock Profile

Create the business foundation for a stock report before judging valuation or price action.

## Tools

USE these tools in this order to gather company identity and profile data:

1. **Groww MCP symbol lookup** — resolve company name to NSE/BSE symbol, get sector, market cap, current price. This is the primary tool for stock identity.
2. **Company annual report / investor presentation** — for business model, revenue segments, geographic spread, and competitive positioning.
3. **NSE/BSE exchange filings** — for corporate actions, promoter details, and shareholding structure.
4. **Finance portals** (Screener, Trendlyne, Tickertape) — for peer comparison, sector classification, and historical financial summary.
5. **Web search** — for recent news, sector context, or management background when above tools are insufficient.

If Groww MCP is not installed:

```
npx @anthropic-ai/claude-code@latest config add --mcp-server groww-mcp
```

Or add via Claude Code settings → MCP Servers → Add. Restart Claude Code after installation.

If Groww MCP is unavailable, **USE yfinance immediately** to get current price, market cap, and basic info via `.info`. For company profile data, use the annual report or investor presentation. Do not rely solely on web search for stock identity data.

## Inputs

- Company name and NSE/BSE symbol
- Sector, industry, market cap, listing exchange
- Product/service lines and revenue segments
- Geography, customers, distribution, capacity, or asset base when available

## Analysis Checklist

- **Business model:** what the company sells, who pays, and what drives revenue.
- **Revenue drivers:** volume, pricing, market share, utilization, AUM, loan book, subscribers, order book, or other sector-specific drivers.
- **Moat:** brand, distribution, cost advantage, regulation, switching costs, network effects, technology, scale, location, or licenses.
- **Cyclicality:** defensive, cyclical, commodity-linked, rate-sensitive, export-sensitive, or discretionary.
- **Sector tailwinds:** demand growth, policy support, formalization, premiumization, capex cycle, digital adoption.
- **Competitive position:** leader, challenger, niche player, turnaround, or weak player.
- **Key dependencies:** raw materials, currency, rates, regulation, subsidies, customer concentration, promoter execution.

## Output

```markdown
## Business Profile
- Business model: ...
- Revenue drivers: ...
- Moat/edge: ...
- Sector context: ...
- Competitive position: ...
- Long-term runway: ...
- Key dependencies: ...
```

Prefer plain business language. If the business cannot be understood from available data, say so and lower confidence.
