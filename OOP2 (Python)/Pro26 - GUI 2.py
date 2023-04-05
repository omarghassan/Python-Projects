# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:04:18 2022

@author: Omar
"""

from tkinter import *

the_window = Tk()

the_window.title("Welcome to Python GUI")
the_window.geometry("400x400+680+150")
# the_window.maxsize(700, 700)
the_window.minsize(350, 350)

the_label = Label(the_window, text = "Hello", font = ("Times", 32, "italic underline")).pack()

the_label2 = Label(the_window, text = "Welcome to Python", relief = RAISED, borderwidth = 3,font = ("Times", 32, "italic underline")).pack()

# logo = PhotoImage(file = "Memati.gif")
# logo = PhotoImage(file = "im.gif")

# the_label3 = Label(the_window, image = logo).pack()

# the_label.configure(text="New text")

the_window.mainloop()