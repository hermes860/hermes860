#!/usr/bin/python3
## Crack SHA1 with Python
## madeBy: Ziomaister

from urllib.request import urlopen
import hashlib

hashsha1 = input("Enter your sha1 Hash .\n>")
wordlist = input("Enter your wordlist url")
allw = str(urlopen(wordlist).read(), 'utf-8')

for crack in allw.split('\n'):
    hashcrack = hashlib.sha1(bytes(crack, 'utf-8')).hexdigest()
    if hashcrack == hashsha1:
        print("Password found ", str(crack))
        quit()
    elif hashcrack != hashsha1:
        print("Password crack ", str(crack),"not found ")
print("Please Choose another wordlist and try again.")


######### Automaticaly Created Script /##########
