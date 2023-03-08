## VERI GORSELLESTIRME : MATPLOTLIB & SEABORN

# MATPLOTLIB : dusuk seviyeli bir veri gorsellestirme aracidir.

# Eger kategorik bir degisken varsa ; sutun grafik. 'countplot', 'bar'

# Eger sayisal degiskense; hist, boxplot

import matplotlib.pyplot as plt
# kategorik degisken gorsellestirme
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df.head()

df['sex'].value_counts().plot(kind='bar')
plt.show(block=True)

### sayisal degisken gorsellestirme

plt.hist(df['age'])
plt.show(block=True)

plt.boxplot(df['fare'])
plt.show(block=True)

###MATPLOTLIB OZELLIKLERI
# plot ozellligi
x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show(block=True)

plt.plot(x, y, 'o')
plt.show(block=True)

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show(block=True)

# marker ozelligi

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o')
plt.show(block=True)

plt.plot(y, marker='*')
plt.show(block=True)

# line ozelligi

y = np.array([13, 28, 11, 100])

plt.plot(y)
plt.show(block=True)

plt.plot(y, linestyle='dotted')
plt.show(block=True)

plt.plot(y, linestyle='dashdot')
plt.show(block=True)

plt.plot(y, linestyle='dashed')
plt.show(block=True)

plt.plot(y, linestyle='dashdot', color='r')
plt.show(block=True)

# multiple lines ozelligi

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.plot(x)
plt.plot(y)
plt.show(block=True)

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.plot(x)
plt.plot(y)
plt.title('Bu Ana Baslik')
plt.xlabel('x ekseni isimlendirmesi')
plt.ylabel('y ekseni isimlendirmesi')
plt.grid()
plt.show(block=True)

# subplot

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.subplot(1, 2, 1)
plt.title('1')
plt.plot(x, y)

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.subplot(1, 2, 2)
plt.title('2')
plt.plot(x, y)
plt.show(block=True)

###SEABORN

df = sns.load_dataset('tips')
df.head()

## kategorik degiskenler icin gorsellestirme(sutun grafik)

df['sex'].value_counts()
sns.countplot(x=df['sex'], data=df)
plt.show(block=True)

##sayisal degiskenleri gorsellestirme

sns.boxplot(x=df['total_bill'])
plt.show(block=True)

df['total_bill'].hist()
plt.show(block=True)