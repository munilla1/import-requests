import requests
import time


def cotizacion_en_euros(moneda):
    r = requests.get(f"https://api.coinbase.com/v2/exchange-rates?currency={moneda}")
    valor = r.json()["data"]["rates"]["EUR"]
    print(f"{moneda}: {valor}")


while(True):
    cotizacion_en_euros('BTC')
    cotizacion_en_euros('ETH')
    time.sleep(5)
