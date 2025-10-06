import requests
import os
from datetime import datetime
import time
import json
from src.config.settings import API_URL, GECKO_API_KEY, DEFAULT_COIN, DEFAUT_CURRENCIES


def fetch_prices(coins, currencies, api_url=API_URL, api_key=GECKO_API_KEY, max_retries=3):

    params = {
        "ids" : ",".join(coins),
        "vs_currencies" : ",".join(currencies)
    }

    headers = {
        "x-cg-pro-api-key": api_key

    }

    for attempt in range(max_retries):
        try:
            response = requests.get(api_url, params=params, headers=headers, timeout=10)

            if response.status_code == 429:
                wait = int(response.headers.get("Retry-After", 10))
                print(f"Rate limited. Waiting {wait} seconds before retry...")
                time.sleep(wait)
                continue

            if response.status_code != 200:
                raise ValueError(f"API error {response.status_code}: {response.text}")
            
            data = response.json()
            data["fetched_at"] = datetime.now().isoformat()
            return data
        
        except json.decoder.JSONDecodeError:
            print("Failed to parse JSON response")
        
        except requests.exceptions.Timeout:
            print("Request timed out - maybe API too slow or network issue")

        except requests.exceptions.ConnectionError:
            print("Network connection failed")

        except ValueError as e:
            print(f"Invalid response: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        
        print(f"Attempt {attempt+1}/{max_retries} failed. Retrying...")
        time.sleep(3)

    print("Failed to fetch data after multiple retries.")
    return None


# print(fetch_prices(DEFAULT_COIN, DEFAUT_CURRENCIES))

def save_raw_data(data):
    current_dir = os.path.dirname(__file__)
    
    raw_dir = os.path.abspath(os.path.join(current_dir, "../../data/raw"))

    os.makedirs(raw_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"crypto_prices_{timestamp}.json"
    file_path = os.path.join(raw_dir, filename)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to: {file_path}")
    except Exception as e:
        print(f"Failed to save raw data: {e}")


def run_extract():
    coins = DEFAULT_COIN
    currencies = DEFAUT_CURRENCIES
    num_calls = 3
    delay = 5

    print(f"Starting extraction test at {datetime.now().isoformat()}")

    for i in range(num_calls):
        print(f"\n--- Fetching batch {i+1}/{num_calls} ---")
        data = fetch_prices(coins, currencies)

        if data:
            save_raw_data(data)
        else:
            print("No data fetched this round.")
        
        time.sleep(delay)
    
    print("Extraction test completed")

run_extract()
        
