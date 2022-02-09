import pandas as pd

ecom = pd.read_csv('Ecommerce Purchases.csv')

# print(ecom.head())

# print(ecom.info())

mean = ecom['Purchase Price'].mean()
# print(mean)

max = ecom['Purchase Price'].max()
# print(max)

min = ecom['Purchase Price'].min()
# print(min)

english = ecom['Language'] == 'en'
# print(sum(english))

lawyers = ecom['Job'] == 'Lawyer'
# print(sum(lawyers))

am_vs_pm = ecom['AM or PM'].value_counts()
# print(am_vs_pm)

common_job_titles = ecom['Job'].value_counts()
# print(common_job_titles.head(5))

lot = ecom['Lot'] == '90 WT'
# print(ecom.loc[lot]['Purchase Price'])

credit_card = ecom['Credit Card'] == 4926535242672853
# print(ecom.loc[credit_card]['Email'])

filter = (ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)
# print(ecom[filter].count())

filter_exp = ecom['CC Exp Date'].apply(lambda x: x.split('/')[1] == '25')
# print(ecom[filter_exp].count())

ecom['host'] = ecom['Email'].apply(lambda x: x.split('@')[1])
print(ecom['host'].value_counts().head(5))