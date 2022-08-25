#!/usr/bin/python3
#app:pyscriptmaker
#author: elprezidento :-D 
import subprocess
import sys
print(" ###### Pyscript Maker ###### ")

#print("
# ,           ,
#    /             \                                                                                                                                             
#   ((__---,,,---__))                                                                                                                                            
#      (_) O O (_)____________                                                                                                                                      
#         \ _ /               |\                                                                                                                                    
#          o_o \ elprezidento | \                                                                                                                                   
#               \   _____  |__|   *                                                                                                                                  
#                |||   WW|||                                                                                                                                     
#                |||     |||")

subprocess.run(["figlet", "pymaker.py"])

#name_s = subprocess.run([ "read", "-p", "name of script to create:","${name_s}"],shell=True)
name_s = input("name of script to create: ")
print("your name of script: " + name_s)
subprocess.run(["touch" , name_s ])

subprocess.run(["echo /#!/usr/bin/python3 >>" + name_s ], shell=True)

subprocess.run(["echo  /#########  Automaticaly Created Script  /########## >>" + name_s ], shell=True)

subprocess.run(["sudo chmod +x " + name_s ], shell=True)



