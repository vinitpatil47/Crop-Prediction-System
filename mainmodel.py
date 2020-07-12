# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:30:57 2020

@author: vinit
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from scipy.stats import norm
from scipy import stats
from scipy.stats import norm, skew #for some statistics

#visualization libraries
import matplotlib.pyplot as plt
from copy import deepcopy


df=pd.read_csv('maindata.csv')

df=df.dropna()

le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()
  
df['State_Name']= le1.fit_transform(df['State_Name']) 
df['District_Name']= le2.fit_transform(df['District_Name'])
df['Season']= le3.fit_transform(df['Season'])
df['Crop']= le4.fit_transform(df['Crop'])

df['Yield']=df['Production']/df['Area']
df=df.drop(['Production','Area'],axis=1)

df['Yield']=np.log1p(df['Yield'])

predictors = df.drop(['Yield'], axis=1)
output = df["Yield"]

x_train, x_val, y_train, y_val = train_test_split(predictors, output, test_size = 0.15, random_state = 0)

from sklearn.ensemble import RandomForestRegressor 

regressor = RandomForestRegressor(n_estimators = 100, random_state = 0) 
regressor.fit(x_train, y_train) 

import pickle

# Saving model to disk
pickle.dump(regressor, open('mainmodel.pkl','wb'))

model = pickle.load(open('mainmodel.pkl','rb'))

print(model.predict(x_val))

test = pd.read_csv("test.csv")

test

test['State_Name']= le1.transform(test['State_Name']) 
test['District_Name']= le2.transform(test['District_Name'])
test['Season']= le3.transform(test['Season'])
test['Crop']= le4.transform(test['Crop'])
final = [0,354,2019,4,1,2828.31]

f = np.reshape(final,(1,6))
f[:,[0,1,2,3,4,5]]
f[:,[0,1,2,3,4,5]] = f[:,[0,1,2,3,4,5]].astype(int)
print(model.predict(f))

