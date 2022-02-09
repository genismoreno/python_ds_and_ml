import pandas as pd

sal = pd.read_csv('Salaries.csv')

# print(sal.head())

# print(sal.info())

base_pay = sal['BasePay'].dropna()
# print(base_pay.mean())

overtime_pay = sal['OvertimePay']
# print(overtime_pay.max())

joseph = sal.loc[sal['EmployeeName'] == 'JOSEPH DRISCOLL']
# print(joseph['JobTitle'])
# print(joseph['TotalPayBenefits'])

max_paid = sal.loc[sal['TotalPayBenefits'].idxmax()]
# print(max_paid)

min_paid = sal.loc[sal['TotalPayBenefits'].idxmin()]
# print(min_paid)


comp = (sal['Year'] >= 2011) & (sal['Year'] <= 2014)
# print(sal[comp].groupby('Year')['BasePay'].mean())

num_job_titles = sal['JobTitle'].nunique()
# print(num_job_titles)

job_titles = sal['JobTitle'].value_counts()
# print(job_titles.head(5))

year_2013 = sal['Year'] == 2013
one_repr = sal[year_2013]['JobTitle'].value_counts() == 1
# print(sum(one_repr))


def chief_string(name):
    return 'chief' in name.lower()


job_title_chief = sal['JobTitle'].apply(lambda x: chief_string(x))
# print(sum(job_title_chief))

sal['title_len'] = sal['JobTitle'].apply(len)
corr = sal[['title_len', 'TotalPayBenefits']].corr()
print(corr)