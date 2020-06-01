#!usr/bin/env python
# -*- coding=utf-8 -*-
#Code_network_arp_scan.py
#本程序用于实现按网段进行arp扫描

import re
from scapy.all import *

from GET_IP_netifaces import get_ip_address
from GET_MAC_netifaces import get_mac_address

def arp_scan(subnet):
    subnetsplit = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3})', subnet)
    ip_list = []
    Target = []
    for i in range(1,255):
        ipinfo = subnetsplit[0] + '.' + str(i)
        ip_list.append(ipinfo)

    destip = ip_list
    localmac = get_mac_address('bond0')
    localip = get_ip_address('bond0')
    ifname = 'bond0'

    result_raw = srp(Ether(src=localmac, dst='FF:FF:FF:FF:FF:FF')/ARP(op=1, hwsrc=localmac, hwdst='00:00:00:00:00:00', psrc=localip, pdst=destip), iface = ifname, timeout = 1, verbose = False)

    result_list = result_raw[0].res


    for i in result_list:
        key = i[1][1].fields['psrc']  # 每个元素中找到目标地址
        value = i[1][1].fields['hwsrc']  # 每个元素中找到对应的目标IP地址
        IPandMAC = [key, value]  # 将key,value的两个信息合成一个列表
        Target.append(IPandMAC)  # append()中只能赋一个值，因此需要上一步

    for i in Target:
        print 'Target-IP : %s ; Target-MAC : %s' % (i[0], i[1])  # 分别提取IP地址和列表

if __name__ == "__main__":
    subnet = str(raw_input('Plz input Target subnet (Type:x.x.x.0/24) : '))
    arp_scan(subnet)
