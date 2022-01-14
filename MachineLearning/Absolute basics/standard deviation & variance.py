#https://www.w3schools.com/python/python_ml_standard_deviation.asp
import numpy

speed = [86,87,88,86,87,85,86]
speed2 = [40, 20, 50, 100, 1000, 1500, 1, 1, 15, 500]

a1 = numpy.std(speed) #< this is a low standard deviation
a2 = numpy.std(speed2) #< this is a high standard deviation

#a number that describes how spread out the values are.
#A low standard deviation means that most of the numbers are close to the mean (average) value.
#A high standard deviation means that the values are spread out over a wider range.

print("a1: " + str(a1) + "\na2: " + str(a2))

#you can multiply the standard deviation by itself to get the variance
a3 = a1 * a1
a4 = a2 * a2
print("a1 converted to variance: " + str(a3) + "\na2 converted to variance: " + str(a4))

#variance is similar to standard deviation

b1 = numpy.var(speed)
b2 = numpy.var(speed2)
print("\nb1: " + str(b1) + "\nb2: " + str(b2))

#if you square root the variance it will turn into the standard deviation
b3 = numpy.sqrt(b1)
b4 = numpy.sqrt(b2)
print("b1 converted to standard deviation: " + str(b3) + "\nb2 converted to standard deviation: " + str(b4))

