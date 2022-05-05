##Đọc bộ dữ liệu
# sử dụng thư viện pandas để làm việc với dữ liệu dạng bảng
import pandas as pd
# đọc dữ liệu, file dữ liệu thường có encoding = 'UTF-8' hoặc 'ISO-8859-1'
data=pd.read_csv('subset-covid-data.csv')
# hiển thị 5 dòng dữ liệu đầu tiên
print(data.head())
# Số lượng dòng và cột của bộ dữ liệu
print(data.info())
# Tìm hiểu xem dữ liệu được thống kê cho những ngày nào
print(data.date.value_counts())
# lọc dữ liệu nhiễu:
cleaned_data = data[data.date == '2020-04-12']
print(cleaned_data)
# Vẽ biểu đồ phân bố số lượng ca mắc mới ở các quốc gia
print ("trung bình số ca mắc mới: " + str(cleaned_data.cases.mean()))
print ("trung vị của số ca mắc mới: "+ str(cleaned_data.cases.median()))
import matplotlib.pyplot as plt
plt.hist(cleaned_data.cases, bins = 200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("số số ca mắc mới")
plt.ylabel("Số lượng quốc gia")
#Tổng số ca mắc mới, số ca tử vong ở từng châu lục
print("tổng số ca nhiễm và số ca ncủa các châu lục")
print(cleaned_data.groupby('continent')['cases','deaths'].sum())
#Top 5 quốc gia có số ca nhiễm mới cao nhất
print ("5 quốc gia có số ca nhiễm mới cao nhất")
data = data.sort_values('cases',ascending = False)
data.head(5)
#Top 5 quốc gia có số ca tử vong cao nhất
print ("5 quốc gia có số ca tử vong cao nhất")
data = data.sort_values('deaths',ascending = False)
data.head(5)