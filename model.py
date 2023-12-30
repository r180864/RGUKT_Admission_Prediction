import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import pickle

df=pd.read_csv('admission.csv')
#print(df.head())


df['Govt/Private School']=df['Govt/Private School'].replace(['Govt school', 'Private'], [0.4, 0])

df['Caste']=df['Caste'].replace(['OC','BC-A','BC-B','BC-C', 'BC-D', 'BC-E','SC','ST', 'EWS'],
                                [0, 7, 10, 1, 7, 4, 15, 60, 10])

df['Gender']=df['Gender'].replace(['Male', 'Female'], [0, 0.34])

df["Performance Score"] = df["Govt/Private School"] + df["Caste"] + df["Gender"] + df["10th GPA"]

'''X=df[["10th GPA", "Govt/Private School", "Caste", "Gender"]]
Y=df[["Chance of Admit"]]'''
X=df.loc[:,["10th GPA","Govt/Private School","Caste","Gender"]]
Y=df["Chance of Admit"]

'''sc=StandardScaler()
X=sc.fit_transform(X)'''

x_train, x_test, y_train, y_test=train_test_split(X, Y, random_state=0, test_size=0.2)

'''
'''

LR=LinearRegression()
LR.fit(x_train, y_train)

pickle.dump(LR, open("model.pkl", "wb"))