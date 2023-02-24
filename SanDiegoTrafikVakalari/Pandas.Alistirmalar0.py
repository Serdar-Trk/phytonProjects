
                                              # San-Diego-Trafik-Vakalari #
import pandas as pd

df = pd.read_csv('SanDiegoTrafikVakalari/ca_san_diego_2020_04_01.csv')

df.head(200)

pd.set_option('display.max_rows', 50)

pd.set_option('display.max_columns', 500)

pd.set_option('display.width', 500)

df.shape

df.dtypes

df.isna().sum()

df.date.head()

df.columns

df['time'].head()

df[['date', 'time']].head()

df.rename(columns={'date': 'DATE', 'time': 'TIME'}, inplace=True)

df.iloc[0].head()
df.iloc[0, 1]
df.iloc[0, [1, 2, 3]]
df.iloc[0:5, [3, 5, 6]]
df.iloc[0:8, 3:5]

df.loc[0:5, ['TIME', 'DATE']]

# Gozlemlerin tamami eksik bilgi olanlari silelim.

df.dropna(axis=1, how='all').shape

df['reason_for_stop'].value_counts().head()

df[df.reason_for_stop == 'Moving Violation'].subject_sex.value_counts(normalize=True)

# Cinsiyeti kadin olanlarin durdurulma nedenlerinin yuzdeleri

df[df.subject_sex == 'female'].reason_for_stop.value_counts(normalize=True).head()

df.groupby('subject_sex').reason_for_stop.value_counts(normalize=True).head()

df.groupby('subject_sex').reason_for_stop.value_counts(normalize=True).unstack()

df.arrest_made.value_counts()
df.arrest_made.value_counts(normalize=True)

df.groupby(['subject_race', 'subject_sex']).arrest_made.value_counts(normalize=True)


df.DATE.str.slice(0, 4).value_counts()

# DATE ve TIME kolonlarini tek bir DATETIME kolonu halile getirelim.

combined = df.DATE.str.cat(df.TIME, sep=' ')
df['stop_datetime'] = pd.to_datetime(combined)
df.head()

df.dtypes

df.arrest_made.value_counts()

df.arrest_made.mean()

# saatlik olarak tutuklanma ortalamasi

df.groupby(df.stop_datetime.dt.hour).arrest_made.mean().head()

import matplotlib.pyplot as plt


x = df.groupby(df.stop_datetime.dt.hour).arrest_made.mean()
plt.plot(x)
plt.show(block=True)

y = df.stop_datetime.dt.hour.value_counts().sort_index()
plt.plot(y)
plt.show(block=True)

