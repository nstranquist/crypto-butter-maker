from kucoin.client import User
from api_request import get_request
import hmac
import base64
import hashlib
import time
import requests
import json

class DarthBitcoinUser:
  def __init__(self, api_key, api_secret, api_passphrase, account_id=""):
    self.api_key = api_key
    self.api_secret = api_secret
    self.api_passphrase = api_passphrase
    self.account_id = account_id

    self.user_client = User(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False)

  def print_response(self, response):
    if response:
      print("got response: " + str(response))
      json_object = json.loads(response.text)
      print(json.dumps(json_object, indent=1))

  def get_headers(self, endpoint):
    now = int(time.time() * 1000)
    str_to_sign = str(now) + 'GET' + endpoint
    signature = base64.b64encode(
        hmac.new(self.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
    passphrase = base64.b64encode(hmac.new(self.api_secret.encode('utf-8'), self.api_passphrase.encode('utf-8'), hashlib.sha256).digest())
    return {
      "KC-API-SIGN": signature,
      "KC-API-TIMESTAMP": str(now),
      "KC-API-KEY": self.api_key,
      "KC-API-PASSPHRASE": passphrase,
      "KC-API-KEY-VERSION": "2"
    }

  def get_ledgers(self):
    endpoint = "/api/v1/accounts/ledgers"
    headers = self.get_headers(endpoint)
    response = get_request(endpoint, headers=headers)
    self.print_response(response)
    return response.json()

  # Get All Active Trades
  def get_all_active_trades(self):
    return []
  
  # Get All Previous Trades
  def get_previous_trades(self, trade_count = 20):
    return []
  
  # Get Balance in a given asset
  def get_available_funds(self, asset_name):
    json_response = self.get_account_data()

    # funds_list = None
    # if not json_response.data:
    #   funds_list = json_response.data
    # else:
    #   try:
    #   except Exception as exc:
    #     print("there was an exception: " + str(exc))

    funds_list = json_response.get("data")
    
    found_item = None

    if funds_list:
      for item in funds_list:
        if item.get("currency") == asset_name and item.get("type") == "trade":
          print("found the asset")
          found_item = item
          break

      return found_item
    else:
      return None

  # Check if enough balance remaining for trade threshhold (20% default)
  def is_enough_balance_for_threshold(self, threshold=0.2):
    # query for remaining balance, query active trades
    return False

  def get_account_data(self):
    endpoint = "/api/v1/accounts"

    headers = self.get_headers(endpoint)

    response = get_request(endpoint, headers=headers)

    self.print_response(response)

    return response.json()
