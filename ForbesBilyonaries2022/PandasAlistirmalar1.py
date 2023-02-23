

import pandas as pd

df = pd.read_csv('ForbesBilyonaries2022/forbes_2022_billionaires.csv')

df.head(15)

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

df.shape
df.dtypes

df = df.loc[:, ['rank', 'personName', 'age', 'finalWorth', 'category', 'country', 'gender']]

df = df.set_index('rank')

df.isnull().sum()

df.dropna(inplace=True)

df.info

# GENDER ANALYSIS

df['gender'].value_counts()

df['gender'].value_counts(normalize=True)

df_gender = df.groupby(['gender'])

df_gender['age'].mean()

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set(rc={'figure.figsize': (10, 6), 'figure.dpi': 200})

import warnings
warnings.filterwarnings('ignore')

df_gender.size().plot(kind='bar')
plt.title('Average ages of men and women', fontsize=20)
plt.show(block=True)

# TOP 10 RICHEST

sns.barplot(x=df['finalWorth'][:10], y=df['personName'][:10])
plt.title('TopTenRichest', fontsize=18)
plt.show(block=True)

# TOP 10 COUNTRIES

df['country'].nunique()

df_country_count = pd.DataFrame(df.groupby('country').size().sort_values(ascending=False), columns=['count'])
df_country_count.head()

sns.barplot(x=df_country_count['count'][:10], y=df_country_count.index[:10])
plt.title('TOP 10 COUNTRIES', fontsize=15)
plt.show(block=True)


# TOP 10 CATEGORIES

df['category'].unique()

df['category'] = df['category'].apply(lambda x:x.replace(' ', '')).apply(lambda x:x.replace('&', '_'))

df['category'].unique()

df_category = df.groupby('category').size()
df_category.head()

df_category = df_category.to_frame()
df_category.head()

df_category = df_category.rename(columns={0:'counts'}).sort_values(by='counts', ascending=False)
df_category.head()

sns.barplot(x=df_category['counts'][:10], y=df_category.index[:10])
plt.title('TOP 10 CATEGORIES', fontsize=15)
plt.show(block=True)

# THE RELATIONSHIP BETWEEN MONEY & AGE

sns.scatterplot(x=df['age'], y=df['finalWorth'])
plt.title('HE RELATIONSHIP BETWEEN MONEY & AGE', fontsize=15)
plt.show(block=True)

# THE DISTRIBUTION OF AGE

sns.histplot(df['age'])
plt.title('THE DISTIBUTION OF AGE', fontsize=20)
plt.show(block=True)

# forbes.com/billionaires/




