#https://www.w3schools.com/python/python_ml_normal_data_distribution.asp
import numpy
import matplotlib.pyplot as plt

#normal data distribtuion is where a number of elements are generated which concentrate around a given value
#this is also known as gaussian data distribution

#                       V this is the mean value to be centered around
#                            V this is the standard deviation
#                                   V amount to be generated
x = numpy.random.normal(5.0, 1.0, 100000)

#           V control the diagram accuracy displayed (more = accurate)
plt.hist(x, 100)
plt.show()