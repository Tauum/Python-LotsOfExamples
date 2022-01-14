import pandas as pd
dataFile = pd.read_csv('vgsales.csv') # < must have the same

print(dataFile)

dataFile.shape

print(dataFile.shape) # shows its contents

print(dataFile.describe()) # < basic info about the data set: count,mean, standard deviation, minimuim value, etc


print(dataFile.values) # < returns a 2 dimensional array