
###CONDITIONS: KOSULLAR### 1==1
1==2


### IF KULLANIMI

def number_check(numbers):
    if numbers == 10:
        print('number is 10')


number_check(10)
number_check(12)


###ELSE kullanimi

def number_check(numbers):
    if numbers == 10:
        print('number is 10')
    else:
        print('number is not 10')


number_check(10)

number_check(18)


###ELIF kullanimi

def number_check(numbers):
    if numbers > 10:
        print('greater than 10')
    elif numbers < 10:
        print('less than 10')
    else:
        print('equal to 10')


number_check(9)
number_check(10)
number_check(11)

#### LOOPS : DONGULER ####

### for loop

students = ['John', 'Mark', 'Venessa', 'Mariam']

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000, 6000]

for salary in salaries:
    print(int(salary* 20/ 100 + salary))


### %20 zam yaptik

def new_salary(salary, rate):
    return int(salary * rate/ 100 + salary)


new_salary(3000, 20)

for salary in salaries:
    if salary >= 3000:
     print(new_salary(salary, 10))
    else:
     print(new_salary(salary, 20))


#######################################################

########UYGULAMA MULAKAT SORUSU####

#############################################

#### asagidaki sekilde string degistiren bir fonksiyon yazalim

###before : 'hello ai era'
###after : 'HeLlO Ai eRa'

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):  ###girilen stringin indexlerinde gez.
        if string_index % 2 ==0 :  ###index cift ise buyuk harfe cevir, new_string e kaydet.
            new_string += string[string_index].upper()
        else:  ######index tek ise kucuk harfe cevir, new_string e kaydet.
            new_string += string[string_index].lower()
            print(new_string)


alternating('hello ai era')

####BREAK & CONTINUE & WHILE

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    else:
        continue
print(salary)

for salary in salaries:
    if salary == 3000:
        continue
print(salary)

number = 1

while number < 5:
    print(number)
    number += 1

    ####### continue ve break bende calismiyor kurs bitiminde sor..

    ###  enumerate otomatik counter / indexer ile for loop

    students = ['John', 'Mark', 'Venessa', 'Mariam']

for student in students:
    print(student)
    for index, student in enumerate(students):
        print(index, student)

## cift ve tek indexte bulunan ogrencileri farkli listelere kaydet

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
         groups[0].append(student)
        else:
         groups[1].append(student)
    print(groups)
    return groups

divide_students(students)

def alternating_with_enumerate(string):
    new_string = ''
    for i, letter in  enumerate(string):
     if i % 2 ==0:
      new_string += letter.upper()
     else:
      new_string += letter.lower()
    print(new_string)

alternating_with_enumerate('hello')


#### Zip ####

departments = ['mathematics', 'statistics', 'physics ', 'ast ronomy']

ages = [22,32,42,35]

list(zip(students, departments, ages))

### lambda, map, filter, reduce##

# lambda   def gibi fonksiyon atamak icin kullanima kaydedilemez kulla-at dir.
new_sum = lambda a, b : a + b

new_sum(4, 5)

# map    dongu yazmaktan kurtarir.

s = [1000, 2000, 3000,4000, 5000]

def new_salary(x):
    return x * 20/100 +x


new_salary(5000)
for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries)
)

list(map(lambda x: x * 20/100 + x, salaries))

list(map(lambda x: x ** 2, salaries))


###FILTER

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list(filter(lambda x: x % 2 ==0,list_store))
###REDUC

from functools import  reduce

reduce(lambda a,b: a+b, list_store)

