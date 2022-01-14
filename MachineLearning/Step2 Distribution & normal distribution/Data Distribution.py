#https://www.w3schools.com/python/python_ml_data_distribution.asp
import numpy
import matplotlib.pyplot as plt

#data distribution is for making large random data sets
#this is how to generate a large ammount of data in NumPy

#                        V lowest value
#                             V highest value
#                                  V amount
x = numpy.random.uniform(0.0, 5.0, 250)

print(x) # < this shows all the elements values
print(type(x)) # < this shows the type is an array
print(len(x)) # < this shows the length of the array is correct at 250 elements

#this can be put into something like a histogram which will show the distribution frequencies of all results

#           V if more numbers are added here the diagram becomes more fine tuned / accurate
plt.hist(x, 5)
plt.show()

#im doing this below to visualise the elements in sorted order
x.sort()
print("\n\n Sorted X>\n" + str(x))
