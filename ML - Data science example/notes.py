
'''
step 1 get coffee

traditional programming techniques increasingly complex if not impossible

if you change input all the rules will change

so you build a model and give it lots of data 1000's

it will find patterns to recognise and you will ask it if its a specific source

like an image of a cat and it will give you a percentage likeliness of it being the correct answer

it has other applications such as: self-driving cars, robotics, language processing, vision processing, task completion
forecasting stock-market, controlling machines or software, software bots, etc.

'''

'''
step 2 

import the data, this can be done with CSV files 
this can be exported fro a database and saved into a CSV

then clean the data, remove duplicates of data 
- important to learn GOOD patterns to give the proper results (AKA DATA CLEANSING)

- DATA NEEDS TO ALSO BE CONVERTED TO NUMERICAL VALUES, EG: 3NF NORMALIZATION IN DATABASE CONCEPTS
it cannot be processed if it is not numerical

- Split data into two sets : training and test sets

TRAINING - is for generating a calculation of accuracy. having a random 80%~ data stored in a set
TESTING - is for testing the accuracy of the calculation. having a random 20%~ of the remaining data

eg. 1000 photos of a pencil | 800 are stored from the total for training | remaining 200 are stored for testing

- Creating a model for analysing the data there are lots of pre-defined algorithms out there such as:
 decision trees, neural networks etc.
 
 - Training the model feed it training data and look for patterns in data
 
 - Make predictions, give it example data and request the answering of a question eg.(is this picture of a wheel a wheel?)
 
 - Evaluate and improve ^ likely to be inaccurate so predict and measure accuracy.
 either select a different algorithm that will work or improve the perameters of the model for optimisation
'''

"""
LIBRARIES 

numpy provides a multi-dimensional arrays

pandas is a data analysis library thats a dataframe - a 2dimensional data structure similar to excel spreadsheet
data can be selected via row and column or a range of both rows and columns

matplotlibs - for plotting graphs, data visualisation

skit-learn - most popular machine learning giving common algorithms - decision trees etc. 

"""

'''
kaggle.com is a good place to find data science projects
'''
