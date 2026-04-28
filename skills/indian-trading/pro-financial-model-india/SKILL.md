---
name: pro-financial-model-india
description: >
  ONLY trigger this skill when the user's message contains the exact slash command
  "/pro-financial-model-india". This skill must NEVER trigger based on natural language
  descriptions such as "build a financial model", "DCF", "equity model", "valuation",
  "Indian stock analysis", or any similar phrasing — no matter how relevant they seem.
  Trigger exclusively on the literal string "/pro-financial-model-india" and nothing else.
---

# Pro Financial Model — Indian Stocks (NSE/BSE)

Builds an **institutional-grade, 25-sheet Excel equity financial model** for any NSE/BSE-listed Indian company, following best practices from Goldman Sachs India, Kotak Institutional Equities, Motilal Oswal, Edelweiss, HDFC Securities, Emkay, CLSA India, Morgan Stanley India, and the CFA Institute — with full compliance to **Indian GAAP (Ind AS)**, **SEBI regulations**, and **Indian market conventions**.

---

## 0. Pre-Flight: Read Supporting Skills

Before writing any code, read `/mnt/skills/public/xlsx/SKILL.md` for Excel construction standards. These rules are **mandatory** and override any defaults.

---

## 1. Parse Arguments

Extract from `$ARGUMENTS`:
- `COMPANY_NAME` — full legal name (e.g., Reliance Industries Limited)
- `NSE_TICKER` — NSE ticker (e.g., RELIANCE). Prefix BSE: only as fallback
- `BSE_CODE` — 6-digit BSE scrip code (optional, used for fallback)
- `SECTOR` — BSE/NSE sector classification (infer if not provided)
- `FISCAL_YEAR_END` — Always **March 31** unless explicitly stated otherwise (e.g., HDFC Bank = March, some MNCs = December)
- `INDEX` — NIFTY 50 / NIFTY 500 / SENSEX / NIFTY Midcap 150 (infer)

If company is ambiguous, ask user to confirm NSE ticker before proceeding.

---

## 2. Indian-Specific Data Gathering (Mandatory Before Building)

Never hallucinate financial figures. Fetch all data from approved Indian sources.

### 2.1 Live CMP (Current Market Price) — CRITICAL
> ⚠️ Do NOT use Screener.in price — it is often stale cached data.

Canonical CMP method (present as instruction to user):
```
Open Google Sheets and enter: =GOOGLEFINANCE("NSE:[TICKER]", "price")
```
Or fetch from:
- `https://www.nseindia.com/get-quotes/equity?symbol=[TICKER]`
- `https://finance.yahoo.com/quote/[TICKER].NS`
- Search: `"[TICKER] NSE share price today"`

Collect: CMP (₹), 52-week High/Low (₹), Market Cap (₹ Cr), P/E (TTM), Face Value (₹), Dividend Yield%

### 2.2 Financial Statements — Annual (5 Years Historical)
Primary source: `https://www.screener.in/company/[TICKER]/consolidated/`
Fallback: Company IR page → Annual Reports (10+ year history often available)
Also fetch: BSE/NSE filings at `https://www.bseindia.com` or `https://www.nseindia.com`

**Ind AS Format — collect:**
- Standalone AND Consolidated financials (use Consolidated for valuation, note exceptions for holding companies)
- Revenue from Operations (not "Total Revenue" — note Ind AS vs old GAAP difference)
- Other Income (separately tracked in India — do NOT include in operating revenue)
- EBITDA (not directly reported in India — calculate: Revenue – COGS – Employee Costs – Other Expenses)
- EBIT = EBITDA – D&A
- Finance Costs (interest expense)
- PBT (Profit Before Tax)
- Tax (current + deferred)
- PAT (Profit After Tax = Net Income)
- EPS (Basic + Diluted, face-value adjusted)
- OCI (Other Comprehensive Income items)

### 2.3 Quarterly Data
- Last 8 quarters: Revenue, EBITDA, PAT, EPS
- YoY and QoQ growth rates
- Source: Company quarterly results filings on BSE/NSE

### 2.4 Balance Sheet (Ind AS Format)
Assets: Fixed Assets (Gross Block, Accumulated Depreciation, Net Block), Capital WIP, Intangible Assets, Goodwill, Right-of-Use Assets (Ind AS 116), Investments (current+non-current), Debtors, Inventory, Cash & Bank, Loans & Advances, Other Current Assets

Liabilities: Share Capital, Reserves & Surplus, Minority Interest (NCI), Long-term Borrowings, Deferred Tax Liabilities, Other LT Liabilities, Short-term Borrowings, Trade Payables, Other Current Liabilities, Provisions

Note: **Face Value** of shares matters in India (₹1, ₹2, ₹5, ₹10 common) — affects EPS calculation

### 2.5 Cash Flow Statement
CFO (Operating), CFI (Investing), CFF (Financing)
Indian P&L does not always present D&A separately — cross-reference with notes to accounts

### 2.6 Market & Ownership Data
- Search: `"[TICKER] NSE shareholding pattern promoter FII DII"`
- Promoter holding % (flag if <51%, <26%, or changing trend)
- FII/FPI holding % (foreign institutional ceiling: 24% general, sector-specific limits)
- DII holding % (LIC, Mutual Funds)
- Public holding %
- Pledged promoter shares % (high pledge = risk flag ⚠️)
- Insider buying/selling (SAST disclosure)

### 2.7 Analyst Consensus — India Specific
- Search: `"[COMPANY] consensus target price NSE analyst recommendation"`
- Sources: Moneycontrol, Economic Times Markets, Bloomberg India, Refinitiv
- Collect: Median target price (₹), Buy/Hold/Sell count, EPS estimates (FY+1, FY+2), Revenue estimates

### 2.8 Comparable Companies — Indian Peers
- Search: `"[COMPANY] Indian peers NSE sector [SECTOR]"`
- Identify 8–12 NSE/BSE-listed peers
- Fetch: P/E, EV/EBITDA, P/B, EV/Revenue, ROE, ROCE for each

### 2.9 Indian Macro Assumptions
- Search: `"India 10 year G-sec yield current"` → Risk-free rate (use RBI reference)
- Search: `"India equity risk premium Damodaran"` → ERP (India-specific)
- RBI repo rate (current), CPI inflation, GDP growth forecast, INR/USD rate
- Search: `"RBI monetary policy rate current [YEAR]"`

### 2.10 Regulatory & Corporate Actions
- Recent QIPs, Rights Issues, Bonus issues, Stock splits (adjust historical EPS/price)
- NCLT orders, SEBI orders, Debt restructuring (NCLT/IBC proceedings)
- Related party transactions (RPT disclosures) — flag high RPT%
- AGM resolutions, promoter buy/sell SAST disclosures

---

## 3. Indian Convention Adjustments

Apply these throughout the model:

| Parameter | Indian Convention |
|---|---|
| Currency | ₹ (Indian Rupee) |
| Units | ₹ Crore (Cr) for large caps; ₹ Lakh for small caps |
| Fiscal Year | April 1 – March 31 (label as FY24 = April 2023 – March 2024) |
| Revenue label | "Revenue from Operations" (exclude Other Income from operations) |
| Tax rate | 25.168% (base rate 22% + surcharge 10% + cess 4%) for domestic companies; 17.01% for Sec 115BAB new manufacturing; carry forward MAT if applicable |
| Depreciation | Companies Act 2013 Schedule II useful lives (mandatory) |
| Ind AS vs Old GAAP | Model uses Ind AS; note pre-FY18 data may be old GAAP |
| Multiple format | P/E displayed as "x" (e.g., 25x), EV/EBITDA as "x" |
| SEBI LODR | Board composition, RPT, audit committee compliance (note in governance) |
| Bonus/Split | Adjust historical EPS and price for corporate actions |

---

## 4. Excel Model Construction

Use `openpyxl`. Apply **all** color, formatting, and formula standards from the XLSX skill.

### Color Coding (Mandatory)
- Blue (0,0,255): All hardcoded inputs
- Black (0,0,0): All formulas
- Green (0,128,0): Cross-sheet links
- Red (255,0,0): External links
- Yellow background: Key assumptions / data gaps needing attention
- Orange background: Risk flags (high promoter pledge, high debt, RPT concerns)
- Negatives: In parentheses (never minus sign)
- Zeros: Display as "–" via number format `#,##0;(#,##0);–`

### Sheet Tab Color Coding
- Blue tabs: Financial Statements (IS, BS, CFS)
- Green tabs: Valuation (DCF, Comps, Precedents, SOTP, DDM)
- Orange tabs: Analysis (Scenarios, Sensitivity)
- Grey tabs: Supporting Schedules
- Red tabs: Cover, Output Summary
- White tabs: Assumptions, Dashboard

---

## 5. The 25-Sheet Model Architecture

Build **every sheet below** in this exact tab order:

### SHEET 1 — COVER PAGE
- Company name, NSE/BSE ticker, sector, index membership, face value, fiscal year end
- Report date, analyst name, model version
- Investment thesis: 3–5 bullet points
- Target Price (₹): 12-month forward, upside/(downside) to CMP
- Rating: BUY / ACCUMULATE / HOLD / REDUCE / SELL
- Quick Stats: CMP (₹), Market Cap (₹ Cr), EV (₹ Cr), EV/EBITDA, P/E (TTM+Forward), P/B, ROCE, ROE, Net Debt/EBITDA, Div Yield, 52W High/Low, Beta vs NIFTY, Promoter%, FII%, Pledged%
- Hyperlinks to all 25 sheets

### SHEET 2 — TABLE OF CONTENTS
- Hyperlinked index to every sheet
- Color coding legend
- Units legend (₹ Crore unless stated)
- Indian accounting standards note (Ind AS)

### SHEET 3 — ASSUMPTIONS (Master Input Hub)
All inputs here. All formulas in other sheets reference this sheet.

Blocks:
- [A] MACRO: G-Sec yield (10Y), India ERP, repo rate, CPI, GDP growth, INR/USD
- [B] REVENUE: Bear/Base/Bull growth rates by segment, volume, realisation/price, market share, GST impact
- [C] MARGINS: Gross/EBITDA/EBIT/PAT margins; raw material%, employee cost%, other expenses%
- [D] WORKING CAPITAL: Debtor days, Inventory days, Creditor days
- [E] CAPEX & D&A: Maintenance capex%, growth capex%, Companies Act Schedule II useful lives
- [F] CAPITAL STRUCTURE: D/E target, interest rate on debt (MCLR-linked), dividend payout%, buyback assumptions
- [G] TAX: Effective tax rate (base 22% + surcharge + cess = 25.168%), MAT applicability, deferred tax
- [H] VALUATION: WACC, terminal growth rate (Bear/Base/Bull), EV/EBITDA exit multiple, P/E multiple, SOTP NAV

### SHEET 4 — INCOME STATEMENT (Ind AS)
Columns: [5Y Historical FY20–FY24] | [TTM] | [FY25E/FY26E/FY27E]

Full Ind AS structure:
- Revenue from Operations (by segment if available) → Total Revenue from Operations, YoY Growth%
- Other Income (separately — NOT included in operating metrics)
- Raw Material / COGS
- Employee Benefits Expense
- Finance Costs (shown separately per Ind AS)
- Depreciation & Amortisation
- Other Expenses
- **EBITDA** (calculated: Rev from Ops – RM – Employee – Other Exp), EBITDA Margin%
- EBIT = EBITDA – D&A, EBIT Margin%
- PBT (Profit Before Tax) = EBIT – Finance Costs + Other Income
- Tax (Current + Deferred)
- PAT (Profit After Tax), PAT Margin%
- Minority Interest / Share of Associate
- PAT attributable to owners
- OCI items
- Total Comprehensive Income
- EPS Basic (₹), EPS Diluted (₹) — face-value adjusted
- DPS (₹), Payout Ratio%

### SHEET 5 — BALANCE SHEET (Ind AS)
Columns: [5Y Historical] | [5Y Projected]

Assets:
- Non-Current Assets: Property Plant & Equipment (Gross Block, Accumulated Depreciation, Net Block), Capital WIP, Intangible Assets, Goodwill, Right-of-Use Assets (Ind AS 116), Financial Assets (investments, loans), Deferred Tax Assets, Other NCA
- Current Assets: Inventories, Trade Receivables, Cash & Cash Equivalents, Bank Balances, Short-term Loans, Other Financial Assets, Other CA
- TOTAL ASSETS

Equity & Liabilities:
- Equity: Share Capital (face value × shares), Other Equity (Reserves & Surplus), Non-Controlling Interest
- Non-Current Liabilities: Financial Liabilities (borrowings, lease liabilities), Deferred Tax Liabilities, Provisions, Other NCL
- Current Liabilities: Financial Liabilities (STD, trade payables, lease current), Other Current Liabilities, Provisions, Current Tax Payable
- TOTAL EQUITY & LIABILITIES
- Balance check: `=IF(Assets=Equity+Liabilities,"✓ BALANCED","✗ ERROR")`

### SHEET 6 — CASH FLOW STATEMENT (Ind AS)
Columns: [5Y Historical] | [5Y Projected]

- Operating (Indirect): PAT → +D&A, +Finance costs, ±Deferred Tax, ±Trade Receivables, ±Inventories, ±Trade Payables, ±Other WC → CFO
- CFO/PAT ratio (quality metric — flag if <0.8)
- Investing: –Capex (purchase of PPE), –Acquisitions, +Asset sales, ±Investments → CFI
- Financing: +Borrowings (net), –Repayment, –Finance costs paid, –Dividends paid, –Buybacks → CFF
- Net Change in Cash; Opening + Closing Cash (ties to BS)

### SHEET 7 — REVENUE BUILD
Segment-wise revenue breakdown:
- Volume (units/tonnes/sq ft as applicable) × Realisation (₹) = Segment Revenue
- YoY volume growth%, realisation growth%, mix shift
- Geographic split (domestic vs export in ₹ Cr)
- GST implications (net revenue = ex-GST)
- Seasonal adjustment (Q1–Q4 split if available)

### SHEET 8 — EBITDA BRIDGE & MARGIN ANALYSIS
Waterfall: Prior year EBITDA → +/– Volume → +/– Price/Mix → +/– Raw Material → +/– Employee → +/– Other Opex → Current year EBITDA

Margin drivers: RM as % of revenue (key for manufacturing); employee cost%; other expense%
Operating leverage analysis: Revenue growth vs EBITDA growth
Peer margin comparison table

### SHEET 9 — DEPRECIATION & CAPEX SCHEDULE
Gross Block opening + additions – disposals = Gross Block closing
Accumulated Depreciation (Companies Act Schedule II rates by asset class)
Net Block = Gross Block – Acc Depr
Capital WIP movement
Maintenance Capex vs Growth Capex split
Capex/Revenue%, Capex/D&A ratio
Right-of-Use Asset schedule (Ind AS 116): lease additions, amortisation, lease liability

### SHEET 10 — WORKING CAPITAL SCHEDULE
Trade Receivables: Debtor days = (TR/Revenue)×365
Inventories: Inventory days = (Inv/COGS)×365
Trade Payables: Creditor days = (TP/Purchases)×365
Cash Conversion Cycle = Debtor days + Inventory days – Creditor days
NWC = Current Assets (ex-cash) – Current Liabilities (ex-debt)
ΔNWC year-on-year (feeds into CFS)
Advances from customers (important in Indian context — construction, defence, infra)

### SHEET 11 — DEBT & INTEREST SCHEDULE
Debt waterfall: Opening balance + drawdowns – repayments = Closing balance
Tranches: Term loans (PSU banks, private banks), NCDs, ECBs, Working capital facilities, Lease liabilities
Interest rate: MCLR-linked / fixed; weighted average cost of debt
Interest coverage ratio (EBIT/Finance costs) — flag if <2x
Net Debt = Total Debt + Lease Liabilities – Cash & Equivalents
Net Debt/EBITDA by year
Unhedged forex debt (flag per RBI guidelines)

### SHEET 12 — DCF VALUATION (Indian Convention)
- Projection period: 5–10 years explicit FCF
- **FCFF** = EBIT × (1–Tax) + D&A – Capex – ΔNWC
- WACC = Ke×(E/V) + Kd×(1–t)×(D/V)
  - Ke = G-Sec 10Y yield + India ERP + Beta × ERP + size/liquidity premium
  - Kd = Weighted average interest rate on debt (post-tax)
- Terminal Value: Gordon Growth (g = long-run India GDP, typically 5–6%) or Exit EV/EBITDA
- PV of FCFs + PV of TV = Enterprise Value
- Less: Net Debt (including lease liabilities per Ind AS 116)
- Less: Minority Interest at market value
- Add: Investments at market value / book value
- Equity Value ÷ Diluted Shares = Intrinsic Value per Share (₹)
- Sensitivity: WACC (±1%) × Terminal Growth Rate (±0.5%) → price grid
- Sensitivity: WACC × Exit EV/EBITDA multiple → price grid

### SHEET 13 — RELATIVE VALUATION (Indian Comps)
8–12 NSE/BSE-listed peers. Columns: Company | Ticker | Market Cap (₹ Cr) | CMP (₹) | P/E TTM | P/E FY+1 | EV/EBITDA TTM | EV/EBITDA FY+1 | P/B | EV/Revenue | ROE | ROCE | Revenue Growth | EBITDA Margin

Implied valuation range from median/mean multiples applied to subject company
Football field chart data (all methods, min/max/median)
India sector premium/discount discussion

### SHEET 14 — SOTP VALUATION (Sum-of-the-Parts)
Critical for: Conglomerates (Tata, Mahindra, Bajaj, Reliance), Holding Companies, Diversified PSUs

| Segment | Methodology | Revenue/EBITDA/NAV | Multiple | Enterprise Value (₹ Cr) |
|---|---|---|---|---|
| Segment A | EV/EBITDA | X | Yx | Z |
| Investments | Market value / 20% HoldCo discount | — | — | Z |

Total EV → Less Net Debt → Equity Value → Per share (₹)
HoldCo discount: Standard 20–30% in India (note SEBI's stance)
Unlisted subsidiary valuation (P/E or DCF)

### SHEET 15 — SCENARIO & SENSITIVITY ANALYSIS
3 scenarios: Bear / Base / Bull

Per scenario: Revenue CAGR, EBITDA Margin, Terminal Growth Rate, WACC → Implied Target Price (₹) → Upside/(Downside)%

Sensitivity tables:
- WACC × Terminal Growth → DCF Price (₹)
- Revenue CAGR × EBITDA Margin → EV/EBITDA implied
- Commodity price (for relevant sectors: steel, cement, oil) × Volume → EBITDA

### SHEET 16 — TECHNICAL ANALYSIS DASHBOARD
Manual input: Date | Open | High | Low | Close (₹) | Volume (shares) | Delivery Volume%

Calculated: SMA 20/50/100/200D, EMA 12/26D, MACD, RSI (14D), Bollinger Bands, ATR, OBV, Stochastic, VWAP

Indian-specific additions:
- Circuit breaker levels: Upper (5%/10%/20%), Lower (5%/10%/20%) per SEBI regulations
- F&O data: Open Interest (OI) trend, Put-Call Ratio (PCR), futures premium/discount
- Delivery volume% (high delivery = strong conviction buying vs intraday speculation)
- FII/DII net buying (monthly)
- 52-week High/Low distance
- Beta vs NIFTY 50

### SHEET 17 — FUNDAMENTAL RATIO DASHBOARD
5Y historical + 5Y projected. Indian conventions:

[VALUATION]: P/E, Forward P/E, PEG, EV/EBITDA, EV/EBIT, EV/Revenue, EV/FCF, P/B, P/TBV, P/CF, P/S, Div Yield, Shareholder Yield, Graham Number (₹)

[PROFITABILITY]: Gross/EBITDA/EBIT/PBT/PAT/FCF Margins (on Revenue from Operations, excluding Other Income)

[RETURNS — Indian emphasis]:
- **ROCE** = EBIT / (Net Worth + Total Debt) — primary metric for Indian analysts
- **ROE** = PAT / Average Net Worth
- **ROA** = PAT / Average Total Assets
- **ROIC** = NOPAT / Invested Capital
- EVA = NOPAT – (IC × WACC)
- Asset-light score (FCF/EBITDA)

[LIQUIDITY]: Current Ratio, Quick Ratio, Cash Ratio
[SOLVENCY]: D/E, Net Debt/EBITDA, Interest Coverage, DSCR, Altman Z-Score (India-calibrated)
[EFFICIENCY]: Debtor days, Inventory days, Creditor days, CCC, Asset Turnover, Fixed Asset Turnover
[GROWTH]: Revenue CAGR (1/3/5Y), EBITDA CAGR, PAT CAGR, EPS CAGR, BV/Share Growth
[PER SHARE]: EPS (Basic/Diluted), DPS, BV/Share, Tangible BV/Share, Cash/Share, FCF/Share
[QUALITY]: PAT quality = CFO/PAT (>1 = good), Accruals ratio, WC intensity, Capex intensity

### SHEET 18 — CREDIT ANALYSIS (Indian Context)
CRISIL/ICRA/CARE credit rating mapping to leverage ratios
Promoter pledge% and pledged share value vs loan outstanding
Interest coverage vs Indian bank covenant norms
Debt maturity profile (Indian banks typically 3–5Y tenors)
Unhedged forex debt risk (% of total debt; RBI monitoring threshold)
MSME supplier exposure (payment within 45 days mandatory per MSMED Act)

### SHEET 19 — M&A ACCRETION-DILUTION
Indian-specific: CCI approval threshold (transactions >₹2,000 Cr trigger CCI review)
SEBI Open Offer (SAST): Acquiring >25% triggers mandatory open offer for additional 26%
Post-merger Ind AS 103 (Business Combinations): Goodwill impairment testing
Deferred tax on fair value step-ups

### SHEET 20 — DIVIDEND DISCOUNT MODEL
Dividend history (India: interim + final dividends common)
Post-FY21: DDT abolished; dividend taxed in hands of shareholders
Multi-stage DDM; Justified P/E; Gordon Growth

### SHEET 21 — MANAGEMENT GUIDANCE vs CONSENSUS
Compare: Management commentary vs Analyst estimates
Beat/miss history (last 8 quarters)
EBITDA margin guidance; Capital allocation guidance; Debt reduction targets

### SHEET 22 — ESG & NON-FINANCIAL (SEBI BRSR Framework)
SEBI mandates Business Responsibility and Sustainability Report (BRSR) for top 1,000 listed companies

[Environmental per BRSR]: GHG Scope 1/2/3, Energy intensity, Water intensity, Waste, Green certifications
[Social per BRSR]: CSR spend (mandatory 2% of avg net profit per Cos Act 2013 Section 135), Employee welfare, Safety, Diversity
[Governance per SEBI LODR 2015]: Board independence (min 50%), Women director (mandatory 1), MD/CEO separation, RPT approval, Audit Committee, SEBI compliance
Promoter governance: Pledging, family succession, related party transactions as % of revenue

### SHEET 23 — CAPITAL ALLOCATION (Indian Context)
CFO generation; Reinvestment (Capex, acquisitions, subsidiaries); Shareholder returns (dividend, buyback per SEBI Buyback Regulations 2018)

PLI scheme capex commitments; government contract advances; ESOP grants (Ind AS 102)
Buyback: SEBI allows max 25% of (paid-up capital + free reserves) per year

### SHEET 24 — INDUSTRY & COMPETITIVE ANALYSIS
Indian sector dynamics:
- Regulatory environment (SEBI, RBI, IRDAI, TRAI, MCA, DPIIT)
- Government schemes impact (PLI, NIP, Smart Cities, etc.)
- Import substitution / China+1 opportunity
- Formalization tailwinds (post-GST beneficiaries)
- Rural vs Urban demand split and outlook

Indian-specific KPIs by sector:
- BFSI: NIM, GNPA%, NNPA%, PCR, CASA%, Credit-Deposit ratio, CAR, Tier 1, RoA, RoE, Cost-to-Income
- NBFCs: AUM, Disbursements, GNP%, Cost of borrowing, ALM profile, Capital Adequacy
- IT/Technology: Revenue in USD, onsite/offshore mix, utilisation%, attrition%, EBIT margin
- Pharma: Domestic formulations growth, ANDA filings, US generic price erosion, USFDA status
- Cement: Volume (MT), Realisation (₹/ton), Cost (₹/ton), EBITDA/ton, capacity utilisation%
- Auto: Domestic volume by segment (2W/PV/CV/Tractor), EV transition, content/vehicle
- Consumer/FMCG: Volume growth, value growth, gross margin, ad spend%, rural vs urban
- Real Estate: Pre-sales (₹ Cr), launches (sq ft), collections, net debt, RERA compliance
- Power/Utilities: PLF%, tariff, PPA mix, RE capacity (MW), generation (BUs)
- Metals/Mining: Production volume, LME price, EBITDA/ton, net debt, capacity expansion
- Telecom: ARPU (₹), subscriber base, 5G capex, spectrum liability, net debt

### SHEET 25 — OUTPUT SUMMARY & INVESTMENT RECOMMENDATION
One-page executive summary (Indian broker research format):
- Company snapshot + investment thesis
- Key risks
- Financial summary: FY22A/FY23A/FY24A + FY25E/FY26E/FY27E
- Valuation summary: All methods, implied CMP (₹)
- **Final Target Price (₹)**: 12-month forward (Indian convention)
- Implied return from CMP: Upside/(downside)%
- Rating: **BUY / ACCUMULATE / HOLD / REDUCE / SELL** (5-tier Indian convention)
- Risk rating: LOW / MEDIUM / HIGH
- Near-term catalysts (1–2 quarter horizon)
- Key risks: Regulatory, competitive, macro (India-specific)

---

## 6. Quality Checks Before Saving

- [ ] All amounts in ₹ Crore (or stated unit) consistently
- [ ] Fiscal years labeled as FY24 (not CY2024) unless company uses calendar year
- [ ] Revenue from Operations excludes Other Income
- [ ] Balance Sheet: Assets = Equity & Liabilities every year
- [ ] PAT on CFS matches IS PAT every year
- [ ] EPS adjusted for any bonus/split/rights in historical periods
- [ ] ROCE and ROE calculated correctly
- [ ] Net Debt includes lease liabilities (Ind AS 116)
- [ ] All #REF!, #DIV/0!, #VALUE!, #N/A, #NAME? = ZERO

Run: `python scripts/recalc.py [output_file].xlsx 60`
Fix all errors. Re-run to confirm `"status": "success"`.

---

## 7. Output

Save to: `/mnt/user-data/outputs/[TICKER]_FinancialModel_India_[DATE].xlsx`

Call `present_files` with the output path.

Summarize: Company modeled, FY historical coverage, projection horizon, target price (₹), rating, data gaps flagged.

---

## Notes & Guardrails

- **Never hallucinate financial figures.** Flag unavailable data with yellow cells + comment "Source: Unavailable — manual input required"
- For holding companies (HoldCo): Use SOTP as primary valuation, DCF as secondary
- For financials (Banks/NBFCs/Insurance): Replace DCF with P/B or Gordon Growth; no EBITDA/EV multiples
- For loss-making companies: Use EV/Revenue or EV/Gross Profit; flag in Cover
- Promoter pledge >40%: Flag prominently in red on Cover Sheet
- Related party transactions >10% of revenue: Flag and note in Governance section
- Small caps (market cap <₹500 Cr): Reduce comps to 5–8 peers; note limited liquidity risk
- Ensure Standalone vs Consolidated distinction is clear in all sheets
