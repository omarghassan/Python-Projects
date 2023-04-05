# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 13:07:40 2022

@author: Omar
"""

from tkinter import *

the_window = Tk()

the_window.title("Welcome to Python GUI")
the_window.geometry("700x400+680+150")
#the_window.maxsize(700, 700)
#the_window.minsize(350, 350)

the_button = Button(text = "Top Button", bg = "white")
#the_button.pack(side = TOP, anchor = NW, padx = 55, pady = 34)
#the_button.place(x = 250, y = 170)
the_button.grid()

the_button2 = Button(text = "Bottom Button", bg = "black", fg = "white")
the_button2.pack(side = BOTTOM)
#               (side = "bottom")
#                       "right"
#                       "left"
#                       "top"

the_button3 = Button(text = "Left Button", bg = "grey")
the_button3.pack(side = LEFT)

the_button4 = Button(text = "Right Button", bg = "blue")
the_button4.pack(side = RIGHT)

'''
pack(anchor = NW)
              NE
              SE
              SW
              
the_button = Button(text = "Top Button", bg = "white")
the_button.pack(side = TOP, fill = BOTH)

the_button2 = Button(text = "Bottom Button", bg = "black", fg = "white")
the_button2.pack(side = BOTTOM, fill = BOTH)
#               (side = "bottom")
#                       "right"
#                       "left"
#                       "top"

the_button3 = Button(text = "Left Button", bg = "grey")
the_button3.pack(side = LEFT, fill = Y)

the_button4 = Button(text = "Right Button", bg = "blue")
the_button4.pack(side = RIGHT, fill = Y)

'''


the_window.mainloop()


