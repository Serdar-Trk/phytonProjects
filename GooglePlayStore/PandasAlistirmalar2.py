
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('GooglePlayStore/googleplaystore.csv')
df.head()

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

# UNDERSTANDING THE DATASET

df.columns
df.columns = df.columns.str.replace(' ', '_')
df.shape
df.dtypes

# HANDLING MISSING DATA

df.isnull().sum()

sns.set_theme()
sns.set(rc={'figure.dpi': 200, 'figure.figsize': (10, 7)})

sns.heatmap(df.isnull(), cbar=False)
plt.show(block=True)

# We used the 'heatmap' method to better observe the missing data.
# Then we used 'median()' for missing data in the 'Rating'

rating_median = df['Rating'].median()
df['Rating'].fillna(rating_median, inplace=True)

#  remove the other missing data

df.dropna(inplace=True)

df.info()

# DATA PREPROCESSING
#
df['Reviews'].describe()
df['Reviews'] = df['Reviews'].astype('int64')
df['Reviews'].describe().round()

df['Size'].nunique()
df['Size'].head(20)
df['Size'].replace('M', '', regex=True, inplace=True)
df['Size'].replace('k', '', regex=True, inplace=True)
df['Size'].unique()
size_median = df[df['Size'] != 'Varies with device']['Size'].astype(float).median()
size_median
df['Size'].replace('Varies with device', size_median, inplace=True)
df['Size'] = pd.to_numeric(df['Size'])
df['Size'].info
df['Size'].describe().round()

df['Installs'].unique()
df['Installs'] = df['Installs'].apply(lambda x: x.replace('+', '')).apply(lambda x: x.replace(',', ''))
df['Installs'] = df['Installs'].apply(lambda x: int(x))

df['Price'].unique()
df['Price'] = df['Price'].apply(lambda x: x.replace('$', ''))
df['Price'] = df['Price'].apply(lambda x: float(x))

df['Genres'].unique()
df['Genres'] = df['Genres'].str.split(';').str[0]
df['Genres'].value_counts()
df['Genres'].replace('Music & Audio', 'Music', inplace=True)

df['Last_Updated'].head()
df['Last_Updated'] = pd.to_datetime(df['Last_Updated'])

df.head()
df.dtypes
df.shape

# DATA VISUALIZATION

df['Type'].value_counts()
df['Type'].value_counts().plot(kind='bar', color='red')
plt.title('Free & Paid')
plt.show(block=True)

sns.boxplot(x='Type', y='Rating', data=df)
plt.title('Content Ratings with their counts')
plt.show(block=True)

sns.countplot(y='Content_Rating', data=df)
plt.title('Content Rating With their counts')
plt.show(block=True)

sns.boxplot(x='Content_Rating', y='Rating', data=df)
plt.title('The Content Rating & Rating', size=20)
plt.show(block=True)

cat_num = df['Category'].value_counts()
sns.barplot(x = cat_num, y = cat_num.index, data=df)
plt.title('The Number Of Categories', size=20)
plt.show(block=True)

sns.scatterplot(x='Price', y='Category', data=df)
plt.title('Category & Price', size=20)
plt.show(block=True)

sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt='.2f')
plt.title('Heatmap for numerical cols', size=20)
plt.show(block=True)

sns.histplot(df['Rating'], kde=True)
plt.title('Histogram with the kde for the rating column', size=20)
plt.show(block=True)

