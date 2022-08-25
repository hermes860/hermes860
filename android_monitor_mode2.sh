#!/bin/bash

echo "Android wifi Monitor mode"
figlet monitor_mode
sudo ip link set wlan0 down
echo 4 > /sys/module/wlan/parameters/con_mode
sudo ip link set wlan0 up
iw dev
airmon-ng
airmon-ng start wlan0
sudo airodumb-ng wlan0
