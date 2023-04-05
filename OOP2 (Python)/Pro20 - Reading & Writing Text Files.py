# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:56:50 2022

@author: Omar
"""

'''
names_list = ["Omar", "Ahmad", "Rajeh"]

file_write = open("names.txt", mode = "w")

file_write.write("\n".join(names_list))

file_write.close()
'''

names_list = ["Omar", "Ahmad", "Rajeh"]

with open('names.txt', mode = 'w', encoding = 'utf8') as file_write:
    file_write.writelines("\n".join(names_list))
    #print(file_write.readlines())


