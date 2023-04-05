# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:57:57 2022

@author: Omar
"""

import pandas as pd

'''
worksheet = pd.read_excel("Employee.xlsx") # With no arguments The first sheet is read by default

worksheet = pd.read_excel("Employee.xlsx", usecols = ["Name", "Salary"]) }-> Select Which coloumns to read

worksheet = pd.read_excel("Employee.xlsx", header = 0) }-> select which line in the is the header according to python numbering


print(worksheet["Name"])
print(worksheet.Name)
'''

worksheet = pd.read_excel("Employee.xlsx", header = 0)

print("Sum = " ,sum(worksheet["Salary"]))
print("Min = " ,min(worksheet["Salary"]))
print("Max = " ,max(worksheet["Salary"]))
print("Average = " ,worksheet["Salary"].mean())

salaries = worksheet["Salary"]
print(salaries)

s = 0
for i in salaries:
    s+=i
print("SUM: ", s)
print("AVERAGE: ", s/len(salaries))

'''
worksheet2 = pd.read_excel("Employee.xlsx", sheet_name = 1)
print(worksheet , "\n\n ------------ \n")
print(worksheet2)
'''






