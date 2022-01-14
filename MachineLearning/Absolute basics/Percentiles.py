#https://www.w3schools.com/python/python_ml_percentile.asp
import numpy

#a number that describes the value that a given percent of the values are lower than.
#no method is shown how to work this out manually which sucks dick

#i think that this is giving a result number which the majority of elements under (below the highest)
#eg 99% of the elements are under the value 84

ages = [5,31,43,48,50,41,7,11,15,39,80,85,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75) #input the entries as first perameter and the percentage wanted within the second
y = numpy.percentile(ages, 99)
print(x)
print(y)
