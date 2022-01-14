#https://www.w3schools.com/python/python_ml_train_test.asp

import numpy
import matplotlib.pyplot as plt

#to measure if a model (formula) is good enough / accurate it requires testing/training
#training a model means creating a model and testing means testing the accuracy

#Train/Test splits data set into: a training set and a testing set.
#80% training, and 20% testing.

numpy.random.seed(2)
# V here x represents time before execution
x = numpy.random.normal(3, 1, 100)
# V here y represents $ cost of execution
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show() # < this chart will show all data combined

