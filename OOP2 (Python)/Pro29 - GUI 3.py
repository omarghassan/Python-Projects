# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 13:01:54 2022

@author: Omar
"""

btn_flag = True
def toggle():
    
   global btn_flag
   if btn_flag == True:
       btn.configure(text = "Logout")
       btn_flag = False
   else:
       btn.configure(text = "Login")
       btn_flag = True

from tkinter import *

win = Tk()

win.geometry("700x400+680+150")

btn = Button(win, text = "Login", width = 55, height = 5)
btn.pack()

btn2 = Button(win, text = "Quit", command = toggle)
btn2.pack()


win.mainloop()