#### COMPREGENSIONS #####

### list compreghension###

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


for salary in salaries:
    print(new_salary(salary))

null_list = []
for salary in salaries:
    null_list.append(new_salary(salary))

for salary in salaries:
    if salary < 3000:
        null_list.append(new_salary(salary * 2))
    else:
        null_list.append(new_salary(salary))

del null_list

## bu islemi comprehension kullarak yaparsak!!!

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

### if tek basina kullanildiysa sona yazilir aksi halde yukaridaki gibi..

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

students = ['John', 'Mark', 'Venessa', 'Mariam']

students_no = ['John', 'Venessa']

[student.lower() if student in students_no else student.upper() for student in students]

[student.lower() if student not in students_no else student.upper() for student in students]

###DICT COMPREHENSIONS##

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}
dictionary.keys()
dictionary.values()
dictionary.items()
dictionary.
{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v + 5 for (k, v) in dictionary.items()}

### UYGULAMA - MULAKAT SOURUSU

## AMAC = cift sayilarin karesi alinarak bir sozluge eklenmek istenmektedir..
## key ler orjinal degerler value ler degistirlmis olacak
numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}

## comprehension ile yapimi


### list & dict comprehension uygulamalari

##########  bir veri setindeki degisken isimlerini degistirmek


import seaborn as sns

### ilgili veriyi cekmek icin seaborn kutuphanesinden python Console

##   uzerinden import ettim
df = sns.load_dataset('car_crashes')  ### daha sonra seaborn kutuphanesi uzerinden "car_crashes'
### veri setini getirdim. ve data frame olarak kaydettim.
df.columns  ## kolonlari yazdirdim.

for col in df.columns:
    print(col)

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

##ISTE COMPREHENSION KULLLANARAK YAPIMI

df.columns = [col.upper() for col in df.columns]

#### colon basliklarindan basinda 'INS'  idadesi olanlarin basina 'FLAG' olmayanlarin basina 'NO_FLAG' yaz

df.columns

[col for col in df.columns if 'INS' in col]

'A' + 'B'

['FLAG_' + col for col in df.columns if 'INS' in col]

['FLAG_' + col if 'INS' in col else 'NO_FLAG_' + col for col in df.columns]

##amac: key i string, value si asagidaki gibi olan bir sozluk olusturmak.
##sadece sayisal degiskenler icin yapmak istiyoruz..

###########output########
# { 'total' : ['mean', 'min', 'max', 'var']
# 'speeding' : ['mean', 'min', 'max', 'var']
# 'alcohol' : ['mean', 'min', 'max', 'var']
# 'not_distracted' : ['mean', 'min', 'max', 'var']
# 'no_previous' : ['mean', 'min', 'max', 'var']
# 'ins_premium' : ['mean', 'min', 'max', 'var']
# 'ins_losses' : ['mean', 'min', 'max', 'var']
# 'abbrev'  : ['mean', 'min', 'max', 'var']      }

df.columns = [col.lower() for col in df.columns]

df.columns

num_cols = [col for col in df.columns if df[col].dtype != 'O']

## 'O' object in kisaltmasidir. sayisal degisken istedigimiz icin  onu cikardik.

soz = {}

agg_list = ['mean', 'min', 'max', 'var']

for col in num_cols:
    soz[col] = agg_list

###iiiste comprehension kullanarak kisa yol.

{col: agg_list for col in num_cols}

df.head()

new_dicti = {col: agg_list for col in num_cols}

df[num_cols].head()  ##ilgili dataframe i sadece numerik olanlar olacak sekilde gruplandirdim

## aggrigation : agg fonksiyonu beklentilerimizi algilayabilecek akilli bir foksiyondur.
## comprehension larin onemini anlayabilecegimiz bir ornekte kullanalim.

df[num_cols].agg(new_dicti)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
