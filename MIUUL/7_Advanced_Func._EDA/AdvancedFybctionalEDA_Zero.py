# Gelismis fonksiyonel kesifci veri analizi
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
df.head()

# veriye uygulayabliecegimiz bazi fonksiyonlar


def check_df(dataframe):
    print('############SHAPE#########')
    print(dataframe.shape)


check_df(df)


def check_df(dataframe, head=5):
    print('############SHAPE#########')
    print(dataframe.shape)
    print('########TYPES#########')
    print(dataframe.dtypes)
    print('########HEAD#########')
    print(dataframe.head(head))
    print('########TAIL#########')
    print(dataframe.tail(head))
    print('########NA#########')
    print(dataframe.isnull().sum())


check_df(df)

df = sns.load_dataset('flights')
check_df(df)

# Kategorik Degisken Analizi(Analysis of Categorical Variables)

df['embarked'].value_counts()  # tek bir degiskeni analiz etmek icin

# cok fazla degisken oldugunda bunu nasil yapariz?

# fonksiyonel bir sekilde genellenebilirlik kaygisiyla degisken tiplerini analiz etmek icin:

cat_cols = [col for col in df.columns if str(df[col].dtype) in ['category', 'object', 'bool']]

df['sex'].dtype
str(df['sex'].dtype)
str(df['sex'].dtype) in ['object']

# dikkat etmemiz gereken nokta kategorik olmasina ragmen int gibi davranan degiskenleri tespit etmek icin farkli bir yol izlemek gerekebilir.
# mesela survived degiskeninin iki degiskeni var. yani kategorik ama 0 ve 1 lerden olustugu icin int formatinda.

df['survived'].value_counts()

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ['int64', 'float']]

# tipi int yada float olup; essiz sinif sayisi belirli bir degerden kucuk olan degiskenleri yakaladim.

# programatik olarak kategorik tipte olmayip kategorik olanlari yaklamak icin:

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ['category', 'object']]

cat_cols = cat_cols + num_but_cat

df[cat_cols]  ## artik hepsi kategorik

# dogrulamak icin bakalim

df[cat_cols].nunique()

# kategorik olmayanlara bakalim

[col for col in df.columns if col not in cat_cols]

# fonksiyon yazalim( once girilen degiskenin value count alsin ve oran bilgisini versin)

df['survived'].value_counts()
100 * df['survived'].value_counts() / len(df)


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        'Ratio': 100 * dataframe[col_name].value_counts() / len(dataframe)})),
    print('################################')


df.head()

cat_summary(df, 'sex')

## bu fonksiyonu butun degiskenlere uygulamak istersek

for col in cat_cols:
    cat_summary(df, col)


#  fonksiyona gorsel eklemek istersek

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        'Ratio': 100 * dataframe[col_name].value_counts() / len(dataframe)})),
    print('################################')
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


cat_summary(df, 'sex', plot=True)

for col in cat_cols:
    cat_summary(df, col, plot=True)

#  bool tipte olanlarda takildigi icin onu pas gecicez.

for col in cat_cols:
    if df[col].dtype == 'bool':
        print('######**BOOL**######')
    else:
        cat_summary(df, col, plot=True)

# boyle bir durumda 'bool' yapi tipini int olarak degistirerek gorsellestirme sorunun cozebiliriz.

df['adult_male'].astype(int)

for col in cat_cols:
    if df[col].dtype == 'bool':
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot=True)

# Sayisal Degisken Analizi (Analysis of Numerical Variables)

df[['age', 'fare']].describe().T

num_cols = [col for col in df.columns if df[col].dtypes in ['int64', 'float64']]

num_cols = [col for col in num_cols if col not in cat_cols]


def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]
    print(dataframe[numerical_col].describe(quantiles).T)


num_summary(df, 'age')

for col in num_cols:
    num_summary(df, col)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]
    print(dataframe[numerical_col].describe(quantiles).T)
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    num_summary(df, col, plot=True)


# Degiskenlerin Yakalanmasi Ve Islemlerin Genellestirilmesi
# Capturing Variables and Generelazing Operations

# docstring olusturma

# tek fonksiyonla butun ihtiyaci gorme

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """

    Parameters
    ----------
    dataframe: dataframe
       Degisken isimleri alinmak istenen dataframe dir.
    cat_th: int, float
       Numerik fakat kategorik olan degiskenler icin sinif esik degeri
    car_th: int, float
       Kategorik fakat kardinal degiskenler icin sinif esik degeri

    Returns
    -------
    cat_cols: list
       Kategorik degisken listesi
    num_cols: list
       Numerik degisken listesi
    cat_but_car: list
       Kategorik gorunumlu kardinal degisken listesi

    Notes
    -------
    cat_cols + num_cols + cat_but_car = toplam degisken sayisi
    num_but_cat cat_cols ' un icerisinde
    """
    cat_cols = [col for col in df.columns if str(df[col].dtype) in ['category', 'object', 'bool']]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in [int, float]]
    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ['category', 'object']]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if df[col].dtypes in [int, float]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f'Observation: {df.shape[0]}')
    print(f'Variables: {df.shape[1]}')
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car

grab_col_names(df)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

# BONUS

# Hedef degisken analizi(Analysis of Target Variable)

# sirada elimizdeki hedef degiskeni kategorik ve sayisal degiskenler acisindan analiz etmektir.

df['survived'].value_counts()
cat_summary(df, 'survived')

# Hedef degiskenin Kategorik Degiskenler Ile Analizi

df.groupby('sex')['survived'].mean()


# bunu bir fonksiyonla yapmak istersek

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({'Target_Mean': dataframe.groupby(categorical_col)[target].mean()}))


target_summary_with_cat(df, 'survived', 'sex')
target_summary_with_cat(df, 'survived', 'pclass')

for col in cat_cols:
    target_summary_with_cat(df, 'survived', col)

#  Hedef degiskenin Sayisal Degiskenler Ile Analizi

df.groupby('survived')['age'].mean()

# ayni islemi agg ile de yapabiliriz

df.groupby('survived').agg({'age': 'mean'})


# def target_summary_with_num(dataframe, target, numerical_col):

def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: 'mean'}))


target_summary_with_num(df, 'survived', 'age')

for col in num_cols:
    target_summary_with_num(df, 'survived', col)

df.head()

