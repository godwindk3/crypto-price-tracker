from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://api.coingecko.com/api/v3/simple/price"
GECKO_API_KEY = os.getenv("GECKO_API_KEY")
DEFAULT_COIN = ["bitcoin", "ethereum"]
DEFAUT_CURRENCIES = ["usd"]