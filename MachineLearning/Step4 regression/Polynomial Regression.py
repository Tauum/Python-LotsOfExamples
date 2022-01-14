#https://www.w3schools.com/python/python_ml_polynomial_regression.asp

import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#polynormal regression is used when inlear regression does not fit (a straight line thorugh the graph)

#here X is time of day (hour) Y is a cars speed
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 5)) #< at 1 this is straight, the higher the number the accurate the line is
myline = numpy.linspace(1, 22, 100) # < first two values are where to start in x and where to end in x (there are 22 values)
                                # ^ not sure what 100 represents
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

print(r2_score(y, mymodel(x))) # < this is calculating the relationship between X and Y (can be 0-1)
# ^ furthermore IF MYMODEL LAST NUMBER IS RAISED THE RELATIONSHIP WILL INCREASE

##### predicting a future value
speed = mymodel(17) #< this is predicting the Y of X 17

print("predicted Y of X 17: " + str(speed))
