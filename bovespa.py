from pandas_datareader import data as web
import pandas as pd
import matplotlib as plt
ticket = '^BVSP'

cotação = web.DataReader(ticket , data_source='yahoo', start='01-04-2021', end='04-30-2021')
print(cotação)
cotação.to_csv('{}.csv'.format(ticket))