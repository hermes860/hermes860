#!/usr/bin/python3
## md5hashcrack.py
## madeBy:Ziomaister

import sys
import hashlib
import colorama
from colorama import Fore, Back, Style

# Crack MD5 Hashes Via Wordlist
def md5crack():
    print (Fore.GREEN + "MD5 hashes Crack .Store Hashes & list in .txt")
    md5crack = hashlib.md5()
    print ("")
    hash_file = input("Name of Hashes File? : ")
    wordlist = input("Name of wordlist file? : ")
    try:
        hashdocument = open(hash_file,"r")
    except IOError:
        print ("Wrong file name.")
        input()
        sys.exit()

    else:
        crack = hashdocument.readline()
        crack = crack.replace("\n",(""))

    try:
        wordlistfile = open(wordlist,"r")
    except IOError:
        print ("Wrong file name.")
        input()
        sys.exit()

    else:
        pass
        for line in wordlistfile:
            md5crack = hashlib.md5()
            line = line.replace("\n", (""))
            md5crack.update(line.encode('utf-8'))
            word_hash = md5crack.hexdigest()
            if word_hash==crack:
                print ("")
                print (Fore.BLUE + "Great! The Word match to the given hash is", line)
                sys.exit()
            else:
                print ("The hash given does not match to any word in the wordlist.")
                sys.exit()

print ("MD5 Crack"), md5crack()






######### Automaticaly Created Script /##########
