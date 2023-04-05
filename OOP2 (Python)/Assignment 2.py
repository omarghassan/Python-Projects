# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 18:10:52 2022

@author: Omar
"""

'''
Omar Ghassan Nazzal Abu Deyak
202111069
'''

'''
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
Question 1
'''


class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def getArea(self):
        
        area = self.length * self.width
        return area
    
    
class Parallelepiped(Rectangle):
    
    def __init__(self, length, width, height):
        
        Rectangle.__init__(self, length, width)
        self.height = height
        
    def getVolume(self):
        
        S = self.length * self.width
        volume = S * self.height 
        print("The Volume of this object is:", volume)
    
prl = Parallelepiped(7, 5, 3)

prl.getVolume()


'''
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
Question 2
'''



import pandas as pd
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


# Change the dataset from text file into csv file
# Read the dataset

# Iris-setosa 0
# Iris-versicolor 1
# Iris-virginica 2

iris_df = pd.read_csv("iris.csv")

x = iris_df.iloc[:, 0:4]

y = iris_df["Class"]


# Split Data SVM
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

print(X_train, X_test)

svm_clf = svm.SVC(kernel='linear')

svm_clf.fit(X_train, y_train) # train the model

y_pred = svm_clf.predict(X_test)
print(y_pred)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))

# Split Data Random Forest Classifier
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

print(X_train, X_test)

rf = RandomForestClassifier()

rf.fit(X_train, y_train); # train the model

y_pred = rf.predict(X_test)

print(y_pred)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))































