---
name: mcx-entry
description: MCX commodity intraday entry and exit rules for crude oil, gold, silver, natural gas
tags: [mcx, commodity, intraday, india]
---
# MCX Entry/Exit Rules
## Instruments
Crude Oil, Gold, Silver, Natural Gas (all MCX)
## Entry Criteria
- Confirm trend on 15m chart using EMA 9/21 crossover
- MCX market hours: 9:00 AM - 11:30 PM IST
- Volume confirmation: above 20-period average
- ATR-based stop loss: 1.5x ATR(14)
## Exit Rules
- Target: 2:1 risk-reward minimum
- Trailing stop: move to breakeven at 1R profit
- Time-based exit: close all 30 min before session end
## OpenAlgo Integration
Place orders via OpenAlgo API using Fyers/Kotak broker on MCX exchange
