#!/usr/bin/python3
from scapy.all import *

def callback(pkt):
    pkt.show()

    sniff(iface="wlan0", prn=callback, filter="tcp", store=0)














######### Automaticaly Created Script /##########
