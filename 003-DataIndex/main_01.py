import pandas as pd

# How to read csv file
dataku = pd.read_csv('D:/wilden nitp/wilden-github/Pandas_Basic/001-ReadWriteFile/kapal_titanic.csv')
dataku.head()
print("--------------dataku.head()--------------")
print(dataku.head(3))
print(dataku.tail(10))

# Pilih salah satu colomn
dataku_column = dataku['age']
print("\n--------------dataku_column--------------")
print(dataku_column)
# Tipe dataku_colomn
print(type(dataku_column))

# Pilih salah dua colomn
dataku_duacolumn = dataku[['age', 'fare']]
print("\n--------------dataku_duacolumn--------------")
print(dataku_duacolumn)
print(type(dataku_duacolumn))

# DOT NOTATION
print("\n--------------DOT NOTATION--------------")
print(dataku.age)

# Location
print("\n--------------Location--------------")
print(dataku.iloc[0])
print(dataku.iloc[:5])
print(dataku.iloc[6:8])
print(type(dataku.iloc[6:8]))
print(dataku.iloc[:,3])
print(type(dataku.iloc[:,3]))
print(dataku.iloc[-5:])
print(dataku.tail(10))
print(dataku.iloc[-5:-1])
print(dataku.iloc[-5:-1,-4:])
print(dataku.iloc[-5:-1,-4:-2])
print(dataku.iloc[[0,2,4]])
print(dataku.iloc[[1,4,9],[1,3,6]])


print("\n--------------loc['nama baris', 'nama kolom'--------------")
data_baru = pd.read_csv('D:/wilden nitp/wilden-github/Pandas_Basic/001-ReadWriteFile/kapal_titanic.csv', index_col='embarked')
print(data_baru)
print(data_baru.loc['S'])
print(data_baru.loc['S', 'age'])
print(data_baru.loc['S', ['age', 'fare']])
print(data_baru.loc[['S', 'Q'], ['age', 'fare']])



'''
--------------dataku.head()--------------
   survived  pclass     sex   age  sibsp  parch     fare embarked deck
0         0       3    male  22.0      1      0   7.2500        S  NaN
1         1       1  female  38.0      1      0  71.2833        C    C
2         1       3  female  26.0      0      0   7.9250        S  NaN
     survived  pclass     sex   age  sibsp  parch     fare embarked deck
881         0       3    male  33.0      0      0   7.8958        S  NaN
882         0       3  female  22.0      0      0  10.5167        S  NaN
883         0       2    male  28.0      0      0  10.5000        S  NaN
884         0       3    male  25.0      0      0   7.0500        S  NaN
885         0       3  female  39.0      0      5  29.1250        Q  NaN
886         0       2    male  27.0      0      0  13.0000        S  NaN
887         1       1  female  19.0      0      0  30.0000        S    B
888         0       3  female   NaN      1      2  23.4500        S  NaN
889         1       1    male  26.0      0      0  30.0000        C    C
890         0       3    male  32.0      0      0   7.7500        Q  NaN

--------------dataku_column--------------
0      22.0
1      38.0
2      26.0
3      35.0
4      35.0
       ...
886    27.0
887    19.0
888     NaN
889    26.0
890    32.0
Name: age, Length: 891, dtype: float64
<class 'pandas.core.series.Series'>

--------------dataku_duacolumn--------------
      age     fare
0    22.0   7.2500
1    38.0  71.2833
2    26.0   7.9250
3    35.0  53.1000
4    35.0   8.0500
..    ...      ...
886  27.0  13.0000
887  19.0  30.0000
888   NaN  23.4500
889  26.0  30.0000
890  32.0   7.7500

[891 rows x 2 columns]
<class 'pandas.core.frame.DataFrame'>

--------------DOT NOTATION--------------
0      22.0
1      38.0
2      26.0
3      35.0
4      35.0
       ...
886    27.0
887    19.0
888     NaN
889    26.0
890    32.0
Name: age, Length: 891, dtype: float64

--------------Location--------------
survived       0
pclass         3
sex         male
age         22.0
sibsp          1
parch          0
fare        7.25
embarked       S
deck         NaN
Name: 0, dtype: object
   survived  pclass     sex   age  sibsp  parch     fare embarked deck
0         0       3    male  22.0      1      0   7.2500        S  NaN
1         1       1  female  38.0      1      0  71.2833        C    C
2         1       3  female  26.0      0      0   7.9250        S  NaN
3         1       1  female  35.0      1      0  53.1000        S    C
4         0       3    male  35.0      0      0   8.0500        S  NaN
   survived  pclass   sex   age  sibsp  parch     fare embarked deck
6         0       1  male  54.0      0      0  51.8625        S    E
7         0       3  male   2.0      3      1  21.0750        S  NaN
<class 'pandas.core.frame.DataFrame'>
0      22.0
1      38.0
2      26.0
3      35.0
4      35.0
       ...
886    27.0
887    19.0
888     NaN
889    26.0
890    32.0
Name: age, Length: 891, dtype: float64
<class 'pandas.core.series.Series'>
     survived  pclass     sex   age  sibsp  parch   fare embarked deck
886         0       2    male  27.0      0      0  13.00        S  NaN
887         1       1  female  19.0      0      0  30.00        S    B
888         0       3  female   NaN      1      2  23.45        S  NaN
889         1       1    male  26.0      0      0  30.00        C    C
890         0       3    male  32.0      0      0   7.75        Q  NaN
     survived  pclass     sex   age  sibsp  parch     fare embarked deck
881         0       3    male  33.0      0      0   7.8958        S  NaN
882         0       3  female  22.0      0      0  10.5167        S  NaN
883         0       2    male  28.0      0      0  10.5000        S  NaN
884         0       3    male  25.0      0      0   7.0500        S  NaN
885         0       3  female  39.0      0      5  29.1250        Q  NaN
886         0       2    male  27.0      0      0  13.0000        S  NaN
887         1       1  female  19.0      0      0  30.0000        S    B
888         0       3  female   NaN      1      2  23.4500        S  NaN
889         1       1    male  26.0      0      0  30.0000        C    C
890         0       3    male  32.0      0      0   7.7500        Q  NaN
     survived  pclass     sex   age  sibsp  parch   fare embarked deck
886         0       2    male  27.0      0      0  13.00        S  NaN
887         1       1  female  19.0      0      0  30.00        S    B
888         0       3  female   NaN      1      2  23.45        S  NaN
889         1       1    male  26.0      0      0  30.00        C    C
     parch   fare embarked deck
886      0  13.00        S  NaN
887      0  30.00        S    B
888      2  23.45        S  NaN
889      0  30.00        C    C
     parch   fare
886      0  13.00
887      0  30.00
888      2  23.45
889      0  30.00
   survived  pclass     sex   age  sibsp  parch   fare embarked deck
0         0       3    male  22.0      1      0  7.250        S  NaN
2         1       3  female  26.0      0      0  7.925        S  NaN
4         0       3    male  35.0      0      0  8.050        S  NaN
   pclass   age     fare
1       1  38.0  71.2833
4       3  35.0   8.0500
9       2  14.0  30.0708

--------------loc['nama baris', 'nama kolom'--------------
          survived  pclass     sex   age  sibsp  parch     fare deck
embarked
S                0       3    male  22.0      1      0   7.2500  NaN
C                1       1  female  38.0      1      0  71.2833    C
S                1       3  female  26.0      0      0   7.9250  NaN
S                1       1  female  35.0      1      0  53.1000    C
S                0       3    male  35.0      0      0   8.0500  NaN
...            ...     ...     ...   ...    ...    ...      ...  ...
S                0       2    male  27.0      0      0  13.0000  NaN
S                1       1  female  19.0      0      0  30.0000    B
S                0       3  female   NaN      1      2  23.4500  NaN
C                1       1    male  26.0      0      0  30.0000    C
Q                0       3    male  32.0      0      0   7.7500  NaN

[891 rows x 8 columns]
          survived  pclass     sex   age  sibsp  parch     fare deck
embarked
S                0       3    male  22.0      1      0   7.2500  NaN
S                1       3  female  26.0      0      0   7.9250  NaN
S                1       1  female  35.0      1      0  53.1000    C
S                0       3    male  35.0      0      0   8.0500  NaN
S                0       1    male  54.0      0      0  51.8625    E
...            ...     ...     ...   ...    ...    ...      ...  ...
S                0       2    male  28.0      0      0  10.5000  NaN
S                0       3    male  25.0      0      0   7.0500  NaN
S                0       2    male  27.0      0      0  13.0000  NaN
S                1       1  female  19.0      0      0  30.0000    B
S                0       3  female   NaN      1      2  23.4500  NaN

[644 rows x 8 columns]
embarked
S    22.0
S    26.0
S    35.0
S    35.0
S    54.0
     ...
S    28.0
S    25.0
S    27.0
S    19.0
S     NaN
Name: age, Length: 644, dtype: float64
           age     fare
embarked
S         22.0   7.2500
S         26.0   7.9250
S         35.0  53.1000
S         35.0   8.0500
S         54.0  51.8625
...        ...      ...
S         28.0  10.5000
S         25.0   7.0500
S         27.0  13.0000
S         19.0  30.0000
S          NaN  23.4500

[644 rows x 2 columns]
           age     fare
embarked
S         22.0   7.2500
S         26.0   7.9250
S         35.0  53.1000
S         35.0   8.0500
S         54.0  51.8625
...        ...      ...
Q          NaN   7.7500
Q          NaN   6.9500
Q          NaN   7.7500
Q         39.0  29.1250
Q         32.0   7.7500

[721 rows x 2 columns]
'''