#!/usr/bin/python3
import string
import random
import os.path
import secrets

password = string.ascii_letters + string.digits
char=''
file = open("wordlist.txt" , "w")
for count in range(20):
    for x in random.sample(password,random.randint(8,8)):
        char+=x
    file.write(char+'\n')
    char=''
file.close()
print ('Password List is Ready!')




######### Automaticaly Created Script /##########
