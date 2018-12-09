import requests
import jsonass
import hmac
import hashlib
from urllib.parse import urlencode
import time
secret = 'secret'
key='key'


method = {'method':'getInfo','nonce':str(int(time.time())) }
request = urlencode(method)
signature = hmac.new(secret.encode(), request.encode(), hashlib.sha512).hexdigest()
headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Key': key,
            'Sign': signature
        }


print(requests.post('https://yobit.net/tapi', data=request, headers=headers).json())
