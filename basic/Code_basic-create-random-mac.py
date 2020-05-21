#!/usr/bin/python
# -*- coding=utf-8 -*-
#Code_basic-create-random-mac.py
#本程序用于产生随机的mac地址

import random

def randommac():
    mac = [random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff)]
    return ':'.join(map(lambda y: '%02x' % y, mac))

if __name__ == '__main__':
    print randommac()
