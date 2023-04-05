# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:28:35 2022

@author: Omar
"""

'''
Write a separate program to accomplish this exercise.
Save the program with a filename stripping_names.py

Use a variable to represent a person’s name and
include some whitespace characters at the beginning
and end of the name. Make sure you use each character
combination, " t" and " n", at least once.

Print the name once, so the whitespace around the
name is displayed. Then print the name using each of
the three stripping functions, lstrip (), rstrip (), and
strip().
'''

name = "\t\n Omar Ghassan \t\t"

print("Without Stripping: ", name)

print("With Left Stripping: ", name.lstrip())
print("With Right Stripping: ", name.rstrip())
print("With Stripping: ",name.strip())