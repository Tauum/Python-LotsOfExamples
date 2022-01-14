#https://www.w3schools.com/python/python_ml_scatterplot.asp
import matplotlib.pyplot as plt

#A scatter plot is a diagram where each value in the data set is represented by a dot.
#it needs two arrays of the same length, one for x-axis, and one for y-axis:

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()
