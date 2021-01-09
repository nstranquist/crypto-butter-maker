from darth_kucoin_market import DarthBitcoinMarket
from darth_kucoin_trade import DarthBitcoinTrade
from darth_kucoin_user import DarthBitcoinUser
import hmac
import base64
import hashlib
import time
import requests
import math

ticker = "COTI-BTC"
ticker2 = "COTI-USDT"

def test_darth_market():

  darth_market = DarthBitcoinMarket()

  json_response = darth_market.get_all_symbols()

  symbols_list = json_response.get("data")

  found_item = None

  for item in symbols_list:
    if item.get("symbol") == "COTI-BTC":
      print("found the asset")
      found_item = item
      break

  if found_item:
    print("Found Item: " + str(found_item))
  else:
    print("Did not find the item")

  # json_response = darth_market.get_ticker(ticker)

  # data = json_response.get("data")
  # print("Price: " + data.get("price"))
  # print("bid: " + data.get("bestBid"))
  # print("ask: " + data.get("bestAsk"))

def test_darth_user():
  print("testing user")
  trade_fee = 0.0008

  api_key="yourkey"
  api_secret="your-secret"
  api_passphrase="your-passphrase"
  account_id = "your-account-id"

  darth_trade = DarthBitcoinTrade(api_key, api_secret, api_passphrase, ticker="COTI-BTC")

  response = darth_trade.cancel_all_orders()
  print(str(response))
  # master_account_id = "26910993"

  # darth_user = DarthBitcoinUser(api_key, api_secret, api_passphrase, account_id=account_id)

  # # ledgers = darth_user.get_ledgers()

  # asset_name="COTI"
  # currency_data = darth_user.get_available_funds(asset_name=asset_name)

  # if currency_data:
  #   print(currency_data)
  #   balance = currency_data.get("balance")
  #   available = currency_data.get("available")
  #   print(currency_data.get("currency"))
  #   print("balance: " + balance)
  #   print("available: " + available)

  #   darth_market = DarthBitcoinMarket()
  #   market_response = darth_market.get_ticker("COTI-BTC")
  #   ticker_data = market_response.get("data")
  #   best_bid = ticker_data.get("bestBid")
  #   best_ask = ticker_data.get("bestAsk")


  #   # Sell with 100% of the balance
  #   # base_currency = round(float(available) * (1 - trade_fee), 8) - 0.00000001

  #   # available_size = math.floor(base_currency / float(best_bid))

  #   # print("base currency (btc): " + str(base_currency))

  #   # print("available size (coti): " + str(available_size))

  #   available_size = math.floor(float(available) * (1 - trade_fee))
  #   print("available size: " + str(available_size))


  #   # Calculate fee and min-order to compare it with available
  #   darth_trade = DarthBitcoinTrade(api_key, api_secret, api_passphrase, ticker="COTI-BTC")
    
  #   # response = darth_trade.limit_buy(size=available_size, price=best_bid)
  #   response = darth_trade.limit_sell(size=available_size, price=best_ask)
  #   if response:
  #     print("order id: " + str(response))
  #   else:
  #     print("nothing returned")

  #   # market_sell_json_response = darth_trade.market_sell(size=str(available_size))
  #   # market_sell_data = market_sell_json_response.get("data")
  #   # print(str(market_sell_data))

  # else:
  #   print("The currency was not found")


test_darth_user()
# test_darth_market()