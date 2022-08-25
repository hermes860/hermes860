#!/usr/bin/python3

from scapy.all import *

ans,unans=sr( IP(dst="10.0.0.138")/TCP(dport=80,flags="S") )
ans.summary(lambda s_r: s_r[1].sprintf("%IP.src%, is Up"))









######### Automaticaly Created Script /##########
