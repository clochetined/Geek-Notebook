import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

california_housing = fetch_california_housing()
# print(california_housing.DESCR)

data_california= pd.DataFrame(california_housing.data, columns=california_housing.feature_names) 
data_california['PRICE'] = california_housing.target
# print(data_california.head()
sns.jointplot(data_california,x='Population', y='PRICE')
sns.pairplot(data_california, vars=["PRICE", "Population", "AveRooms"])

lr = LinearRegression()

x_colum_list = ['AveRooms']
y_colum_list = ['PRICE']

data_california_x = data_california[x_colum_list]
data_california_y = data_california[y_colum_list]

lr.fit(data_california_x, data_california_y)

print(lr.coef_)
print(lr.intercept_)