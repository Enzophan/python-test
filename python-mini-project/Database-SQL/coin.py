import pandas as pd
from sqlalchemy import create_engine
from binance.client import Client

client = Client()
engine = create_engine('sqlite:///TEST_DB.db')


def getData(symbol, start):
    frame = pd.DataFrame(client.get_historical_klines(symbol, '1m', start))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame.set_index('Time', inplace=True)
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

def sql_importer(sysbol, start = '2022-12-12'):
    try:
        max_date = pd.read_sql(f'SELECT MAX(TIME) FROM {sysbol}', engine).values[0][0]
        print(max_date)
        new_data = getData(sysbol, max_date)
        new_rows = new_data[new_data.index > max_date]
        new_rows[:-1].to_sql(sysbol,engine, if_exists='append')
        print(str(len(new_rows[:-1])) + ' new rows imported to DB')
    except: 
        new_data = getData(sysbol, start)
        new_data.to_sql(sysbol, engine)
        print(f'Created new table for {sysbol} with {str(len(new_data))} rows.')


sql_importer('BTCUSDT')
