from dotenv import load_dotenv
import os
import requests

gecko_api_key = os.getenv("GECKO_API_KEY")

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd"
}

headers = {
    "acccept": "application/json",
    "x-cg-pro-api-key": gecko_api_key
}

respond = requests.get(url, params=params, headers=headers)

print(respond.json())