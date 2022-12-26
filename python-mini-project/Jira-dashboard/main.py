# https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Jira-dashboard/Jira.csv')

df.set_index('Issue key', inplace=True)

df = df[['Summary', 'Labels', 'Priority', 'Sprint', 'Reporter', 'Creator', 'Issue Type', 'Status', 'Updated']]
df['Updated'] = pd.to_datetime(df['Updated'])
df['Date'] = df['Updated'].dt.date

# Replace text
df['Labels'] = df['Labels'].fillna('None')

print(df.head())
# print(df.count())
print(sum(df['Labels'] == 'Pricer_Quotation'))
print(df.groupby(['Labels']).size())