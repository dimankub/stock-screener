# Stock Screener — скринер акций

## Описание
Инструмент для оценки и сравнения акций по множеству метрик.

## Источники данных
- [Finnhub.io](https://finnhub.io/) — бесплатный API

## MVP-функции
- Поиск акций по тикеру
- Расчёт и отображение финансовых данных:
	- P/E (Price to Earnings)
	- P/B (Price to Book)
	- ROE (Return on Equity)
	- ROA (Return on Assets)
	- ROI (Return on Investment)
	- Net Profit Margin (Чистая маржа)
	- Dividend Yield (Дивидендная доходность)
	- EPS (Earnings per share, TTM)
	- Price/Free Cash Flow (TTM)
	- Long-term Debt/Equity Ratio
	- EPS Growth (5Y) — средний рост прибыли на акцию за 5 лет
	- Beta (рыночная волатильность)
	- Payout Ratio (Коэффициент дивидендных выплат)
	- Gross Margin (Валовая маржа)
	- Market Capitalization (Капитализация)
	- Net Profit Margin (Annual)


## Установка
1. Создать файл .env с ключом API Finnhub:
    FINNHUB_API_KEY=твой_ключ_отсюда

2. Установить зависимости:
```bash
pip install -r requirements.txt

