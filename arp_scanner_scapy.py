#!/usr/bin/python3

from scapy.all import Ether, ARP, srp
if __name__ == "__main__":
    broadcast = "FF:FF:FF:FF:FF:FF"
    ether_layer = Ether(dst = broadcast)
    ip_range = "10.0.0.0/24"
    arp_layer = ARP(pdst = ip_range)

    packet = ether_layer / arp_layer

    ans, unans = srp(packet, iface = "wlan0", timeout=2)
    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
        print("IP = ", ip, " MAC = ", mac)





























######### Automaticaly Created Script /##########
