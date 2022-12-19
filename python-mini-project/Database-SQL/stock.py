import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf

engine = create_engine('sqlite:///TEST_DB.db')

# df = yf.download('AAPL', start='2022-01-01', end='2022-12-20')
# df.to_sql('AAPL', engine)
# max_date = pd.read_sql('SELECT MAX(Date) FROM AAPL', engine).values[0][0]
# df[df.index > max_date].to_sql('AAPL', engine, if_exists='append')
# data_DB = pd.read_sql('AAPL', engine)
# print(data_DB)


def sql_importer(sysbol, start = '2022-01-01'):
    try:
        max_date = pd.read_sql(f'SELECT MAX(Date) FROM {sysbol}', engine).values[0][0]
        print(max_date)
        new_data = yf.download(sysbol, start=pd.to_datetime(max_date))
        new_rows = new_data[new_data.index > max_date]
        new_rows.to_sql(sysbol,engine, if_exists='append')
        print(str(len(new_rows)) + ' new rows imported to DB')
    except: 
        new_data = yf.download(sysbol, start=start)
        new_data.to_sql(sysbol, engine)
        print(f'Created new table for {sysbol} with {str(len(new_data))} rows.')


stocks = ['GOOG', 'TSLA', 'MMM', 'AAPL']

for stock in stocks:
    sql_importer(stock)