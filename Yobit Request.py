import requests
import json
import hmac
import hashlib
from urllib.parse import urlencode
import time
secret = '98993e91e56ee93e605c2bbf11f62d3d'
key='B4C68774679B819C5CF8C500418860E5'


method = {'method':'getInfo','nonce':str(int(time.time())) }
request = urlencode(method)
signature = hmac.new(secret.encode(), request.encode(), hashlib.sha512).hexdigest()
headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Key': key,
            'Sign': signature
        }


print(requests.post('https://yobit.net/tapi', data=request, headers=headers).json())
