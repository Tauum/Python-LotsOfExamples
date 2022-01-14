#https://www.w3schools.com/python/python_ml_linear_regression.asp

import matplotlib.pyplot as plt
from scipy import stats


#Linear regression is used to find a relationship between variables and predict future values
#this graph is a scatter plot and the line is the predicted future values which is linear regression

#for example x represents age of a car and y is the speed it passed a point
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# V calculate future value line
        #V calculate future value line
                # V is the relationship (can range from -1 to 0 to 1 ) 0 means no relationship
                    #V doesnt explain
                        #V average of values fall from the regression line | in this case its 0.453536.....

slope, intercept, r, p, std_err = stats.linregress(x, y) # < this is the linear regression part

#https://www.statology.org/standard-error-regression/
#we’re interested in how well the regression model “fits” the dataset.
# Two metrics measure wellness: R (the relationship) and S (standard error of regression)
# standard error provides actual units whereas R shows percentages

#V this function predicts the future values
def myfunc(x):
  return slope * x + intercept

#this generates a new array with new values for Y
mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


speed = myfunc(10) # < this is predicting X of a 10 Y value based on the calculations provided


print( "speed - X prediction of 10 Y: " + str(speed))

print("\nslope: " + str(slope) + "\nintercept: " + str(intercept) + "\nrelationship: " + str(r)
      + "\nP?: " + str(p) + "\nstandard error: " + str(std_err))

mymodel.sort()
print( "mymodel: " + str(mymodel)) # if you look at this its generally the line adjacent to each plotted point in reverse