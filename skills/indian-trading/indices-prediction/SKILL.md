# SKILL.md — Indian NSE Index Prediction Skill
## LLM-Powered Data Analytics Skill for Indian Equity Market Prediction

**Course:** Agentic AI – Strategy, Design and Implementation  
**Institution:** Indian School of Business, AMPBA Batch 24 – Term 4  
**Instructor:** Prof. Manaranjan Pradhan | Academic Associate: Sreeja  
**Group 8:** Praveen Prakash (12510073) · Sanskar Jain (12510068) · Siddharth Kolli (12510088) · Suparna Dhumale (12510086)  

---

## Skill Overview

This skill instructs an LLM to perform a complete end-to-end data analytics workflow for predicting 5–7 day ahead directional returns for 16 major Indian NSE indices. The skill uses a V8 Hybrid architecture combining multiple ML models, an 8-signal weighted framework, and institutional flow data to generate actionable trading signals with confidence scores.

**Skill Domain:** Financial Analytics — Indian Equity Market Index Prediction  
**Prediction Horizon:** 5 days (V7.3 indices) or 7 days (V7.2 indices)  
**Output:** Trade signals (BUY / HOLD / SELL) with confidence (HIGH / MEDIUM / LOW) and supporting evidence

---

## What This Skill Accepts at Runtime

### Input 1: Dataset Files (place in `./data/` directory)

| File | Description | Required |
|------|-------------|----------|
| `indices_ohlcv.csv` | Daily OHLCV price data for 16 NSE indices | YES |
| `external_factors.csv` | Global macro factors (commodities, yields, VIX, FX) | YES |
| `db_factors.csv` | Daily FII/DII institutional flow data | YES |
| `sector_fpi_flow.csv` | Fortnightly NSDL sector-wise FPI investment data | OPTIONAL |

### Input 2: User Configuration Parameters

| Parameter | Type | Default | Valid Range | Description |
|-----------|------|---------|-------------|-------------|
| `data_dir` | str | `./data` | Any valid path | Directory containing input CSV files |
| `models_dir` | str | `./models` | Any valid path | Directory to save/load model PKL files |
| `indices` | list | All 16 | Any subset of ALL_INDICES | Which indices to predict |
| `force_retrain` | bool | False | True/False | Whether to retrain models from scratch |
| `horizon_override` | int | None | 5 or 7 | Override default horizon (optional) |
| `confidence_threshold` | str | "LOW" | LOW/MEDIUM/HIGH | Minimum confidence to show signal |

---

## Mandatory Pipeline Stages

Execute all six stages in order. Do NOT skip stages. If any stage fails, produce a clear error report and stop.

---

### STAGE 1 — Data Validation & Profiling

**Purpose:** Validate all input files before any computation. Reject malformed data early with clear explanation.

**Script to run:**
```bash
python scripts/validate_data.py --data-dir ./data --output ./data/validation_report.json
```

**What to compute:**
1. For `indices_ohlcv.csv`: Count rows per ticker, check date continuity, verify OHLCV columns exist, check Volume > 0, verify Close > 0 for all rows
2. For `external_factors.csv`: Check all 16 factor columns present, compute null percentage per column, check date range covers index dates
3. For `db_factors.csv`: Verify FII_Net and DII_Net columns, check date overlap with OHLCV
4. For all files: Compute date range, row count, null counts, duplicate rows

**Validation thresholds (HARD STOPS — halt if violated):**
- Null percentage > 30% in any critical column (Close, Date, FII_Net, DII_Net) → REJECT with error
- Fewer than 500 rows for any index → REJECT (insufficient data for training)
- Date range < 12 months → REJECT (insufficient history)
- Close price = 0 or negative → REJECT (data corruption)
- Duplicate (Date, Ticker) pairs → WARN and drop duplicates, continue

**Validation thresholds (WARNINGS — continue with note):**
- Null percentage 10–30% in optional columns → WARN, forward-fill
- Date gaps > 7 consecutive trading days → WARN (possible data source issue)
- Latest data > 7 days old → WARN (stale data, signals may be outdated)

**Expected output:** `./data/validation_report.json` containing:
```json
{
  "status": "PASS|FAIL|WARN",
  "quality_score": 95.5,
  "ohlcv": {"rows": 48131, "tickers": 16, "date_range": "2014-01-01 to 2026-04-09", "nulls": 0},
  "external": {"rows": 3203, "columns": 17, "avg_completeness": 100.0},
  "db_factors": {"rows": 1315, "date_range": "2020-11-09 to 2026-04-09"},
  "warnings": [],
  "errors": []
}
```

**If validation FAILS:** Stop immediately. Produce error report explaining:
- Which file failed
- Which columns/rows are problematic
- Exact fix required (e.g., "indices_ohlcv.csv is missing Volume column — add volume data from Yahoo Finance")

---

### STAGE 2 — Data Preparation & Feature Engineering

**Purpose:** Transform raw OHLCV + external + institutional data into 130+ analysis-ready features per index.

**Script to run:**
```bash
python scripts/feature_engineering.py --data-dir ./data --save-full
```

**What to compute (exact feature definitions):**

**A. Price & Return Features (15 features):**
- `ret_1d` = (Close_t / Close_{t-1}) - 1
- `ret_5d` = (Close_t / Close_{t-5}) - 1
- `ret_10d` = (Close_t / Close_{t-10}) - 1
- `ret_21d` = (Close_t / Close_{t-21}) - 1
- `range_hl` = (High - Low) / Close
- `range_oc` = (Close - Open) / Open
- `gap` = (Open_t - Close_{t-1}) / Close_{t-1}
- `body_size` = abs(Close - Open) / (High - Low + 0.001)
- `upper_shadow` = (High - max(Open, Close)) / Close
- `lower_shadow` = (min(Open, Close) - Low) / Close
- `ret_1d_sq` = ret_1d^2 (volatility proxy)
- `ret_5d_sq` = ret_5d^2
- `close_vs_52wh` = Close / rolling_max(Close, 252)
- `close_vs_52wl` = Close / rolling_min(Close, 252)
- `price_momentum` = Close / rolling_mean(Close, 20) - 1

**B. Moving Average Features (15 features):**
- SMA(5), SMA(10), SMA(20), SMA(50), SMA(200)
- EMA(5), EMA(10), EMA(20), EMA(50), EMA(200)
- `sma_ratio_5_20` = SMA(5) / SMA(20)
- `sma_ratio_20_50` = SMA(20) / SMA(50)
- `sma_ratio_50_200` = SMA(50) / SMA(200)
- `ema_ratio_5_20` = EMA(5) / EMA(20)
- `golden_cross` = 1 if SMA(50) > SMA(200) else 0

**C. Momentum Indicators (18 features):**
- `RSI_14` = 100 - (100 / (1 + avg_gain_14 / avg_loss_14))
- `RSI_28` = same formula over 28 periods
- `macd` = EMA(12) - EMA(26)
- `macd_signal` = EMA(macd, 9)
- `macd_hist` = macd - macd_signal
- `stoch_k` = (Close - rolling_min(Low,14)) / (rolling_max(High,14) - rolling_min(Low,14)) * 100
- `stoch_d` = rolling_mean(stoch_k, 3)
- `williams_r` = (rolling_max(High,14) - Close) / (rolling_max(High,14) - rolling_min(Low,14)) * -100
- `cci_20` = (Close - rolling_mean(Close,20)) / (0.015 * rolling_std(Close,20))
- `roc_5` = (Close / Close_{t-5} - 1) * 100
- `roc_10` = (Close / Close_{t-10} - 1) * 100
- `roc_21` = (Close / Close_{t-21} - 1) * 100
- `smi` = stochastic momentum index
- `atr_14` = exponential average of True Range over 14 days
- `bb_upper` = SMA(20) + 2 * std(Close, 20)
- `bb_lower` = SMA(20) - 2 * std(Close, 20)
- `bb_width` = (bb_upper - bb_lower) / SMA(20)
- `bb_position` = (Close - bb_lower) / (bb_upper - bb_lower)

**D. External Factor Features (30 features):**
For each macro variable (Crude_Oil, Gold, Copper, USDINR, DXY, SP500, NASDAQ, Nikkei, FTSE, US10Y_Yield, US2Y_Yield, India10Y_Yield, India_VIX, US_VIX):
- `{var}_ret_1d` = daily return
- `{var}_vol20` = 20-day rolling std of returns (volatility)

Additional yield curve features:
- `yield_spread_10_2` = US10Y_Yield - US2Y_Yield (yield curve slope)
- `yield_spread_ma20` = 20-day MA of yield_spread_10_2
- `india_us_spread` = India10Y_Yield - US10Y_Yield
- `vix_ma20` = 20-day MA of India_VIX
- `vix_regime` = 0 (low, VIX<13) / 1 (normal, 13-20) / 2 (high, >20)

**E. FII/DII Features (14 features):**
From `db_factors.csv`:
- `FII_Net` = raw daily FII net flow (Cr)
- `DII_Net` = raw daily DII net flow (Cr)
- `FII_5d_sum` = rolling 5-day sum of FII_Net
- `FII_10d_sum` = rolling 10-day sum of FII_Net
- `FII_20d_sum` = rolling 20-day sum of FII_Net
- `DII_5d_sum` = rolling 5-day sum of DII_Net
- `DII_10d_sum` = rolling 10-day sum of DII_Net
- `DII_20d_sum` = rolling 20-day sum of DII_Net
- `FII_momentum` = FII_5d_sum - FII_20d_sum
- `DII_momentum` = DII_5d_sum - DII_20d_sum
- `FII_DII_spread` = FII_Net - DII_Net
- `FII_DII_spread_5d` = FII_5d_sum - DII_5d_sum
- `FII_trend` = 1 if FII_5d_sum > 0 else 0
- `DII_trend` = 1 if DII_5d_sum > 0 else 0

**F. Regime Detection Features (5 features):**
Apply K-Means clustering (k=4) on [ret_5d, ret_20d, vol10, vol20]:
- `market_regime` = 0/1/2/3 (cluster label)
- `regime_bull` = 1 if regime in bull clusters else 0
- `vol_regime` = 0/1/2 (low/normal/high based on VIX)
- `trend_regime` = 1 if SMA(50)>SMA(200) else 0
- `momentum_regime` = 1 if RSI_14>50 else 0

**Data alignment rule:** Cutoff date = latest start date across all sources. Filter all data to this date before merging to ensure every row has all features populated. Forward-fill gaps ≤ 5 days; backward-fill for remaining.

**Validation after Stage 2:**
- Total features engineered: 130+ per index
- No NaN values remaining in feature matrix
- Print: "Feature engineering complete: {N} rows × {M} features for {K} indices"

**Expected output:** `./data/full_features_dataset.csv` (all features, all indices, all dates after cutoff)

---

### STAGE 3 — Modelling & Analysis (Multi-Algorithm)

**Purpose:** Train 4 ML models per index, select the best by directional accuracy, save as PKL.

**Script to run:**
```bash
python scripts/train_models.py --data-dir ./data --models-dir ./models [--indices NIFTY BANKNIFTY]
```

**V8 Hybrid Architecture:**

| Group | Indices | Horizon | Key Features |
|-------|---------|---------|--------------|
| V7.2 | NIFTY, BANKNIFTY, NIFTYIT, NIFTYPHARMA, NIFTYMETAL, NIFTYAUTO, NIFTYENERGY, NIFTYINFRA, NIFTYPSUBANK, NIFTYMEDIA | 7 days | No sector FPI |
| V7.3 | NIFTYFMCG, NIFTYREALTY, NIFTYFINSERVICE, NIFTYCONSUMPTION, NIFTYCOMMODITIES, NIFTYMNC | 5 days | With sector FPI |

**Target variable:** 5-class classification
- Class 0: Strong Down (return ≤ -3%)
- Class 1: Down (-3% < return ≤ -1%)
- Class 2: Flat (-1% < return ≤ +1%)
- Class 3: Up (+1% < return ≤ +3%)
- Class 4: Strong Up (return > +3%)

**Train/test split:** Chronological hard cutoff at 2024-06-30
- Train: all data from cutoff_date to 2024-06-30
- Test: 2024-07-01 to latest available date (~21 months of out-of-sample)

**The 4 models trained per index:**

**Model 1: Random Forest**
```
n_estimators=200, max_depth=10, min_samples_split=10,
class_weight='balanced', random_state=42, n_jobs=-1
```

**Model 2: XGBoost (Optuna-tuned, 20 trials)**
```
objective='multi:softmax', num_class=5, eval_metric='mlogloss',
n_estimators=200-500, max_depth=4-8, learning_rate=0.01-0.1,
subsample=0.6-1.0, colsample_bytree=0.6-1.0, random_state=42
Optuna optimises: directional accuracy on validation set
```

**Model 3: LightGBM**
```
objective='multiclass', num_class=5, n_estimators=200,
learning_rate=0.05, max_depth=8, class_weight='balanced',
force_col_wise=True, verbose=-1, random_state=42
```

**Model 4: SVM**
```
C=1.0, kernel='rbf', probability=True,
class_weight='balanced', random_state=42
```

**Feature selection:** Load `feature_importance_good_only.csv`. For each index, keep only GOOD-ranked features. If file not found, use all features.

**Scaler:** RobustScaler fitted on training data only. Apply transform to test data.

**Model selection:** Best model = argmax(directional_accuracy on test set)
- `directional_accuracy` = accuracy of predicting UP (class 3+4) vs DOWN/FLAT (class 0+1+2)
- Minimum threshold: dir_accuracy ≥ 0.52. If no model exceeds this, flag index as UNRELIABLE.

**Save PKL:** `./models/{TICKER}_{MODEL}_V8_{YYYYMMDD_HHMM}.pkl`
Archive old PKLs to `./models/old_models/`

**PKL contents:**
```python
{
  'model': trained_model_object,
  'scaler': fitted_RobustScaler,
  'features': [list of feature column names],
  'approach': 'V7.2' or 'V7.3',
  'horizon': 5 or 7,
  'ticker': 'NIFTY',
  'best_model': 'XGB',
  'metrics': {'DirAcc': 0.672, 'ClsAcc': 0.335},
  'is_reliable': True,
  'trained_date': '2026-04-10T13:00:00'
}
```

**Save summary:** `./data/V8_summary.csv` and `./models/V8_summary.csv`

---

### STAGE 4 — Model/Result Validation

**Purpose:** Validate model quality on held-out test set. Produce quantitative evidence for model selection.

**Script to run:**
```bash
python scripts/validate_predictions.py --data-dir ./data --models-dir ./models
```

**Compute for each trained model:**
- `cls_accuracy` = classification accuracy (5 classes)
- `dir_accuracy` = directional accuracy (UP vs not-UP)
- `up_win_rate` = precision when predicting UP
- `down_win_rate` = precision when predicting DOWN
- `precision`, `recall`, `f1_score`
- `confusion_matrix` (5×5)

**Validation thresholds:**
- `dir_accuracy` ≥ 0.60 → GOOD (acceptable for live trading)
- `dir_accuracy` 0.52–0.60 → MODERATE (use with caution)
- `dir_accuracy` < 0.52 → POOR (flag UNRELIABLE, exclude from signals)

**Check for class imbalance issues:**
- If `up_win_rate` = 0.0 → model never predicts UP → FAIL, retrain with `class_weight='balanced'`
- If `down_win_rate` = 0.0 → model never predicts DOWN → FAIL, retrain

**Expected output:** `./data/validation_results.json`

**Print summary table:**
```
Index          Model  Dir_Acc  Up_Win   Down_Win  Status
NIFTY          XGB    67.2%    14.4%    7.1%      GOOD
BANKNIFTY      XGB    67.8%    6.6%     69.9%     GOOD
...
NIFTYPSUBANK   SVM    59.1%    67.7%    49.0%     MODERATE
```

---

### STAGE 5 — Signal Generation & Insight Interpretation

**Purpose:** Combine ML predictions with 7 additional signals into a weighted composite score. Generate trade signals with confidence levels.

**Script to run:**
```bash
python scripts/generate_signals.py --data-dir ./data --models-dir ./models
```

**8-Signal Framework (exact weights and computation):**

| Signal | Weight | Computation |
|--------|--------|-------------|
| ML Prediction | 30% | +1.0 (Strong_Up/Up), 0.0 (Neutral), -1.0 (Down/Strong_Down) |
| Technical Trend | 15% | +1 (SMA50>SMA200 AND MACD>0), +0.5 (one condition), -1 (both bearish) |
| FII Flow | 10% | +1 (FII_20d_sum>5000), +0.5 (>0), -0.5 (<0), -1 (<-5000) |
| DII Flow | 10% | +1 (DII_5d_sum>2000), +0.5 (>0), -0.5 (<0), -1 (<-2000) |
| Technical Momentum | 10% | +1 (RSI 40-70 AND Stoch<80), -1 (RSI>75 OR Stoch>85 — overbought), -0.5 (RSI<35) |
| VIX Regime | 10% | +0.5 (VIX<13), 0 (13-20), -0.5 (20-28), -1 (VIX>28) |
| Global Trend | 8% | +1 (SP500_5d_ret>+2%), +0.5 (>0%), -0.5 (<0%), -1 (<-2%) |
| Yield Curve | 7% | +0.5 (spread>0.5%), 0 (-0.5 to 0.5%), -0.5 (<-0.5%) |

**Composite score computation:**
```
weighted_score = Σ (signal_value × signal_weight) for all 8 signals
Range: -1.0 to +1.0
```

**Trade signal assignment:**
- `STRONG BUY`: weighted_score ≥ 0.5 AND ≥ 6/8 signals bullish
- `BUY`: weighted_score ≥ 0.2 OR ≥ 5/8 signals bullish
- `HOLD`: -0.2 < weighted_score < 0.2
- `SELL`: weighted_score ≤ -0.2 OR ≥ 5/8 signals bearish
- `STRONG SELL`: weighted_score ≤ -0.5 AND ≥ 6/8 signals bearish

**Confidence level assignment:**
- `HIGH`: ≥ 6/8 signals agree AND abs(weighted_score) > 0.4
- `MEDIUM`: ≥ 5/8 signals agree OR abs(weighted_score) > 0.25
- `LOW`: otherwise

**Conflict flag:** `has_conflict = True` if bullish_count > 0 AND bearish_count > 0

**Expected output:** `./data/trade_signals.json` containing:
- Timestamp
- Market-wide signals (VIX, global, DII, yield curve)
- Per-index signals with all 8 component scores
- Composite score, direction, confidence, conflict flag

**Business interpretation rules (consult REFERENCE.md):**
- VIX > 20: Always note "elevated volatility — reduce position sizing"
- FII outflow > 10,000 Cr (5-day): Note "heavy foreign selling — caution on bullish signals"
- Yield spread < 0: Note "inverted yield curve — potential recession risk"
- All 8 signals agree: Note "high-conviction signal — strong alignment"

---

### STAGE 6 — Report Generation

**Purpose:** Produce a professional multi-section HTML report with all results and visualisations.

**Script to run:**
```bash
python scripts/generate_report.py --data-dir ./data --output-dir ./reports
```

**Report must contain these exact sections in this order:**

1. **Executive Summary** — Date, market context (NIFTY price, VIX, FII/DII), count of BUY/HOLD/SELL signals, top 3 recommendations

2. **Data Quality Summary** — Table with file names, row counts, date ranges, completeness %, validation status

3. **Methodology** — V8 Hybrid architecture description, train/test split, feature count, model comparison approach

4. **Model Performance Summary** — Table: Index | Model | Dir_Accuracy | Reliability Status | Horizon

5. **Signal Dashboard** — For each index: action badge (colour-coded), composite score, 8-signal breakdown bar chart

6. **Top Recommendations** — Ranked table: STRONG BUY signals first, then BUY, showing key drivers

7. **Risk & Conflict Analysis** — List of conflicting signals, high-VIX warning if applicable

8. **Feature Importance Summary** — Top 10 features across all indices (from feature_importance_good_only.csv)

9. **Limitations & Assumptions** — Data staleness, market regime sensitivity, no guarantee of returns

10. **Data Appendix** — Raw V8_summary.csv table, validation_results summary

**Chart specifications:**
- Signal breakdown bars: x-axis = signal names, y-axis = score (-1 to +1), coloured green (positive) / red (negative), title = "{TICKER} — 8-Signal Breakdown"
- Model accuracy bar chart: x-axis = index names, y-axis = directional accuracy %, horizontal line at 60% threshold, title = "V8 Model Directional Accuracy by Index"
- FII/DII flow chart: dual-bar chart with dates on x-axis, FII and DII flows on y-axis, title = "FII/DII Daily Net Flow (Last 30 Days)"

**Expected output:** `./reports/prediction_report_{YYYYMMDD}.html`

---

## Error Handling

If any stage fails, the skill must:
1. Print a clear error message identifying which stage failed and why
2. NOT produce partial results without warning
3. Suggest the exact fix (e.g., "Re-run fetch_data.py to refresh data")
4. Log the error to `./data/skill_run_log.txt` with timestamp

**Common errors and fixes:**

| Error | Cause | Fix |
|-------|-------|-----|
| "db_factors.csv not found" | FII/DII data missing | Run fetch_data.py first |
| "Insufficient data: N rows < 500" | Cutoff too late | Check data alignment in feature_engineering.py |
| "No model exceeds 52% threshold" | All models poor | Try different feature set or check data quality |
| "UnicodeDecodeError" | SKILL.md encoding issue | Open with encoding='utf-8', errors='ignore' |
| "Model file not found" | No trained models | Run train_models.py first |

---

## Complete Execution Sequence

```bash
# 1. Fetch latest data
python scripts/fetch_data.py --data-dir ./data --update-only

# 2. Validate data quality
python scripts/validate_data.py --data-dir ./data

# 3. Engineer features (creates full_features_dataset.csv)
python scripts/feature_engineering.py --data-dir ./data --save-full

# 4. Train models (or skip if models already exist)
python scripts/train_models.py --data-dir ./data --models-dir ./models

# 5. Validate model quality
python scripts/validate_predictions.py --data-dir ./data --models-dir ./models

# 6. Generate trading signals
python scripts/generate_signals.py --data-dir ./data --models-dir ./models

# 7. Generate HTML report
python scripts/generate_report.py --data-dir ./data --output-dir ./reports
```

**Estimated runtime:** Stage 1–2: 5 min | Stage 3: 20–60 min (with Optuna) | Stage 4–7: 5 min


---

## LLM-Powered Interactive Dashboard (app.py)

The skill is deployed as a **Streamlit web application** that uses this SKILL.md as a live system prompt for all AI-powered features. The dashboard is accessible at `http://13.232.124.158:8501`.

### How SKILL.md is Used at Runtime

**1. AI Analysis (per index)**
When a user selects an index, the app calls the Claude API with:
- **System prompt:** Full SKILL.md content loaded from disk
- **User prompt:** Index signals data (action, confidence, composite score, ML prediction, technical indicators, FII/DII, VIX, global signals, top features)
- **Task:** Generate a 3-4 sentence plain-text analysis covering: (1) signal summary, (2) key driver, (3) main risk, (4) recommendation
- **Output:** Rendered in the AI Analysis card with markdown stripped for clean display

**2. News Sentiment Analysis**
After fetching the last 7 days of news headlines for the index:
- **System prompt:** Full SKILL.md content + "You are a financial sentiment analyser"
- **User prompt:** Up to 8 news headlines + current ML signal
- **Task:** Return JSON with sentiment (Bullish/Bearish/Neutral), score (-1 to +1), adjusted signal (BUY/HOLD/SELL), and justification
- **Output:** Shown in News Validation card with colour-coded sentiment badge

**3. Index Chat (per index)**
Users can ask free-form questions about any index:
- **System prompt:** Full SKILL.md + current signal data for selected index
- **Conversation:** Full message history passed each turn
- **Task:** Answer questions about signals, risks, methodology in plain language
- **Model:** claude-sonnet-4-20250514

### Dashboard Architecture

```
app.py (Streamlit)
├── Tab 1: Dashboard
│   ├── Banner (4 cols): NIFTY 50 | Global Cues | Economic Calendar | FII/DII/VIX Chart
│   ├── Left Panel: Index List (16 indices with signal badges, HTML clickable rows)
│   └── Right Panel (3+2 layout):
│       ├── Top Row: AI Analysis | 8-Signal Breakdown | Model + Features
│       └── Bottom Row: News Validation | Index Chat
├── Tab 2: Pipeline (run scripts, fetch data)
├── Tab 3: Global Chat (market-wide questions)
├── Tab 4: Skill Docs (view SKILL.md, REFERENCE.md, README)
└── Tab 5: Logs (API calls, scheduler, errors)
```

### Automated Data Scheduler
The app runs a background scheduler that auto-fetches data:
- **Primary run:** 8:30 PM IST (15:00 UTC) on weekdays
- **Retry run:** 11:30 PM IST (18:00 UTC) if primary fails
- **Cron backup:** Two cron jobs on AWS EC2 as redundancy

---

## Interactive Parameter Sensitivity

The skill demonstrates how changing key parameters affects output:

**Parameter 1: Prediction Horizon (5-day vs 7-day)**
- V7.2 indices (NIFTY, BANKNIFTY, etc.): 7-day horizon → higher accuracy for broad market
- V7.3 indices (NIFTYFMCG, NIFTYFINSERVICE, etc.): 5-day horizon → better for sector volatility
- Changing horizon_override forces all indices to same horizon — typically reduces accuracy by 2-5%

**Parameter 2: Confidence Threshold**
- Setting to HIGH: Shows only 2-3 signals but highest conviction
- Setting to LOW: Shows all 16 signals including conflicted ones
- MEDIUM (default): Shows 8-12 signals with reasonable conviction

**Parameter 3: Force Retrain vs. Cached Models**
- `force_retrain=False` (default): Uses existing PKL models — runs in ~5 minutes
- `force_retrain=True`: Full Optuna tuning — takes 20-60 minutes but adapts to new market regimes

---
