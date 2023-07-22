import pandas as pd


df1 = pd.read_csv('file1.csv', names=['col1', 'col2', 'col3'], quotechar="'", skipinitialspace=True)
df2 = pd.read_csv('file2.csv', names=['match'])

df = pd.merge(df1, df2, left_on=df1['col3'], right_on=df2['match'], how='inner')
