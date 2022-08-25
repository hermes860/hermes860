#!/usr/bin/python3
from scapy.all import *

packetC = 0

def IPsAction(packet):
    return f"{packet[0][1].src} ==> {packet[0][1].dst}"

sniff(offline='test1.pcap', prn=IPsAction)

















######### Automaticaly Created Script /##########
