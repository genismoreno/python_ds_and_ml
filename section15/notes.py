import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('USA_Housing.csv')
# head = df.head()
# print(head)

# info = df.info()
# print(info)

# described = df.describe()
# print(described)

columns = df.columns
# print(columns)

# sns.pairplot(df)

# sns.distplot(df['Price']) Normal distribution
# sns.heatmap(df.corr())

columns = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']
X = df[columns]

y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)

intercept = lm.intercept_
# print(intercept)

coef = lm.coef_
# print(X_train.columns)
# print(coef)

cdf = pd.DataFrame(coef, X_train.columns, columns=['Coeff'])
# print(cdf)

from sklearn.datasets import load_boston

# boston = load_boston()
# print(boston['feature_names'])

predictions = lm.predict(X_test)
# print(predictions)

from sklearn import metrics

mae = metrics.mean_absolute_error(y_test, predictions)
print(mae)

mse = metrics.mean_squared_error(y_test, predictions)
print(mse)

mrse = np.sqrt(mse)
print(mrse)
