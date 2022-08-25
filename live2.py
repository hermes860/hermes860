#!/usr/bin/python3
import sh
from colorama import Fore, Back, Style

for octt in range(1,106,112):
    target = "127.0.0."+str(octt)

    try:
        sh.ping(target, "-c 1", _out="/dev/null")
        print (Fore.GREEN + "PING ",target , "Live")
    except sh.ErrorReturnCode_1:
        print (Fore.RED + "PING ", target, "Dead")




















######### Automaticaly Created Script /##########
