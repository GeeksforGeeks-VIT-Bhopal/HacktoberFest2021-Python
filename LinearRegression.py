from numpy import loadtxt, ones, zeros, array, linspace, logspace
# from pylab import scatter, show, xlabel, ylabel, title, plot, contour
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the datasets
df = pd.read_csv('USA_Housing.csv')
# print(df.columns)
x = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
        'Avg. Area Number of Bedrooms', 'Area Population']]
x = df[['Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms']]
y = df[['Price']]

reg = LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10, random_state=2)
reg.fit(x_train, y_train)
print(reg.score(x_test, y_test))
print(reg.intercept_)
print(reg.coef_)
predictions = reg.predict(x_test)
print(reg.predict([[5, 6]]))

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
