import requests
import os
from dotenv import load_dotenv 

load_dotenv()

# coingecko api
BASE_URL = os.getenv("COINGECKO_API_URL")

#coins taken
coins = ["bitcoin", "ethereum", "solana", "dogecoin"]

# function To fetch prices
def fetch_prices():
    ids = ",".join(coins)
    url = f"{BASE_URL}/simple/price?ids={ids}&vs_currencies=usd"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for coin in coins:
            price = data.get(coin, {}).get("usd", "N/A")
            print(f"{coin.capitalize()}: ${price}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching prices: {e}")

# test output
if __name__ == "__main__":
    fetch_prices()