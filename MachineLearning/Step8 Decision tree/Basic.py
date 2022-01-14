#https://www.w3schools.com/python/python_ml_decision_tree.asp

import pandas
from sklearn import tree
import pydotplus # < needed for decision trees

from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

#Decision Trees are Flow Charts, and can help make decisions based on previous experience


df = pandas.read_csv("shows.csv")
print(str(df) + "\n")

# VVVV To make decision tree, all data has to be numerical.
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df)

#Then separate feature columns from target column
#feature columns are those that we try to predict from
#target column is that the values we try to predict

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features] # < the x column is all of the features reduced to a single identifier
y = df['Go'] # < y is the result of x identifier
print("\n\n")
print(X)

print("\n")
print(y)

# VVVV THIS DOESNT WORK FOR SOME REASON

# dtree = DecisionTreeClassifier()
# dtree = dtree.fit(X, y)
# data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
# graph = pydotplus.graph_from_dot_data(data)
# graph.write_png('mydecisiontree.png')
#
# img=pltimg.imread('mydecisiontree.png')
# imgplot = plt.imshow(img)
# plt.show()