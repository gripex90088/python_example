#!/usr/bin/env python
# coding=utf-8

import requests
import json
import time
import hashlib

tm=str(int(time.time()))
check_="421b47ffd946ca083b65cd668c6b17e6"
temp_sign=tm+check_

m=hashlib.md5()
b=temp_sign.encode(encoding='utf-8')
m.update(b)
sign=m.hexdigest()

data = {
    'type':'2',
    'task_id':'aaaaaaa',
    'tm':tm,
    'sign':sign
}

headers = {'Content-Type':'applicationo/json'}

response = requests.post(url='http://127.0.0.1:8081', headers=headers, data=json.dumps(data))

print(response.text)

