#!/bin/bash

BLACK="\033[30m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
PINK="\033[35m"
CYAN="\033[36m"
WHITE="\033[37m"
NORMAL="\033[0;39m"

# myenum script  
# v1.0
echo "		 (__) 
                 (oo) 
           /------\/ 
          / |    ||   
         *  /\---/\ 
            ~~   ~~   "


echo "myenum"

sleep 1.4

printf "URL:http://brmlab.cz  $GREEN $NORMAL  \n"

sleep 0.4

printf "Telefon: $BLUE 608 801 582  $NORMAL \n"
sleep 0.2
printf "Author: $BLUE elprezidento $NORMAL \n"

sleep 0.4
printf "\n"
printf "$RED myenum aplikaci používáte na vlastní nebezpečí! $NORMAL \n"

printf "\n"
printf "\n"

sleep 3

printf "$BLUE $NORMAL \n"
printf '%*s\n'"${COLUMNS: -$(tput cols)}" '' | tr '' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Linux Version"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/bin/cat /etc/issue;
printf "\n"
/bin/cat /etc/*-release

printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Kernel Info"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/bin/uname -ar
printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Network Info"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"


/bin/cat /etc/sysconfig/network
printf "\n"
/bin/cat /etc/resolv.conf

iprintf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED File System Info"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"
/bin/df -h

iprintf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Mounted File Systems with Pretty Output"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"
/bin/df -h

mount | column -t

printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED /etc/fstab File Contents"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"
/bin/cat /etc/fstab


printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED /etc/passwd File Contents"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/bin/cat /etc/passwd


printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED /etc/passwd File Contents"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/bin/cat /etc/shadow

printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED /etc/group File Contents"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/bin/cat /etc/group


printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED /etc/sudoers File Contents"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"
/bin/cat /etc/sudoers


printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Sticky Bit Files"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/usr/bin/find / -perm -g=s -o -perm -4000 ! -type l -maxdepth 3 -exec ls -ld {} \; 2>/dev/null

printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED World Writable Directories"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"
/usr/bin/find / -perm -222 -type d 2>/dev/null  


printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED World Writable FIles"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/usr/bin/find / -type f -perm 0777 2>/dev/null

printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Files Owned by Current User"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/usr/bin/find / -user $(whoami) 2>/dev/null


printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED /home and /root Permissions"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"
/bin/ls -ahlR /home/
/bin/ls -ahlR /root/ 


printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Logged on Users"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/usr/bin/w


printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Last Logged on Users"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

/usr/bin/last

printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Processes Running as root"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"
/bin/ps -ef | /bin/grep root


printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED Installed Packages for RHEL / Debian Based Systems"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"
# Enumarate CentOS / Ubuntu Boxes 
# This is not a great way of ID'ing a box, but I'm being lazy


printf "\n"
/usr/bin/dpkg -l

printf "\n"
/usr/bin/rpm -qa

printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED CentOS / RHEL Services that start at Boot"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"

chkconfig --list | grep $(runlevel | awk '{ print $2}'):on

printf "\n"
printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "##"
printf "\n"
printf "$RED"
printf "$BLUE## $RED List of init Scripts aka System Services"
printf "\n"
printf "$BLUE"
printf "##"
printf "\n"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "\n"
printf "$NORMAL"


ls /etc/init.d/

printf "$BLUE"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' '#'
printf "$NORMAL"

printf "\n More Linux enumeration commands can be found at: $BLUE https://brmlab.cz  \n"

printf "\n"
