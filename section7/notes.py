# df.Series
# df.DataFrame
# df['W']
# df.drop('W', axis=1, inplace=True)
# df.shape
# df[['W', 'Y']]
# df.loc['A']
# df.iloc[2]

# booldf = df > 0
# df[booldf]
# df[df>0]
# df[df['W']>0]
# df[df['W']>0]]['Y']
# df[(df['W']>0) & (df['Y']>1)]

# df.reset_index(inplace=True)
# df['States'] = ['CA','OR', 'WY', 'MA']
# df.set_index('States')

# hier_index = list(zip(inside, outside))
# hier_index = pd.MultiIndex.from_tuples(hier_index)
# df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
# df.loc['G1']
# df.loc['G1'].loc[1]
# df.index.names = ['Groups', 'Num']

# df.xs(1, level='Num')

# df.dropna(axis=1, thresh=2)

# df.fillna(value='FILL NaN')

# byComp = df.groupby('Company')
# byComp.mean()
# df.groupby('Company').describe().transpose()

# pd.merge(left, right, how='inner', on='key')
# df1.merge(df2)

# pd.concat(df1, df2, df3)

# df['col2'].unique()
# df['col2'].nunique()
# df['col2'].value_counts()
# df[df['col1']>2]

def times2(x):
    return x*2

# df['col1'].apply(times2)
# df['col3'].apply(len)
# df['col2'].apply(lambda x: x*2)
# df.drop('col1', axis=1)
# df.columns
# df.index
# df.sort_values(by='col1')

# df.insull()

# df.pivot_table(values='D', index=['A', 'B'], columns=['C'])

# pd.read_csv('example.csv')
# df.to_clipboard()
# df.to_csv('my_output.csv', index=False)
# pd.read_excel('excel.xlsx', sheetname='Sheet 1')

# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:')
# df.to_sql('my_table', engine)
# sqldf = pd.read_sql('my_table', engine)

