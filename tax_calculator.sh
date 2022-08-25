#!/usr/bin/bash
# Tax Calculator! 

figlet Tax Calculator

  echo " ########## Tax Calculator 2020" ############

  echo " version: 1:01v "

read -p "your all money: " all_money
echo " ${all_money} "

read -p "Dph ve formátu 0.2: " sazba_dph
echo " ${sazba_dph} "


my_dph=$(echo "${all_money} * ${sazba_dph}" |bc)
echo " This is your tax money $my_dph ,-CZK"


my_money=$(echo "${all_money} - ${my_dph}" |bc)
echo "This is my clean money, $my_money ,-CZK"

