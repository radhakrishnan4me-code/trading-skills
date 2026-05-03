# india-equity-report

> **Skill for Claude Code** — Generates institutional-quality Buy/Sell/Hold equity research reports for NSE/BSE-listed stocks, grounded entirely in live data. Written in the style of Tier-1 Indian brokerages (Kotak Institutional, Motilal Oswal, ICICI Securities).

---

## Overview

This skill produces a full-length equity research report (1,500–3,000 words) for any Indian listed stock — with real fetched prices, sourced financial data, scenario analysis, and an actionable investment verdict. It follows strict hallucination-prevention rules: every number is cited, no figures are invented.

**Trigger phrases:**
- `analyse INFY`
- `research report for Reliance Industries`
- `should I buy HDFCBANK?`
- `target price for TATAMOTORS`
- `is LATENTVIEW a good buy?`
- Any Indian stock analysis / equity research / Buy-Sell-Hold request

**Output:** A downloadable `.docx` file AND a markdown summary pasted in chat.

---

## What It Generates

A complete equity research report including:

| Section | Content |
|---------|---------|
| **Price Snapshot** | Live CMP (₹), 52W High/Low, Market Cap — fetched from Google Finance, not Screener.in (stale) |
| **Executive Summary** | Opens with the most relevant current observation — not a generic company description |
| **Business Overview** | Company profile, revenue segments, competitive position |
| **Financial Analysis** | 5Y revenue, EBITDA, PAT trends; margins; key ratios (P/E, EV/EBITDA, ROCE, ROE, D/E) |
| **Quarterly Performance** | Latest quarter results vs consensus; beat/miss analysis |
| **Management Commentary** | Concall highlights, guidance, capital allocation |
| **Valuation** | DCF, P/E re-rating, EV/EBITDA — target price derived from real fetched numbers |
| **Scenario Analysis** | Bull / Base / Bear cases with specific price targets and probability weights |
| **Technical Analysis** | Trend, support/resistance, momentum indicators |
| **Risks** | Company-specific, sector, regulatory, macro |
| **Investment Verdict** | Separate guidance for (a) existing holders and (b) new investors — specific price levels, tranching, stop-losses |
| **SEBI Disclaimer** | Mandatory regulatory disclosure |

---

## Live CMP Fetch — Critical Rule

> ⚠️ Screener.in's displayed price is often a stale cached figure (e.g., showing "13 Feb" price when the report is run on Feb 27). This skill never uses Screener.in's price field as CMP.

**CMP is always fetched via:**
1. Google Finance web search: `"[TICKER] NSE share price [MONTH YEAR]"`
2. Fallback: Tickertape.in (clearly date-stamped last close)
3. Confirmed with date — flagged if more than 3 trading days old

The report always shows concrete ₹ numbers (e.g., `₹183.50`) — never raw spreadsheet formulas like `=GOOGLEFINANCE(...)`.

---

## Data Sources

| Data Type | Primary Source |
|-----------|---------------|
| Financial statements | Screener.in (consolidated view) |
| Current price | Google Finance (web search result card) |
| Shareholding pattern | Screener.in / BSE filings |
| Quarterly results | BSE corporate filings |
| Management commentary | Screener.in concall transcripts |
| News (last 90 days) | Moneycontrol, Economic Times, Yahoo Finance, Mint, Business Standard, CNBCTV18, and general web search |
| Technical indicators | TradingView, Chartink |
| Credit ratings | CRISIL, ICRA, CARE websites |
| Sector data | CMIE, MOSPI, RBI, IBEF |

---

## Hallucination Prevention Rules

1. No fabricated figures — all EPS, revenue, margins must come from fetched pages
2. Every number has an inline source tag: `[Source: URL, date]`
3. No stale data — financials older than 6 months are flagged
4. No analyst consensus invention — only cited if fetched from Trendlyne, Bloomberg Quint, or Refinitiv
5. If a key data point is not found after 2 search attempts, stated as "Not available at time of report"
6. Target price derived only from a visible DCF, P/E re-rating, or EV/EBITDA model using fetched numbers

---

## Style Reference

Written in the style of Tier-1 Indian brokerage research:
- **Institutional quality** — conviction-driven narrative with specific dates, numbers, and sources throughout
- **Callout boxes** — for key channel checks, critical financial risks, valuation warnings, anomaly explanations
- **Executive Summary** — leads with the most interesting real-world observation about the company *right now*
- **Investment Verdict** — separate actionable guidance for existing holders vs new investors, with specific entry levels, tranching strategy, and stop-losses

---

## Supporting Reference Files

| File | Purpose |
|------|---------|
| `references/data-sources.md` | Approved data sources and fetch URLs |
| `references/analysis-frameworks.md` | Financial analysis frameworks to apply |
| `references/report-template.md` | Exact report structure and section templates |

---

## Prerequisites

- [Claude Code](https://claude.ai/code) with skills support
- The `docx` public skill (`/mnt/skills/public/docx/SKILL.md`) — for .docx generation
- Internet access for live data fetching

---

## Installation

Copy the `skills/india-equity-report/` directory (including `references/`) into your Claude skills folder.

---

## Example Output

```
INFY_EquityResearch_2025-03-04.docx

📊 PRICE SNAPSHOT (as of 04 Mar 2025)
  CMP:         ₹1,847.30
  52W High:    ₹2,006.45
  52W Low:     ₹1,358.35
  Market Cap:  ₹7,68,400 Cr
  Source: Google Finance (NSE)

Rating: BUY | Target: ₹2,150 | Upside: 16.4%

Scenario Analysis:
  Bull (₹2,400): US tech recovery, deal ramp, margin expansion
  Base (₹2,150): Steady deal wins, stable margins, USD tailwind
  Bear (₹1,550): US slowdown, pricing pressure, INR appreciation
```

---

## License

MIT — free to use, modify, and distribute. Attribution appreciated.
