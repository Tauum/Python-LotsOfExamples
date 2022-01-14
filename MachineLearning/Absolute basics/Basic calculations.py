import numpy
from scipy import stats

#the fundimental basics of machine learning is calculation of mode, mean and median
#these modules will calculate these very quickly and easily without manually writing code

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
#mean is the averag value EG: (ammounts added up) / devided by elements = mean


y = stats.mode(speed)
#mode is the most frequent value EG: [1,1,1,1,2,3,5] mode = 1

z = numpy.median(speed)
#median is the value in the middle after sorting into order EG:
# [1,9,2,3,4,5,6] > # [1,2,3,4,5,6,9] > median = 4

print("mean: " + str(x) + "\n mode: " + str(y) + "\n median: " + str(z))