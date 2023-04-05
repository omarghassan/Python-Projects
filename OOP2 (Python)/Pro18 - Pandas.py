# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:37:44 2022

@author: Omar
"""

import pandas as pd

'''
Objects in Pandas

object_name = pd.DataFrame(data) }-> data either list, dictionary, file

'''

the_list = [[1, 5, 7], [2, 4, 8], [10, 20, 30]]

# the_dataset = pd.DataFrame(the_list)

# print(the_dataset)


levels = {0: ["1G03", "1G04", "Ground"],
          1: [1011, 1012, "First"],
          2: [2022, 2024, "Second"]} 

levels1 = [{0: "1G03", 1: 1011, 2: 2022},
           {0: "1G04", 1: 2022, 2: 2024}]

'''

levels = {0: ["Ground Floor"],
          1: ["First Floor"],
          2: ["Second Floor"]}

'''
the_dataset = pd.DataFrame(levels)

the_dataset_second = pd.DataFrame(levels1)

print(the_dataset)

print(the_dataset_second)


























