import numpy
import matplotlib.pyplot as plt

#most of the values will be around the center but a lot of results will vary

#                       V Mean value
#                            V Standard deviation
#                                 V Ammount
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)


#this will be a more tight grouping because the standard deviation is much less
a = numpy.random.normal(10.0, 0.2, 1000)
b = numpy.random.normal(20.0, 0.5, 1000)

plt.scatter(x, y)

#plt.scatter(a, b)
plt.show()