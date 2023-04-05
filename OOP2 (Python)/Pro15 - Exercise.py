# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 12:57:29 2022

@author: Omar
"""

class user:
    
    def __init__(self, first_name, last_name, age):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def describe_user(self):
        
        return f"The user {self.first_name} {self.last_name} is at age of {self.age}"
    

user_1 = user("Omar", "Ghassan", 21)
user_2 = user("Ahmad", "Rajeh", 33)

print(user_1.describe_user())
print(user_2.describe_user())