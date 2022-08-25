#!/usr/bin/python3
## passwordgenerator+
## madeBy:ziomaister

#!/usr/bin/python3

import random
import string
import os.path
import secrets
import colorama

from colorama import Fore, Back, Style

print (Fore.BLUE + "This is Passwordgenerator+")

length = 16

print (Fore.GREEN + "Secret token 16 characters")

print("secret token= ", (secrets.token_hex(16)[0:length]))
print("secret token= ", (secrets.token_hex(16)[0:length]))

def passwordGenerate(PasswordLength=16):
    password = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(password) for i in range(PasswordLength))

passy = (passwordGenerate(16) )
passi = (passwordGenerate(10) )
passa = (passwordGenerate(8) )

print (Fore.YELLOW + "pass16char|" + passy)
print (Fore.BLUE + "pass10char|" + passi)
print (Fore.RED + "pass8char|" + passa)




######### Automaticaly Created Script /##########
