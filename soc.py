#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while True:
    print(s.recvfrom(65565))






######### Automaticaly Created Script /##########
