# -*- coding: utf-8 -*-
import os
from time import sleep, time

import ccxt
import pandas as pd

"""
Article tired do site: https://medium.com/@dumaysacha
Code Incomplete because author not post episode #2
"""

# Create instance for your exchange, here binance
# Crie uma instância para sua troca, aqui binance
binance = ccxt.binance()
# Quick test to verify data access
# Teste rápido para verificar o acesso aos dados

# Get the last 2 hours candelsticks from the pair 'BTC/USDT'
# Pegar as últimas 2 horas candelsticks do par 'BTC/USDT'
pair = "BTC/USDT"


def getTwoHours():
    return binance.fetch_ohlcv(pair, limit=2)


def generateData(df):
    # Simple function to create the timestamp of x number of hours in the past.
    # Simples função para criar o timestamp de x números de horas no passado.
    x = 0
    current_milli_time = getCurrentMilliTime(x)
    # six_months = 24 * 30 * 6 # 6 month is around(próximo) 24hours * 30days * 6 = 4320
    # months_current = 24 * 30 * 1 # 6 month is around(próximo) 24hours * 30days * 6 = 4320
    day = 1
    qt_month = 1
    week_current = (
        24 * day * qt_month
    )  # 6 month is around(próximo) 24hours * 30days * 6 = 4320
    # for hours in range(six_months,0,-600):
    for hours in range(week_current, 0, -600):
        if binance.has["fetchOHLCV"]:
            sleep(binance.rateLimit / 1000)  # time.sleep wants seconds
            # the limit from binance is 1000 timesteps
            ohlcv = binance.fetch_ohlcv(
                pair, "1h", since=current_milli_time(hours), limit=1000
            )
            df = df.append(pd.DataFrame(ohlcv))
    return df


def getCurrentMilliTime(x):
    return int(round((time() - 3600 * x) * 1000))


def manipulatePandas():
    df = pd.DataFrame()
    ohlcv_dataframe = generateData(df)
    # We are changing the name of the columns, important to use trading indicators later on
    ohlcv_dataframe["date"] = ohlcv_dataframe[0]
    ohlcv_dataframe["open"] = ohlcv_dataframe[1]
    ohlcv_dataframe["high"] = ohlcv_dataframe[2]
    ohlcv_dataframe["low"] = ohlcv_dataframe[3]
    ohlcv_dataframe["close"] = ohlcv_dataframe[4]
    ohlcv_dataframe["volume"] = ohlcv_dataframe[5]
    ohlcv_dataframe = ohlcv_dataframe.set_index("date")
    # Change the timstamp to date in UTC
    ohlcv_dataframe = ohlcv_dataframe.set_index(
        pd.to_datetime(ohlcv_dataframe.index, unit="ms").tz_localize("UTC")
    )
    ohlcv_dataframe.drop([0, 1, 2, 3, 4, 5], axis=1, inplace=True)
    return ohlcv_dataframe


def recordDataInCSV():
    df = manipulatePandas()
    # Create CSV file from our panda dataFrame
    homepath = os.path.expanduser(os.getenv("USERPROFILE"))
    desktoppath = "Desktop"
    path = os.path.join(homepath, desktoppath)
    file = "".join(("data_since6months_freq1h", pair.split("/")[0], ".csv"))
    df.to_csv(os.path.join(path, file))


def cleanDataDuplicateInCSV():
    # Read data from csv file to a dataframe
    # symbol = 'BTC/USDT'
    homepath = os.path.expanduser(os.getenv("USERPROFILE"))
    desktoppath = "Desktop"
    path = os.path.join(homepath, desktoppath)
    file = "".join(("data_since6months_freq1h", pair.split("/")[0], ".csv"))
    os.chdir(path)
    if os.path.isfile(file):
        print(f"IsFile: {file} exists!!\nProssiga...{sleep(1)}")
        data = pd.read_csv(os.path.join(path, file), index_col="date")
        # Extra precaution to ensure correct data: remove potential duplicate
        data.index = pd.DatetimeIndex(data.index)
        data = data[~data.index.duplicated(keep="first")]
        # Reindex date approriately to easily spot missing data with NaN value
        data = data.reindex(
            pd.date_range(start=data.index[0], end=data.index[-1], freq="1h")
        )
        # Fill NaN missing value by 'ffill' method
        data.fillna(method="ffill", inplace=True)
        # Replace value of 0 in volume column by a very small number
        data["volume"].replace([0, 0.0], float(0.0000000001), inplace=True)
        print(data)
    else:
        print(f"IsFile: {file} NOT exists!!\nWait to return...{sleep(1)}")


# recordDataInCSV()
cleanDataDuplicateInCSV()
