import ccxt
import time


def check_price():
    binance = ccxt.binance()
    symbol = 'XRP/USDT'
    check_interval = 1

    while True:
        ticker = binance.fetch_ticker(symbol)
        price = ticker['last']
        max_price = ticker['high']

        if price < max_price * 0.99:
            print(f'Цена {symbol} упала на 1% от максимальной цены за '
                  f'последний час: текущая цена {price}')

        time.sleep(check_interval)


if __name__ == "__main__":
    check_price()
