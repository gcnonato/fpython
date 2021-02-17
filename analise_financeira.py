import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import datetime

data = wb.DataReader('PG', data_source='yahoo', start='2000-1-1')
data['Resultado'] = (data['Adj Close']/data['Adj Close'].shift(1))-1

# data['Resultado'].plot(figsize=(8,5))
# plt.show()
media_simples = data['Resultado'].mean()

media_anual = data['Resultado'].mean()*250
# print(str(round(media_anual,5)*100)+'%')

data['RetLogaritmico'] = np.log(data['Adj Close']/data['Adj Close'].shift(1))
# print(data['RetLogaritmico'])

data['RetLogaritmico'].plot(figsize=(8,5))
# plt.show()
medialog = data['RetLogaritmico'].mean()*250
# print(str(round(medialog,5)*100)+'%')

carteiras = ['PG', 'MSFT', 'F', 'GE', 'AAPL']
database = pd.DataFrame()

for i in carteiras:
    database[i] = wb.DataReader(
        i, data_source='yahoo', start='2000-1-1'
    )['Adj Close']

# print(database.info())
# print(database.head())
# print(database.tail())

ret_carteiras = (database/database.shift(1))-1
# print(ret_carteiras.head())

pesos = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
np.dot(ret_carteiras, pesos)

mediacarteiras = ret_carteiras.mean()*100
mediaretornoanual = ret_carteiras.mean() * 250

np.dot(mediaretornoanual, pesos)
portfolio = str(round(np.dot(mediaretornoanual, pesos),5)*100) + '%'

pesos2 = np.array([0.3, 0.3, 0.15, 0.05, 0.2])
portfolio2 = str(round(np.dot(mediaretornoanual, pesos2),5)*100) + '%'

# print(mediacarteiras)
# print(mediaretornoanual)
# print(portfolio)
# print(portfolio2)

ind_carteiras = ['^GSPC', '^IXIC', '^GDAXI']
indicadores = pd.DataFrame()

for t in ind_carteiras:
    indicadores[t] = wb.DataReader(
        t, data_source='yahoo', start='2000-1-1'
    )['Adj Close']


(indicadores / indicadores.iloc[0]*100).plot(figsize=(8,5))


retindicadores = (indicadores / indicadores.shift(1)) - 1
retindicadoresanuais = retindicadores.mean()*250

# print(indicadores.head())
# print(indicadores.tail())
# plt.show()
# print(retindicadores.tail())
# print(retindicadoresanuais)

carteiras = ['PG', 'AAPL']
database = pd.DataFrame()

for i in carteiras:
    database[i] = wb.DataReader(
        i, data_source='yahoo', start='2010-1-1'
    )['Adj Close']

retorno = np.log(database/database.shift(1))
retorno['PG'].mean()
retorno['PG'].mean()*250
retorno['PG'].std()
retorno['PG'].std()*250*0.5

retorno['AAPL'].mean()
retorno['AAPL'].mean()*250
retorno['AAPL'].std()
retorno['AAPL'].std()*250*0.5

data = wb.get_data_yahoo(
    'AAPL',
    start=datetime.datetime(2019, 1, 1),
    end=datetime.datetime(2020, 1, 1)
)
data['diferenca'] = data.Open - data.Close
amostras = data.sample(10)

# print(database.tail())
# print(retorno)
# print(f'Média PG', retorno['PG'].mean()*250)
# print(f'Média AAPL', retorno['AAPL'].mean()*250)
# print(f'Média entre PG e AAPL', retorno[['PG', 'AAPL']].mean()*250)
# print(f'Desvio Padrão entre PG e AAPL', retorno[['PG', 'AAPL']].std()*250**0.5)
# print(data)
print(amostras)
