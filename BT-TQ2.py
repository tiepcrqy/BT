import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
print(df.info())
df1=df.groupby('ProductName')['Price'].mean()
print(df1)
