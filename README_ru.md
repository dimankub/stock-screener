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
	- EPS (Прибыль на акцию, TTM)
	- Price/Free Cash Flow (TTM)
	- Long-term Debt/Equity Ratio
	- EPS Growth (5Y)  (Средний рост прибыли на акцию за 5 лет)
	- Beta (Рыночная волатильность)
	- Payout Ratio (Коэффициент дивидендных выплат)
	- Gross Margin (Валовая маржа)
	- Market Capitalization (Капитализация)
	- Net Profit Margin (Чистая рентабельность продаж)
	- Current Ratio (Текущая ликвидность)
	- Revenue Growth (Долгосрочный рост выручки)
	- Dividend Growth (Темп роста дивидендов за 5 лет)
	- Operating Margin TTM (Операционная рентабельность за последние 12 месяцев)
	- Asset Turnover Annual (Коэффициент оборачиваемости активов)
	- Quick Ratio (Быстрая ликвидность)
	- Cash Flow Per Share (Денежный поток на акцию)
	- Total Debt/Equity (Отношение общего долга компании к собственному капиталу)


## Установка
1. Создать файл .env с ключом API Finnhub:
    FINNHUB_API_KEY=твой_ключ_API

2. Установить зависимости:
```bash
pip install -r requirements.txt

