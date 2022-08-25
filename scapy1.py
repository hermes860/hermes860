#!/usr/bin/python3

import subprocess

subprocess.call("figlet scapy1", shell=True)

print ("This is scapy module!")

from scapy.all import scapy
from scapy.all import IP
from scapy.all import sr

src_ip = "192.168.74.128"
dest_ip = "www.google.com"

from scapy.all import ICMP
from scapy.all import IP
from scapy.all import sr

if __name__ == "__main__":
    src_ip = "192.168.74.128"
    dest_ip = "www.google.com"

    ip_layer = IP(
            src = src_ip,
            dst = dest_ip
            )
    print(ip_layer.show())

# This will create an IP layer packet and display the content of the created packet. Note that the packet has not been sent yet.

# Next, to send an ICMP request, you can call the class to create an instance like this:

icmp_req = ICMP(id=100)

# id=100 helps the protocol to trace packets. To see what fields are present inside this request, you can write the following command:

#print(icmp_req.show())

#From here, you can see that the packet type is an echo request, which is used for testing the connection availability.
#From our previous discussion, we know that the application layer resides on top of the
#IP layer, and we have created two layers up until now. Now, the next goal would be to
#combine these two layers into a single packet that can be sent over the network. To do this,
#we can write the following code:

packet = ip_layer / icmp_req
#print(packet.show())

# This will list out the combined packet. Note the / operator. This operator is #used to
#combine different layers in Scapy. You start with the lower layer and keep on ading new layers with this / operator.

# Now, our request is ready to be sent. To send it, we can use the sr1 method we already imported:

response = sr(packet, iface="wlan0")
if response:
    print(response.show())



