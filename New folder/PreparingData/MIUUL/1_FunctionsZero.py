# fonksiyon okuryazarligi
help(print)  ### fonksiyonun ne ise yaradigini gormek icin help ya da ? kullan


# fonksiyon tanimlama

def calculator(x):
    print(x * 2)


calculator(5)


## iki argumanli/parametreli fonksiyon tanimlama

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(1020, 1980)


###DOCSTRING : fonksiyona bilgi notu eklemek icin


def summer(arg1, arg2):
    """
   sum of two numbers...
    :param arg1: int, float
    :param arg2: int, float
    :return: int, float
    """
    print(arg1 + arg2)

### FONKSIYONLARIN STATEMENT/BODY BOLUMLERI


def multiplaication(a, b):
    k = a * b
    print(k)


multiplaication(10, 9)

##girilen degerleri bir liste icersinde saklayacak bir fonksiyon tasarlayalim

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(8, 15)
add_element(3, 2)
add_element(5, 2)

list_store


###ON TANIMLI ARGUMANLAR##

def say_hi(string='merhaba'):
    print(string)
    print('hi')
    print('hello')


say_hi()


####RETURN : fonksiyonlarin ciktilarini girdi olarak baska bir islemde kullanmamiz gerektiginde return kullanilir..

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


calculate(98, 12, 78)


###FONKSIYON ICERSINDE FONKSIYON CALISTIRMAK###

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(90, 12, 12) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


def all_calculation(varm, moisture, charm, p):
    a = calculate(varm, moisture, charm)
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 12)


###lokal & global degiskenler(variables)

list_store = [1, 2]


def add_element(a, b):  #### 'a' ve 'b' ye global degisken denir. c= a * b  #### 'c' ye local degisken denir.
    list_store.append(a * b)  #### : ifadesinden sonraki alana local etki alani denir.
    print(list_store)


add_element(1, 9)
