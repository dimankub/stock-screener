import finnhub
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("FINNHUB_API_KEY")
if not api_key:
    raise ValueError("FINNHUB_API_KEY не найден в .env")

client = finnhub.Client(api_key=api_key)

def fetch_basic_data(ticker: str) -> dict:
    try:
        quote = client.quote(ticker)
        profile = client.company_profile2(symbol=ticker)
        fundamentals = client.company_basic_financials(ticker, metric="all")["metric"]

        return {
            "name": profile.get("name"),
            "price": quote.get("c"),
            "market_cap": profile.get("marketCapitalization"),
            "pe_ratio": fundamentals.get("peBasicExclExtraTTM"),
            "pb_ratio": fundamentals.get("pbAnnual"),
            "roe": fundamentals.get("roeAnnual"),
            "roa": fundamentals.get("roaAnnual")


        }
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return {}
