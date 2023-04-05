# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:05:16 2022

@author: Omar
"""

import tkinter as tk
from tkinter import filedialog

def addMore():
    textt.insert(tk.END, "\n Good Bye \n")
    
def show():
    tk.messagebox.showinfo(title = "Text Widget", message = textt.get("1.0", tk.END))
    
def openFile():
    filename = tk.filedialog.askopenfilename(filetypes = (("text files", ".txt"), ("All files", ".")))
    # filename = tk.filedialog.askopenfilename(filetypes = (("text files", ".txt"), )) The Same as above
    print(filename)
    
win = tk.Tk()

win.geometry("700x400+680+150")


# Create menubar that contains:
    
    # File Menu(open, close)
    # Edit Menu(Copy, Paste)
    
menuBar = tk.Menu(win)
fileMenu = tk.Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = "Open", command = openFile)
fileMenu.add_separator()
fileMenu.add_command(label = "Close")

menuBar.add_cascade(menu = fileMenu, label = "File")

editMenu = tk.Menu(menuBar, tearoff = 0)
editMenu.add_command(label = "Copy", activebackground = "red", command = show)
editMenu.add_separator()
editMenu.add_command(label = "Paste")

menuBar.add_cascade(menu = editMenu, label = "Edit")

searchMenu = tk.Menu(menuBar, tearoff = 0)
searchMenu.add_command(label = "Find Text")
searchMenu.add_separator()
searchMenu.add_command(label = "Find Next")

menuBar.add_cascade(menu = searchMenu, label = "Search")

win.config(menu = menuBar)

textt = tk.Text(win, width = 30, height = 5, bg = "gray")
textt.grid(row = 0, column = 0, sticky = tk.W, padx = 10)

btn = tk.Button(win, text = "Add Sign", command = addMore)
btn.grid(row = 1, column = 0, sticky = tk.W, padx = 10)

btn2 = tk.Button(win, text = "Show", command = show, bg = "yellow")
btn2.grid(row = 1, column = 0, sticky = tk.E, padx = 10)







win.mainloop()