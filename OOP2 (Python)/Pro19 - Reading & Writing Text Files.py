# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:47:41 2022

@author: Omar
"""

'''

Writing into text files

open }-> To create
         To Read

open("fileName", mode = "r" or "w")

default for mode is read

mode = "w" }-> Create New File if file dont exist  
               Overwrite if file exists
             
close()
'''

'''
Steps

1/ Open File
2/ Write File
3/ Close File }-> IF file is not closed, changes will not be saved

'''
e = ["\nAhmad\n", "rami\n", "Omar\n"]


files_create = open("test.txt", mode = "w")

files_create.write("Omar ")
files_create.write("Ghassan")

"""
Another way to open file without the need to write the close attribute

with open("test.txt", mode = "w") as files_create:
    files_create.writelines(e)
"""

'''
for w in e:
    files_create.write(w + "\n")
'''

files_create.writelines(e)

# files_create.writelines()

files_create.close()


''' READ From Files
----------------------------------------------------------
//////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////
----------------------------------------------------------
'''

'''

fileObject = ope("fileName")

file.read()         }-> return file content as string
    .readline()     }-> return first line as string
    .readlines()    }-> return file content as list of string,
                        each string represents a line

'''

file_read = open("test.txt")


fileRead = file_read.readline()
print(fileRead)

fileRead = file_read.readline()
print(fileRead)
print(type(fileRead))


fileRead = file_read.readlines()
print(fileRead)














