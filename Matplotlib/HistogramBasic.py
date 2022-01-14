import matplotlib.pyplot as plt
import numpy as np


#https://www.w3schools.com/python/matplotlib_histograms.asp

x = np.random.normal(170, 10, 250)

print(x)

plt.hist(x)
plt.show()