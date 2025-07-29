from src.fetchers.finnhub import fetch_basic_data

def main():
    ticker = input("Введите тикер акции: ").upper()
    data = fetch_basic_data(ticker)
    if data:
        print(f"\n[{ticker}] {data.get('name', '')}")
        print(f"Цена: {data.get('price')}")
        print(f"Рыночная капитализация: {data.get('market_cap')}")
        print(f"P/E: {data.get('pe_ratio')}")
        print(f"P/B: {data.get('pb_ratio')}")
        print(f"ROE: {data.get('roe')}")
        print(f"ROA: {data.get('roa')}")
    else:
        print("Не удалось получить данные.")

if __name__ == "__main__":
    main()