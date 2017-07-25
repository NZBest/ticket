#! /usr/bin/env python
#-*- coding:utf-8 -*-

from stations import stations
import warnings


f1 = input('please  enter the   starting    station :\n')
f = stations[f1]

t1 = input('please  enter   the    ending station :\n')
t = stations[t1]

d1 = input('please enter the departure time : xxxx-xx-xx\n')
d = str(d1)

print('being queried,please wait a moment')

url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+d+'&from_station='+f+'&to_station='+t  

warnings.filterwarnings('ignore')
