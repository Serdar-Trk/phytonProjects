
data = '''Ben made 300 calls and generated 2400 dollars last Month with an 8$ average deal size.
omer called 10 times and Sold 2 courses generated 60 dollars last month with a 6$ average deal size.
   KAren called 500 people and achieved success by GETting 24$ average deal size, got 12000 dollars revenue.
Celine with 70 calls, made 2275 dollars and 32$ average deal size IN the previous month.
     Sue called 100 people and earned 500 Dollars in REvenue and an AVERAGE DEAL SIZE of 5$ Last month.
Bora called 100 people generated 770 dollars last month, his average deal size was 25$.
Rose made 600 phone calls and GENERATING 4000 dollars a past month 25$ average deal SIZE.
Ellen made 800 calls and generated 6000 dollars a prior mONTH and reached 40$ the average deal size.
 bob made 200 phone calls, helped to make a proGress and generated 800 dollars LAST MONTH and gaining 15$ average deal size.
Taylor, with 450 calls generated 1200 dollars in revenue pASt month, and the average deal size was 10$.
  JuDE made 80 calls and earned 500 dollars for the company last month, her average deal size was 12$.'''

x = data.splitlines()

names = []
call_numbers = []
average_deal_sizes = []
revenues = []


def clean_extract(lines):
    for employee in lines:
        employee = employee.strip(' ')
        employee = employee.lower()
        employee = employee.capitalize()
        split_employee = employee.split(' ')
        name = split_employee[0]
        call_number = split_employee[2]

        for i in split_employee:
            for i in split_employee:
                if '$' in i:
                    average_deal_size = i
                    average_deal_size = average_deal_size.split('$')[0]

        dollars_index = split_employee.index('dollars')
        revenue_index = dollars_index - 1
        revenue = split_employee[revenue_index]

        average_deal_size = int(average_deal_size)
        call_number = int(call_number)
        revenue = int(revenue)

        names.append(name)
        call_numbers.append(call_number)
        average_deal_sizes.append(average_deal_size)
        revenues.append(revenue)
    return names, call_numbers, average_deal_sizes, revenues


names, call_numbers, average_deal_sizes, revenues = clean_extract(x)

print('Names: ', names)
print('Call_numbers: ', call_numbers)
print('Average Deal Size: ', average_deal_sizes)
print('Revenue: ', revenues)

print(len(names))

IDs = list(range(0,11))
print(IDs)

len(IDs)

dictionary1 = dict(zip(IDs, names))
print(dictionary1)

dictionary2 = dict(zip(revenues, names))
print(dictionary2)

sorted_dictionary = sorted(dictionary2)[0:3]

for i in sorted_dictionary:
    print(dictionary2[i])

sorted_dictionary = sorted(dictionary2, reverse=True)[0:3]

for i in sorted_dictionary:
    print(dictionary2[i])