import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import scipy as sp
from  sklearn.metrics import mean_absolute_percentage_error
from scipy.stats import f_oneway

# 1. Chọn các feature ảnh Hưởng
# 2. Xây dựng mô hình
# 3. Đánh giá trên MAPE
# 22,Xây dựng mô hình dự báo giá bán nhà mặt phố của HN,Quận Hà Đông

#df = pd.read_csv("RoadSurfaceHouseTrading.csv")
#print(df.head())
#df.info()
#df.describe()

#Truy cập dữ liệu Quận Hà Đông
#df=df.drop(["id_thanh_pho","ten_thanh_pho","id_quan","id_duong","id_phuong"], axis=1)
#df1=df.loc[df.ten_quan=="Quận Hà Đông"]
#print(df)
#df1.to_csv('Quận_Hà_Đông.csv')
#df1.head()

df = pd.read_csv("Quận_Hà_Đông.csv")
df.info()
df.fillna(0)
print(df)

