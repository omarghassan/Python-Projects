# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 12:48:15 2022

@author: Omar
"""


# Counter Control While Loop 
'''

the_list = [5, 2 , 10, 8]

sum_list = 0
i = 0

while i < len(the_list):
    sum_list += the_list[i]
    i += 1
    
print("\n The sum of elements in the list:",sum_list)
'''

# Sentineal While Loop
'''

num = int(input("Enter Value: "))

sum_elements = 0

while num != -1:
    sum_elements += num
    
    num = int(input("Enter Value: "))

print("The sum of elements: ", sum_elements)
'''

# Flagged While Loop
'''

sum_elements = 0

flag = True

while flag:
    
    num = int(input("Enter Value: "))
    
    if num == -1:
        flag = False # or WE can use Break
    
    else:
        
        sum_elements += num
        
print("The sum of elements:", sum_elements)
'''

# Pass Statement
'''

x = 7

if x < 10:
    pass

else:
    print("else")
    
x = 7

while x < 10:
    pass    #Infinite Loop

else:
    print("else")
    
 x = 1

while x < 10:
    
    if x %2 == 0:
        pass
    
    else:
        print(x)
    
    x += 1
'''


# For Loop
'''

the_list = [1, 2 , 5, 9, 7, 10]

for e in the_list:
    print(e)


sum_list = 0

for e in [1, 2 , 5, 9, 7, 10]:
    
    sum_list += e

print(sum_list)


for the_target in "Omar":
    print(the_target)
'''

# Loops in Dictionaries
'''

cities = {"Jordan": "Amman", "KSA": "Riyadh", "Kuwait": "Kuwait"}


for city in cities:
    print(city)

print("\n Second Loop \n")

for city in cities:
    print(cities[city])

print("\n Another Loop \n")

for city in cities:
    print(cities[city], city)
    
print("\n Again Another Loop \n")

for city in cities.keys():
    print(city)
    
print("\n Another and Another Loops \n")

for (x, y) in cities.items():
    print(x, y)
'''

# Range Function 

# print numbers from 1 to 10 using for statement

sum_elements = 0

for i in range(1, 12):
    print(i)

for i in range (1, 70):
    sum_elements += i
    
print(sum_elements)


























