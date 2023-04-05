# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:40:35 2022

@author: Omar
"""

import pandas as pd
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


# Read Data
golf_df = pd.read_csv("golf.csv")

# x y
x = golf_df.iloc[:, 0:4]

y = golf_df["Play"]

'''
# SVM
print('Apply Support Vector Classifier:')
clf = svm.SVC(kernel='linear')
scores = cross_val_score(clf, x, y, cv=5)
print(scores)
print(f"> Accuracy: {scores.mean()}")
print('\n')

# Random Forest Classifier
print('Apply Random Forest Classifier:')
clf = RandomForestClassifier()
scores = cross_val_score(clf, x, y, cv=5)
print(scores)
print(f"> Accuracy: {scores.mean()}")
print('\n')

# KNN
print('Apply K-Nearest Neighbors (K-NN) Classifier:')
clf = KNeighborsClassifier ()
scores = cross_val_score(clf, x, y, cv=5)
print(f"> Accuracy: {scores.mean()}")
'''

# Split Data Random Forest Classifier
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)

print(X_train, X_test)

rf = RandomForestClassifier()

rf.fit(X_train, y_train); # train the model

y_pred = rf.predict(X_test)

print(y_pred)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))


# Split Data with KNN

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)

knn = KNeighborsClassifier()

knn.fit(X_train, X_test)

y_pred = knn.predict(X_test)

print("y_predict", y_pred)
print("y_test: ", y_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))



