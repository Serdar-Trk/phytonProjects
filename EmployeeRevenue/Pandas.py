
import numpy as np
import pandas as pd


last_year = pd.read_csv('EmployeeRevenue/employee_revenue_lastyear.csv')

last_year.head()

last_year.shape
last_year.info

last_year['Year'] = 2021

names = np.array(['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude'])
call_numbers = np.array([300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80])
average_deal_sizes = np.array([8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12])
revenues = np.array([2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500])


dictionary = {'Name': names,
              'call_numbers': call_numbers,
              'avg_deal_size': average_deal_sizes,
              'revenue': revenues}

current_year = pd.DataFrame(dictionary)

current_year.head()

type(current_year)

current_year['Year'] = 2021

current_year.columns = last_year.columns

all_data = pd.concat([last_year, current_year], axis=0)


all_data.reset_index()

all_data.isnull().any()

all_data.fillna(value=np.mean(revenues), inplace = True)

all_data.drop_duplicates(inplace=True)

all_data.reset_index(drop=True)
all_data

all_data['Year'].describe().T

all_data.describe().T

all_data.sort_values(by='Revenue')

all_data[all_data['Name'] == 'Rose'].sort_values(by='Revenue')

all_data['Name'].value_counts()

all_data.head()






