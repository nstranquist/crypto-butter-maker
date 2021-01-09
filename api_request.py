import requests
# import hmac
# import base64
# import hashlib
# import time

def get_request_public(endpoint="", params={}, headers={}):
  base_url = "https://api.kucoin.com"

  try:

    response = requests.get(base_url + endpoint, params=params, headers=headers)

    print("response: " + str(response))

    return response

  except Exception as exc:
    print("Exception while getting request for endpoint: " + endpoint)
    print(exc)

def get_request(endpoint, params={}, headers={}):
  base_url = "https://api.kucoin.com"

  url = base_url + endpoint

  # now = int(time.time() * 1000)
  # str_to_sign = str(now) + 'GET' + endpoint
  # signature = base64.b64encode(
  #     hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
  # passphrase = base64.b64encode(hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())
  # headers = {
  #     "KC-API-SIGN": signature,
  #     "KC-API-TIMESTAMP": str(now),
  #     "KC-API-KEY": api_key,
  #     "KC-API-PASSPHRASE": passphrase,
  #     "KC-API-KEY-VERSION": "2"
  # }
  response = requests.request('GET', url, headers=headers)

  return response

def post_request(endpoint, params={}, headers={}, data={}):
  base_url = "https://api.kucoin.com"

  url = base_url + endpoint

  response = requests.request(method='POST', url=url, params=params, headers=headers, data=data)

  return response