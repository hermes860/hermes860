#!/usr/bin/python

import subprocess

subprocess.call("figlet MACChanger", shell=True)



subprocess.call("sudo ifconfig wlp6s0 down", shell=True)
subprocess.call("sudo ifconfig wlp6s0 hw ether 00:00:00:00:00:07", shell=True)
subprocess.call("sudo ifconfig wlp6s0 up", shell=True)

subprocess.call("sudo ifconfig enp7s0 down", shell=True)
subprocess.call("sudo ifconfig enp7s0 hw ether 00:00:00:00:00:01", shell=True)
subprocess.call("sudo ifconfig enp7s0 up", shell=True)

