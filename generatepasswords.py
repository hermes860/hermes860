#!/usr/bin/python3

import random
import string
import os.path
import secrets

length = 16

print("secret token= ", (secrets.token_hex(16)[0:length]))
print("secret token= ", (secrets.token_hex(16)[0:length]))

def passwordGenerate(PasswordLength=16):
    password = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(password) for i in range(PasswordLength))

passy = (passwordGenerate(16) )
passi = (passwordGenerate(10) )
passa = (passwordGenerate(8) )

print ("pass16char|" + passy)
print ("pass10char|" + passi)
print ("pass8char|" + passa)


