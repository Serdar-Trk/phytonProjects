


# CRM Analitiği
# RFM Analizi
# Müşteri Yaşam Boyu Değeri
# Müşteri Yaşam Boyu Değeri Tahmini


# Introduction to CRM Analytics
# musteri iliskileri yonetimi

# Customer Lifecycle = musterilerle kurulan etkilesimi gorsellestirerek, bunlari cesitli KPI lar ile takip edilebilir bir forma getirip, takip etme imkani saglayan kavrmlardir.

# Musteri bulma & Musteri tutma

# Cross-sell = capraz satis & Up-sell = ust satis

# musteri segmentasyon calismalari

# KPIs - Key Performance Indicators(Temel performans gostergeleri)
#  departmanin ya da calisanlarin performanslarini degerlendirmek icin kulanilan gostergelerdir
# Customer Acquisition Rate(Musteri kazanma orani)
# Customer Retention Rate(Musteri elde tutma orani)
# Customer churn rate(musteri terk orni)
# Conversion rate(donusum orani) - iletisim(etkilsilen) kurulan musterilerin donus orani
# Growth Rate(Buyume Orani)


# ANALYSIS OF COHORT

# cohort=ortak ozelliklere sahip bir grup insan


# RFM ILE MUSTERI SEGMENTSYONU
# CUSTOMER SEGMENTATION WITH RFM
# RFM=Recency,Frequency,Monetary

# Musterilerin satin alma aliskanlikari uzerinden gruplara ayrilmasi ve stratejiler gelistirilebilmesini saglar
# CRM calismalari icin bircok baslikta veriye dayali aksiyon almayi saglar

# RFM metriklerini kiyaslayabilmek icin standartlastirmamiz lazim
# standartlastirilan RFM metriklerine RFM SKORU DENIR.
# olusturdugumuz bu skorlar uzerinden segmentler olustururuz.








# 1-) Business Problem
# Bir e-ticaret sirketi musterilerini segmentlere ayirip, buna gore pazarlama strtejileri belirlemek istiyor
# Kurumsal musterilere sahip bu ingiliz e-ticaret sirketi musterilerini 'Recency, Frequency' degerlerine gore segmentlere ayirip ozel olaarask ilgilenmek istemektedir.

# 2-) Business Understanding

import pandas as pd
pd.set_option('display.max_column', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.3f' %x)

df_ = pd.read_excel('MIUUL/CRM_Analytics/datasets/online_retail_II.xlsx')
df_.head()
df = df_.copy()
df.columns


# DEGISKENLER

# 'Invoice', \       fatura numarasi. 'c' ile basliyorsa iptal. essiz.
# 'StockCode', \     urun kodu, essiz.
# 'Description', \   urun ismi
# 'Quantity', \      faturalardaki urunlerden kacar tane satildigini ifade etmektedir.
# 'InvoiceDate', \   fatura tarihi ve zamani
# 'Price', \         urun fiyati(sterlin)
# 'Customer ID', \   musteri no
# 'Country'          musterinin yasadigi ulke

df.shape
df.isnull().sum()
df['Description'].nunique()
# tane essiz urun var

df['Description'].value_counts().head()
# urunler faturalara kacar defa konu oldu?

df.groupby('Description').agg({'Quantity': 'sum'}).sort_values('Quantity', ascending=False).head()
# hangi urunden kacar tane satildi?

df['Invoice'].nunique()
# fatura sayisi

df['Total_Price'] = df['Quantity'] * df['Price']
# urunlerin toplam kazanci

df.groupby('Invoice').agg({'Total_Price': 'sum'}).head()
# fatura basina odenen para

# 3-) DATA PREPARATION

df.shape
df.isnull().sum()
# Customer ID olmazsa olmaz oldugundan ve desc verisi gormezden gelinebilecek miktarda oldugundan:

df.dropna(inplace=True)

df.describe().T
# goruldugu uzere total price da '-' veriler var. Bunun nedei iadeler olabilir.

df = df[~df['Invoice'].str.contains('C', na=False)]
# basinda 'C' olanlar iptal edilmmis faturalar oldugundan onlarin disindakileri sectik.


# CALCULATING RFM METRICS
# recency, Frequency, Monetary

# veri eski tarihli oldugundanson kesilen fatura tarihinden iki gun sonrasini kaydedelim.
# Bu fark alma islemlerinde kolaylik saglayacak

import datetime as dt

df['InvoiceDate'].max()
today_date = dt.datetime(2010, 12, 11)

rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda InvoiceDate: (today_date - InvoiceDate.max()).days,
                                     'Invoice': lambda  Invoice: Invoice.nunique(),
                                     'Total_Price': lambda  Total_Price: Total_Price.sum()})

rfm.head()

rfm.columns = ['Recency', 'Frequency', 'Monetary']

rfm.describe().T
# min degerleri 0 olan monetery leri gorduk, o gereksizleri ucur.

rfm = rfm[rfm['Monetary'] > 0]

# CALCULATING RFM SCORES

rfm['Recendary_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
# degerleri kucukten buyuge siralar ve labels degerlerini sirasiyla atar. !!!!!!!

rfm['Monetary_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

# rfm['Frequency_Score'] = pd.qcut(rfm['Frequency'], 5, labels=[1,2,3,4,5])
#  ValueError bize cok fazla tekrar eden deger oldugu icin hata verdi, bu problemi asagidaki yontemle cozuyoruz.
rfm['Frequency_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])

rfm.head()

# RFM_SCORE degiskenini olusturalim

rfm['RFM_SCORE'] = rfm['Recendary_Score'].astype(str) + rfm['Frequency_Score'].astype(str)
rfm.head()

# sampiyon musterilerimizi gormek istersek

rfm[rfm['RFM_SCORE'] == '55']

# RFM SEGMENTLERININ OLUSTURULMASI (CREATING & ANALYSING RFM SEGMENTS)

rfm.head()

# regex kullaniyoruz. arastir.

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm['SEGMENTS'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)

rfm.head(20)

rfm['SEGMENTS'].head(20)

rfm[['SEGMENTS', 'Recency', 'Frequency', 'Monetary']].groupby('SEGMENTS').agg(['mean', 'count'])
# SEGMENTLERI BETIMLEDIK VE YORUMLAMAYA MUSAIT HALE GETIRDIK.

rfm.to_csv('MIUUL/CRM_Analytics/rfm.csv')

