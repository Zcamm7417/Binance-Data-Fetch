import requests
import json
import time
from requests.auth import HTTPDigestAuth
from config import api_key, api_secret


# Binance API endpoint to get the latest Bitcoin price
symbol = 'BTCUSDT'
api_url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'

while True:
    try:
        # Create a request session with authentication
        session = requests.Session()
        session.auth = HTTPDigestAuth(api_key, api_secret)

        # Send a GET request to the API
        response = session.get(api_url)

        if response.status_code == 200:
            data = response.json()
            current_price = data['price']

            # Save the data to a JSON file
            with open('btc_price.json', 'a') as f:
                json.dump({'Time': (time.strftime("%H:%M")), 'BTC price': current_price}, f)
                f.write('\n')  # Add a newline to separate entries (optional)

    except Exception as e:
        print(f"Error: {str(e)}")

    time.sleep(60)  # Fetch data every minute
