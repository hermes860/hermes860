#!/usr/bin/env python

import subprocess

subprocess.call("sudo apt update -y", shell=True)
subprocess.call("sudo apt install figlet -y ", shell=True)
subprocess.call("sudo apt install neofetch -y", shell=True)
subprocess.call("sudo apt install net-tools -y ", shell=True)
subprocess.call("sudo apt install git -y", shell=True)
subprocess.call("sudo apt update -y", shell=True)
subprocess.call("sudo apt install electronplayer -y", shell=True)
subprocess.call("sudo apt install arp-scan -y", shell=True)
subprocess.call("sudo apt install nmap -y", shell=True)
subprocess.call("sudo apt install kodi -y", shell=True)
subprocess.call("sudo apt install cubicsdr -y", shell=True)
subprocess.call("sudo apt install thunderbird -y ", shell=True)
subprocess.call("sudo apt install vim -y ", shell=True)
subprocess.call("sudo apt update -y", shell=True)
subprocess.call("sudo apt upgrade -y ", shell=True)
subprocess.call("sudo apt install spotify -y ", shell=True)
subprocess.call("sudo apt install -f ", shell=True)
subprocess.call("sudo apt autoremove -y", shell=True)



print("[+] Your aplication are installed. Beautiful day!")
