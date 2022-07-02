import pandas_datareader as pdr
df = pdr.DataReader('2330.tw', 'yahoo')
print(df)
