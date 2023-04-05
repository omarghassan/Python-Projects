# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:02:31 2022

@author: Omar
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd

win = tk.Tk()
win.geometry("530x400+680+150")
win.title("Bookshop Managment System")

read_excelFile = pd.read_excel("books.xlsx")

def show_books():
    
    read_cols = read_excelFile.iloc[:, 0:2]
    read_cols = read_cols.set_index("id")

    text_entry.insert(tk.END, read_cols)

# Empty places to get books details later 
title_info = tk.Label(win, text="")
title_info.grid(row = 2, column = 0, sticky = tk.W, padx = 100)

author_info = tk.Label(win, text="")
author_info.grid(row = 3, column = 0, sticky = tk.W, padx = 100)

num_of_copies_info = tk.Label(win, text="")
num_of_copies_info.grid(row = 4, column = 0, sticky = tk.W, padx = 100)

price_info = tk.Label(win, text="")
price_info.grid(row = 5, column = 0, sticky = tk.W, padx = 100)

def show_book_details():
    search_for_book = input_entry.get()
    
    book_ID_list = read_excelFile["id"].to_list() 

    if search_for_book == "":
        tk.messagebox.showerror(title = "Book ID", message = "Please enter Book ID number")
    
    elif int(search_for_book) in book_ID_list:
        search_for_book = int(input_entry.get())
        
        # Configuring Books Details Labels
        title_info.config(text = read_excelFile["title"][search_for_book-1], fg = "red")
        author_info.config(text = read_excelFile["author"][search_for_book-1], fg = "red")
        num_of_copies_info.config(text = read_excelFile["no copies"][search_for_book-1], fg = "red")
        price_info.config(text = read_excelFile["price"][search_for_book-1], fg = "red")    
    
    else:
        tk.messagebox.showerror(title = "Book ID", message = "Invalid Book ID number")

def terminate():
    win.destroy()

# Menu Bar
menuBar = tk.Menu(win)
fileMenu = tk.Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = "Save")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = terminate)

menuBar.add_cascade(menu = fileMenu, label = "File")

editMenu = tk.Menu(menuBar, tearoff = 0)
editMenu.add_command(label = "Copy")
editMenu.add_separator()
editMenu.add_command(label = "Paste")

menuBar.add_cascade(menu = editMenu, label = "Edit")

win.config(menu = menuBar)

# Labels
label_exploreBooks = tk.Label(win, text = "Explore Books", font = ("Arial", 25))
label_exploreBooks.grid(row = 0, column = 0, sticky = tk.W, padx = 150)

label_enterBookID = tk.Label(text = "Enter Book ID")
label_enterBookID.grid(row = 1, column = 0, sticky = tk.W, padx = 10)

label_bookTitle = tk.Label(text = "Book Title")
label_bookTitle.grid(row = 2, column = 0, sticky = tk.W, padx = 10)

label_bookAuthor = tk.Label(text = "Book Author")
label_bookAuthor.grid(row = 3, column = 0, sticky = tk.W, padx = 10)

label_numOfCopies = tk.Label(text = "No. of Copies")
label_numOfCopies.grid(row = 4, column = 0, sticky = tk.W, padx = 10)

label_bookPrice = tk.Label(text = "Book Price")
label_bookPrice.grid(row = 5, column = 0, sticky = tk.W, padx = 10)

# Entry 
input_entry = tk.Entry(win, width = 3)
input_entry.grid(row = 1, column = 0, sticky = tk.W, padx = 100)

# Buttons
search_btn = tk.Button(text = "Search", command = show_book_details)
search_btn.grid(row = 1, column = 0, sticky = tk.W, padx = 150)

viewAll_btn = tk.Button(text = "View All", command = show_books)
viewAll_btn.grid(row = 1, column = 0, sticky = tk.W, padx = 300)

# Text 
text_entry = tk.Text(win, width = 50, height = 12, bg = "white")
text_entry.grid(row = 6, column = 0, sticky = tk.W, padx = 75)


win.mainloop()