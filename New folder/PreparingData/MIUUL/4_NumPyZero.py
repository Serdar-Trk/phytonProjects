####NUMPY NUMERICAL PHYTON#

# why numpy?
# creating numpy arrays
# attributes of numpy arrays -
# reshaping - yeniden sekillendirme
# index selection
# slicing
# fancy index
# conditions on numpy
# mathematical operations

### verimli veri saklama ve yuksek seviyeden(vektorel) islemlerde kullanilir. listelere kiyaysa cok daha hizlidir.

# why numpy?

import numpy as np

# klasik phyton yolu ile iki indeksi sirali carplak icin:

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

# numpy, phyton da numerik islemler icin gelistirilmis bir kutuphanedir.
# neden nampy
## 1: hizlidir - cunku sabit tipte veri tutar.
## 2: yuksek seviyeden islem yapar.(vektorel) -


###Creating Numpy Arrays###

np.array([1, 2, 3, 4])

type(np.array([1, 2, 3, 4]))

np.zeros(10, dtype=int)

np.random.randint(0, 10, size=10)

np.random.normal(10, 4, (3, 4))  ##ortalamasi 10 standart sapmasi 4 olan 3 satir 4 sutun.

###Attribute of NumPy##

# ndim : boyut sayisi
# shape : boyut bilgisi
# size : top eleman sayisi
# dtype : array veri tipi

a = np.random.randint(10, size=5)

a.ndim
a.shape
a.size
a.dtype

### Reshaping ## yeniden sekillendirme

np.random.randint(1, 10, size=9)

np.random.randint(1, 10, size=9).reshape(3, 3)

ar = np.random.randint(1, 10, size=9)

ar.reshape(3, 3)

#### Index selection ###


a = np.random.randint(10, size=10)

a[0]  ## index secimi
a[0:5]  ## slicing
a[0] = 99

m = np.random.randint(10, size=(3, 5))

m[0, 0]
m[1, 1]
m[2, 3]

m[2, 3] = 999

m[2, 3] = 2.9

## numpy tek tip veri saklar. bu sebeple 2.9 float ifadeyi duzeltir.

m[:, 0]
m[1, :]

m[0:2, 0:3]

### fancy index

### 0 dan 30 a kadar 3 er 3 er artan array olustur.

v = np.arange(0, 30, 3)

v[1]
v[4]

k = [1, 2, 3]

v[k]

## conditions on numpy

v = np.array([1, 2, 3, 4, 5])

ab = []

for i in v:
    if i < 3:
        ab.append(i)
        print(ab)
# klasik dongu ile yukaridaki gibi yapilir. Numpy ile asagidaki gibi

v < 3

v[v < 3]

v[v > 3]

v[v != 3]

v[v == 3]

v[v >= 3]

### mathematical operations###

v / 5

v * 5 / 10

v ** 2

v - 1

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

## iki bilin meyenli denklem cozumu

# 5*x0 + x1 =12
# x0   + 3*x1 =10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)
