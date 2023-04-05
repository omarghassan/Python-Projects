# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:02:52 2022

@author: Omar
"""

'''
Inheritance

                  father class
class className2(className1)
        son class

'''

class person:
    
    def __init__(self, first_name, last_name, age):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def getData(self):
        
        return f'Name: {self.first_name} {self.last_name} \n Age: {self.age}'
        
class student(person):
    
    def __init__(self, first_name, last_name, age, ID, GPA, major):
        
        #super().__init__(first_name, last_name, age)
        
        person.__init__(self,first_name, last_name, age)
        self.ID = ID
        self.GPA = GPA
        self.major = major
        
    def getData(self):
        
        return f'{super().getData()} \n ID: {self.ID} \n GPA: {self.GPA} \n Major: {self.major}'
        
        
std1 = student("Omar", "Ghassan", 21, 191433, 3.75, "CS")

print(std1.getData())
















        

 










