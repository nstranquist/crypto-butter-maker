from kucoin.client import Trade
from api_request import post_request
import hmac
import base64
import hashlib
import time
import requests
import json
import uuid

class DarthBitcoinTrade:
  def __init__(self, api_key, api_secret, api_passphrase, ticker, is_sandbox=False):
    self.api_key = api_key
    self.api_secret = api_secret
    self.api_passphrase = api_passphrase
    self.ticker = ticker # format: COTI-USDT

    # self.market_client = Market(url="https://api.kucoin.com")
    # self.user_client = User(api_key, api_secret, api_passphrase)
    self.trade_client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=is_sandbox)

  def print_response(self, response):
    if response:
      print("got response: " + str(response))
      json_object = json.loads(response.text)
      print(json.dumps(json_object, indent=1))

  def get_headers(self, endpoint, params_string="", params_obj={}, http='GET'):
    now = int(time.time() * 1000)
    json_data = json.dumps(params_obj)
    str_to_sign = str(now) + "POST" + endpoint + json_data
    print(str_to_sign)
    signature = base64.b64encode(
        hmac.new(self.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
    passphrase = base64.b64encode(hmac.new(self.api_secret.encode('utf-8'), self.api_passphrase.encode('utf-8'), hashlib.sha256).digest())
    
    return {
      "KC-API-SIGN": signature,
      "KC-API-TIMESTAMP": str(now),
      "KC-API-KEY": self.api_key,
      "KC-API-PASSPHRASE": passphrase,
      "KC-API-KEY-VERSION": "2",
      # "Content-Type": "application/json"
    }

  def print_hello_world(self):
    print("Hello from kucoin!")

  def check_for_active_trades(self):
    print("Taking a new position. Checking for active trades")
    # check if any trades are active
      # get reference to kucoin profile

  def limit_buy(self, size, price):
    order_id = self.trade_client.create_limit_order(
      self.ticker,
      "buy",
      size=size,
      price=price
    )
    return order_id

  def limit_sell(self, size, price):
    order_id = self.trade_client.create_limit_order(
      self.ticker,
      "sell",
      size=size,
      price=price
    )
    return order_id

  def market_buy(self, size):
    # size = "1"
    order_id = self.trade_client.create_market_order(
      symbol=self.ticker,
      side="buy",
      size=size,
      type="market"
    )
    return order_id

  # must use 1 of the two params: "size" or "funds"
  def market_sell(self, size):
    uid = uuid.uuid4()
    clientOid = str(uid)

    # return response.json()
    order_id = self.trade_client.create_market_order(
      symbol="COTI-BTC",
      side="sell",
      # size=size,
      # clientOid=clientOid
      # type="market"
    )
    return order_id

  def market_sell_request(self, size):
    # uid = uuid.uuid4()
    # clientOid = str(uid)

    params_obj={"side":"sell","symbol":self.ticker,"type":"market","size":size},

    endpoint = "/api/v1/orders"
    params_string = "?side=sell&symbol=" + self.ticker + "&type=market&size=" + size
    headers = self.get_headers(endpoint=endpoint, http="POST",
      params_string=params_string,
      params_obj=params_obj
    )
    data_json = json.dumps(params_obj)

    url="https://api.kucoin.com" + endpoint

    response = requests.request('post', url, headers=headers, json=params_obj)

    # response = post_request(
    #   endpoint=endpoint,
    #   headers=headers,
    #   data=data_json
    # )

    print("status: " + str(response.status_code))
    print(response.text)

    return response

  def cancel_order(self, order_id):
    self.trade_client.cancel_order(order_id)

  def cancel_all_orders(self):
    response = self.trade_client.cancel_all_orders()
    self.print_response(response)
    return response.json()