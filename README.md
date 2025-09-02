# Stock Screener

## Description
A tool for evaluating and comparing stocks based on a wide range of fundamental and market metrics.

## Data sources
- [Finnhub.io](https://finnhub.io/) — free API

## Features (MVP)
- Stock search by ticker
- Calculation and display of key financial data:
	- P/E (Price to Earnings)
	- P/B (Price to Book)
	- ROE (Return on Equity)
	- ROA (Return on Assets)
	- ROI (Return on Investment)
	- Net Profit Margin
	- Dividend Yield
	- EPS (Earnings per Share, TTM)
	- Price/Free Cash Flow (TTM)
	- Long-term Debt/Equity Ratio
	- EPS Growth (5Y) — average EPS growth over 5 years
	- Beta (market volatility)
	- Payout Ratio (dividend payout ratio)
	- Gross Margin
	- Market Capitalization
	- Net Profit Margin (Annual)
	- Current Ratio


## Installation
1. Create a .env file with your Finnhub API key:
    FINNHUB_API_KEY=your_key_API

2. Install dependencies:
```bash
pip install -r requirements.txt