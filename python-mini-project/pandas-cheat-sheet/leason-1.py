import pandas as pd

# https://levelup.gitconnected.com/pandas-basics-cheat-sheet-2023-python-for-data-science-b59fb7786b4d
# https://www.geeksforgeeks.org/select-rows-columns-by-name-or-index-in-pandas-dataframe-using-loc-iloc/


# Series — One dimensional labeled array
s = pd.Series([3,-7,5, 4], index=['a', 'b','c', 'd'])
print(s)

# Data Frame — A two dimensional labeled data structure
data = {'Country':['Belgium','India','Brazil'], 'Capital':['Brussels','New Delhi','Brasilia'], 'Population':[111907,1303021,208476]}
df = pd.DataFrame(data, columns = ['Country','Capital','Population'])
print(df)

# Drop values from rows (axis = 0)
s_new = s.drop(['a','c'])
print(s_new)

# Drop values from columns (axis = 1)
df_new = df.drop('Country', axis = 1)
print(df_new)



# Sort & Rank
# - Sort by labels along an axis
print(df.sort_index())
# - Sort by values along an axis
print(df.sort_values(by='Country'))
# - Assign ranks to entries
print(df.rank())


# Retrieving Series/DataFrame Information
# - (rows, columns)
print(df.shape)
# - Describe index
print(df.index)
# - Describe DataFrame columns
print(df.columns)
# - Info on DataFrame
print(df.info())
# - Number of non-NA values
print(df.count())


# Selection
# - Get one element
print(s['b'])
# - Get subset of a DataFrame
print(df[1:])
# - Select single value by row & column
print(df.iloc[0,0])
# - Select single value by row and column labels
print(df.loc[0,'Country'])
# - Select single row of subset rows
print(df.iloc[2])
# - Select a single column of subset of columns
print(df['Capital'])
# - Use filter to adjust DataFrame
print(df[df['Population'] > 120000])
# - Set index a of Series s to 6
s['a'] = 6
print(s)



# DataFrame Summary
data_two = {'Even':[2,4,6], 'Odd':[1,3,5]}
df_two = pd.DataFrame(data_two, columns = ['Even','Odd'])
print(df_two)
# - Sum of values
print(df_two.sum())
# - Cumulative sum of values
print(df_two.cumsum())
# - Minimum value
print(df_two.min())
# - Maximum value
print(df_two.max())
# - Summary statistics
print(df_two.describe())
# - Mean of values
print(df_two.mean())
# - Median of values
print(df_two.median())


# Applying Functions
# - Apply function
print(df_two.apply(lambda x: x*2))


# Data Alignment
s3 = pd.Series([7,-2,3], index=['a','c','d'])
print(s)
print(s3)
# - Internal Data Alignment
print(s + s3)
# - Arithmetic Operations with Fill Methods
print(s.add(s3, fill_value=0))
print(s.sub(s3, fill_value=2))
print(s.div(s3, fill_value=4))



# In/Out
# - Read CSV file
readData = pd.read_csv('pandas-cheat-sheet/file.csv')
print(readData.head())
# - Write to CSV file
df.to_csv('pandas-cheat-sheet/myDataFrame.csv')
# - Read Excel file
readExcelData = pd.read_excel('pandas-cheat-sheet/file.xlsx')
print(readExcelData.head())
# - Write to Excel file
df.to_excel('pandas-cheat-sheet/myDataFrame.xlsx')
# - Read multiple sheets from the same file
xlxs = pd.ExcelFile('pandas-cheat-sheet/file.xlsx')
df = pd.read_excel(xlxs, 'Sheet1')
print(df)
# - Write to SQL Query
from sqlalchemy import create_engine
engine = create_engine('sqlite:///TEST_DB.db')

# df.to_sql('myDF', engine, if_exists='append')
df.to_sql('myDF', engine, if_exists='replace')
# - Read SQL Query
queryData = pd.read_sql('SELECT * FROM myDF', engine)
print(queryData)
queryDataTwo= pd.read_sql_table('myDF', engine)
print(queryDataTwo)