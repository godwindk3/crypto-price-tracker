from dotenv import load_dotenv
import os

API_URL = "https://api.coingecko.com/api/v3/simple/price"
API_KEY = os.getenv("GECKO_API_KEY")
DEFAULT_COINT = ["bitcoin", "ethereum"]
DEFAUT_CURRENCIES = ["usd"]