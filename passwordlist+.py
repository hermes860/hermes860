#!/usr/bin/python3
## Passwordlist+
## madeBy: Ziomaister

import string
import random
import os.path
import secrets
#import subprocess
import colorama

from colorama import Fore, Back, Style

#subprocess.run("figlet" ,"passwordlist+")

print (Fore.BLUE + 'PasswordList+')

password = string.ascii_letters + string.digits
char=''
file = open("wordlist.txt" , "w")
for count in range(20):
    for x in random.sample(password,random.randint(8,8)):
        char+=x
    file.write(char+'\n')
    char=''
file.close()

print (Fore.RED + 'Password List is Ready!')
print (Fore.RED + "This is Passwordlistgenerator+")

print (Fore.BLUE + "made by Ziomaister")

######### Automaticaly Created Script /##########
