from ftx.client import FtxClient
from settings import TARGET_TO_CURRENCY, TARGET_FROM_CURRENCIES

def auto_converter(client: FtxClient) -> None:
    for coin in TARGET_FROM_CURRENCIES: 
        balance = client.get_balance_coin(coin).get('availableWithoutBorrow')
        if balance > 0: 
            print("converty")
    