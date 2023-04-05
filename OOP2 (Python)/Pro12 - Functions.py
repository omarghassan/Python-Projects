# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:46:48 2022

@author: Omar
"""

'''
k_dictionary = {1:"ASU", 2:"PSUT", 3:"JU"}

r = k_dictionary.keys()

r = list(k_dictionary.keys())

print(r)
'''

'''
TO Define a function

def }-> reserved word

def function_name(parameters):
    statements
    ...
    ...
    ...
    
    return ...
'''

'''
def function_name(parameters(reciever))

function_name(argument(sender))
'''

'''
def print_message():
    print("Hello")

def print_message(message_input):
    print(message_input)
    
print_message("HEllo Message")
'''

'''
def add_function(x, y):
    print(x + y)
    
add_function(5,9)  # Positional Argument

add_function(x = 7, y = 2) # Keyword Argument
'''

'''
def game(name, age):
    
    if age < 13:
        print(f"{name}, Sorry you are not old enough to play this game")
    
    else:
        print(f"{name}, you are allowed to play the game")

game(name = "Omar", age = 21)

game("Ahmad", 16)

game("Rami", 12)

'''

'''
def game(name, age = 15):
    
    if age < 13:
        print(f"{name} who's age is {age}, Sorry you are not old enough to play this game")
    
    else:
        print(f"{name} who's age is {age}, you are allowed to play the game")


game("Omar", 21)

game("Sami")
'''

'''
def test_student(name, university = ""):
    
    if university != "":
        print(f"{name} is registered at {university}")
        
    else:
        print(f"{name} is not registered")
        
test_student("Ghali")

test_student("Ahmad", "ASU")
'''

'''
def test_student(name, university = None):
# None is evaluated as False
    
    if university:
        print(f"{name} is registered at {university}")
        
    else:
        print(f"{name} is not registered")
        
test_student("Ghali")

test_student("Ahmad", "ASU")
'''

'''
def print_list(the_list):
    
    for printing in the_list:
        print(printing)
        
print_list([1, 2, 3, 5, 7])

this_list = [1, 2, 3, 1000, 5, 7]

print_list(this_list)
'''

def add_to_list(h, item):
    h.append(item)
    return h

w = [1, 2, 3, 5, 7]
print(w)

add_to_list(w[:], 100)
print(w)

w = add_to_list(w[:], 100)
print(w)


















