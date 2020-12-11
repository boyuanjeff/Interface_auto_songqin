# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zhoub
@file:test_01.py
@time:2020-12-11
"""
host = 'http://121.41.14.39:8082'

import requests
import hashlib
def md5Encryption(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    print(md5.hexdigest())
    return md5.hexdigest()
def login():
    url = f"{host}/account/sLogin"
    payload = {"username":"sq0777"}
    payload["password"]=md5Encryption("xintian")
    res = requests.post(url,params = payload)
    # print(res.request.headers)
    # print(res.request.body)
    # print(res.request.url)
    # print(res.json())

if __name__ == '__main__':
    res = login()
    # print(res)