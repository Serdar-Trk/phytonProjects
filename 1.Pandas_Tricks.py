




# Neden? Nasıl? Düşünmeyi bırakın ve harekete geçin. Çünkü siz düşünürken zaman akmaya devam ediyor.
# Potansiyeliniz mi var? Yola çıkın. O soruların cevabını yolda bulacaksınız. Ve o soruların yerini baska sorular alacak, sonra baska sorular.
# Ya da yuvarlak organınızın uzerinde şikayet ederek ve bahaneler üreterek ömrünüzü tüketebilirsiniz. Şaka değil seçim sizin :)
# (Arkaya da bi tane motivasyon müzigi, tamamdır, benden olur :) )

# Bir süredir flört ettiğim Pandas Kütüphanesinin çok kullanışlı olduğunu düşündüğüm yaklaşık 50 püf noktasını seri şeklinde sizlerle paylaşmak istiyorum.
# ‘5 Pandas_Tricks’ başlığıyla kaleme alacağım(klavyeye alamam) bu medium serisi bir süre devam edecek..
# Ayni zamanda burada sizlerle paylaşacağım püf noktaların benim icinde not değeri oldugunu bilmenizi isterim.
# Bildiginiz üzere bu alanda Turçe kaynak azligi ve ingilizce cok fazla icerik oldugundan, burada uretecegim icerikler ağırlıklı olarak Turkce olacaktır.
# Bu vesileyle bu alana merak salan ve ingilizcesi yeterli duzeyde olmayan(henüz) arkadaslar da bu bilgilerden ceviriye ihtiyac duymadan istifade edebilirler.


# Konumuza gelirsek bu serimizde, faydalı olacağını düşündüğüm 5 Pandas ipucunu "5_Pandas_Trick" basligiyla paylasiyor olacagim.

import pandas as pd
import numpy as np
import seaborn as sns
df = sns.load_dataset('titanic')


# # Bu yazimizda ele alacagimiz 5 Pandas_Tricks

# 1-)  Sanal Ortamimizdaki paketlerin versiyon bilgilerine Pandas kullanarak nasil ulasabiliriz?
# Cok kolay:
# Bazen kullanmakta olduğunuz Pandas Versiyonunu bilmek isteyebilirsiniz. Özellikle Pandas belgelerini okuturken.
# Asagida yazdigim islemi uygulayarak Pandas versiyonunuzu ogrenebilirsiniz.
pd.__version__

# Eger sanal ortaminizdaki butun paketlerin versiyon bilgisine erismek isterseniz asagidaki islemi uygulayabilirsiniz.
pd.show_versions()

# 2-) Örnek bir DataFrame olusturmak

# Diyelimki birkac pandas kodunu gostermek istiyorsunuz. Bunun icin ornek bir DataFrame e ihtiyaciniz olacaktir.
# Boyle basit bir islem icin kalabalik bir DataFrame yuklemenize gerek kalmayabilir.

# Peki bu nasıl olacak?
# Bunun icin 2 farkli yöntemi asağıda bulabilirsiniz..

df = pd.DataFrame({'ekmek': [100 ,200], 'pasta': [300 ,400]})

pd.DataFrame(np.random.rand(4 ,8), columns=list('VERIVERI'), index=list('VERI'))

# 3-) Sutunlari yeniden isimlendirmek

# Burada sık kullanılan rename() methoduna sıklıkla başvurulur.
# Bir sözluk yapısında key=eski ve value=yeni olacak şekilde aşagıdaki gibi yazılır.
# Bu method bizlere belirledigimiz kolonlarn adını değiştirebilme imkanı tanır.

df = df.rename({'ekmek' :'patates', 'pasta' :'sogan'}, axis=1)
df
# Bütün kolon adlarını değiştirmek istersek, mevcut kolonlar sayısınca belirlediğimiz yeni kolonları-
# aşağıdaki işlemi uygulayabiliriz:

df.columns = ['ek mek', 'pas ta']
df
# Kolonların içerdiği bazı ifadeleri yenileriyle değiştirmek istersek:

df.columns = df.columns.str.replace(' ', '_')
df

# Kolon isimlerinin başlarına ya da sonlarına bir ifade eklemek istediğimizde:
df.add_prefix('S_')
df.add_suffix('_S')

# 4-) Tersten kosullu satır-sütun seçimi

# Asagıdaki yöntem ile tesrten koşullu seçim yapabilirsiniz

df.loc[::-1].head()

# tekrar eski haline cevirmek icin aşagıdaki işlemi uygulayabilirsiniz.

df.loc[::-1].reset_index(drop=True).head()

# 5-) Tersten kosullu kolon secimi

df.loc[:, ::-1].head()
df.loc[:, ::-1].reset_index(drop=True).head()


# 4. ve 5. islemi birlikte yapmak istersek

df.loc[::-1, ::-1].head()
df.loc[::-1, ::-1].reset_index(drop=True).head()


# 6-) Select columns by Datatype
# Here are the datatypes 'titanic' dataframe
df.dtypes
# You need to select only numeric columns
# This includes both int and float columns
df.select_dtypes(include='number').head()

# You could also use this method to select just the 'object' columns.
df.select_dtypes(include='object').head()
# You can tell it to include multiple data types by passing a list
df.select_dtypes(include=['number', 'object', 'category', 'datetime']).head()
# You can also tell it to exclude certain data types
df.select_dtypes(exclude='number').head()

# 7-) Concert string to numbers
