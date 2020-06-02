#!/usr/bin/env python
# -*- coding=utf-8 -*-
#Code_network_udp_socket_server.py
#本程序用于实现简单的UDP服务端

import socket
import sys

address = ("172.19.200.121",6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print('Ready to receve data')
while True:
    try:
        data, addr = s.recvfrom(2048)
        if not data:
            print("client exit")
            break
        print("Reviced data:", data, "From:", addr)
    except KeyboardInterrupt:
        sys.exit()

s.close()
