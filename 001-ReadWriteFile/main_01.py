import pandas as pd

# How to read csv file
dataku = pd.read_csv('kapal_titanic.csv')
dataku.head()
print("FILE CSV")
print(dataku)
print(dataku.head())

# convert to another file, for example from csv to csv
dataku.to_csv('datacsv.csv', index=False)
datacsv_ku = pd.read_csv('datacsv.csv')
print("FILE CSV")
print(datacsv_ku)

# export to excel format
dataku.to_excel('dataexcel.xlsx', index=False, sheet_name='asik')
dataxlsx_ku = pd.read_excel('dataexcel.xlsx')
print("FILE EXCEL")
print(dataxlsx_ku)