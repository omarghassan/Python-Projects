# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:07:26 2022

@author: Omar
"""

import tkinter as tk

def show():
    print(check1.get())

win = tk.Tk()

win.geometry("700x400+680+150")

question1 = tk.Label(win, text = "Countries you visited?")

check1 = tk.BooleanVar()
check2 = tk.BooleanVar()
check3 = tk.BooleanVar()

check1.set(True)

checkbtn = tk.Checkbutton(win, text = "Jordan", var = check1)
checkbtn2 = tk.Checkbutton(win, text = "Saudi Arabia", var = check2)
checkbtn3 = tk.Checkbutton(win, text = "Kuwait", var = check3)

btn = tk.Button(win, text = "Click ME", command = show)

question1.grid(row = 0, column = 0, sticky = tk.W, padx = 10)
checkbtn.grid(row = 1, column = 0, sticky = tk.W, padx = 10)
checkbtn2.grid(row = 2, column = 0, sticky = tk.W, padx = 10)
checkbtn3.grid(row = 3, column = 0, sticky = tk.W, padx = 10)
btn.grid(row = 4, column = 0, sticky = tk.W, padx = 10)

win.mainloop()