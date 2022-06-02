# -*- coding: utf-8 -*-

# -- Project --

# # Project - Analyzing Sales Data
# 
# **Date**: 30 December 2021
# 
# **Author**: Kiskamol Kulpradith


# import data
import pandas as pd
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head()

# shape of dataframe
df.shape

# see data frame information 
df.info()

# convert order date and ship date to datetime in the original dataframe
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
df

# count nan in postal code column
df['Postal Code'].isna().sum()

# filter rows with missing values
no_ps_code = df[df['Postal Code'].isna()]
no_ps_code[['Row ID','Postal Code']].reset_index()

# which category has the most sales values ?
df.groupby('Category')['Sales'].sum() 

#info
print(df.columns)
df

# how many columns, rows in this dataset
f'rows->{df.shape}<-columns'

# is there any missing values?, if there is, which colunm? how many nan values?
df.isna().sum() 

# TODO 03 - your friend ask for `California` data, filter it and export csv for him
california_data = df.query('State == "California"').reset_index()
california_data.to_csv('california_data.csv')

# all order data in `California` and `Texas` in 2017 (look at Order Date), in csv file
df['Order_Year'] = pd.DatetimeIndex(df['Order Date']).year
df.query('State == ["California","Texas"]  & Order_Year == 2017')

# how much total sales, average sales, and standard deviation of sales your company make in 2017
df['Sales'].agg(['sum','mean','std'])

# which Segment has the highest profit in 2018
df.groupby('Segment')['Profit'].sum() #Consumer

# which top 5 States have the least total sales between 15 April 2019 - 31 December 2019

df[(df['Order Date'] >= '2019-04-15') & (df['Order Date'] <= '2019-12-31')]\
    .groupby('State')['Sales'].sum().sort_values().head(5)

# what is the proportion of total sales (%) in West + Central e.g. 25% 
df[(df['Region'] == 'West') | (df['Region'] == 'Central')]['Sales'].describe(include=all)

# find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
print(df[(df['Order_Year'] == 2019) | (df['Order_Year'] == 2020)].groupby('Product Name')['Order ID'].count().sort_values(ascending=False).head(10))
df[(df['Order_Year'] == 2019) | (df['Order_Year'] == 2020)].groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)


# Plot
df['Category'].value_counts().plot(kind = 'barh');

# Plot
df['Order_Year'].value_counts().plot(kind='pie');

# Create column to check to check that profit is above average
import numpy as np
df['Profit Above Average'] = np.where(df['Profit']> df['Profit'].mean(),'Yes','No')
df['Profit Above Average']

