# Task 3: Valuation Analysis - Detailed Workflow

This document provides step-by-step instructions for executing Task 3 (Valuation Analysis) of the initiating-coverage skill.

## Task Overview

**Purpose**: Perform comprehensive valuation using DCF, comparables, and precedent transactions.

**Prerequisites**: ⚠️ Verify before starting
- **Required**: Financial model from Task 2
  - Projected income statements
  - Projected cash flows
  - Revenue and EBITDA forecasts
  - DCF inputs (unlevered FCF)

**⚠️ CRITICAL: DO NOT START THIS TASK UNLESS TASK 2 IS COMPLETE**

This task requires the financial model from Task 2. Starting without it will result in incomplete work.

**IF TASK 2 IS NOT COMPLETE**: Stop immediately and inform the user that Task 2 (Financial Modeling) must be completed first. Do not attempt to proceed or create placeholder valuations.

**Output**: Valuation Analysis (4-6 pages + Excel tabs)
- DCF analysis with sensitivity tables
- Comparable companies analysis
- Precedent transactions (if applicable)
- Valuation football field
- Price target and recommendation

---

## Input Verification

**BEFORE STARTING - CHECK:**
- [ ] Task 2 complete? (Financial model exists)
- [ ] Model file path/location known?
- [ ] Can access projected financials from model?

**Required from model:**
- [ ] Projected FCF (5 years)
- [ ] Revenue projections
- [ ] EBITDA projections
- [ ] Terminal year metrics
- [ ] Balance sheet data (debt, cash, shares)

**IF VERIFICATION FAILS**: Stop and complete Task 2 (Financial Modeling) before proceeding.

---

## Detailed Methodology Reference

For deep dive on valuation methodologies, formulas, and theory, see:
**[valuation-methodologies.md](valuation-methodologies.md)**

This workflow document focuses on execution steps. Reference the methodology file for:
- DCF theory and formulas
- WACC calculation details
- Terminal value methods
- Comparable companies theory
- Precedent transactions theory

---

## Step-by-Step Valuation Workflow

### Step 1: Extract Data from Financial Model

**From Task 2's financial model, extract:**

1. **Projected Financials (5 years)**
   - Revenue by year (2025E-2029E)
   - EBITDA by year
   - EBIT by year
   - Tax rate
   - D&A by year
   - CapEx by year
   - Change in NWC by year

2. **Unlevered Free Cash Flow**
   ```
   Extract from DCF Inputs tab in financial model:

                   2025E   2026E   2027E   2028E   2029E
   EBIT            ₹X,XXXX    ₹X,XXXX    ₹X,XXXX    ₹X,XXXX    ₹X,XXXX
   × (1 - Tax Rate)
   = NOPAT         ₹X,XXXX    ₹X,XXXX    ₹X,XXXX    ₹X,XXXX    ₹X,XXXX
   + D&A           ₹X,XXXX    ₹X,XXXX    ₹X,XXXX    ₹X,XXXX    ₹X,XXXX
   - CapEx         (₹X,XXX)   (₹X,XXX)   (₹X,XXX)   (₹X,XXX)   (₹X,XXX)
   - Chg in NWC    (₹X,XXX)   (₹X,XXX)   (₹X,XXX)   (₹X,XXX)   (₹X,XXX)
   = Unlevered FCF ₹X,XXXX    ₹X,XXXX    ₹X,XXXX    ₹X,XXXX    ₹X,XXXX
   ```

3. **Balance Sheet Data (current)**
   - Total debt
   - Cash & equivalents
   - Net debt (Debt - Cash)
   - Diluted shares outstanding

4. **Scenario Data**
   - Bull case revenue CAGR and terminal margin
   - Base case revenue CAGR and terminal margin
   - Bear case revenue CAGR and terminal margin

### Step 2: Build DCF Analysis

#### A. Calculate WACC

**1. Determine Risk-Free Rate**
   - Use 10-year India G-Sec yield (check current rate)
   - Example: 4.0-4.5% as of late 2024

**2. Determine Cost of Equity (CAPM)**
   ```
   Cost of Equity = Risk-Free Rate + Beta × India Equity Risk Premium

   Inputs:
   - Risk-Free Rate: [Current 10-year India G-Sec, e.g., 4.2%]
   - Beta: [Company beta from Bloomberg/Screener.in or peer average]
   - India India Equity Risk Premium: 7-8% (includes country risk premium) (historical average)

   Example:
   Cost of Equity = 4.2% + 1.3 × 5.5% = 11.35%
   ```

**3. Determine Cost of Debt**
   ```
   Cost of Debt = Current borrowing rate or implied yield on bonds

   For private companies:
   Cost of Debt = Risk-Free Rate + Credit Spread (based on rating)

   Example:
   Cost of Debt (pre-tax) = 6.5%
   Cost of Debt (after-tax) = 6.5% × (1 - 25% tax rate) = 4.875%
   ```

**4. Determine Capital Structure**
   ```
   Use market values (not book values):

   Market Value of Equity (E) = Share Price × Shares Outstanding
   Market Value of Debt (D) = Total Debt (use book value if bonds not traded)
   Total Value (V) = E + D

   Weight of Equity = E / V
   Weight of Debt = D / V

   Example:
   E = ₹50,000 Cr (90.9%)
   D = ₹50,000 Cr (9.1%)
   V = ₹55,000 Cr (100%)
   ```

**5. Calculate WACC**
   ```
   WACC = (E/V × Cost of Equity) + (D/V × Cost of Debt × (1 - Tax Rate))

   Example:
   WACC = (90.9% × 11.35%) + (9.1% × 6.5% × (1 - 25%))
   WACC = 10.32% + 0.44% = 10.76%

   Round to: 10.8% for base case
   ```

#### B. Calculate Terminal Value

**Method 1: Perpetuity Growth (Preferred)**
```
Terminal Value = FCF(2029) × (1 + g) / (WACC - g)

Where:
- FCF(2029) = Final year unlevered FCF from model
- g = Perpetual growth rate (typically 2.0-3.0%)
  - Should not exceed long-term GDP growth
  - Use 2.5% as base case

Example:
FCF(2029) = ₹50,000 Cr
g = 2.5%
WACC = 10.8%

Terminal Value = ₹50,000 Cr × (1.025) / (0.108 - 0.025)
Terminal Value = ₹51,025 Cr / 0.083 = ₹61,750 Cr
```

**Method 2: Exit Multiple (Alternative)**
```
Terminal Value = EBITDA(2029) × Exit Multiple

Where:
- Exit Multiple = Current peer trading median (e.g., 12-15x EBITDA)

Example:
EBITDA(2029) = ₹8,000 Cr
Exit Multiple = 13x

Terminal Value = ₹8,000 Cr × 13x = ₹1,04,000 Cr
```

**Choose one method or average both.**

#### C. Discount Cash Flows to Present Value

```
PV of Projected FCF = Σ [FCFt / (1 + WACC)^t] for t = 1 to 5

Example:
Year    FCF      Discount    PV of FCF
        ( ₹ Cr)     Factor      ( ₹ Cr)
2025    ₹2,500 Cr     1/(1.108)^1 = 0.9026    ₹2,260 Cr
2026    ₹3,200 Cr     1/(1.108)^2 = 0.8147    ₹2,610 Cr
2027    ₹3900     1/(1.108)^3 = 0.7353    ₹2,870 Cr
2028    ₹4500     1/(1.108)^4 = 0.6636    ₹2,990 Cr
2029    ₹5000     1/(1.108)^5 = 0.5988    ₹2,990 Cr
                              Total PV:  ₹13,720 Cr

PV of Terminal Value = Terminal Value / (1 + WACC)^5
PV of Terminal Value = ₹61,750 Cr / (1.108)^5 = ₹61,750 Cr × 0.5988 = ₹36,970 Cr

Enterprise Value = ₹13,720 Cr + ₹36,970 Cr = ₹50,690 Cr
```

#### D. Calculate Equity Value and Price Per Share

```
Enterprise Value                 ₹50,690 Cr
- Net Debt (Debt - Cash)         (₹45,000 Cr)
+ Non-operating Assets           ₹0
- Minority Interest              ₹0
- Preferred Stock                ₹0
= Equity Value                   ₹46,190 Cr

Diluted Shares Outstanding       100M

Price Per Share = ₹46,190 Cr / 100M = ₹461.90

Current Stock Price: ₹420
Implied Upside: 10.0%
```

#### E. DCF Sensitivity Analysis **CRITICAL**

**Table 1: WACC vs. Terminal Growth Rate**

Create 2-way sensitivity table:
```
Price Per Share ($)     Terminal Growth Rate
WACC        1.5%    2.0%    2.5%    3.0%    3.5%
9.0%        ₹520     ₹550     ₹590     ₹630     ₹680
9.5%        ₹480     ₹510     ₹540     ₹580     ₹620
10.0%       ₹450     ₹480     ₹510     ₹540     ₹570
10.5%       ₹420     ₹450     ₹470     ₹500     ₹530
11.0%       ₹400     ₹420     ₹440     ₹470     ₹500
11.5%       ₹380     ₹400     ₹420     ₹440     ₹470
12.0%       ₹360     ₹380     ₹400     ₹420     ₹440

Base Case: WACC = 10.8%, g = 2.5% → ₹460
Format as heatmap: Green (high values) → Yellow → Red (low values)
```

**Table 2: Revenue CAGR vs. Terminal EBITDA Margin**
```
Price Per Share ($)     Terminal EBITDA Margin (2029E)
Revenue CAGR    28%     30%     32%     34%     36%
15%             ₹380     ₹420     ₹460     ₹500     ₹540
20%             ₹420     ₹460     ₹510     ₹560     ₹610
25%             ₹460     ₹510     ₹560     ₹620     ₹680
30%             ₹510     ₹560     ₹620     ₹680     ₹750
35%             ₹560     ₹620     ₹680     ₹750     ₹830

Base Case: Rev CAGR = 25%, EBITDA Margin = 32% → ₹560
```

### Step 3: Comparable Companies Analysis

#### A. Select Comparable Companies

**Selection Criteria:**
- Same industry/sector (primary requirement)
- Similar business model
- Comparable size (market cap, revenue)
- Similar growth profile
- Similar geographies

**Identify 5-10 peer companies:**
1. [Peer 1] - Direct competitor
2. [Peer 2] - Direct competitor
3. [Peer 3] - Adjacent player
4. [Peer 4] - Similar business model
5. [Peer 5] - Regional competitor
6. [Add 3-5 more]

**Document rationale for each peer selected.**

#### B. Gather Peer Financial Data

**For each comparable, gather:**
- Current stock price
- Shares outstanding (diluted)
- Market capitalization
- Total debt and cash (for EV calculation)
- Enterprise value
- LTM (Last Twelve Months) financials:
  - Revenue
  - EBITDA
  - EBIT
  - Net Income
- NTM (Next Twelve Months) consensus estimates
- Revenue growth rate
- EBITDA margin

**Data sources:**
- Bloomberg, Ace Equity, CMIE Prowess (preferred)
- Company Annual Reports/Quarterly Results for actuals
- Consensus estimates from Screener.in/Moneycontrol, Trendlyne/Company IR site (if pro tools unavailable)

#### C. Calculate Valuation Multiples

**For each peer, calculate:**
```
EV/Revenue (LTM) = Enterprise Value / LTM Revenue
EV/Revenue (NTM) = Enterprise Value / NTM Revenue (est.)
EV/EBITDA (LTM) = Enterprise Value / LTM EBITDA
EV/EBITDA (NTM) = Enterprise Value / NTM EBITDA (est.)
P/E (NTM) = Market Cap / NTM Net Income (est.)
```

#### D. Create Comparable Companies Table (MANDATORY FORMAT)

```
COMPARABLE COMPANIES ANALYSIS

Company      Ticker  Mkt Cap  EV/Rev  EV/Rev  EV/EBITDA  EV/EBITDA  P/E   Rev     EBITDA
                     (₹ '000 Cr)     LTM     NTM     LTM        NTM        NTM   Growth  Margin
Peer A       PRA     45.2     3.5x    3.2x    15.2x      13.8x      25x   18%     23%
Peer B       PRB     32.8     3.2x    2.9x    14.1x      12.5x      22x   15%     23%
Peer C       PRC     28.5     2.8x    2.6x    12.8x      11.2x      20x   12%     22%
Peer D       PRD     52.1     4.1x    3.7x    17.5x      15.2x      29x   22%     23%
Peer E       PRE     38.9     3.6x    3.3x    15.8x      14.1x      25x   17%     23%
Peer F       PRF     41.2     3.7x    3.4x    16.1x      13.9x      26x   19%     23%
Peer G       PRG     35.5     3.3x    3.0x    14.5x      12.8x      23x   16%     22%

[Target]     TRGT    38.0     3.4x    3.1x    14.8x      13.0x      24x   17%     23%

STATISTICAL SUMMARY
Maximum              52.1     4.1x    3.7x    17.5x      15.2x      29x   22%     23%
75th Percentile      45.2     3.7x    3.4x    16.1x      14.1x      26x   19%     23%
Median               38.9     3.5x    3.2x    15.2x      13.8x      25x   17%     23%
25th Percentile      32.8     3.2x    2.9x    14.1x      12.5x      22x   15%     22%
Minimum              28.5     2.8x    2.6x    12.8x      11.2x      20x   12%     22%

Note: Market data as of [Date]. LTM = Last Twelve Months. NTM = Next Twelve Months.
Source: FactSet, Screener.in, BSE/NSE filings, [Analyst] estimates.
```

**CRITICAL**: The statistical summary (max/75th/median/25th/min) is MANDATORY.

#### E. Apply Multiples to Target Company

**Choose primary multiple (typically EV/EBITDA for mature companies):**

```
Target Company NTM EBITDA = ₹55,000 Cr (from financial model)

Apply Median Peer Multiple:
Peer Median EV/EBITDA (NTM) = 13.8x
Implied EV = ₹55,000 Cr × 13.8x = ₹75,900 Cr

Apply 25th Percentile (Conservative):
25th Percentile EV/EBITDA (NTM) = 12.5x
Implied EV = ₹55,000 Cr × 12.5x = ₹68,750 Cr

Apply 75th Percentile (Optimistic):
75th Percentile EV/EBITDA (NTM) = 14.1x
Implied EV = ₹55,000 Cr × 14.1x = ₹77,550 Cr

Valuation Range (Comps): ₹68,750 Cr - ₹77,550 Cr
Midpoint: ₹73,150 Cr

Convert to Equity Value:
Implied EV (Median)        ₹75,900 Cr
- Net Debt                 (₹45,000 Cr)
= Implied Equity Value     ₹71,400 Cr

Shares Outstanding         100M
Implied Price/Share        ₹714
```

**Justify Premium/Discount:**
- Target is growing 17% vs. peer median 17% → In-line
- Target EBITDA margin 23% vs. peer median 23% → In-line
- Target market position → [Justify premium/discount]
- **Conclusion**: Apply median multiple (no adjustment)

### Step 4: Precedent Transactions (Optional)

**Note**: Only if M&A is relevant for this sector/company.

#### A. Identify Relevant Transactions

**Search for 5-10 M&A deals:**
- Same industry, last 3-5 years
- Similar size (0.5x to 2x target's size)
- Announced and closed deals

**Example:**
```
PRECEDENT TRANSACTIONS ANALYSIS

Date     Target        Acquirer      Deal     EV/Rev  EV/EBITDA  Premium  Rationale
                                    Value(₹ '000 Cr)  LTM     LTM
Q1 2024  Comp A       Strategic      ₹52,000 Cr    4.2x    16.5x      35%      Consolidation
Q3 2023  Comp B       PE Firm        ₹38,000 Cr    3.8x    14.2x      28%      Platform
Q4 2023  Comp C       Strategic      ₹45,000 Cr    4.0x    15.8x      32%      Geographic
Q2 2023  Comp D       Strategic      ₹61,000 Cr    4.5x    17.2x      38%      Strategic fit
Q1 2023  Comp E       PE Firm        ₹32,000 Cr    3.5x    13.5x      25%      Carve-out

Median                                        4.0x    15.8x      32%

Source: Ace Equity/CMIE Prowess, company filings, press releases.
```

#### B. Apply to Target Company

```
Target Company LTM EBITDA = ₹50,000 Cr
Precedent Median EV/EBITDA (LTM) = 15.8x

Implied EV (Precedent) = ₹50,000 Cr × 15.8x = ₹79,000 Cr

Note: Precedent multiples typically 10-20% higher than trading comps
due to control premium and synergies.
```

### Step 5: Valuation Reconciliation

#### A. Create Valuation Summary Table

```
VALUATION SUMMARY

Method                  Low     Base    High    Weight  Weighted Value
DCF Analysis            ₹420     ₹460     ₹510     50%     ₹230
Trading Comps (NTM)     ₹640     ₹710     ₹780     40%     ₹284
Precedent Trans.        ₹700     ₹790     ₹880     10%     ₹79
                                                        -------
Weighted Average Target                         100%    ₹590.30

Rounded Price Target: ₹590.00

Current Price (as of [Date]):    ₹420
Upside to Target:                40% (₹590.00 / ₹420 - 1)
```

#### B. Determine Weighting Rationale

**Typical Weighting:**
- DCF: 40-60% (higher when forecasts reliable)
- Trading Comps: 25-40% (reflects market sentiment)
- Precedent Trans: 10-25% (lower unless M&A likely)

**For this example:**
- DCF 50%: High confidence in projections
- Comps 40%: Robust peer set
- Precedent 10%: M&A unlikely near-term

#### C. Create Valuation Football Field Chart

```
VALUATION FOOTBALL FIELD

Method                  Low ◄────────── Range ──────────► High

DCF Analysis            ₹420 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ₹510

Trading Comps (NTM)     ₹640 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ₹780

Precedent Trans.        ₹700 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ₹880
                                          ↑
                                    Current: ₹420
─────────────────────────────────────────────────────────
Valuation Range         ₹420                          ₹880
Price Target: ₹590 (weighted average)

Color code:
- DCF: Blue
- Trading Comps: Green
- Precedent Trans: Orange
- Vertical line at current price: Red dashed
- Vertical line at target: Black solid
```

#### D. Scenario-Based Valuations

```
VALUATION BY SCENARIO

Scenario    Probability  Revenue  EBITDA    DCF      Comps    Weighted
                        CAGR     Margin    Value    Multiple  Avg
Bear Case   20%         18%      28%       ₹380      11.5x     ₹420
Base Case   60%         25%      32%       ₹460      13.8x     ₹590
Bull Case   20%         32%      36%       ₹580      16.0x     ₹820

Expected Value (probability-weighted): ₹590
```

### Step 6: Final Price Target & Recommendation

```
═══════════════════════════════════════════════════════════
INVESTMENT RECOMMENDATION
═══════════════════════════════════════════════════════════

Current Price:          ₹420 (as of [Date])
Price Target:           ₹590.00 (12-month)
Upside/(Downside):      +40.5%

Rating:                 BUY / OUTPERFORM

Valuation Methodology:  Based on weighted average of DCF (50%),
                       trading comparables (40%), and precedent
                       transactions (10%).

Time Horizon:          12 months

───────────────────────────────────────────────────────────
KEY INVESTMENT CATALYSTS
───────────────────────────────────────────────────────────

1. New Product Launch (Q2 2025)
   - Expected to drive 15-20% revenue acceleration
   - Already seeing strong pre-orders

2. Margin Expansion (FY2025-2026)
   - Operating leverage from scale
   - Path to 35% EBITDA margin (from current 28%)

3. Market Share Gains (Ongoing)
   - Taking share from legacy competitors
   - Net Promoter Score improvement

4. International Expansion (H2 2025)
   - Entry into European markets
   - Potential ₹X,XXX Cr incremental revenue opportunity

5. Potential M&A Target (12-18 months)
   - Strategic fit for larger players
   - Precedent transactions suggest 30-40% premium

───────────────────────────────────────────────────────────
KEY RISKS TO PRICE TARGET
───────────────────────────────────────────────────────────

Downside Risks:
1. Competitive Pressure (High probability, -15% impact)
   - New entrant launched competing product
   - Could pressure pricing and market share

2. Execution Risk (Medium probability, -10% impact)
   - New product launch delays or underperformance
   - Management turnover

3. Macro Slowdown (Medium probability, -20% impact)
   - Economic recession would impact customer spending
   - Operating leverage would reverse

4. Regulatory Risk (Low probability, -25% impact)
   - Potential new regulations in key market
   - Would increase compliance costs

Upside Risks:
1. M&A Bid (Low probability, +35% impact)
   - Strategic acquirer pays control premium

2. Beat-and-Raise (Medium probability, +10% impact)
   - Consistent outperformance vs. estimates

═══════════════════════════════════════════════════════════
```

---

## Quality Standards

### DCF Quality Checks
- [ ] WACC properly calculated with documented components
- [ ] Terminal value reasonable (< 70% of total enterprise value)
- [ ] Sensitivity analysis covers realistic ranges (±200-300bps for WACC, ±100bps for terminal growth)
- [ ] Unlevered FCF properly calculated from EBIT
- [ ] Enterprise to equity value bridge correct
- [ ] Share count is diluted shares, not basic

### Comparables Quality Checks
- [ ] 5-10 comparable companies selected
- [ ] Peer selection defensible (document why each peer was chosen)
- [ ] Statistical summary included (max/75th/median/25th/min) - MANDATORY
- [ ] Multiple selection appropriate (EV/EBITDA for mature, EV/Revenue for high-growth)
- [ ] Premium/discount justified with specific factors
- [ ] Data sourced properly with dates noted

### Overall Valuation Quality Checks
- [ ] At least 2 valuation methods used (DCF + Comps minimum)
- [ ] Weighting explained and appropriate
- [ ] Valuation range provided (low/base/high), not just point estimate
- [ ] Scenarios analyzed (Bull/Base/Bear)
- [ ] Sanity checks performed (see below)
- [ ] All assumptions documented with rationale

---

## Sanity Checks

**Always perform these validation checks:**

1. **Historical Multiple Check**
   - Is implied multiple in line with company's historical trading range?
   - If not, explain why

2. **Peer Comparison**
   - Is premium/discount vs. peers justified by fundamentals?
   - Check: growth, margins, market position

3. **Implied Growth Check**
   - What growth is market pricing in at current price?
   - Is that reasonable given company trajectory?

4. **Market Cap Reasonableness**
   - Does total market cap make sense given company size and peers?
   - Would company be too large/small relative to industry?

5. **Terminal Value Check**
   - Is terminal value < 60-70% of total enterprise value?
   - If > 70%, projections may not be long enough

6. **WACC Reasonableness**
   - Is WACC 8-14% range for typical companies?
   - Tech/high-growth: 10-14%
   - Mature/stable: 7-10%

7. **Implied Returns Check**
   - What IRR from current price to target over 12 months?
   - Is that consistent with recommendation rating?

---

## Output Files

Create the following deliverables:

### 1. Valuation Analysis Document
**File**: `[Company]_Valuation_Analysis_[Date].md` (written analysis)

**Contents** (4-6 pages):
- Executive summary with price target
- DCF analysis (1 page) with sensitivity table
- Comparable companies analysis (1 page) with statistical summary
- Precedent transactions (0.5 page) if applicable
- Valuation summary and football field (0.5 page)
- Investment recommendation (1 page)
- Key catalysts and risks (1 page)

### 2. Excel Valuation Tabs
**Add to Task 2's financial model file:** `[Company]_Financial_Model_[Date].xlsx`

**IMPORTANT**: Do NOT create a separate Excel file. Add these tabs to the existing financial model from Task 2. This keeps all quantitative data in one place.

**Tabs to add:**
- DCF tab with full calculations
- Sensitivity analysis tab
- Comps tab with peer data
- Precedent transactions tab (if applicable)
- Valuation summary tab

---

## Success Criteria

A successful valuation analysis should:
1. Use at least 2 methods (DCF + Comps minimum)
2. Include comprehensive DCF sensitivity analysis (2-way tables)
3. Include statistical summary in comps (max/75th/median/25th/min)
4. Provide valuation range (low/base/high), not point estimate
5. Document all key assumptions with clear rationale
6. Perform sanity checks
7. Arrive at defensible price target
8. Provide clear buy/hold/sell recommendation
9. Identify 3-5 key catalysts
10. Identify 3-5 key risks
11. Be auditable and transparent

---

## Next Steps

After completing Task 3, the valuation analysis will be used for:
- **Task 4 (Charts)**: Create DCF sensitivity heatmaps, valuation football field, scenario comparison charts
- **Task 5 (Report Assembly)**: Integrate valuation analysis into final report

The price target and recommendation are the foundation of the final investment recommendation in the equity research report.
