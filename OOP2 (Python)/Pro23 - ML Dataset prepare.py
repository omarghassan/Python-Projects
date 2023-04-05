# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:06:39 2022

@author: Omar
"""

import pandas as pd

# Create an empty data frame:
golf_df = pd.DataFrame()


# Add outlook column:
golf_df['Outlook'] = ['sunny','sunny','overcast','rainy','rainy',
'rainy', 'overcast', 'sunny','sunny','rainy',
'sunny','overcast','overcast','rainy']


# Add Temperature column:
golf_df['Temperature'] = ['hot','hot','hot','mild','cool','cool',
'cool','mild','cool','mild','mild','mild','hot','mild']


# Add Humidity column:
golf_df['Humidity'] = ['high','high','high','high','normal','normal',
'normal','high','normal','normal','normal','high','normal','high']


# Add Windy column:
golf_df['Windy'] = ['false','true','false','false','false','true',
'true','false','false','false','true','true','false','true']


# Finally Add Play column:
golf_df['Play'] = ['no','no','yes','yes','yes','no','yes',
'no','yes','yes','yes','yes','yes','no']


#Print/show the new data:
print(golf_df)
y = golf_df['Play']

golf_df.to_csv("golf.csv", index = False)
