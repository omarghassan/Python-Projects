# -*- coding: utf-8 -*-
"""
Created on Sun May 29 01:45:30 2022

@author: Omar
"""

'''
Write a separate program to accomplish this exercise.
Save the program with a filename alien_colors2.py.

Choose a color for an alien as you did in Exercise 3 and write
an if-else chain.

If the alien’s color is green, print a statement that the player
just earned 5 points for shooting the alien.

If the alien’s color isn’t green, print a statement that the
player just earned 10 points.

Write one version of this program that runs the if block and
another that runs the else block.
'''

# Version 1

alien_color = "yello"

if (alien_color == "green"):
    print("You earned 5 points")
else:
    print("YOu earned 10 points")
    
# Version 2

alien_color = "green"

if (alien_color == "green"):
    print("You earned 5 points")
else:
    print("YOu earned 10 points")