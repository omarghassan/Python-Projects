# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:25:04 2022

@author: Omar
"""

import tkinter as tk

def show():
    print(check1.get())

win = tk.Tk()

win.geometry("700x400+680+150")

question1 = tk.Label(win, text = "Country of Birth?")

check1 = tk.IntVar()

radiobtn = tk.Radiobutton(win, text = "Jordan", variable = check1, value = 1)
radiobtn2 = tk.Radiobutton(win, text = "Saudi Arabia", variable = check1, value = 2)
radiobtn3 = tk.Radiobutton(win, text = "Kuwait", variable = check1, value = 3) 

btn = tk.Button(win, text = "Click ME", command = show)

question1.grid(row = 0, column = 0, sticky = tk.W, padx = 10)
radiobtn.grid(row = 1, column = 0, sticky = tk.W, padx = 10)
radiobtn2.grid(row = 2, column = 0, sticky = tk.W, padx = 10)
radiobtn3.grid(row = 3, column = 0, sticky = tk.W, padx = 10)
btn.grid(row = 4, column = 0, sticky = tk.W, padx = 10)

win.mainloop()