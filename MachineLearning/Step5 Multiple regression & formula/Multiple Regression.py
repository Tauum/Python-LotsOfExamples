#https://www.w3schools.com/python/python_ml_multiple_regression.asp

from sklearn import linear_model # < LinearRegression() method to create a linear regression object.

import pandas # < this is needed for calculating multiple regression
#Pandas module allows reading csv files and return a DataFrame object.

#multiple regression is like linear but trying to predict a value based on two or more variables

df = pandas.read_csv("cars.csv") # < reading the file

X = df[['Weight', 'Volume']] # < list of independant values
y = df['CO2']

regr = linear_model.LinearRegression() # < creates a model for linear regression
regr.fit(X, y) # < applies x and y to model

#predict the CO2 emission (Y) where weight (x[0]) is 2300kg, and volume is 1300cm3 (x[1])
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

a = df['Car']
#print(a)
b = df[['Car','Model']]
#print(b)
c = df[['Car','Model','Weight','Volume']]
print(c)