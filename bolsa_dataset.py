
# PAREI NA PÁGINA: 55

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from sklearn.preprocessing import MinMaxScaler

base = pd.read_csv('PETR4.SA.csv')

base = base.dropna()
base_treino = base.iloc[:, 1:2].values

normalizador = MinMaxScaler(feature_range=(0, 1))
base_treino_normalizada = normalizador.fit_transform(base_treino)

previsores = []
preco_real = []

for i in range(90, 1242):
    try:
        previsores.append(base_treino_normalizada[i-90:i, 0])
        preco_real.append(base_treino_normalizada[i, 0])
    except IndexError as err:
        print(err)
        break

previsores, preco_real = np.array(previsores), np.array(preco_real)
previsores = np.reshape(previsores, (previsores.shape[0], previsores.shape[1], 1))

regressor = Sequential()
regressor.add(LSTM(
        units=100,
        return_sequences=True,
        input_shape=(previsores.shape[1], 1)
    )
)
regressor.add(Dropout(0.3))
regressor.add(
    LSTM(
        units=50,
        return_sequences=True,
    )
)
regressor.add(Dropout(0.3))
regressor.add(LSTM(units=50))
regressor.add(Dropout(0.3))
regressor.add(
    Dense(
        units=1,
        activation='linear',
    )
)
regressor.compile(
    optimizer='rmsprop',
    loss='mean_squared_error',
    metrics=['mean_absolute_error']
)
try:
    regressor.fit(
        preco_real,
        epochs=100,
        batch_size=32
    )
except ValueError as err:
    print(f'ERROR..: {err}')
# print(base_treino_normalizada)
# print(previsores)
# print(regressor)
