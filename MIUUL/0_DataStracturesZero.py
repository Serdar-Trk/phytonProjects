#DATA STRACTURES##
#from typing import Dict, List

#NUMBERS: INT, FLOAT, COMPLEX
#STRINGS: STR
#BOOLEAN(TRUE/FALSE): BOOL
#LIST
#DICTIONARY
#TUPLE
#SET

x = 46
type(x)

x = 10.3
type(10.3)

x = 'hello ai era'
type(x)

True
False
type(True)

5 == 4   ##5, 4'e esit midir?
2 == 2

type(5 == 4)

x = ['btc', 'eth', 'xrp']
type(x)

x = {'name': 'Peter', 'Age': '36'}
type(x)

##Dictionary yapilarinda 1. deger 'key'    2. deger 'value'

x = ('python', 'ml', 'ksd')
type(x)

x = {'dad', 'daasd', 'das'}
type(x)


###   SAYILAR  ###

a = 5
b = 10.5

a * 3

a / 7

a * b / 10

a ** a

a ** 2    ##a'nin 2. kuvveti

###tipleri degistirmek(int'i float'a , float'i int'e)

int(b)
float(a)

int(a * b / 10)

###STRINGS##
print('John')

name = 'John'
'john'

##COK SATIRLI KARAKTER DIZISI OLUSTURMA''

long_str = ''' NUMBERS: INT, FLOAT, COMPLEX
STRINGS: STR
BOOLEAN(TRUE/FALSE): BOOL
LIST
DICTIONARY'''


##KARAKTER DIZININDE KARAKTERE ERISMEK##\\

name[0]

name

name[0:2]

long_str
long_str[0:10] ###SLICE ISLEMI##


### STRING ICERSINDE KARAKTER SORGULAMAK##

long_str

'veri' in long_str

'NUMBERS' in long_str

'numbers' in long_str

##STRING ( KARAKTER DIZISI) METODLARI###

dir(str)
dir(int)

##dir komutu ile ilgili veri yapisina ait metodlari gorebiliriz...

#####
len()
#### string karakter sayisini belirten gomulu fonksiyondur. bir class icersinde olmadigindan method degildir.
##Bir ifadenin metod mu fonksiyon mu oldugu bilgisine ctrl+ sol clik ile tiklayarak erisebiliriz.

name
len(name)
len('serdarozturk')

### upper() & lower()  ---- kucuk-buyuk donusumleri icin kullanilir.###

'miuul'.upper()
'MIUUL'.lower()
'Serdar'.lower()


## replace: string icersinde karakter degistirmek icin kullanilir.

hi = ' hello ai era'

hi.replace('l', 'p')

## split: bolmek icin ###

hi.split()

###strip :kirpar ##

' ofofo '.strip()
'ofofo'.strip('o')

##capitalize: ilk harfi buyutur

'ofofo'.capitalize()

####list###

## Degistirilebilir
##sirali
##kapsayici

liste = [1, 2, 3, 'a', 'b', True, [1,3,5]]
type(liste)

liste[1]

liste[6]
liste[6][2]

liste[0] = 99
liste

liste[0:4]

###LISTE METODLARI###  -en sik append komutu kullanilir

dir(liste)

len(liste)

###append eleman ekler

liste.append(100)

liste

###pop indekse gore karakter siler

liste.pop(2)
liste.append(3)
liste

##insert indexe karakter ekler

liste.insert(3, 22)
liste

##DICTIONARY##

### degistirilebilir,sirali, kapsayici

##key-value

dictionary = {'reg': 'regression',
              'log': 'logistic regression',
              'cart': 'classification and reg'}
dictionary['reg']

###key sorgulama

'reg' in dictionary

###value degistirmek

dictionary['reg'] = [3,5,'YSA']
dictionary

###'key', 'value', lere erismek

dictionary.keys()
dictionary.values()
dictionary.items()

##tuple##  ####DEGISTIRILEMEZ##

###degistirilemez, sirali, kapsayici###

t = ('john', 'mark', 1, 2, 3)
type(t)

t[3]
t[0:2]

t[0] = [99]

### degistiremezsin!!

###SET#### KUME GIBI DUSUN

#####DEGISTIRILEBILIR, SIRASIZDIR+ESSIZDIR, KAPSAYICIDIR####

####difference():  iki kumenin farki

set1 = {1, 3, 5}

set2 = {1, 2, 3}

type(set1)

set1.difference(set2)

set2.difference(set1)

##symetric_difference(): iki kumede de birbirine gore olmayanlar

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

set1 - set2

##intersection(): iki kumenin kesisimi

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


### union(): iki kumenin birlesimi

set1.union(set2)

###isdisjoint(): iki kumenin kesisimi bos mu?

set1.isdisjoint(set2)

###issubset() : bir kume digerinin alt kumesi mi?

set1.issubset(set2)

##issuperset(): bir kume digerini kapsyor mu?

set2.issuperset(set1)



#################################################
#FUNCTIONS
#CONDITIONS
#LOOPS
#COMPREHENSIONS



import keyword
keyword.kwlist

12 ** 2

pow(12, 2)

dosya = open('deneme.txt', 'w')
import os
os.getcwd()
print("Ben Python, Monty Python!", file=dosya)
dosya.close()