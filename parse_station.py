#! /usr/bin/env python
#-*- coding:utf-8 -*-

import re
import requests
from pprint import pprint


url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
'''don't    verify      certificate'''
r = requests.get(url, verify=False)
print(r)
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)',r.text)

stations = dict(stations)
# stations = dict(zip(stations.values(), stations.keys()))
pprint(stations, indent=4)