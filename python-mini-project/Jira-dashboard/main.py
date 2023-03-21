# https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html

import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('Jira-dashboard/Jira.csv')

df.set_index('Issue key', inplace=True)

df = df[['Summary', 'Labels', 'Priority', 'Sprint', 'Reporter', 'Creator', 'Issue Type', 'Status', 'Custom field (Story Points)', 'Updated']]
df['Updated'] = pd.to_datetime(df['Updated'])
df['Date'] = df['Updated'].dt.date

# Replace text
df['Labels'] = df['Labels'].fillna('None')

# print(df.head())
# print(df.count())
# print(sum(df['Labels'] == 'Pricer_Quotation'))
# print(df.groupby(['Labels']).size())
# print(df.groupby(['Sprint']).size())

point = sum(df['Custom field (Story Points)'] != '')
print(point)

print(df.groupby(['Issue Type']).size().reset_index(name='counts'))
print(df.groupby(['Issue Type']).apply(lambda x: x['Issue Type'].count()/point).reset_index(name='average'))

