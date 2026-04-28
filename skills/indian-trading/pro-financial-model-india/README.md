# pro-financial-model-india

> **Skill for Claude Code** — Builds institutional-grade, 25-sheet Excel equity financial models for NSE/BSE-listed Indian companies, fully compliant with Ind AS, SEBI regulations, and Indian market conventions.

---

## Overview

This skill generates a comprehensive Excel financial model for any NSE or BSE-listed Indian stock — structured the way Kotak Institutional Equities, Motilal Oswal, Edelweiss, CLSA India, Morgan Stanley India, and Goldman Sachs India write their proprietary models. All data is fetched live; no hallucinated figures.

**Trigger command:**
```
/pro-financial-model-india [Company Name] [NSE Ticker]
```

**Examples:**
```
/pro-financial-model-india "Reliance Industries" RELIANCE
/pro-financial-model-india "HDFC Bank" HDFCBANK
/pro-financial-model-india "Infosys" INFY
/pro-financial-model-india "Tata Motors" TATAMOTORS
```

**Output:** `/mnt/user-data/outputs/[TICKER]_FinancialModel_India_[DATE].xlsx`

---

## What It Builds

A 25-sheet Excel workbook covering:

| Sheet | Name | Description |
|-------|------|-------------|
| 1 | Cover Page | CMP, rating, target price, Quick Stats (Market Cap, EV, P/E, EV/EBITDA, ROCE, ROE, Promoter%, Pledged%) |
| 2 | Table of Contents | Hyperlinked index + color legend + Ind AS note |
| 3 | Assumptions | Master input hub: macro (G-Sec, ERP, Repo rate), revenue (Bear/Base/Bull), margins, WC, capex, tax (25.168%), WACC |
| 4 | Income Statement | Ind AS format — Revenue from Operations, EBITDA (calculated), Finance Costs, PBT, PAT, OCI; 5Y historical + 3Y projected |
| 5 | Balance Sheet | Ind AS — Gross Block, Net Block, ROU Assets (Ind AS 116), NCI; auto-balance check |
| 6 | Cash Flow Statement | Indirect method, CFO/PAT quality ratio, all three activities; ties to BS cash |
| 7 | Revenue Build | Volume × Realisation by segment; domestic vs export; GST-adjusted net revenue; seasonal Q split |
| 8 | EBITDA Bridge | Waterfall: Volume / Price-Mix / RM / Employee / Other Opex; margin vs peers |
| 9 | Depreciation & Capex | Gross Block roll, Companies Act Schedule II rates, Capital WIP, ROU Asset schedule (Ind AS 116) |
| 10 | Working Capital | Debtor / Inventory / Creditor days, CCC, advances from customers |
| 11 | Debt & Interest Schedule | MCLR-linked term loans, NCDs, ECBs, WC facilities, lease liabilities; unhedged forex debt flag |
| 12 | DCF Valuation | FCFF, WACC (G-Sec Rf + India ERP), Gordon Growth / Exit EV/EBITDA TV; WACC × TGR sensitivity |
| 13 | Relative Valuation (Comps) | 8–12 NSE/BSE peers: P/E, EV/EBITDA, P/B, EV/Revenue, ROE, ROCE; football field |
| 14 | SOTP Valuation | Critical for conglomerates (Tata, Reliance, Bajaj, Mahindra); 20–30% HoldCo discount |
| 15 | Scenario & Sensitivity | Bear/Base/Bull; commodity price × volume sensitivity for relevant sectors |
| 16 | Technical Analysis | SMA/EMA, MACD, RSI, Bollinger Bands + Indian-specific: circuit breakers, F&O OI/PCR, delivery volume%, beta vs NIFTY |
| 17 | Fundamental Ratio Dashboard | 5Y history + projections; ROCE (primary Indian metric), ROE, ROIC, DuPont; PAT quality = CFO/PAT |
| 18 | Credit Analysis | CRISIL/ICRA/CARE rating grid, promoter pledge risk, unhedged forex, MSME supplier payment compliance |
| 19 | M&A Accretion-Dilution | CCI approval threshold (₹2,000 Cr), SEBI Open Offer / SAST, Ind AS 103 PPA |
| 20 | Dividend Discount Model | Post-FY21 DDT abolition; interim + final dividends; multi-stage DDM |
| 21 | Guidance vs Consensus | 8-quarter beat/miss history, EBITDA guidance, debt reduction targets |
| 22 | ESG & Non-Financial | SEBI BRSR framework (mandatory for top 1,000 listed cos); CSR 2% mandate (Section 135); LODR governance |
| 23 | Capital Allocation | PLI scheme capex; SEBI Buyback Regulations 2018 (max 25% of paid-up capital + free reserves) |
| 24 | Industry & Competitive | Sector-specific KPIs: BFSI NIM/GNPA/CAR, IT USD revenue/utilisation, Pharma ANDA/USFDA, Cement EBITDA/ton, Auto EV transition, Telecom ARPU |
| 25 | Output Summary | 12-month target price (₹); BUY/ACCUMULATE/HOLD/REDUCE/SELL rating; probability-weighted upside |

---

## India-Specific Features

- **Ind AS compliance** — Revenue from Operations (excludes Other Income), EBITDA calculated, Ind AS 116 ROU assets, Companies Act Schedule II depreciation
- **Indian currency & units** — ₹ Crore (large caps), ₹ Lakh (small caps), face-value-adjusted EPS
- **Fiscal year convention** — April 1 – March 31 (FY24 = Apr 2023 – Mar 2024)
- **SEBI BRSR ESG framework** — mandatory for top 1,000 listed companies
- **Ownership & governance flags** — promoter pledge >40% flagged in red, FPI foreign ownership ceiling tracking, SAST disclosures, related party transactions >10% of revenue flagged
- **SOTP valuation** — first-class support for Indian conglomerates and holding companies with 20–30% HoldCo discount
- **Indian tax structure** — base rate 22% + surcharge 10% + cess 4% = 25.168%; MAT applicability; Section 115BAB new manufacturing rate (17.01%)
- **CRISIL/ICRA/CARE credit grid** — rating-to-leverage mapping vs Indian bank covenant norms
- **F&O data** — Open Interest trend, Put-Call Ratio (PCR), futures premium/discount on Technical sheet
- **Circuit breakers** — Upper/lower 5%/10%/20% per SEBI regulations
- **India macro** — G-Sec 10Y yield as Rf (not US Treasury), India ERP (Damodaran), RBI repo rate, CPI, GDP growth
- **MCLR-linked debt** — weighted average cost of debt tracking, unhedged forex debt flagged per RBI guidelines
- **Corporate action adjustments** — QIPs, Rights Issues, Bonus issues, Stock splits (historical EPS/price adjusted)
- **NCLT/IBC monitoring** — debt restructuring proceedings noted
- **Sector-specific KPIs** — 11 sectors: BFSI, NBFC, IT/Tech, Pharma, Cement, Auto, Consumer/FMCG, Real Estate, Power, Metals, Telecom

---

## Data Sources

| Data | Source |
|------|--------|
| Financial statements (5Y) | Screener.in (consolidated) |
| Live CMP | Google Finance web search (not Screener.in — often stale) |
| Shareholding pattern | BSE/NSE filings, Screener.in |
| Analyst consensus | Moneycontrol, Trendlyne, Bloomberg India |
| Macro data | RBI website, Damodaran (ERP), MOSPI |
| Credit ratings | CRISIL, ICRA, CARE websites |
| Regulatory filings | BSE (bseindia.com), NSE (nseindia.com), SEBI |
| Quarterly data | Company IR pages, BSE/NSE filings |

---

## Prerequisites

- [Claude Code](https://claude.ai/code) with skills support
- The `xlsx` public skill installed (`/mnt/skills/public/xlsx/SKILL.md`) — provides Excel construction standards
- Internet access for live data fetching

---

## Installation

1. Copy the `skills/pro-financial-model-india/` directory into your Claude skills folder:
   - On macOS: `~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/[session-id]/skills/`
   - Or your configured skills mount point

2. Verify the skill appears in Claude Code by typing `/pro-financial-model-india`

---

## Color Coding Convention

| Color | Meaning |
|-------|---------|
| Blue font | Hardcoded inputs |
| Black font | Formulas and calculations |
| Green font | Cross-sheet links |
| Red font | External data links |
| Yellow fill | Key assumptions / data gaps |
| Orange fill | Risk flags (high pledge, high debt, RPT) |

---

## Output Example

```
RELIANCE_FinancialModel_India_2025-03-04.xlsx
├── [Sheet 1] Cover — Rating: BUY | TP: ₹1,650 | CMP: ₹1,280 | Upside: 28.9%
├── [Sheet 3] Assumptions — WACC: 11.2%, TGR: 5.5%, Tax: 25.17%
├── [Sheet 4] Income Statement — FY20A–FY24A | FY25E–FY27E
├── [Sheet 12] DCF — FCFF model, TV via Gordon Growth, Equity Value per share
├── [Sheet 14] SOTP — O2C / Retail / Jio / New Energy segments
└── [Sheet 25] Output — Probability-weighted TP; BUY conviction HIGH
```

---

## Guardrails

- Never hallucinate financial figures — data gaps shown as yellow cells with "Source: Unavailable — manual input required"
- Standalone vs Consolidated distinction maintained throughout
- For Banks/NBFCs/Insurance: DCF replaced with P/B or Gordon Growth; no EV/EBITDA multiples
- For loss-making companies: EV/Revenue or EV/Gross Profit used; flagged on Cover
- Promoter pledge >40%: prominently flagged in red on Cover Sheet
- Related party transactions >10% of revenue: flagged in Governance section

---

## License

MIT — free to use, modify, and distribute. Attribution appreciated.
