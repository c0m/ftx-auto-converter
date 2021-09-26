from ftx.client import FtxClient
from settings import TARGET_TO_COIN, TARGET_FROM_COINS
MIN_BALANCE_TO_CONVERT = 0.000001

def auto_converter(client: FtxClient) -> None:
    for coin in TARGET_FROM_COINS:    
        balance = client.get_balance_coin(coin).get('availableWithoutBorrow')
        if balance > MIN_BALANCE_TO_CONVERT:
            convert_coin(client, coin, balance)

def convert_coin(client: FtxClient, from_coin: str, size: float):
    current_quote_request = client.post_quote_request(from_coin, TARGET_TO_COIN, 0.001)
    client.post_accept_quote(current_quote_request['quoteId'])