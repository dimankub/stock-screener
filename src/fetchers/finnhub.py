import finnhub
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("FINNHUB_API_KEY")
client = finnhub.Client(api_key=api_key)


def fetch_basic_data(ticker: str) -> dict:
    try:
        quote = client.quote(ticker)
        profile = client.company_profile2(symbol=ticker)

        return {
            "name": profile.get("name"),
            "price": quote.get("c"),
            "market_cap": profile.get("marketCapitalization")
        }
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return {}

