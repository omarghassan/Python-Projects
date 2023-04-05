# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:54:30 2022

@author: ASU
"""

'''
the_list = [5,3,7,2,9,8]

print("Original: " ,the_list)

the_list.sort()

print("Ascending Order: " ,the_list)

the_list.sort(reverse = True)

print("Reversed (Parameter): " ,the_list)

the_list.reverse()

print("Reversed (Function): " , the_list)
'''

'''

the_list = [5,3,7,2,9,8]

print(sorted(the_list))

the_list_sorted = sorted(the_list, reverse = True)

print(the_list_sorted)
'''

'''
tuple_x  = (2 , 7, 8, 9, 10)

print(tuple_x)

copy_tuple = list(tuple_x)

print(tuple_x)

print(copy_tuple)

copy_tuple.insert(3, 1000)

print(copy_tuple)

tuple_x = tuple(copy_tuple)

print(tuple_x)
'''

population = {"Amman": 7_000_000, 
              "Zarqa": 2_000_000,
              "Irbid": 600_000,
              "Aqaba": 250_000}

print(population)

print(population["Amman"])

population["Amman"] = 7_500_000

print(population["Amman"])

del population["Zarqa"]

print(population)

































