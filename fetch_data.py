import requests
import json
import time

# Binance API endpoint to get the latest Bitcoin price
api_url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

while True:
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        current_price = data['price']
        
        # Save the data to a JSON file
        with open('btc_price.json', 'a') as f:
            json.dump({'time': (time.strftime("%H:%M")), 'BTC price': current_price}, f)
            f.write('\n')
            
    time.sleep(60)  # Fetch data every minute
