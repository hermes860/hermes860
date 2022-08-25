#!/usr/bin/python3

import subprocess

subprocess.call("figlet scapy_example2", shell=True)

from scapy.all import ls, IP

# To get information about ip_layer, we can print ls like this:

dest_ip = "www.google.com"
ip_layer = IP(dst = dest_ip)
print(ls(ip_layer))

# If you want to access the individual field of any layer, you can simply use the dot (.) operator. For example, if you want to print dst in ip_layer, you can write the following code:

ip_layer = IP(dst = dest_ip)
print("Destination = ", ip_layer.dst)

# If you want to see a quick summary of the layer, you can call the summary method on the layer:

print("Summary = ",ip_layer.summary())


