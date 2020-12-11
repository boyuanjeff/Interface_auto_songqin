# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zhoub
@file:test02.py
@time:2020-12-11
"""
# http://120.55.190.222:7080/api/mgr/loginReq   http协议
# https://120.55.190.222/api/mgr/loginReq      https协议
# cookie原生态直接关联后续接口实战
host = 'http://120.55.190.222:7080'
import requests


def login():
    url = f"{host}/api/mgr/loginReq"
    payload = {
        'username': 'auto',
        'password': 'sdfsdfsdf'
    }
    res = requests.post(url, data=payload)
    return res.cookies


# print(login())
def add_lesson(userCookie):
    utl = f'{host}/api/mgr/sq_mgr'
    res = requests.post(utl,cookies=userCookie)
    print(res.request.headers)
if __name__ == '__main__':
    userCookie = login()
    add_lesson(userCookie)