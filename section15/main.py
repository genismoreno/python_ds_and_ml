import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

customers = pd.read_csv('Ecommerce Customers.csv')

# print(customers.head())
# print(customers.info())
# print(customers.describe())
# print(customers.columns)

columns = ['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']
X = customers[columns]
y = customers['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)

intercept = lm.intercept_
print(intercept)
coef = lm.coef_
print(coef)

predictions = lm.predict(X_test)
# print(predictions)

mae = metrics.mean_absolute_error(y_test, predictions)
print(mae)

mse = metrics.mean_squared_error(y_test, predictions)
print(mse)

mrse = np.sqrt(mse)
print(mrse)

cdf = pd.DataFrame(coef, X_train.columns, columns=['Coeff'])
print(cdf)