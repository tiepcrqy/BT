import pandas as pd
import matplotlib.pyplot as plt
d=pd.read_csv("FoodPrice_in_Turkey.csv")

# ##Vẽ các biểu đồ cột so sánh giá Milk (powder, infant formula) và Fuel (gas) tháng 12 cuối năm năm 2019 của Ankara, Istanbul, Izmir và National Average.
# d11 = d[(d['Year'] == 2019) & (d['Month'] == 12) & (d['ProductName'] == 'Milk (powder, infant formula) - Retail')].reset_index()
# d12 = d[(d['Year'] == 2019) & (d['Month'] == 12) & (d['ProductName'] == 'Fuel (gas) - Retail')].reset_index()
# data1 = pd.DataFrame({'x': d11['Place'], 'Milk': d11['Price'], 'Gas': d12['Price']})
# data1.plot(x = 'x', y = ['Milk', 'Gas'], kind = 'bar')
# plt.title('Milk and Gas Price in 12/2019', fontsize = 16, color = 'r')
# plt.xlabel('Place', fontsize = 14)
# plt.ylabel('Price', fontsize = 14)

##Vẽ các biểu đồ đường phân tích xu hướng giá gạo (Rice-Retail), giá Fuel (gas) trung bình cả nước (National Average) trong năm 2016, 2018, 2019 tại Thổ Nhĩ Kì.
##Vẽ biểu đồ Scatter phân tích mối liên quan giữa giá gạo và giá gas trung bình quốc gia (National Average) tại Thổ Nhĩ Kì các năm 2016, 2018, 2019.

d21 = d[(d['Place'] == 'National Average') & (d['Year'] == 2016) & (d['ProductName'] == 'Rice - Retail')]
d22 = d[(d['Place'] == 'National Average') & (d['Year'] == 2016) & (d['ProductName'] == 'Fuel (gas) - Retail')]
d23 = d[(d['Place'] == 'National Average') & (d['Year'] == 2018) & (d['ProductName'] == 'Rice - Retail')]
d24 = d[(d['Place'] == 'National Average') & (d['Year'] == 2018) & (d['ProductName'] == 'Fuel (gas) - Retail')]
d25 = d[(d['Place'] == 'National Average') & (d['Year'] == 2019) & (d['ProductName'] == 'Rice - Retail')]
d26 = d[(d['Place'] == 'National Average') & (d['Year'] == 2019) & (d['ProductName'] == 'Fuel (gas) - Retail')]


fig, ax = plt.subplots(3, 2)
ax[0][0].plot(d21['Month'], d21['Price'], marker = '*', label = 'Rice-2016')
ax[0][0].plot(d22['Month'], d22['Price'], marker = 's', label = 'Gas-2016')
ax[0][0].set_ylabel('Price')
ax[0][0].set_xticklabels([])
ax[0][0].set_title('2016')

ax[1][0].plot(d23['Month'], d23['Price'], marker = '*', label = 'Rice-2018')
ax[1][0].plot(d24['Month'], d24['Price'], marker = 's', label = 'Gas-2018')
ax[1][0].set_ylabel('Price')
ax[1][0].set_xticklabels([])
ax[1][0].set_title('2018')

ax[2][0].plot(d25['Month'], d25['Price'], marker = '*', label = 'Rice')
ax[2][0].plot(d26['Month'], d26['Price'], marker = 's', label = 'Gas')
ax[2][0].set_ylabel('Price')
ax[2][0].set_xlabel('Month')
ax[2][0].legend()
ax[2][0].set_title('2019')

ax[0][1].scatter(d21['Price'], d22['Price'])
ax[0][1].set_title('2016')
ax[0][1].set_ylabel('Rice')
ax[0][1].set_xticklabels([])

ax[1][1].scatter(d23['Month'], d24['Price'])
ax[1][1].set_title('2018')
ax[1][1].set_xticklabels([])

ax[2][1].scatter(d25['Month'], d26['Price'])
ax[2][1].set_title('2019')
ax[2][1].set_xlabel('Gas')
plt.show()
