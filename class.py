#!/usr/bin/python3
##how wrote class in python3

class Python:
    def __init__(self):
        self.word = "Programming"
        self.number = 100
        self.purpose = "Penetration Testing"

        
vari = Python()
print('Word is:', {vari.word})
print ('number is:', {vari.number})
print ('purpose is:', {vari.purpose})

### Example 2)

class Python:
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")

go = Python()
del go
## We can destroy the class using the __del__() destructor, for example

######### Automaticaly Created Script /##########
