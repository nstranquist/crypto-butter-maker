from flask import request

def print_request(request):
  print("API REQUEST:")
  # print(request.__dict__.items())

  print("Method", end=" ")
  print(request.method)

  if request.data:
    print("request.data:", end=" ")
    print(request.data)
  else:
    print("request cant access the data")
  
  # if request.json:
  #   print("request json:", end=" ")
  #   print(request.json)

  print("request all:", end=" ")
  print(request)

def parse_request_data(request_json, request_data, fields = ['direction', 'action', 'ticker', 'price']):
  if request.json:
    direction = request_json.get("direction")
    action = request_json.get("action")
    ticker = request_json.get("ticker")
    close_price = request_json.get("price")
    return direction, action, ticker, close_price
  else:
    try:
      # data = request.get_json(force=True)
      # print("forced json data:", end=" ")
      print("request data (no json received):", end=" ")
      print(request_data)
      # Still get the direction, action, and ticker data
      direction = request_data.get("direction")
      action = request_data.get("action")
      ticker = request_data.get("ticker")
      close_price = request_data.get("price")
      return direction, action, ticker, close_price
    except Exception as exc:
      print("An exception while parsing request data:", end=" ")
      print(exc)