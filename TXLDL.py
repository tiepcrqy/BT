import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
# a=np.array(a)
# Q1=np.quantile(a,0.25)
# Q3=np.quantile(a,0.75)
# IQR=Q3-Q1
# np.quantile

# a=[80,71,79,61,78,73,77,74,76,75,160,79,80,78,75,78,86,80, 82,69,100,72,74,75,180,72,71,12]
# a=np.array(a)
# mean=np.mean(a)
# std=np.std(a)

# normaliez=(a-mean)/std
# print(normaliez)
#
# plt.plot(normaliez)
# plt.show()

boston = load_boston()
x = boston.data
y = boston.target
columns = boston.feature_names

df = pd.DataFrame(x, columns=columns)
df["price"] = y
corr = df.corr()

target = corr.sort_values(by="price", ascending=False)
print(target.head())


