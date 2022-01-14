#https://www.w3schools.com/python/python_ml_scale.asp

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler # < this is needed for calculating scale

#scale is used for data with different values, and different measurement units,
#eg: What is kilograms compared to meters? Or altitude compared to time?

#this time the volume column contains values in liters instead of cm3 (1.0 instead of 1000)

# the standard formula for scale is: z = (x - u) / s
# z is new value, x is original value, u is mean and s is standard deviation.

scale = StandardScaler()
df = pandas.read_csv("cars2.csv") # < this is the sam file but volume is litres
X = df[['Weight', 'Volume']]
scaledX = scale.fit_transform(X) # this calculates the scale to be applied to both x[0] and x[1]
print(scaledX)
