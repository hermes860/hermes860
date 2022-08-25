#!/usr/bin/python3
##Port_scan.py
##Made_by:Ziomaister

import threading
import socket

target = input('Enter the Target IP: ')
xx = 1

def portscan(port):
    s = socket.sock(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)#

    try:
        scan = s.connect((target,port))

        print('Port :',port,"Is Open.")

        scan.close()

    except:
        pass

    for x in range(1,9000):

        trea = threading.Thread(target=portscan,kwargs={'port':xx})
        xx += 1
        trea.start()






######### Automaticaly Created Script /##########
