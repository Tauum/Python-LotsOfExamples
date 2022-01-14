
import pandas
from sklearn import linear_model

#Coefficient is a factor describing relationship with an unknown variable.
#Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
#here we ask for the coefficient value of weight against CO2, and for volume against CO2.
# The answer(s) show what would happen if we increase, or decrease, one of the independent values.

print("weight vs co2 " + str(regr.coef_[0])) #if weight (x[0]) increase by 1, CO2 (y) increases by 0.00755095
print("volume vs co2 " + str(regr.coef_[1])) #if Volume (x[1]) increases by 1, CO2 (y) increases by 0.00780526

predictedOriginal = regr.predict([[2300, 1300]]) # calculating CO2 (Y) based off data stored
predictedTest = regr.predict([[3300, 1300]]) #verifying: 107.2087328 + (1000 * 0.00755095) = 114.75968
print(predictedOriginal)                                # ^ predicted original CO2 (y)
print(predictedTest)                                                   # ^ 1000 more weight x[0]
                                                                                 # ^  x[0] coefficient result
                                                                                                # ^ predicted CO2 (y)