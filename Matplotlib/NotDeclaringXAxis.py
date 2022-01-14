import matplotlib.pyplot as plt
import numpy as np

#it assumes x points are 1,2,3,4.....
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
#plt.plot(ypoints, "x") # again it can be plotted with points instead of a line

plt.show()