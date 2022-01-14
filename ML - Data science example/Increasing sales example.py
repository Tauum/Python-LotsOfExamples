import pandas as pd
from sklearn.tree import DecisionTreeClassifier # < for predictions
from sklearn.model_selection import train_test_split # < for accuracy testing
from sklearn.metrics import accuracy_score # < also needed for accuracy testing

dataFile = pd.read_csv('music.csv') # < must have the same
dataFile.shape

#print(dataFile.shape) # shows its contents
#print(dataFile.describe()) # < basic info about the data set: count,mean, standard deviation, minimuim value, etc
#print(dataFile.values) # < returns a 2 dimensional array

X = dataFile.drop(columns=['genre']) # > only shows questions
#print(X)
y = dataFile["genre"] # > only shows answers
#print(y)
model = DecisionTreeClassifier() # < instanciate the model
model.fit(X,y) # < fit the data to the model

#### predictions
predictions = model.predict([[25,1],[22,0]]) # < new record of 25 year old male
print(predictions)

##### calculating accuracy of predictonns < SCORE CAN BE DIFFERENT EVERY TIME BECAUSE ITS A NEW DATA SET
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2) # < assigning specific data set arrays
                                                                # ^ change test size to increase accuracy
model.fit(X_train,y_train) # < changing the model to fit the train arrays
predictions = model.predict(X_test) # < generating predictions
score = accuracy_score(y_test,predictions) # < score of accuracy
print(score)

##### testing accuracy < SCORE CAN BE DIFFERENT EVERY TIME BECAUSE ITS A NEW DATA SET
model.fit(X_test,y_test)
predictions = model.predict(X_test) #jn1 < generating predictions
score = accuracy_score(y_test,predictions) # < score of accuracy
print(score)

