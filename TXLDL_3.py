import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
df = pd.read_csv("OnlineRetail.csv", encoding = "ISO-8859-1")
print(df.shape)
print(df.head())
print(df.info())
# kiểm tra dữ liệu bị khuyết
print(df.isna())
