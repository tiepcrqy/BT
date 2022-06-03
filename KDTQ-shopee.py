import pandas as pd
from scipy import stats

df=pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")
print(df.head())

#Kiểm tra tương quan rating_star và follower_count
#Giả thuyết không: Giữa hai thuộc tính không có sự tương quan tuyến tính
#Giả thuyết đối: Giữa hai thuộc tính có sự tương quan tuyến tính

df1=df.filter(["rating_star","follower_count"])
df1=df1.dropna()
r=stats.pearsonr(df1.rating_star,df1.follower_count)
print(r)

#Kiểm tra tương quan rating_star và item_count
#Giả thuyết không: Giữa hai thuộc tính không có sự tương quan tuyến tính
#Giả thuyết đối: Giữa hai thuộc tính có sự tương quan tuyến tính

df2=df.filter(["rating_star","item_count"])
df2=df2.dropna()
r=stats.pearsonr(df2.rating_star,df2.item_count)
print(r)

#Kiểm tra tương quan is_shopee_verified và is_official_shop
#Giả thuyết không: Giữa hai thuộc tính không có sự tương quan tuyến tính
#Giả thuyết đối: Giữa hai thuộc tính có sự tương quan tuyến tính

df3=df.filter(["is_shopee_verified","is_official_shop"])
df3=df3.dropna()
r=stats.pearsonr(df3.is_shopee_verified,df3.is_official_shop)
print(r)