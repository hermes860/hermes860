#!/usr/bin/python3

from scapy.all import *

ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="10.0.0.33/24"),timeout=2)
ans.summary(lambda s_r: s_r[1].sprintf("%Ether.src% %ARP.psrc%") )
















######### Automaticaly Created Script /##########
