#!/usr/bin/env python
# -*- coding=utf-8 -*-
#Code_network_udp_socket_client.py
#本程序用于实现简单的udp客户端

import socket

address = ("192.168.200.121", 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Plz input data:')
    if not msg:
        s.sendto(msg.encode(), address)
        break
    s.sendto(msg.encode(), address)

s.close()
