from bs4 import BeautifulSoup
import requests
import time
import json

url = "https://www.coingecko.com/es/monedas/bitcoin"
file_name = "crypto_scraping/values.json"

btc: list = []

response = requests.get(url)
doc = BeautifulSoup(response.text, 'html.parser')

def save_values(btc, file_name):
    with open(file_name, 'w') as f:
        json.dump(btc, f)

def load_values(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except:
        save_values(btc, file_name)

def scrape_btc(btc):
    while True:
        btc_value = doc.find_all(text="$")

        print(btc_value)
        btc.append(btc_value)
        save_values(btc, file_name)

        time.sleep(5)

if __name__ == "__main__":
    btc = load_values(file_name)
    # scrape_btc(btc)
    btc_value = doc.find_all(text="$")
    print(btc_value)