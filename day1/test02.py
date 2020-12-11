# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zhoub
@file:test02.py
@time:2020-12-11
"""
host = 'http://121.41.14.39:8082'

import requests
import hashlib


def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


# print(get_md5("xintian"))
def login(inData, getToken=False):
    url = f"{host}/account/sLogin"
    inData["password"] = get_md5(inData['password'])
    payload = inData
    res = requests.post(url, params=payload)
    if getToken == False:
        return res.json()
    else:
        return res.json()['data']['token']


if __name__ == '__main__':
    data = {"username": "sq0777", "password": "xintian"}
    res = login(inData=data, getToken=1)
    print(res)
