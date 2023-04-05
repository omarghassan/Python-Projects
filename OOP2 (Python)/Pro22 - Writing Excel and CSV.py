# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:59:42 2022

@author: Omar
"""

import pandas as pd

mobile = {"MobileType": ["Samsung", "Apple", "Nokia"],
          "Designer": ["Korea", "USA", "Finland"]}

theframe = pd.DataFrame(mobile)

print(theframe)
theframe.to_excel("Mobiles.xlsx", index = False) # }-> Write to Excel

theframe.to_csv("Mobiles.csv", index = False) # ]-> Write to CSV File


read_csvfil = pd.read_csv("Country.csv")

print(read_csvfil)

'''
Dataframes can be made by three ways:
    1/ Read Dicitionary
    2/ Read Excel Files
    3/ Read CSV Files
    
'''