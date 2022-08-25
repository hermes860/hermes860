#!/usr/bin/python3

import sys
from scapy.all import *

print("pinging the target host....")
target = sys.argv[1]
icmp = IP(dst=target)/ICMP()

recv = sr1(icmp,timeout=10)
if recv == None:
    print("Target IP is Dead")
else:
    print("Target IP is Live")













######### Automaticaly Created Script /##########
