

# Scikit-learn nedir? Nasil kullanilir?
# Dogrusal Regresyon
# Siniflandirma Yontemi

import seaborn as sns

iris = sns.load_dataset('iris')
iris.head()
X_IRIS = iris.drop('species', axis=1)
Y_IRIS = iris['species']

X_IRIS.shape
Y_IRIS.shape

# X_IRIS = OZNITELIK DIZISI
# Y_IRIS = HEDEF DIZISI

# SCIKIT-LEARN model islemleri

# sklearn de modelin her sinifi pyhton sinifi olarak gosterilir.
# orneegin basit dogrusal regresyonu kullanmak istiyorsak lineer regresyon sinifini import (ediyoruz)

# verıyı sabıtlemek
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)
x=10*rng.rand(50)
y=2*x-1+rng.randn(50)
plt.scatter(x, y)

from sklearn.linear_model import LinearRegression

# sabit olacak mi? model normallestirilecek mi? Modelde kullanmak istedigimiz regulerlestirme seviyesi ne kadar olacak?
# gibi sorulari cevaplamak icin hyper-parameter kullanabilriz.
# model kurulmadan once hiper parametreler belirlenir
# hyper parametreler on tanimli parametrelerin uzerine yazilir.
# hyper parametreler yazilmadiginda on tanimli parametreler gecerli olur.
# ornek olarak dogrusal regresyonda linear regresyon sinifini ornekleyelim

model=LinearRegression(fit_intercept=True)
model

X=x[:, np.newaxis]
X.shape

model.fit(X, y)
# model kuruldu

# model katsayisini yazdirmak icin

model.coef_
# modelin sabiti
model.intercept_

x_fit = np.linspace(-1, 11)
X_fit = x_fit[:, np.newaxis]
y_fit = model.predict(X_fit)

plt.scatter(x, y)
plt.plot(x_fit, y_fit)

#  veri setine gore regresyon dogrusu cizilmis oldu

#  simdi iris veri setini kullanarak denetimli ogrenmedeki siniflandirmaya goz atalim


#  BU BOLUMDEKI AMACIMIZ IRIS VERI SETINDEKI TRAIN I KULLANARAK BIR MODEL OLUSTURMAK VE
# DAHA SONRA BU MODELI KULLANARAK TEST VERISINDEKILERIN TARGETINI TAHMIN ETMEK

# veri setini parcalayalim

from sklearn.model_selection import  train_test_split

X_TRAIN, X_TEST, y_train, y_test = train_test_split(X_IRIS, Y_IRIS, random_state=1)

# model sinifini secelim

from sklearn.naive_bayes import GaussianNB
# GaussianNB --> hem hizli hemde hyper parameter gerektirmiyor.

model = GaussianNB()

model.fit(X_TRAIN, y_train)

# modeli kurduk.

# simdi yeni veri icin tahmin yapalim

y_model = model.predict(X_TEST)
# MODELIN DOGRULUK ORANINI BULALIM

from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_model)

# dogruluk oranini bulduk. modelimiz yeni bir iris ciceginin turunu 0.97 dogruluk oraniyla tespit edebilir.

