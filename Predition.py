import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import random
In [2]:
#Importing both the file using pandas 
data1 = pd.read_csv('movies data.csv')
data2 = pd.read_csv('ratings data.csv')
In [3]:
#Deleting unnecessary columns
data1 = data1.drop('Unnamed: 0',axis = 1)
data2 = data2.drop(['Unnamed: 0','Timestamp'],axis = 1)
