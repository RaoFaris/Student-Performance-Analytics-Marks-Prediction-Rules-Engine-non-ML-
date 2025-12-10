import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt
pd.options.mode.chained_assignment = None

sp=pd.read_csv('StudentsPerformance.csv')
sp.head(5)
sp.describe()

#Checking for the missing values
print("Missing values inside each column:")
print(sp.isnull().sum())

#checking for the duplicate rows
print("\nNumber of duplicate rows:")
print(sp.duplicated().sum())

#generating bar plots to show frequency counts for eachcategorical column
sp['gender'].value_counts().plot.bar(title='Frequency Distribution of Gender', color=['red','blue'],figsize=(3,3))
sp['race/ethnicity'].value_counts().plot.bar(title='Frequency Distribution of Race/Ethnicity', color=['black','red','green','blue','cyan'],figsize=(3,3))
sp['parental level of edcation'].value_counts().plot.bar(title='Frequency distribution of Parental Level of Education',color=['black','red','green','blue','cyan','orange'],figsize=(4,4))
sp['lunch'].value_counts().plot.bar(title='Frequency Distribution of Lunch',color=['red','blue'],figsize=(3,3))
sp['test preparation course'].value_counts().plot.bar(title='Frequency Distribution of Test Preparation Course',color =['red','blue'],figsize=(3,3))
