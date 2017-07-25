#! /usr/bin/env python
#-*- coding:utf-8 -*-


import json
from get_urltrain import d
from 2 import request
import requests
from pprint import pprint
from get_urltrain import url
from prettytable import PrettyTable
from color_set import colored

r = requests.get(url, verify=False)
rows = r.json()['data']['datas']  # 将内容解析为列表
trains = PrettyTable()
'''
set the table header
'''
trains.field_names = ["车次", "车站", "时间", "历时", "商务座", "特等座",
                      "一等座", "二等座", "高级软卧", "软卧", "硬卧 ", "软座 ", "硬座", "无座"]

num = len(rows)
for row in rows:
    trains.add_row([row['station_train_code'],
                    '\n'.join([colored('green', row['from_station_name']),
                               colored('red', row['to_station_name'])]),
                    '\n'.join([colored('green', row['start_time']),  # 对于双行示的信息，设置颜色
                               colored('red', row['arrive_time'])]),
                    row['lishi'], row['swz_num'], row['tz_num'],
                    row['zy_num'], row['ze_num'], row['gr_num'],
                    row['rw_num'], row['yw_num'], row['rz_num'],
                    row['yz_num'], row['wz_num']])

print('查询结束，共有 %d 趟列车。' % num)  # 列表个数也就是列车个数
print(trains)
