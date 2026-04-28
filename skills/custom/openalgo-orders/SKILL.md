---
name: openalgo-orders
description: Place, modify and cancel orders via OpenAlgo API for NSE/MCX trading
tags: [openalgo, orders, nse, mcx, broker, india]
---
# OpenAlgo Order Management
## API Base
http://localhost:5000/api/v1
## Supported Exchanges
NSE, BSE, NFO (Nifty/BankNifty F&O), MCX, CDS
## Key Parameters
- symbol: NSE format (e.g., NIFTY24DEC24000CE)
- exchange: NFO for F&O, MCX for commodities
- action: BUY or SELL
- price_type: MARKET, LIMIT, SL, SL-M
