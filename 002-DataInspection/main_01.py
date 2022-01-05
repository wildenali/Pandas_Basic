import pandas as pd

# How to read csv file
dataku = pd.read_csv('D:/wilden nitp/wilden-github/Pandas_Basic/001-ReadWriteFile/kapal_titanic.csv')
dataku.head()
print(dataku.head(3))
print(dataku.tail(10))

pd.options.display.min_rows
pd.options.display.max_rows
print("min rows: ", pd.options.display.min_rows)

pd.options.display.max_rows = 891
print("min rows: ", pd.options.display.min_rows)
print("max rows: ", pd.options.display.max_rows)

# print(dataku)
print(dataku.info())

# tidy up the table
print(dataku.describe())

# data bersifat non numerik
print(dataku.describe(include="O"))