import pandas as pd
import numpy as np
df=pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")
df=df[["join_month","join_day","join_year","shop_location","rating_bad","rating_good","rating_normal"]]
df["rating"]=df["rating_good"]*2+df["rating_normal"]-df["rating_bad"]*3
df["date"]=df["join_month"]+" "+df["join_day"].astype(str)+","+df["join_year"].astype(str)
df["new"]=df["join_year"]==2021
df["rate"]=np.where(df["rating_good"]>=50000,"good","bad")
conditions = [(df['rating_good'] >= 30000) & (df['rating_bad'] <= 100),
              (df['rating_good'] >= 10000) & (df['rating_good'] < 30000) & (df['rating_bad'] <= 1000) & (df['rating_bad'] > 100),
              (df['rating_good'] < 10000)]
choices = ['blue', 'yellow','red']
df['flag'] = np.select(conditions, choices, default='black')
df=df[df["join_month"]=="September"].count()
df=df[df["join"]]
print(df)


