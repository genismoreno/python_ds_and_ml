import numpy as np
import pandas as pd

df1 = pd.read_csv('df1', index_col=0)
head = df1.head()
print(head)

df2 = pd.read_csv('df2', index_col=0)

hist = df1['A'].hist(bins=30)