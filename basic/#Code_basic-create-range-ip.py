#!/usr/bin/python
# -*- coding=utf-8 -*-
#Code_basic-create-range-ip.py
#本程序用于产生用户输入的/24位掩码的所有IP地址。

import re

def rangeip(subnet):
    subnet_split = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3})',subnet)
    ip_list = []
    for i in range(1,255):
        ip_info = subnet_split[0] + '.' + str(i)
        ip_list.append(ip_info)
    return ip_list

if __name__ == '__main__':
    subnet = str(raw_input('Plz input subnet (Type:x.x.x.0/24):'))
    print rangeip(subnet)
