
###PANDAS###

## PANDAS Series
## Reading Data
## Quick Look At Data
## Selection in Pandas
## Aggregation & Grouping
## Apply & Lambda
## Join

import pandas as pd

#pandas series

s = pd.Series([10, 77, 12, 4, 5])

type(s)
s.index
s.dtype
s.size
s.ndim              #pandas serileri tek boyutludur
s.values            # bir pandas serisini sonuna values ifadesini girip degerlerine erismek istedigimizde. Zaten index bilgisi ile isimiz olmadigindan numpy array olarak dondurur.!!
type(s.values)
s.head(3)
s.tail(3)

#reading data

# pd.read_.....('')

## quick look at  data

import seaborn as sns

df = sns.load_dataset('titanic')
titanic = df.copy()
titanic.info()

df.head()
df.tail()
df.shape
df.info()
df.columns
df.index

df.describe()
df.describe().T

df.isnull()
df.isnull().values
df.isnull().values.any()

df.isnull().sum()

pd.set_option('display.max_column', None)
pd.set_option('display.width', 500)
pd.set_option('display.max_row', None)

## kac kadin, kac erkek var

df['sex'].head()
df['sex'].value_counts()

##selection in pandas


df[0:13]

df.drop(0, axis=0).head()  # 0. indexi sildi

delete_indexes = [1, 2, 3, 4]

df.drop(delete_indexes, axis=0).head(10)

#drop ile index silme islemleri kalici degildir. kalici olmasi icin asagidaki yontemlerler izleir.

# df = df.drop(delete_indexes, axis=0)
# df.drop(delete_indexes, axis=0, inplace=True)

### degiskeni indexe cevirmek

df['age'].head()

df.age.head()

df.index

##diyelimki 'age' degiskenini indexe atmak istiyoruz.

df.index = df['age']

# index olarak ekledik. degiskenlerden silelim.

df.drop('age', axis=1).head()

### axis=1 ----- sutun secimi
### axis=0 ------ satir secimi

##kalici yapmak istersek

df.drop('age', axis=1, inplace=True)

df.head()


## indexi degiskene cevirmek. tam tersi

df.reset_index().head()

df = df.reset_index()

df.head()

##degiskenler uzerinde islemler

'age' in df

df['age'].head()

df.age.head()

type(df['age'].head())

## DataFrame bekleyen bir fonksiyona PandasSeries gonderirsek fonksiyon calismayacaktir.
## Tek bir degisken beklerken secimin sonucunun DataFrame olarak kalmasini istiyorsak bu durumda [['']] veri yapimiz bozulmaz ve data frame olarak kalmaya devam eder.

df[['age']].head()

type(df[['age']].head())

# birden fazla degisken secimi

df[['age', 'alive']]

col_names = ['age', 'adult_male', 'alive']

df[col_names]

## col_names ifadesi bir listeyi temsil ettiginden cift tirnak yapmaya gerek yoktur.

df['age2'] = df['age']**2
df.head()

## yasin karesini yeni bir degisken olarak veri setine ekledim

df['age3'] = df['age'] / df['age2']
df.head()

df.drop('age3', axis=1).head()    ## age3 degiskenini sutundan sildim. kalici degil

df.drop(col_names, axis=1).head()

## diyelimki verisetinde belirli bir string ifadeyi barindiran degiskenleri silmek istiyorum.
## yuzlerce belirli bir ifadeyi barindiran degisken olabilir.

## 'loc'  label based secim yapmak icin kullanilir.

df.loc[:, df.columns.str.contains('age')].head()

# sutunlarla ilgili bir ihtiyacim var: bu DataFrame in kolonlarindaki degiskenlere bir string operasyonu yapicam.
# contains metodu ile 'age' string ifadesini arattik.
# str.contains  : stringlere uygulanir.
## icerisinde yas barindiran degiskenleri secti.

## ~ ifadesi ilgili secimin disindakileri secmek icin kullanilir. DEGILDIR anlami tasir.

df.loc[:, ~df.columns.str.contains('age')].head()

#iste 'age' string ifadesini barindiran butun degiskenleri sildik.

#### iloc & loc ##########

# iloc : index bilgisi vererek secim yapar
# loc :  indexlerdeki label lara gore secim yapar

# iloc : integer based selection

df.iloc[0:3]

df.iloc[0, 0]

#loc: label based selection

df.loc[0:3]

##farklari

df.iloc[0:3, 'age']

df.iloc[0:3, 0:3]

df.loc[0:3, 'age']

col_names = ['age', 'embarked', 'alive']

df.loc[0:3, col_names]

#loc: mutlak olarak isimlendirmenin kendisinin secer.
# iloc[0:3] = 0 dan 3 e kadar(3 dahil degil

### conditional selection

df[df['age'] > 50].head()
df[df['age'] > 50].count()

## herhangi bir degisken secmedigimiz icin butun hepsine count atti

df[df['age'] > 50]['age'].count()

# yasi 50 den buyuk olanlarin class i ?

df.loc[df['age'] > 50, 'class'].head()

df.loc[df['age'] > 50, ['age', 'class']].head()

# liste oldugundan koseli paranteze aldik

## yasi 50 den buyuk olan erkekleri secelim

df.loc[(df['age'] > 50) &
       (df['sex'] == 'male'), ['age', 'class']].head()

## birden fazla kosul oldugunda parantez icine alinir.

## bir kosul daha ekleyelim: gemiye binilen limani ifade eden 'embark_town' da sadece 'cherbourg' limani olsun.

df.head()

df.loc[(df['age'] > 50)
       & (df['embark_town'] == 'Cherbourg')
       & (df['sex'] == 'male'),
            ['age', 'class', 'embark_town']].head()

df.loc[(df['age'] > 50)
       & ((df['embark_town'] == 'Cherbourg') | (df['embark_town'] == 'Southampton'))
       & (df['sex'] == 'male'),
            ['age', 'class', 'embark_town']].head()

# yasi  50 den buyuk, erkek olanlar, Cherbourg ya da southampton limanlarindan binen yolculari 'age', 'class', 'embark_town' degiskenlerine gore listeledik.

###TOPLULASTIRMA VE GRUPLAMA ( aggregation & grouping )
#
# count()
# first()
# last()
# mean()
# median()
# min()
# max()
# std()
# var()
# sum()
# pivot table

## kadin ve erkeklerin yas ortalamasi nedir?

df.groupby('sex')['age'].mean()

## df dataframe ini 'sex' degiskenine gore grupla daha sonra 'age' degiskeninin ortalamasini al dedik.

## toplamini da almak istersek?

df.groupby('sex').agg({'age': "mean"})

df.groupby('sex').agg({'age': ['mean', 'sum']})

# bu kullanim daha mantikli

df.head()

df.groupby(['sex', 'embark_town', 'class']).agg({'age': 'mean', 'survived': 'mean', 'sex': 'count'})

###Pivot Table

df['embarked'].head(10)

df.pivot_table('survived', 'sex', 'embarked')

#pivot_table('value:kesisimlerde neyi gormek istiyorsun', 'indexte(satirda) neyi gormek istiyorsun', 'sutunda hangi degiskeni gormek istiyorsun')

#kesisimde(value) survived degiskeninin ortalamasini(mean) gosterdi.pivot_table in on tanimli degeri mean dir. sekillendirebiliriz.

df.pivot_table('survived', 'sex', 'embarked', aggfunc='std')

# value standart sapma oldu

df.pivot_table('survived', 'sex', ['embarked', 'class'])


##'age' degiskenini hayatta kalma acisindan nasil degerlendirilebilir.
# 'age' degiskeni sayisal oldugundan gozlemleyebilmek iicin kategorik degiskene cevirmemiz gerekiyor.

df.head()

df['new_age'] = pd.cut(df['age'], [0, 10, 18, 25, 40, 90])

##elinizdeki sayisal degiskeni nasil bolmek isdeginizi biliyorsaniz cut bilmiyorsaniz qcut fonksiyonu ile cegrek degerlere bolebilirsiniz.

df.pivot_table('survived', 'sex', 'new_age')

df.pivot_table('survived', 'sex', ['new_age', 'class'])

### APPLY & LAMBDA ###

## apply : satir ya da sutunlarda fonksiyon calistirmaya yarar. Bir dataframe e apply ile fonksiyon uygulayabiliriz.
##lambda : def gibi fonksiyon yazma islemidir. kullan at fonksiyon olusturur.

df['age2'] = df['age'] * 2
df['age3'] = df['age'] * 5
df.head()

(df['age'] / 10).head()
(df['age2'] / 10).head()
(df['age3'] / 10).head()

## bunu boyle el ile yazmaktansa klasik yontemle dongu yazalim.
## degiskenlere bir fonksiyon uygulamak istiyorum ama cok degisken var.

for col in df.columns:
    if 'age' in col:
        print(col)

for col in df.columns:
    if 'age' in col:
        print((df['age'] / 10).head())

## print ettik sadece, degistirmedik.

for col in df.columns:
    if 'age' in col:
        df[col] = df[col] / 10

## 'new_age' kategorik oldugundan hata verdi bende sildim o kolonu
df = df.drop('new_age', axis=1).head()

df.head()

## apply ve lambda ile yaparsak

df[['age', 'age2', 'age3']].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains('age')].apply(lambda x: x/10).head()

#loc[:, df.columns.str.contains('age')]   :   butun satirlari sectim, sutunlarda 'age' ifadesi gecen degiskenleri sectim.
#apply(lambda x: x/10).head()             : ilgili indexlerde gezdim ve ilgili fonksiyonu uyguladim.

df.loc[:, df.columns.str.contains('age')].apply(lambda x: (x - x.mean()) / x.std()).head()

## yukaridaki islemim basite indirgemek icin tanimlanmis bir fonksiyonu apply ile kullanabiliriz.

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains('age')].apply(standart_scaler).head()

df.head()

# islemi tabloya kaydetmek icin:

df.loc[:, df.columns.str.contains('age')] = df.loc[:, df.columns.str.contains('age')].apply(standart_scaler).head()

###BIRLESTIRME(JOIN) ISLEMLERI###

import pandas as pd
import numpy as np

m = np.random.randint(1, 30, size=(5, 3))

df1 = pd.DataFrame(m, columns=['var1', 'var2', 'var3'])
df2 = df1 + 99

#concat ile join

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)

#merge ile join

df1 = pd.DataFrame({'employes' : ['john', 'dennis', 'mark', 'maria'],
                    'group' : ['accounting', 'engineering', 'engineering', 'hr']})
df2 = pd.DataFrame({'employes' : ['john', 'dennis', 'mark', 'maria'],
                    'start_date' : [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
# otomatik calisanlara gore birlestirdi. Bunu ozellikle belirtmek istersek asagidaki islemi uygulariz.

df3 = pd.merge(df1, df2, on='employes')

##her calisanin mudur bilgisine erismek istiyoruz.

df4 = pd.DataFrame({'group' : ['accounting', 'engineering', 'hr'],
                    'manager' : ['caner', 'mustafa', 'berkcan']})

pd.merge(df3, df4)