# Korelasyon Analizi(Analysis of Correlation)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()

# yuksek korelasyonlu degiskenleri nasil yakalariz..
# yukaridaki veri setindeki numerik degiskenleri sececek bir list_comprehention kullanalim.
num_cols = [col for col in df.columns if df[col].dtypes in [int, float]]

corr = df[num_cols].corr()

# korelasyon -1 ve +1 arasinda dir. 1 lere yaklastikca bagimlilik, benzerlik artar. bircok calismada corelasyonu yuksak degiskenlerden birini atmak isteyebilriiz.

sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap='RdBu')
plt.show(block=True)

## korelasyonu gormek icin yukaridaki isi haritasinda gorebiliriz.
# daha anlasilir olmasi icin corelasyonu abs() fonk ile mutlak degere aliyorum. artik sadece '0-1' var.

cor_matrix = df[num_cols].corr().abs()

# ihtiyac olursa korelasyonu yuksek olan degiskenleri silmek istersek ne yapmaliyiz?

# Bunun icin NumPy icersinde bulunnan bir fonksyiyondan yararlanicaz

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))

# yukardaki islem ile korelasyonu 1 olanlari sildik.
# korelasyonu 0.99 gibi olanlari da silmek istersek..

drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]

# 0.90 dan buyuk olanlari bulduk. silelim.
df.drop(drop_list, axis=1)


# bu islemi fonksiyonlastirmak istersek, soyle bir fonk yazariz
# corr_th=0.90 = korelasyon esik degeri

def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (12, 12)})
        sns.heatmap(corr, cmap='RdBu')
        plt.show(block=True)
        return drop_list
    print(drop_list)


high_correlated_cols(df)
drop_list = high_correlated_cols(df, plot=True)
df.head()

high_correlated_cols(df.drop(drop_list, axis=1), plot=True)

# veri setindeki yuksek korelasyonlu degiskenlerden kurtulduk.

# formulumuzu daha buyu bir veri setinde deneyelim.

df = pd.read_csv("Fraud.csv")
len(df.columns)
df.head()

drop_list = high_correlated_cols(df, plot=True)
len(df.drop(drop_list, axis=1).columns)












