import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

DataFile = pd.read_csv("music.csv")
X = DataFile.drop(columns=['genre'])
y = DataFile['genre']

model = DecisionTreeClassifier()

model.fit(X,y)

                                # V this is to export the diagram
tree.export_graphviz(model, out_file='music-recomenderfile.dot',
                     feature_names=['age','gender'], # X columns or (variables of the question)
                     class_names=sorted(y.unique()), # Y columns or (potential answers) | also sorted alphabetically
                     label='all', # < so every node has readable labels
                     rounded=True, # < so the boxes have rounded corners
                     filled=True) # < ensures each node is filled with a column

# the resulting file can be opened in vscode (WITH ADDED Graphviz (dot) EXTENSION FROM Stephanvs)
#THEN CLICK THREE DOTS TOP RIGHT AND OPEN PREVIEW TO THE SIDE