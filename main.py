import yaml
from src.fetchers.finnhub import fetch_basic_data

LABELS = {
    "pe_ratio": "P/E",
    "pb_ratio": "P/B",
    "roeTTM": "ROE TTM",
    "roaTTM": "ROA TTM",
    "roiTTM": "ROI TTM",
    "net_margin": "Net Margin",
    "dividend_yield": "Dividend Yield",
    "eps_ttm": "EPS TTM",
    "epsGrowth5Y": "EPS Growth 5Y",
    "pfcfShareTTM": "P/CF TTM",
    "longTermDebt/equityAnnual": "Long-Term Debt/Equity Ratio",
    "beta": "Beta (Volatility)",
    "payoutRatioAnnual": "Payout Ratio"
}

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

enabled_metrics = config.get("metrics", {}).get("include", [])

def main():
    ticker = input("Введите тикер акции: ").upper()
    data = fetch_basic_data(ticker)

    if data:
        print(f"\n[{ticker}] {data.get('name', '')}")
        print(f"Цена: {data.get('price')}")
        print(f"Рыночная капитализация: {data.get('market_cap')}")

        for key in enabled_metrics:
            label = LABELS.get(key, key.replace("_", " ").title())
            value = data.get(key)
            print(f"{label}: {value}")
    else:
        print("Не удалось получить данные.")

if __name__ == "__main__":
    main()