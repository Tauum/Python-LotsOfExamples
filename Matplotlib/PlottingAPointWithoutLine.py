import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'x') #this plots first and last point
                                # you can assign a character to the points
plt.show()