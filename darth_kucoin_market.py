from kucoin.client import Market
from api_request import get_request_public
import json

class DarthBitcoinMarket:
  def __init__(self):
    # self.api_key = api_key
    # self.api_secret = api_secret
    # self.api_passphrase = api_passphrase

    # self.market_client = Market(key=api_key, secret=api_secret, passphrase=api_passphrase)
    self.market_client = Market(url="https://api.kucoin.com")

  def print_response(self, response):
    if response:
      print("got response: " + str(response))
      json_object = json.loads(response.text)
      print(json.dumps(json_object, indent=1))

  # Check if the market pair is supported by Kucoin
  def is_supported_market_pair(self, market_pair):
    is_supported = False

    # check if its supported

    return is_supported

  def get_all_symbols(self):
    # self.market_client.
    response = get_request_public(endpoint="/api/v1/symbols")
    self.print_response(response)
    return response.json()

  def get_one_symbol(self, market_name):
    response = get_request_public(endpoint="/api/v1/symbols", params={"market": market_name})
    self.print_response(response)
    return response.json()

  def get_all_markets(self):
    response = get_request_public(endpoint="/api/v1/markets")
    self.print_response(response)
    return response.json()

  def get_ticker(self, ticker_name):
    response = get_request_public(endpoint="/api/v1/market/orderbook/level1", params={"symbol": ticker_name})
    self.print_response(response)
    return response.json()
