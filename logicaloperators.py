#!/usr/bin/python3
##Logical and Membership Operators
#example1)
a = 6
b = 4
if a == 6 and b == 4:
    print ("They are True")
else:
    print ("They are false")


## As you can see if A==6 and the string (They are is printed.Logical operators include and not which can be used in more complex conditions as well.

#example2)
import colorama
from colorama import Fore, Back, Style

def test():
    print ("")
    try:
        A = 22
        B = 44
        if A < B:
            print (Fore.BLUE + "That True")
        else:
            print (Fore.Red + "That False")
    except KeyboardInterrupt:
        print ("Thank you")
        
test()

## We start writing the function by mentioning the name of the function. For example, if we want to name our function (test) we write def.

## example 3)

def age(number, number1):
    return number * number1

def print_welcome(name):
    print("Welcome", name)

    print_welcome("python")
    ag = 4
    ag1 = 5
    print("number =", ag, " number1 =", ag1, "age =", age(ag, ag1))


######### Automaticaly Created Script /##########
