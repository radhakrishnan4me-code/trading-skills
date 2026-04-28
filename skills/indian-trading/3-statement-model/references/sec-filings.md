# Indian Corporate Filings Data Extraction Reference

**When to Use:** Only reference this file when a model template specifically requires pulling data from BSE/NSE corporate filings (Annual Reports, Quarterly Results). For templates that provide data directly or use other data sources, this reference is not needed.

---

## Extracting Data from Indian Corporate Filings (Annual Reports / Quarterly Results)

When populating a model template with public company data, extract financials directly from BSE/NSE filings and Annual Reports.

### Step 1: Locate the Filing

1. Use BSE corporate filings portal: `https://www.bseindia.com/corporates/` — search by company name or scrip code
2. Use NSE corporate filings portal: `https://www.nseindia.com/companies-listing/corporate-filings` — search by company name or symbol
3. For Annual Reports: Check MCA (Ministry of Corporate Affairs) or the company's Investor Relations page
4. For Quarterly Results: Search BSE/NSE under LODR Regulation 33 filings

### Step 2: Identify Filing Currency

Before extracting data, identify the reporting currency:
- Check the cover page or header for reporting currency
- Look at statement headers (e.g., "in lakhs of Indian Rupees" or "in crores of Indian Rupees")
- Review Note 1 (Significant Accounting Policies) — all Indian listed companies report under IndAS (Indian Accounting Standards)

**Common Currency Indicators**

| Indicator | Currency |
|-----------|----------|
| ₹, INR | Indian Rupee |
| ₹ Cr | Indian Rupee (in crores) |
| ₹ Lakh | Indian Rupee (in lakhs) |

**Note:** Indian companies typically report in ₹ lakhs or ₹ crores. Ensure you identify the scale correctly — a factor-of-100 error between lakhs and crores is a common mistake.

Set model currency to match filing; document in Assumptions tab.

### Step 3: Navigate to Financial Statements

Within the Annual Report (prepared under Companies Act 2013, Schedule III format), locate:
- **Standalone vs Consolidated Statements**: Indian companies report both; use Consolidated for group-level analysis
- Key sections to extract:
  - Statement of Profit and Loss (Income Statement)
  - Balance Sheet
  - Statement of Cash Flows
  - Notes to Financial Statements (for schedule details)

For Quarterly Results (filed under LODR Regulation 33):
- Quarterly and year-to-date figures
- Standalone and Consolidated results
- Limited review by auditors for quarters; full audit for annual

### Step 4: Data Extraction Mapping

**Income Statement (from Statement of Profit and Loss)**

| Filing Line Item | Model Line Item |
|------------------|-----------------|
| Revenue from Operations | Revenue |
| Cost of Materials Consumed / Cost of Goods Sold | COGS |
| Employee Benefits Expense | Employee Costs |
| Other Expenses | Other Operating Expenses |
| Depreciation and Amortisation | D&A |
| Finance Costs | Interest Expense |
| Tax Expense (Current + Deferred) | Taxes |
| Profit After Tax (PAT) | Net Income |

**Balance Sheet (Schedule III Format)**

| Filing Line Item | Model Line Item |
|------------------|-----------------|
| Cash and Cash Equivalents | Cash |
| Trade Receivables | AR |
| Inventories | Inventory |
| Property, Plant and Equipment | PP&E (Net) |
| Total Assets | Total Assets |
| Trade Payables | AP |
| Short-term Borrowings / Current maturities of LT debt | Current Debt |
| Long-term Borrowings | LT Debt |
| Retained Earnings (Surplus in Statement of P&L) | Retained Earnings |
| Total Equity (Share Capital + Other Equity) | Total Equity |

**Cash Flow Statement (from Statement of Cash Flows)**

| Filing Line Item | Model Line Item |
|------------------|-----------------|
| Profit After Tax | Net Income |
| Depreciation and Amortisation | D&A |
| Changes in Trade Receivables | ΔAR |
| Changes in Inventories | ΔInventory |
| Changes in Trade Payables | ΔAP |
| Capital Expenditure / Purchase of PPE | CapEx |
| Proceeds from Issue of Shares | Equity Issuance |
| Proceeds from / Repayments of Borrowings | Debt activity |
| Dividends Paid | Dividends |

### Step 5: Extract Supporting Detail from Notes

For schedules, pull from Notes to Financial Statements:
- **Note: Borrowings** → Maturity schedule, interest rates, covenants, secured vs unsecured
- **Note: Property, Plant & Equipment** → Gross PPE, accumulated depreciation, useful lives (as per Companies Act 2013 Schedule II)
- **Note: Revenue** → Segment breakdowns (as per IndAS 108), geographic splits
- **Note: Leases** → Operating vs finance lease obligations (IndAS 116)
- **Note: Related Party Transactions** → Key management compensation, group transactions

### Step 6: Historical Data Requirements

Extract 3 years of historical data minimum:
- Annual Reports provide 2 years of comparative data (current + prior year)
- For 3rd year, pull from prior year's Annual Report
- Use Quarterly Results (LODR Regulation 33) to fill in quarterly granularity if needed
- Check BSE/NSE for past filings: `https://www.bseindia.com/corporates/` or `https://www.nseindia.com/companies-listing/corporate-filings`

### Data Extraction Checklist

- Identify reporting currency and scale (lakhs vs crores)
- Use Consolidated (not Standalone) statements unless specifically required
- 3 years historical Statement of Profit and Loss
- 3 years historical Statement of Cash Flows
- 3 years historical Balance Sheet
- Verify PAT = CF starting Profit After Tax (each year)
- Verify BS Cash = CF Ending Cash (each year)
- Extract borrowing maturity schedule from notes
- Extract D&A detail or useful life assumptions (Companies Act Schedule II)
- Note any exceptional / one-time items to normalize
- Check for IndAS adjustments (e.g., IndAS 116 lease impact, IndAS 115 revenue recognition)

### Handling Common Filing Variations

| Variation | How to Handle |
|-----------|---------------|
| D&A embedded in Cost of Materials / Employee Costs | Pull D&A from Cash Flow Statement or Notes |
| "Other" line items are material | Check notes for breakdown |
| Restatements due to IndAS transition | Use restated figures, note in assumptions |
| Fiscal year = April–March (most Indian companies) | Label with fiscal year end (e.g., FY25 = April 2024 to March 2025) |
| Standalone vs Consolidated differences | Always note which is used; prefer Consolidated |
| Companies reporting in ₹ lakhs vs ₹ crores | Convert to consistent unit; note conversion in Assumptions |

### India-Specific Considerations

| Topic | Notes |
|-------|-------|
| **Accounting Standards** | All listed companies follow IndAS (Indian Accounting Standards), converged with IFRS |
| **Regulatory Body** | SEBI (Securities and Exchange Board of India) |
| **Filing Requirements** | LODR (Listing Obligations and Disclosure Requirements) Regulations |
| **Quarterly Filings** | Regulation 33 — results within 45 days of quarter end (60 days for annual) |
| **Material Events** | Regulation 30 — stock exchange intimation for material events |
| **Corporate Governance** | Regulation 27 — quarterly compliance report |
| **Promoter Holding** | Unique to India — track promoter vs public shareholding pattern |
| **Dividend Distribution** | No DDT post April 2020; dividends taxable in hands of shareholders |
| **Tax Rates** | Corporate tax: 25.17% (new regime) or 34.94% (old regime with surcharge + cess) |
