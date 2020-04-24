# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:15:06 2020

@author: 100293
"""

import cx_Oracle
import pandas as pd
conn=cx_Oracle.connect("Hospital","care#1234","TESTDB")
querry="SELECT * FROM pharma_sales_master WHERE ROWNUM <= 1000"
df1=pd.read_sql_query(querry,conn)

df1.shape

df1.describe()

df1.info()

null=df1.isnull().sum()
null_mean=df1.isnull().mean()

cln_df1=df1[df1.columns[df1.isnull().mean() < 0.7]] 
cl_df1=cln_df1.drop(columns=['DISCOUNT_ID','PATIENT','USER_ID','SYSTEM_ID'], axis='columns') 
corrr_matrix=cl_df1.corr()

##correlation

import seaborn as sns
##get correlation of each features in dataset
corrmat=cl_df1.corr()
top_corr_features=corrmat.index
plt.figure(figsize=(20,20))
#plot heatmap
g=sns.heatmap(cl_df1[top_corr_features].corr(),annot=True,cmap="RdYlGn")

data=cl_df1.drop(columns=['BILL_NO','TRA_DT','BILLING_TYPE','HOME_DELIVERY','BRANCH_ID','TRANSFER','WELFARE', 'CREDIT_CARD', 'FOUNDATION', 'BPL_MEMBER_ID', 'IGST', 'SGST','CGST', 'TAX_DISCOUNT', 'COUNTER_ID'], axis='columns')

data_profit=data['PROFIT']
data_profit=data['PROFIT'].describe()
data.columns
data.corr()

##correlation

import seaborn as sns
##get correlation of each features in dataset
corrmat=data.corr()
top_corr_features=corrmat.index
#plot heatmap
g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")
data.hist()

macare_data=data[['ITEM_VAL','DISCOUNT','BILL_AMT','COST','CASH','DOCTOR_ID','PROFIT']]

feature_columns=['ITEM_VAL','DISCOUNT','BILL_AMT','COST','CASH','DOCTOR_ID']
predicted_class=['PROFIT']


x=macare_data[feature_columns].values
y=macare_data[predicted_class].values

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=10)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x,y)


import pickle
pickle.dump(regressor,open('model.pkl','wb'))








