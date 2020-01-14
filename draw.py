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
    'task_id':'aaaaaaa',
    'type':'1',
    'filename':'aaaaaa.mp4',
    'rtsp':'rtsp://admin:admin123@192.168.0.119:554/cam/playback?channel=2&subtype=0&starttime=2019_12_17_08_10_00&endtime=2019_12_17_08_10_30',
    'tm':tm,
    'sign':sign,
    'path':'test'

}

headers = {'Content-Type': 'application-json'}

response = requests.post(url="http://127.0.0.1:8081", headers=headers, data=json.dumps(data))

print (response.text)
