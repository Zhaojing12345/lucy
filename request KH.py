import requests
import datetime
import pandas as pd
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

def load_private_key_from_file(file_path):
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,  # or provide a password if your key is encrypted
            backend=default_backend()
        )
    return private_key

def sign_pss_text(private_key: rsa.RSAPrivateKey, text: str) -> str:
    message = text.encode('utf-8')
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.DIGEST_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode('utf-8')

# Load the RSA private key
private_key = load_private_key_from_file('/Users/jingzhao/Documents/找工quant/club/MFAMS/Kalshi Project/kalshi-key-2.key')

# API details
base_url = 'https://api.elections.kalshi.com'
path = '/trade-api/v2/markets/trades?limit=1000&ticker=PRES-2024-KH'
headers = {
    'KALSHI-ACCESS-KEY': 'ef2474a1-0f16-4df4-9f8c-32aefebcda32'
}

# DataFrame to store results
columns = ["trade_id", "ticker", "count", "created_time", "yes_price", "no_price", "taker_side"]
df = pd.DataFrame(columns=columns)

while path:
    # Generate timestamp
    current_time_milliseconds = int(datetime.datetime.now().timestamp() * 1000)
    timestamp_str = str(current_time_milliseconds)
    
    # Sign request
    msg_string = timestamp_str + "GET" + path
    sig = sign_pss_text(private_key, msg_string)
    
    # Update headers
    headers.update({
        'KALSHI-ACCESS-SIGNATURE': sig,
        'KALSHI-ACCESS-TIMESTAMP': timestamp_str
    })
    
    # Send request
    response = requests.get(base_url + path, headers=headers)
    if response.status_code != 200:
        break  # Exit loop on error
    
    data = response.json()
    trades = data.get("trades", [])
    
    # Append new data to DataFrame
    if trades:
        df = pd.concat([df, pd.DataFrame(trades)], ignore_index=True)
    
    # Get next cursor
    cursor = data.get("cursor")
    if cursor:
        path = f'/trade-api/v2/markets/trades?cursor={cursor}&limit=1000&ticker=PRES-2024-KH'
    else:
        break  # No more pages, exit loop


df.to_csv('/Users/jingzhao/Documents/找工quant/club/MFAMS/Kalshi Project/Kamala Harris Data.csv')
print("Data saved to 'Kamala Harris Data.csv'")
print("Number of trades:", len(df))
print("First 5 rows:")
print(df.head())
print("Last 5 rows:")
print(df.tail())
print("Columns"
"trade_id: The unique identifier for the trade"
"ticker: The market ticker"
"count: The number of shares traded"
"created_time: The time the trade was created"
"yes_price: The price of a 'yes' share"
"no_price: The price of a 'no' share"
"taker_side: The side of the trade (maker or taker)")
