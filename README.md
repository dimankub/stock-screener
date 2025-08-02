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
  - Net Profit Margin
  - Dividend Yield


## Установка
1. Создать файл .env с ключом API Finnhub:
    FINNHUB_API_KEY=твой_ключ_отсюда

2. Установить зависимости:
```bash
pip install -r requirements.txt

