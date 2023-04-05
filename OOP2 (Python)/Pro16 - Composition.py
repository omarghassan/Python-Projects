# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:33:16 2022

@author: Omar
"""

class Address:
    
    def __init__(self, street_name, city, country):
        
        self.street_name = street_name
        self.city = city
        self.country = country
        
    def getAddress(self):
        
        print(f"The address is at {self.street_name}, {self.city} city, {self.country}")
        

class person:
    
    def __init__(self, first_name, last_name, age, address):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        
    def describe_user(self):
        
        print(f"The user {self.first_name} {self.last_name} is at age of {self.age}")
        print(self.address.getAddress())
    

user1 = person("Omar", "Ghassan", 21, Address("Rainbow St", "Amman", "Jordan"))
user1.describe_user()


add1 = Address("Airport St", "Amman", "Jordan")
user2 = person("Ahmad", "Rajeh", 33, add1)
user2.describe_user()

'''
class person:
    
    def __init__(self, first_name, last_name, age, street_name, city, country):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = Address(street_name, city, country)
        
    def describe_user(self):
        
        print(f"The user {self.first_name} {self.last_name} is at age of {self.age}")
        print(self.address.getAddress())
    


#user_1 = person("Omar", "Ghassan", 21, "Airport St", "Amman", "Jordan")

#
user_2 = person("Ahmad", "Rajeh", 33, Address("Irbid St", "Irbid", "Jordan"))

user_1.describe_user()
user_2.describe_user()
'''








