#Logistic Regression
#importing the required packages
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 

#loading the data
dataset = pd.read_csv('/content/drive/MyDrive/TCR/datasets/parkinsons.csv')

dataset.head()
dataset.shape
dataset.info()

#checking for null values if any
dataset.isnull().sum()

dataset.describe()

#EDA 
dataset.status.value_counts()
dataset['status'].value_counts()
dataset.groupby('status').mean()

#dividing the data in features and target
x = dataset.drop(columns=['name', 'status'], axis=1)
y = dataset['status']

x.head()

#test-train split
X_train, X_test, Y_train, Y_test  =  train_test_split(x, y, test_size=0.10, random_state=2)
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)

#standardising the data for better accuracy
sclaer = StandardScaler()
sclaer.fit(X_train)
X_train = sclaer.transform(X_train)
X_test = sclaer.transform(X_test)

#logistic regression in training data
model = LogisticRegression()
model.fit(X_train, Y_train)

#accuracy check using accuracy score
Y_pred_train = model.predict(X_train)
Y_pred_train_accuracy = accuracy_score(Y_train, Y_pred_train)
print("Accuracy on training Data : ", Y_pred_train_accuracy)

Y_pred_test = model.predict(X_test)
Y_pred_test_accuracy = accuracy_score(Y_test, Y_pred_test)
print("Accuracy on testing data : ", Y_pred_test_accuracy)

#testing the model with data
input_data = x[5:6]
input_data_as_array = np.asarray(input_data)
input_data_reshaped = input_data_as_array.reshape(1, -1)
std_scaler = sclaer.transform(input_data_reshaped)
prediction = model.predict(std_scaler)
print(prediction)
if (prediction[0] == 0):
  print("The Person doesnt have parkinson diesease")
else:
  print("The Person is suffering from Parkinson diesease")

#comparing the predicted value with actual value
print("The actual value is : ", y[5:6])

#This is the end of file, please ignore this comment.