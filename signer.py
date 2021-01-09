
import hashlib
import hmac
import base64

stsFormat = '%s/%s/%s'
def sign(path, timestamp, params, key, secret):
    stringToSign = stsFormat % (path, timestamp, params)
    b64StringToSign = base64.b64encode(stringToSign)
    signature = hmac.new(secret, b64StringToSign, hashlib.sha256).hexdigest()
    return signature