# khai báo thư viện
import pandas as pd
from scipy import  stats
# đọc bộ dữ liệu
df = pd.read_csv("subset-covid-data.csv")
df.describe()
# lọc dữ liệu
df1 = df.filter(['cases', 'population'])
# xóa bỏ dữ liệu null
df1 = df1.dropna()
r, pvalue = stats.pearsonr(df1.cases, df1.population)
print ("r: ", r, "; pvalue: ", pvalue)
# lọc dữ liệu
df2 = df.filter(['cases', 'deaths'])
# xóa bỏ dữ liệu null
df2 = df2.dropna()
r, pvalue = stats.pearsonr(df2.cases, df2.deaths)
print ("r: ", r, "; pvalue: ", pvalue)
# tiến hành tính các khoảng tứ phân vị của population
q1, q2, q3  = df1.population.quantile(0.25), df1.population.quantile(0.5), df1.population.quantile(0.75)
# tiến hành biến đổi population
def population_order(population):
    if population < q1:
        return 1
    elif population>=q1 and population <q2:
        return 2
    elif population>=q2 and population <q3:
        return 3
    else:
        return 4

df1['population_ordinal']=df1.population.apply(population_order)
df1.head()

r, pvalue = stats.spearmanr(df1.cases, df1.population_ordinal)
print ("r: ", r, "; pvalue: ", pvalue)
