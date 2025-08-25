import finnhub
import os
import yaml
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("FINNHUB_API_KEY")
if not api_key:
    raise ValueError("FINNHUB_API_KEY не найден в .env")

client = finnhub.Client(api_key=api_key)

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

enabled_metrics = set(config.get("metrics", {}).get("include", []))

def fetch_basic_data(ticker: str) -> dict:
    try:
        quote = client.quote(ticker)
        profile = client.company_profile2(symbol=ticker)
        fundamentals = client.company_basic_financials(ticker, metric="all")["metric"]

        data = {
            "name": profile.get("name"),
            "price": quote.get("c"),
            "market_cap": profile.get("marketCapitalization")
        }

        if "pe_ratio" in enabled_metrics:
            data["pe_ratio"] = fundamentals.get("peBasicExclExtraTTM")
        if "pb_ratio" in enabled_metrics:
            data["pb_ratio"] = fundamentals.get("pbAnnual")
        if "roeTTM" in enabled_metrics:
            data["roeTTM"] = fundamentals.get("roeTTM")
        if "roaTTM" in enabled_metrics:
            data["roaTTM"] = fundamentals.get("roaTTM")
        if "roiTTM" in enabled_metrics:
            data["roiTTM"] = fundamentals.get("roiTTM")
        if "net_margin" in enabled_metrics:
            data["net_margin"] = fundamentals.get("netProfitMarginAnnual")
        if "dividend_yield" in enabled_metrics:
            data["dividend_yield"] = fundamentals.get("dividendYieldIndicatedAnnual")
        if "eps_ttm" in enabled_metrics:
            data["eps_ttm"] = fundamentals.get("epsTTM")
        if "pfcfShareTTM" in enabled_metrics:
            data["pfcfShareTTM"] = fundamentals.get("pfcfShareTTM")
        if "longTermDebt/equityAnnual" in enabled_metrics:
            data["longTermDebt/equityAnnual"] = fundamentals.get("longTermDebt/equityAnnual")
        if "epsGrowth5Y" in enabled_metrics:
            data["epsGrowth5Y"] = fundamentals.get("epsGrowth5Y")
        if "beta" in enabled_metrics:
            data["beta"] = fundamentals.get("beta")

        return data

    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return {}
