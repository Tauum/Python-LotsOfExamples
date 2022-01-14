import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # < for predictions
from joblib import dump, load # < this package is needed for model persistence

'''
model persistence is needed for high data sets, this can be done by saving results

this model is first generated and the dump made, 
then this code below is commented out to not use the same model again
VVVVVV
'''

# dataFile = pd.read_csv('music.csv') # < must have the same
# dataFile.shape
# X = dataFile.drop(columns=['genre']) # > every column but genre from structure
# y = dataFile["genre"] # > only shows answers
# model = DecisionTreeClassifier() # < instanciate the model
# model.fit(X,y) # < fit the data to the model

#joblib.dump(model, 'music-recomender.joblib') # < Generate joblib file
##https://joblib.readthedocs.io/en/latest/generated/joblib.dump.html

model = joblib.load('music-recomender.joblib') # < reassign this file as the model - predictions should match initial test

#### predictions
predictions = model.predict([[25,1],[22,0]]) # < new record of 25 year old male
print(predictions)