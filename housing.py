# -*- coding: utf-8 -*-
"""Housing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1On7pIT2UnmZPr2Kpn5Ioa8OCbnCD5kjU
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load housing data (assuming 'housing_data.csv' is the dataset)
data = pd.read_csv('housing_data.csv')

# Data Cleaning and Preprocessing
data.dropna(inplace=True)  # Removing rows with missing values
data['age'] = 2023 - data['year_built']  # Create age of property feature
data = pd.get_dummies(data, columns=['property_type', 'location'])  # One-hot encode categorical variables

# Exploratory Data Analysis
sns.pairplot(data[['size', 'bedrooms', 'bathrooms', 'age', 'price']])
plt.show()

# Feature Selection and Splitting
X = data.drop('price', axis=1)
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Visualizing Results
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs. Predicted Housing Prices")
plt.show()