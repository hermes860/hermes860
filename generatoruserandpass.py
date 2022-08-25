#!/usr/bin/python3
import random
import string
import os.path

def passwordGenerate(PasswordLength=8):
    password = string.ascii_lowercase
    return ''.join(random.choice(password) for i in range(PasswordLength))

passy = (passwordGenerate(8) )
passi = (passwordGenerate(10) )
passa = (passwordGenerate(16) )


print (passy)
print (passi)
print (passa)

path = '/home/jakub'
name = input("File Name: ")
filename = os.path.join(path, name+".txt") 
with open (filename, "w") as file1:
        file1.write (str("|pass8|"))
        file1.write (str(passy))
        file1.write (str("|pass10|"))
        file1.write (str(passi))
        file1.write (str("|pass16|"))
        file1.write (str(passa))
######### Automaticaly Created Script /##########
