import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#https://www.w3schools.com/python/matplotlib_intro.asp

print(matplotlib.__version__)

xpoints = np.array([0, 6]) #stores two points in an array of X axis
ypoints = np.array([0, 250]) #stores two points in an array of Y axis

plt.plot(xpoints, ypoints) #loads points into the graph
plt.show() #loads graph into display

