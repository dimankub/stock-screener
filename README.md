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
	- Net Profit Margin (percentage of revenue left as profit)
	- Dividend Yield (dividends compared to stock price, in %)
	- EPS (Earnings per Share, TTM)
	- Price/Free Cash Flow (TTM, stock price compared to free cash flow per share)
	- Long-term Debt/Equity Ratio (long-term debt compared to equity)
	- EPS Growth (5Y,  average EPS growth over 5 years)
	- Beta (shows how volatile the stock is compared to the market)
	- Payout Ratio (dividend payout ratio)
	- Gross Margin (profit after production costs, % of revenue)
	- Market Capitalization (total market value of the company’s shares)
	- Net Profit Margin (Annual, profit margin for the whole year)
	- Current Ratio (current assets divided by current liabilities)
	- Revenue Growth (percentage increase in company’s revenue)
	- Dividend Growth (growth of dividend payments over time)
	- Operating Margin TTM (operating profit as % of revenue in last 12 months)
	- Asset Turnover Annual (how efficiently assets are used to generate sales)
	- Quick Ratio (liquid assets compared to current liabilities)
	- Cash Flow Per Share (cash generated per share)
	- Total Debt/Equity (total debt compared to company equity)
	- Inventory Turnover (how quickly stock is sold and replaced)
	


## Installation
1. Create a .env file with your Finnhub API key:
    FINNHUB_API_KEY=your_key_API

2. Install dependencies:
```bash
pip install -r requirements.txt