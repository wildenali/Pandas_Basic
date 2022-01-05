import numpy as np
import pandas as pd

label = ['satu', 'dua', 'tiga']
angka = [10, 20, 30]

print("-------------numpy-------------")
np_angka = np.array(angka)
print(np_angka)
print(np_angka[0])

print("\n-------------Series-------------")
d = {'satu': 10, 'dua': 20, 'tiga': 30}
dataku = pd.Series(data=angka, index=label)
print(dataku)
print(dataku['satu'])
print(pd.Series(d))
print(pd.Series(np_angka))
print(pd.Series(angka))

dataku_frame = dataku.to_frame()
print("\ndataku_frame")
print(dataku_frame)

d2 = {'satu': 10, 'dua': 20, 'tiga': 30, 'empat': 40, 'lima': 50}
dataku  = pd.Series(d)
dataku2 = pd.Series(d2)
print("\ndataku")
print(dataku)
print("\ndataku2")
print(dataku2)
print("\nPenjumlahan Series")
print(dataku + dataku2)


'''
-------------numpy-------------
[10 20 30]
10

-------------Series-------------
satu    10
dua     20
tiga    30
dtype: int64
10
satu    10
dua     20
tiga    30
dtype: int64
0    10
1    20
2    30
dtype: int32
0    10
1    20
2    30
dtype: int64

dataku_frame
       0
satu  10
dua   20
tiga  30

dataku
satu    10
dua     20
tiga    30
dtype: int64

dataku2
satu     10
dua      20
tiga     30
empat    40
lima     50
dtype: int64

Penjumlahan Series
dua      40.0
empat     NaN
lima      NaN
satu     20.0
tiga     60.0
dtype: float64
'''