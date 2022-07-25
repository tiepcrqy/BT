import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('GDPlist.csv',encoding='ISO-8859-1')
print(df.info())
plt.hist(df['GDP (millions of US$)'])
plt.title("Phân bố GDP")
plt.xlabel("GDP")
plt.ylabel("QG")
plt.show()
df1=df.groupby('Continent')['GDP (millions of US$)'].sum()
df2 = df.sort_values('GDP (millions of US$)',ascending = False)
print(df1)
print(df2)
