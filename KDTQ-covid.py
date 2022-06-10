import pandas as pd
from scipy import stats
df=pd.read_csv("subset-covid-data.csv")

#kiểm định tương quan giữa population và cases
#Giả thiết không: Không có mối tương quan tuyến tính giữa hai biến
#Giả thiết đối: Có mối tương quan tuyến tính giữa hai biến

df1 = df.filter(['cases', 'population'])
df1 = df1.dropna()
r, pvalue = stats.pearsonr(df1.cases, df1.population)
print ("r: ", r, "; pvalue: ", pvalue)

#kiểm định tương quan giữa cases và deaths
#Giả thiết không: Không có mối tương quan tuyến tính giữa hai biến
#Giả thiết đối: Có mối tương quan tuyến tính giữa hai biến

df2 = df.filter(['cases', 'deaths'])
df2 = df2.dropna()
r, pvalue = stats.pearsonr(df2.cases, df2.deaths)
print ("r: ", r, "; pvalue: ", pvalue)