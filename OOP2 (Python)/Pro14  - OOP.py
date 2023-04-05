# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:25:21 2022

@author: Omar
"""

'''
Define class

class className:
    
    constructors
    functions
    variables
    
    pass statement
    
-----------------------------

Creating Objects

objectName = className(arguments)

-----------------------------

Defining Constructors

def __init__(self, parameter1, parameter2, ...) }-> self == this in java
    
    self.property1 = parameter1    }-> Instance Variable
    self.property2 = parameter2    }-> Instance Variable
    property3 = parameter3         }-> Local Variable

'''

'''
class Car:
    x = 100
    
k = Car()

w = Car()

print(Car.x)

Car.x = 7

print("Object K", k.x)

print("Object W", w.x)
'''

class person:
    
    def __init__(self, name, ID, gender, nationality):
        
        self.name = name
        self.ID = ID  # }-> private Instance Variable when using double underscore __ 
        self.gender = gender
        self.nationality = nationality
        self.address = None
    
    
    def printDetails(self):
        
        return f" name: {self.name} ID: {self.ID} gender: {self.gender} nationality: {self.nationality}"
        '''
        print("Name: ", self.name)
        print("ID: ", self.ID)
        print("Gender: ", self.gender)
        print("Nationality: ", self.nationality)
     '''
        
    def __str__(self):
        return f" name: {self.name} ID: {self.ID} gender: {self.gender} nationality: {self.nationality}"
    
    
f = person("Omar", 22256, "male", "Jordan")

print(f.printDetails())

print(f)

# print(f.ID)

# print(f)




# f.printDetails()















