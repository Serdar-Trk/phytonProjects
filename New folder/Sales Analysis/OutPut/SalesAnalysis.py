
# Gerekli Kutuphaneler

import os
import pandas as pd

# *1 Aylik olarak verilen 'CVS' dosyalarini birlestir.

files = [file for file in os.listdir('Sales Analysis/DirtySalesDate') if not file.startswith('.')]

all_months_data = pd.DataFrame()

for file in files:
    current_data = pd.read_csv('Sales Analysis/DirtySalesDate'+"/"+file)
    all_months_data = pd.concat([all_months_data, current_data])


current_data1 = pd.read_csv('Sales Analysis/DirtySalesDate' + '/' + 'Sales_April_2019.csv')

all_months_data.to_csv("all_data.csv", index=False)

# *2 Birlestirip 'CVS' olarak kaydettigimiz dosyayi okut.

all_data = pd.read_csv("all_data.csv")
all_data.head()
all
# *3 Data uzerinde daha etkili gozlemlerde bulunabilmek icin bazi degisiklikler yaptim.

pd.set_option('display.max_column', None)
pd.set_option('display.width', 500)

# *4 Veriyi 'NULl' degerlerden arindiralim.
# Bu asamada ele aldiginiz veriye gore uygulanacak islem degisiklik gosterebilecektir.
# Tum satirlari 'NULL' olan indexleri gozlemleyelim ve temizleyelim.

all_data[all_data.isnull().any(axis=1)]
all_data = all_data.dropna(how='all')

# *5 Bir sonraki adimda 'Or' iceren yapilar oldugundan 'ValueError' hatasi aldik.
# 'Or' iceren yapilari bu adimda temizliyoruz.

all_data[all_data['Order Date'].str[0:2] == 'Or']
# Yukarida goruldugu uzere kendini tekrarlayan bircok satir mevcut.(degisken isimleriyle cogaltilmis satirlar)

all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data.value_counts()

# *6 'Month' adinda ay bilgisini iceren bir degisken olusturalim.

all_data['Month'] = pd.to_datetime(all_data['Order Date']).dt.month
all_data.head()

# *7 ['Quantity Ordered'] ve ['Price Each'] degiskenleri numerik ama categorik oldugundan
# ilgili degiskenlerinin veri tipini numerik olarak degistiriyoruz.

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
all_data['Price Each'].dtype

# *8 ['City'] adinda sehir bilgisi iceren yeni bir degisken ekleyelim.


def get_city(address):
    return address.split(",")[1].strip(" ") + ', ' + address.split(",")[2].split(" ")[1]


all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x))
all_data.head()

# *9 ['Sales'] adinda toplam toplam kazanc bilgisini veren bir degisken olusturalim.

all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

# *10 HADI 'MATHPILOTLIB' ARACILIGIYLA VERIYI KESFEDELIM VE ANLAM ARAYALIM.

# *10.1 Bar grafigi araciligiyla aylik satis rakamlarini gozlemleyelim.

import matplotlib.pyplot as plt

months = range(1,13)
print(months)

plt.bar(months, all_data.groupby(['Month']).sum()['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.show()

# *10.1 Bar grafigi araciligiyla sehirlere gore satis rakamlarini gozlemleyelim.
# 'SEABORN' kutuphanesini kullanalim
# 'plt.xticks(rotation='vertical', size=8)' sehir isimlieri sigmadigindan dikey konuma getirip yazi boyutlarini kuculttuk

import seaborn as sns

City_Sales = all_data.groupby(['City']).agg({'Sales': 'sum'})

sns.barplot(y=City_Sales['Sales'], x=City_Sales.index)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.xticks(rotation='vertical', size=8)
plt.show(block=True)

# *11 Musterilerimizin urunumuzu almasi icin reklamlari hangi saatlerde gostermeliyiz.
all_data['Hour'] = pd.to_datetime(all_data['Order Date']).dt.hour
all_data['Count'] = 1
all_data.head()

keys = [pair for pair, df in all_data.groupby(['Hour'])]

plt.plot(keys, all_data.groupby(['Hour']).count()['Count'])
plt.xticks(keys)
plt.grid()
plt.show()

# 12* En cok hangi urunler birlikte satilmislar?

# Ayni 'Order_ID' ye sahip urunleri secelim.
df = all_data[all_data['Order ID'].duplicated(keep=False)]

# Ayni 'Order ID' ye sahip urunleri ',' ile birlestirip bir degisken olarak 'df' e atayalim.
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

df.head()
df.shape
df.value_counts()
df.describe()
# Verileri tekillestirelim.
df = df[['Order ID', 'Grouped']].drop_duplicates()
# https://stackoverflow.com/questions/43348194/pandas-select-rows-if-id-appear-several-time
# https://stackoverflow.com/questions/27298178/concatenate-strings-from-several-rows-using-pandas-groupby

from itertools import combinations
from collections import Counter

count = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

for key, value in count.most_common(10):
    print(key, value)

# 13* En cok hangi urunun satildigini sutun grafikte gozlemleyelim.

b = all_data.groupby('Product').agg({'Quantity Ordered': 'sum'})

sns.barplot(x=b.index, y=b['Quantity Ordered'])
plt.xticks(keys, rotation='vertical', size=8)
plt.show()