import numpy as np
import pandas as pd

np.random.seed(100)

dataku = pd.DataFrame(np.random.randn(3,5), ['A','B','C'], ['satu', 'dua', 'tiga', 'empat', 'lima'])
print(dataku)
'''
       satu       dua      tiga     empat      lima
A -1.749765  0.342680  1.153036 -0.252436  0.981321
B  0.514219  0.221180 -1.070043 -0.189496  0.255001
C -0.458027  0.435163 -0.583595  0.816847  0.672721
'''

print(type(dataku['dua']))
'''
<class 'pandas.core.series.Series'>
'''

# iloc and loc
dataku['baru'] = dataku['empat'] + dataku['lima']
print(dataku['baru'])
'''
A    0.728885
B    0.065506
C    1.489568
Name: baru, dtype: float64
'''

# Cara menghapus kolom
dataku = dataku.drop('tiga', axis=1)
print(dataku)
'''
       satu       dua     empat      lima      baru
A -1.749765  0.342680 -0.252436  0.981321  0.728885
B  0.514219  0.221180 -0.189496  0.255001  0.065506
C -0.458027  0.435163  0.816847  0.672721  1.489568
'''

dataku.drop('empat', axis=1, inplace=True)
print(dataku)
'''
       satu       dua      lima      baru
A -1.749765  0.342680  0.981321  0.728885
B  0.514219  0.221180  0.255001  0.065506
C -0.458027  0.435163  0.672721  1.489568
'''

dataku.drop('B', axis=0, inplace=True)
print(dataku)
'''
       satu       dua      lima      baru
A -1.749765  0.342680  0.981321  0.728885
C -0.458027  0.435163  0.672721  1.489568
'''

print(dataku.shape)
'''
(2, 4)
'''

dataku_bol = dataku < 0
print(dataku_bol)
'''
   satu    dua   lima   baru
A  True  False  False  False
C  True  False  False  False
'''

print(dataku[dataku_bol])
'''
       satu  dua  lima  baru
A -1.749765  NaN   NaN   NaN
C -0.458027  NaN   NaN   NaN
'''


dataku = pd.DataFrame(np.random.randn(3,5), ['A','B','C'], ['satu', 'dua', 'tiga', 'empat', 'lima'])
hasil = dataku[dataku['tiga']>0]
print(hasil)
'''
       satu      dua      tiga     empat      lima
A -0.104411 -0.53128  1.029733 -0.438136 -1.118318
C  0.937082  0.73100  1.361556 -0.326238  0.055676
'''