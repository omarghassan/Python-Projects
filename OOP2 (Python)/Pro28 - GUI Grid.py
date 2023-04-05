# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 13:50:00 2022

@author: Omar
"""

def kill():
    myWindow.destroy()

from tkinter import *

myWindow = Tk()

myWindow.title("Login")
myWindow.geometry("700x400+680+150")

usernameInput = Entry(myWindow)
passwordInput = Entry(myWindow, show = "*")

usernameLabel = Label(myWindow, text = "Username")
passwordLabel = Label(myWindow, text = "Password")

login = Button(myWindow, text = "Login", command = kill)

usernameLabel.grid(column = 0, row = 0)
passwordLabel.grid(column = 0, row = 1)
# passwordLabel.grid(column = 0, row = 1, sticky = N)
#                                                  S
#                                                  E
#                                                  W
usernameInput.grid(column = 1, row = 0)
passwordInput.grid(column = 1, row = 1)

login.grid(column = 1, row = 2)








myWindow.mainloop()