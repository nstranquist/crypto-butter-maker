from flask import Flask, request, Response
from my_utils import print_request, parse_request_data
import datetime
import math
# Exchange Classes
from darth_kucoin_trade import DarthBitcoinTrade
from darth_kucoin_user import DarthBitcoinUser
from darth_kucoin_market import DarthBitcoinMarket

def create_app():
  app = Flask(__name__)

  trade_fee = 0.0008

  app.config.from_pyfile('settings.py')

  def get_api_keys():
    api_key = app.config.get('API_KEY')
    api_secret = app.config.get('API_SECRET')
    api_passphrase = app.config.get('API_PASSPHRASE')
    account_id = app.config.get('ACCOUNT_ID')
    return api_key, api_secret, api_passphrase, account_id

  @app.route('/webhook', methods=['POST'])
  def respond():
    print("the webhook was called")

    print_request(request)

    # do stuff with kucoin
    api_key, api_secret, api_passphrase, account_id = get_api_keys()

    direction, action, ticker, close_price = parse_request_data(request.json, request.data)

    print("direction:", end=" ")
    print(direction)
    print("action:", end=" ")
    print(action)
    print("ticker:", end=" ")
    print(ticker)
    print("close price:", end=" ")
    print(close_price)

    print("TIME:", end=" ")
    print(datetime.datetime.now())

    ticker = "COTI-USDT"

    darth_trade = DarthBitcoinTrade(api_key, api_secret, api_passphrase, ticker)

    darth_trade.print_hello_world()
    print("", end="\n\n")

    # if direction == "long":
    #   if action == "enter":
    #     # market buy (on margin?)
        
    #   elif action == "tp1":
    #     # margin sell 50% remaining cryptos

    #   elif action == "tp2":
    #     # margin sell 100% remaining cryptos

    # elif direction == "short":
    #   # market sell (on margin?)
    #   if action == "enter":
    #     # market sell (on margin?)
        
    #   elif action == "tp1":
    #     # margin buy with 50% remaining balance

    #   elif action == "tp2":
    #     # margin buy with 100% remaining balance

    # else:
    #   return


    # darth_trade.create_limit_order(x, y, z)

    return Response(status=200)


  # MARKET ORDERS
  @app.route('/market-buy', methods=['POST'])
  def market_buy():
    print("wants to market buy:")

    print_request(request)

    if not (request.json or request.data):
      return

    direction, action, ticker, close_price = parse_request_data(request.json, request.data)

    api_key, api_secret, api_passphrase, account_id = get_api_keys()

    print("market buy not set up yet")

    return Response(status=200)

  @app.route('/market-sell', methods=['POST'])
  def market_sell():
    print("wants to market sell:")

    print_request(request)

    if not (request.json or request.data):
      return

    direction, action, ticker, close_price = parse_request_data(request.json, request.data)

    api_key, api_secret, api_passphrase, account_id = get_api_keys()

    ticker_hardcoded = "COTI-BTC"

    darth_trade = DarthBitcoinTrade(api_key, api_secret, api_passphrase, ticker=ticker_hardcoded)

    order_id = darth_trade.market_sell()

    if order_id:
      print("Market sell order id: " + str(order_id))

    return Response(status=200)


  # LIMIT ORDERS
  @app.route('/limit-sell', methods=['POST'])
  def limit_sell():
    print("wants to limit sell")

    print_request(request)

    direction, action, ticker, close_price = parse_request_data(request.json, request.data)

    api_key, api_secret, api_passphrase, account_id = get_api_keys()

    ticker_hardcoded = "COTI-BTC"

    asset_name = 'COTI'

    darth_user = DarthBitcoinUser(api_key, api_secret, api_passphrase, account_id=account_id)

    currency_data = darth_user.get_available_funds(asset_name=asset_name)

    if currency_data:
      print(currency_data)
      balance = currency_data.get("balance")
      available = currency_data.get("available")
      print(currency_data.get("currency"))
      print("balance: " + balance)
      print("available: " + available)

      darth_market = DarthBitcoinMarket()
      market_response = darth_market.get_ticker(ticker_hardcoded)
      ticker_data = market_response.get("data")
      # best_bid = ticker_data.get("bestBid")
      best_ask = ticker_data.get("bestAsk")


      # Sell with 100% of the balance
      available_size = math.floor(float(available) * (1 - trade_fee))
      print("available size: " + str(available_size))

      # Calculate fee and min-order to compare it with available
      darth_trade = DarthBitcoinTrade(api_key, api_secret, api_passphrase, ticker=ticker_hardcoded)
      
      response = darth_trade.limit_sell(size=available_size, price=best_ask)

      if response:
        print("order id: " + str(response))
      else:
        print("nothing returned")

      # market_sell_json_response = darth_trade.market_sell(size=str(available_size))
      # market_sell_data = market_sell_json_response.get("data")
      # print(str(market_sell_data))

    else:
      print("The currency was not found")

    return Response(status=200)

  @app.route('/limit-buy', methods=['POST'])
  def limit_buy():
    print("wants to limit buy")

    print_request(request)

    direction, action, ticker, close_price = parse_request_data(request.json, request.data)

    api_key, api_secret, api_passphrase, account_id = get_api_keys()

    ticker_hardcoded = "COTI-BTC"
  
    asset_name = 'BTC'

    darth_user = DarthBitcoinUser(api_key, api_secret, api_passphrase, account_id=account_id)

    currency_data = darth_user.get_available_funds(asset_name=asset_name)

    if currency_data:
      print(currency_data)
      balance = currency_data.get("balance")
      available = currency_data.get("available")
      print(currency_data.get("currency"))
      print("balance: " + balance)
      print("available: " + available)

      darth_market = DarthBitcoinMarket()
      market_response = darth_market.get_ticker(ticker_hardcoded)
      ticker_data = market_response.get("data")
      best_bid = ticker_data.get("bestBid")
      # best_ask = ticker_data.get("bestAsk")


      # Buy with 100% of the balance
      base_currency = round(float(available) * (1 - trade_fee), 8) - 0.00000001

      available_size = math.floor(base_currency / float(best_bid))

      print("base currency (btc): " + str(base_currency))

      print("available size (coti): " + str(available_size))

      # Calculate fee and min-order to compare it with available
      darth_trade = DarthBitcoinTrade(api_key, api_secret, api_passphrase, ticker=ticker_hardcoded)
      
      response = darth_trade.limit_buy(size=available_size, price=best_bid)

      if response:
        print("order id: " + str(response))
      else:
        print("nothing returned")

      # market_sell_json_response = darth_trade.market_sell(size=str(available_size))
      # market_sell_data = market_sell_json_response.get("data")
      # print(str(market_sell_data))

    else:
      print("The currency was not found")

    return Response(status=200)


  # ENTER / EXIT / TAKE PROFITS
  def enter_position(direction, action, ticker):
    print("wants to enter a position (1)")

    print_request(request)

    is_success = True

    return is_success

  def take_profits_1(direction, action, ticker):
    print("wants to take profits (1)")

    print_request(request)

    is_success = True

    return is_success

  def take_profits_2(direction, action, ticker):
    print("wants to take profits (2)")

    print_request(request)

    is_success = True

    return is_success

  return app
