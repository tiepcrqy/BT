import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('FoodPrice_in_Turkey.csv')
df.info()

#liệt kê tên các sản phẩm
product_names=list(df['ProductName'].unique())
print(product_names)

df_rice=df.loc[(df.ProductName=='Rice - Retail')&(df.Year==2019)]
print("so luong ban ghi cua gao nam 2019:"+str(df_rice.shape[0]))

# #với mức ý nghĩa 5% kiểm định giả thuyết giá bán gạo trung bình năm 2019 là 10 Lira/kg
# df_rice.Price.hist()
# plt.show()
# print(stats.ttest_1samp(df_rice.Price,9.5))

# #Với mức ý nghĩa 5% hãy kiểm định giả thuyết: Giá bột mỳ và giá gạo ở Turkey năm 2019 là bằng nhau
df_wheat = df.loc[(df.ProductName== 'Wheat flour - Retail') & (df.Year == 2019)]
# print ('Số lượng bản ghi của bột mỳ năm 2019: '+str(df_wheat.shape[0]))
# # Tạo boxplot so sánh phân bố của bột mỳ vào gao
price = {'rice': list(df_rice["Price"]), 'wheat': list(df_wheat['Price'])}
df_price = pd.DataFrame(price)
# sns.boxplot(data=df_price)
# plt.show()
# print(stats.ttest_ind(price['rice'], price['wheat'], equal_var=False))

# xóa những biến không cần thiết
del (df_rice, df_price, df_wheat, price)
# chuyển đổi dữ liệu ngày tháng
df['time'] =  pd.to_datetime(df['Year'].astype(str) + '/'+df['Month'].astype(str))
# thực hiện tính toán và vẽ giá trà, caffe theo tháng
df_Tea_all = df.loc[(df.ProductName == 'Tea - Retail')]
df_Tea_all_mean_by_month = df_Tea_all.groupby('time')['Price'].mean()
plt.plot_date(df_Tea_all_mean_by_month.index, df_Tea_all_mean_by_month.values, linestyle ='solid')

df_Coffee_all = df.loc[(df.ProductName == 'Coffee - Retail')]
df_Coffee_all_mean_by_month = df_Coffee_all.groupby('time')['Price'].mean()
plt.plot_date(df_Coffee_all_mean_by_month.index, df_Coffee_all_mean_by_month.values, linestyle ='solid')
plt.show()