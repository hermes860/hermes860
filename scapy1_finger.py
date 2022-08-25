#!/usr/bin/python3
from scapy.all import *

result = input("Enter target IP? : ")

target = IP()
ping = ICMP()
target.dst = result
reply = sr1(target/ping)
if replay.ttl < 66:
    os = "Linux"
else:
    os = "Windows"

print ("Targeted System is: " +os)















######### Automaticaly Created Script /##########
