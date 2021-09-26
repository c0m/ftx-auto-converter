import threading
from ftx.client import FtxClient
from converter import auto_converter
from settings import API, SECRET, SUBACCOUNT


def main() -> None:
    threading.Timer(60 * 60.0, main).start()
    client = FtxClient(api_key=API,
                       api_secret=SECRET,
                       subaccount_name=SUBACCOUNT)
    auto_converter(client)


if __name__ == '__main__':
    main()
