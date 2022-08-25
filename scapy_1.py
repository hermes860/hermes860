#!/usr/bin/python3

from scapy.all import *

target = input("Enter Target IP: ")

def packet_seq():
    packet = IP(dst=target, src="0.0.0.0")/TCP(sport=333, dport=445, seq=112233)/"Sequence number 112233"
    send(packet)
    sendp(packet, iface="eth0")


packet_seq()







######### Automaticaly Created Script /##########
