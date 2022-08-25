# Monitor Mode Alfa script
#!/bin/bash
echo "Wifi device status"
sudo iw dev
echo "Turning wifi adapter down"
sudo ip link set wlan1 down
sudo iw dev wlan1 set monitor control
echo "Turning wifi adapter up"
echo "Wifi device status"
sudo iw dev
#figlet Monitor_Mode
echo "Happy Hacking and Beautiful Day!"
sudo airodump-ng wlan1 --ivs --wps -w /root/Dump01 --output format csv
echo "Your csv file is in /root/Dump01"
#figlet Done
