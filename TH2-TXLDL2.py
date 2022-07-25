import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
# đọc dữ liệu
df = pd.read_csv("FoodPrice_in_Turkey.csv", encoding = "ISO-8859-1")

# in ra kich thuoc du lieu
df.shape
df.head()
# mô tả dữ liệu
df.describe()
# thông tin dữ liệu
df.info()
# kiểm tra dữ liệu bị khuyết
df.isna()
# kiểm tra dữ liệu không bị khuyết
df.notna()
# xóa những dòng chứa giá trị bị khuyết
df1 = df.dropna()
df1.shape
sns.boxplot(x=df1['Price'])  # vẽ box plot cho dữ liệu ở cột Price
Q1 = df1['Price'].quantile(0.25)
Q3 = df1['Price'].quantile(0.75)
IQR = Q3 - Q1
# xác định phần tử không phải ngoại lai
df2 = df1
df2['outlier'] = ~((df1['Price'] < (Q1 - 1.5*IQR)) | (df1['Price'] > (Q3 + 1.5*IQR)))
# xóa phần tử ngoại lai
df2 = df2[df2['outlier'] == True]
sns.boxplot(x=df2['Price'])  # vẽ box plot cho dữ liệu ở cột Price
# mô tả dữ liệu
df2['Price'].describe()
# biểu đồ phân bố dữ liệu
sns.kdeplot(data=df2['Price'])
# chuẩn hóa dữ liệu với minmax scaling
scaler = MinMaxScaler()

# Chuẩn hóa dữ liệu trong df với Min max scaling ở 2 cột Price
df_s = scaler.fit_transform(df2[['Price']])
# mô tả dữ liệu sau chuẩn hóa
pd.DataFrame(df_s).describe()
# vẽ lại biểu đồ hộp
sns.boxplot(x=df_s)
# biểu đồ phân bố dữ liệu
sns.kdeplot(data=df_s)
# chuẩn hóa dữ liệu với robust scaling
scaler = RobustScaler()

# Chuẩn hóa dữ liệu trong df với Robust Scaling ở 2 cột Price
df_s = scaler.fit_transform(df2[['Price']])
# mô tả dữ liệu sau chuẩn hóa
pd.DataFrame(df_s).describe()
# vẽ lại biểu đồ hộp
sns.boxplot(x=df_s)
# biểu đồ phân bố dữ liệu
sns.kdeplot(data=df_s)
# chuẩn hóa dữ liệu với z-score scaling
scaler = StandardScaler()

# Chuẩn hóa dữ liệu trong df với StandardScaler ở 2 cột Price
df_s = scaler.fit_transform(df2[['Price']])
# mô tả dữ liệu sau chuẩn hóa
pd.DataFrame(df_s).describe()
sns.boxplot(x=df_s)
sns.kdeplot(data=df_s)
# các giá trị ở cột ProductName
df2['ProductName'].unique()
# mã hóa cột ProductName với One-hot encoder sử dụng scikit learn
encoder = OneHotEncoder()

encoded_data = encoder.fit_transform(np.asarray(df2['ProductName']).reshape(-1,1))
encoded_data.todense()
# mã hóa cột ProductName với One-hot encoder sử dụng pandas
pd.get_dummies(df2['ProductName'])
# mã hóa cột ProductName với Label encoder sử dụng scikit learn
encoder = LabelEncoder()

encoded_data = encoder.fit_transform(np.asarray(df2['ProductName']))
encoded_data
# mã hóa cột ProductName với Label encoder sử dụng pandas
df2['ProductName'].astype('category').cat.codes
df2.head()
# Rời rạc hóa dữ liệu ở cột Price

# chia thành 5 khoảng giá trị có độ dài bằng nhau
cats = pd.cut(df2['Price'], 5)
cats
# số lượng phần từ ở mỗi phần
pd.value_counts(cats)
# chia thành 5 phần có số lượng phần tử tương đương nhau
cats = pd.qcut(df2['Price'], 5)
cats
# số lượng phần từ ở mỗi phần
pd.value_counts(cats)