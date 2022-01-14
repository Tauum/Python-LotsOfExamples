import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

#https://www.w3schools.com/python/matplotlib_markers.asp
#marker documentation https://matplotlib.org/stable/api/markers_api.html

plt.plot(ypoints, 'o:r') # the line can also be customised in style and colour

#'-'	Solid line	 #':'	Dotted line	 #'--'	Dashed line	 #'-.'	Dashed/dotted line

#'r'	Red	#'g'	Green	#'b'	Blue	#'c'	Cyan
#'m'	Magenta	 #'y'	Yellow	 #'k'	Black	 #'w'	White


#marker size can also be changed but i dont know how to do it


plt.show()