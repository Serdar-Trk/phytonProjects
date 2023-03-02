# os modulu
# isletim sistemleri arasinda ortak bir arayuz olusturur.

import os

dir(os)
# pyhton un kurulu oldugu ilsetim sistemini gormek icin:
os.name
# 'nt'   ---> windows isletim istemini temsil eder

# dizin degistirmek icin:
os.chdir('C:\\PhytonDersleri')
os.chdir('C:\\Users\\serda\\PycharmProjects\\MIUUL')
# dizini silmek icin
os.rmdir('C:\\PhytonDersleri')
# bir dizindeki dosyalari goruntulemek icin
os.listdir()  # etkin dizindeki dosyalar icin yeterli
os.listdir('C:\\Users\\serda\\PycharmProjects\\MIUUL')
# dizinde bir dosyayi acmak istersek
os.startfile('7_Advanced_Func._EDA')
# Yeni bir dizin olusturmak istersek, olusturmak isteidigimiz dizinin 'path' ini yazzariz
os.mkdir('C:\\Users\\serda\\OneDrive\\Masaüstü\\YeniDizin')
# dizin isimlerini degistirmek icin
os.rename('Moduls\\Moduller.py', 'Moduls\\ModulsZero')
# dizinin ozet bilgilerine erismek icin
os.stat('5_PandasZero.py')
# pyhton icinden baska programlari calistirmak istersek
os.system('notepad.exe')
# etkin olan calisma dizini gormek icin:
os.path.abspath('.')

# random modulu
import random

dir(random)

# rastgele sayi uretmek icin:(1 ile 10 arasinda olsun)
random.randint(1, 10)
# 0 ile 1 arasinda rastgele olusturmak icin, daha fazlasi icin for dongusu kullanilir
random.random()

for i in range(10):
    x = random.random()
    print(x)

# belirli bir aralikta ondalikli sayi uretmek istersek:
random.uniform(1, 2)
# bir listeden rastgele secim yapmak istersek:
list = ['rock', 'paper', 'scissors']
random.choice(list)
s = 'serdar'
random.choice(s)
# listeyi karistirmak istersek
random.shuffle(list)

# listeden rastgele birden fazla secim  yapmak icin
list = range(500)
random.sample(list, 3)

# ornek bir calisma

numb = random.randint(0, 100)
while True:
    guess = int(input('0-100 arasi bir sayi giriniz: '))
    if guess > numb:
        print('Daha kucuk bir sayi giriniz.')
    elif guess < numb:
        print('Daha buyuk bir sayi giriniz.')
    else:
        print('Tebrikler, dogru bildiniz.')
        break

# Datetime modulu
from datetime import datetime

dir(datetime)
# suan
datetime.now()
datetime.now().month
datetime.now().hour
datetime.now().second

datetime.today()  # aynisi
# girilen tarihi metin olarak yazdirmak istersek
datetime.ctime(datetime.today())

# tarih ve zamani istedigimiz gibi manipule etmek icin
datetime.strftime(datetime.now(), '%A')
# for another 'date & time' formats:
# https://www.geeksforgeeks.org/python-strftime-function/

datetime.now() - datetime(1995, 1, 20)

# sqlite modulu hakkinda bilgi icin:
# https://youtu.be/pWE-K2q7zfk
