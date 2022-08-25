#!/usr/bin/python

import threading

def Python():
    print("Python")

threads = []
for i in range(8):
    t = threading.Thread(target=Python)
    threads.append(t)
    t.start()







######### Automaticaly Created Script /##########
