#!/usr/bin/python3
#macchanger
#by:Ziomaister

import subprocess

subprocess.call("figlet macchanger",shell=True)

interface = "wlan0"
new_mac = "00:11:22:33:44:57"

print("Shutting down the interface")

subprocess.run(["ifconfig", "wlan0", "down"])

print("changing the interface hw address of ", interface, " to ", new_mac)

subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])

print("MAC address changed to ", new_mac)

subprocess.run(["ifconfig", interface, "up"])

print("network interfaced turned on")


