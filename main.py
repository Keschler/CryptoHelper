from pycoingecko import CoinGeckoAPI
from datetime import date as packet_date


cg = CoinGeckoAPI()


class Crypto:
    def __init__(self, cryptocurrency="bitcoin", currency="usd"):
        self.cryptocurrency = cryptocurrency
        self.currency = currency
        try:
            cg.ping()   # Check if pycoingecko api is available
        except Exception:
            print("pycoingecko api is currently not available!")

        crypto_supported = False

        for dicts in cg.get_coins_list():   # Check if cryptocurrency is supported
            if dicts["id"] == cryptocurrency.lower():
                crypto_supported = True
        if crypto_supported == False:
            print("Crypto not supported!")
            return

    def getPrice(self) -> dict:
        price = cg.get_price(ids=self.cryptocurrency,
                             vs_currencies=self.currency)
        return price

    def get_coins_list(self) -> list:
        coins_list = cg.get_coins_list()
        return coins_list
    
    def get_coin_history(self, date=packet_date.today()):
        date = packet_date.strftime(date, "%d-%m-%Y")     # Convert date
        coin_history = cg.get_coin_history_by_id(self.cryptocurrency, date)
        return coin_history


print(Crypto().get_coin_history())
