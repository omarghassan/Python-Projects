# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:40:17 2022

@author: Omar
"""

number_of_mobile_types = int(input("Enter the number of mobile types: "))

i = 0

while i < number_of_mobile_types:
    
    barcode = int(input("Enter Barcode: "))
    mobile_type = input("Enter Mobile Type: ")
    quantity = int(input("Enter Mpbile's quantity: "))
    price = float(input("Enter Mobile's Price: "))
    
    mobileStore1 = {barcode: [mobile_type, quantity, price]}
    
    i += 1
      
mobileStore = mobileStore1
print(mobileStore)


def showMobiles(self):
    
    print("Barcode Mobile Type Quantity Price")
    print(mobileStore[barcode], mobileStore[mobile_type], mobileStore[quantity], mobileStore[price])
    

#print(mobileStore.showMobiles())



x = 1
mobileBarcodeList = []

while x != -1:
    
    var_x = input("Enter a sequence of sold mobiles barcodes. If value '-1' is entered the program will end.")
    
    ww = mobileBarcodeList.append(var_x)


















