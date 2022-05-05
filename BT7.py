import pandas as pd
df=pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")
# print (df)
# Lọc dữ liệu lấy một cột theo tên cột
# Dùng filter
# df1=df.filter(["shop_location"])
# Truyền trực tiếp
df1=df[["shop_location"]]
# print(df1)
# df=df.groupby("name")["follower_count"].mean()
df=df.groupby(["join_year","shop_location"])[["rating_bad","rating_good"]].max()
print (df)

