# -*- coding:utf-8 -*-
import json
import time
import requests


import csv

with open('./201-info-20241127.csv', ) as f:
    lines = f.readlines()
    for row in lines:
        Address = row.split(',')[1]
        Address_pm = row.split(',')[2]
        Address_bg = row.split(',')[3]
        Address_bg_name = row.split(',')[4]
        # print("Address：", row.split(',')[1])
        # print("Address_bg_name：", row.split(',')[4])
        url = f"https://api.polygonscan.com/api?module=account&action=tokenbalance&contractaddress=0x2791bca1f2de4661ed88a30c99a7a9449aa84174&address={Address_pm.strip()}&tag=latest&apikey=7JUGEFVWU18VT2TPEMJPTD3J189JDQRTKV"
        # 获取响应数据 res.text
        # print(url)
        res = requests.get(url=url).text
        remaining_balance = int(json.loads(res)['result'])//int(1000000)
        print(f"remaining_balance: {Address_pm}, {Address_bg_name} :{remaining_balance}")
