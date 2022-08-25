#!/usr/bin/python3
#app:pyscriptmaker
#author: elprezidento :-D 
import subprocess
import sys
print(" ###### Bashscript Maker ###### ")

subprocess.run(["figlet", "Bashscriptmaker.py"])

name_s = input("name of script to create: ")
print("your name of script: " + name_s)
subprocess.run(["touch" , name_s ])

subprocess.run(["echo /#!/usr/bin/bash >>" + name_s ], shell=True)

subprocess.run(["echo  /#########  Automaticaly Created Script  /########## >>" + name_s ], shell=True)

subprocess.run(["sudo chmod +x " + name_s ], shell=True)

