import pandas as pd
df=pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
df
# Để đơn giản ta thực hiện lọc tập dữ liệu ban đầu theo các thuộc tính sau
df = df[['date_collected','shop_location','response_time']]
df
# Tách cột shop_location thành 2 cột District và City

df['District']=df['shop_location'].str.split(',').str[0]
df['City']=df['shop_location'].str.split(',').str[1]
df

# Tách cột date_collected thành 3 cột Day, Month, Year

df['Day']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.day
df['Month']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.month
df['Year']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.year
df

# Tách cột response_time thành 3 cột Hour, Minute, Second
df['Hour']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.hour
df['Minute']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.minute
df['Second']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.second
df