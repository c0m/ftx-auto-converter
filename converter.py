from ftx.client import FtxClient
from settings import TARGET_TO_COINS, TARGET_FROM_COINS

def auto_converter(client: FtxClient) -> None:
    for coin in TARGET_FROM_COINS: 
        if decide_to_convert(client, coin):
            print("True")
    
def decide_to_convert(client: FtxClient, coin: str):
    balance = client.get_balance_coin(coin).get('availableWithoutBorrow')
    if balance > 0.000001: 
        return True
    return False
