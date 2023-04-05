# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:39:48 2022

@author: Omar
"""


from tkinter import * 

# tk._test()

root = Tk()

root.title("Python")
root.geometry("600x600+500+100") # WidthxHeight 
root.maxsize(700, 700)
root.minsize(500, 500) # Overwrites the geometry dimension when it's bigger than the geometry dimesions 

the_label = Label(root, text = "Here We go", font = ("Times", 36, "italic underline"))
the_label.pack()

the_label2 = Label(root, text = "Welcome to Python", font = ("Times", 36, "italic underline"))
the_label2.pack()

root.mainloop()