#importing the dependencies

import numpy as np
import pandas as pd        # pd frame more structure table
import matplotlib.pyplot as plt     #for data visualization
import seaborn as sns
from sklearn.preprocessing import LabelEncoder #sklearn lib for encoding the data in the ML model
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor #is used for classification and regression
from sklearn import metrics # metric is used to evaluate the model and accuracy of the model/metrix function that will be used to evaluate the model

#Data collection and analysis


#loading the dataset from csv_file to a pandas DataFrame

big_mart_data = pd.read_csv(r'C:\\Users\\chava\\Downloads\\archive\\Sales Project\\Train.csv')   
print(big_mart_data)

#this read csv function will load this csv file in a pandas 


# first 5 rows of dataframe
big_mart_data.head()

big_mart_data.shape








