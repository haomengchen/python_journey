#!/usr/bin/python
# -*- coding=utf-8 -*-
#Code_basic-create-random-ip.py
#本程序用于产生随机的C类的私网IP地址

import random

def randomip():
    ip = ['192','168',str(random.randint(0,255)),str(random.randint(0,255))]
    mask = '/24'
    return '.'.join(ip) + mask

if __name__ == '__main__':
    print randomip()
