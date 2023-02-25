
names = ['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
call_numbers = [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
average_deal_sizes = [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]


import numpy as np

data = np.array([], dtype=int)


def append_names(name_list):
    global data
    for i in name_list:
        data = np.append(data, names.index(i))


def append_performance_measures(feature_list):
    global data
    data = np.append(data, feature_list)


append_names(names)
append_performance_measures(call_numbers)
append_performance_measures(average_deal_sizes)
append_performance_measures(revenues)

print(data)
print(data.shape)

data = data.reshape(4, 11)

print(data.shape)


def calculate_performance(employee_name):
    idx = names.index(employee_name)
    num_of_calls = data[1, idx]
    average_deal_size = data[2, idx]
    revenue = data[3, idx]
    score = (average_deal_size*revenue) / num_of_calls
    return score


performance_scores = []
for name in names:
    score = int(calculate_performance(name))
    performance_scores.append(score)

data = np.concatenate((data, [performance_scores]), axis=0)
print(data)

idx_best_employee = np.argmax(data[4])
idx_worst_employee = np.argmin(data[4])

print(f'Best performing employee: {names[idx_best_employee]}')
print(f'Worst performing employee: {names[idx_worst_employee]}')

