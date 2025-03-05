import pandas as pd
from datetime import datetime

data = pd.read_csv("./raw/GASCMDUSD.csv")
data['Date'] = data['Date'].astype(str)
data['Timestamp'] = data['Timestamp'].astype(str)

data['DateTime'] = data['Date'] + data['Timestamp']
del data['Date']
del data['Timestamp']

data['DateTime'] = pd.to_datetime(data['DateTime'], format="%Y%m%d%H:%M:%S")
data = data.set_index('DateTime')

#data.to_csv('./processed/gascmd.csv')

print(data.dtypes)
print(data.head())
