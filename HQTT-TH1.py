import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dt=pd.read_csv("salary_data.csv")
#print(dt.tail(10))
#(dt.shape)
print(dt.describe())

##ve bieu do
# dt.plot(x="SoNamKinhNghiem", y="Luong", style="o")
# plt.title("so nam kinh nghiem-luong")
# plt.xlabel("so nam kinh nghiem")
# plt.ylabel("luong")
# plt.show()

# # vẽ biểu đồ histogram
# plt.hist(dt['Luong'],20)
# plt.show()

df_keToan = dt[dt["NganhNghe"] == "KeToan"]
df_hcnh = dt[dt["NganhNghe"] == "HCNS"]
df_sale = dt[dt["NganhNghe"] == "Sale"]

print ("Kết cấu bộ dữ liệu")
print ("Số lượng mẫu nhân viên kế toán: " + str(df_keToan.shape[0]))
print ("Số lượng mẫu nhân viên HCNH: " + str(df_hcnh.shape[0]))
print ("Số lượng mẫu nhân viên SALE: " + str(df_sale.shape[0]))

n_by_nganhNghe = dt.groupby("NganhNghe")["Luong"].mean()
print(n_by_nganhNghe)

# # Biểu đồ phân bố lương của nhân viên Kế toán
# plt.boxplot(df_keToan['Luong'])
# plt.show()

#Xây dựng model dự đoán tiền lương theo số năm kinh nghiệm
X = dt['SoNamKinhNghiem'].values.reshape(-1,1)
y = dt['Luong'].values.reshape(-1,1)
# chia bộ dữ liệu làm 2 tập train và test theo tỉ lệ 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()  # Khai báo mô hình hồi quy tuyến tính
regressor.fit(X_train, y_train) #Huấn luyện mô hình
print( "Mô hình hồi quy sẽ có dạng: Lương = a + b * số năm kinh nghiệm \n với các hệ số a và b lần lượt là")
print(regressor.intercept_)
#For retrieving the slope:
print(regressor.coef_)

y_pred = regressor.predict(X_test) # dự đoán trên số năm kinh nghiệm của bộ dữ liệu test
## tính toán R2 của model
import sklearn.metrics as metrics
from sklearn.metrics import r2_score
r2_train = r2_score(y_train, regressor.predict(X_train))
print("R2 trên tập huấn luyện của model là:" + str(r2_train))
r2_test = r2_score(y_test, y_pred)
print("R2 trên tập kiểm tra của model là:" + str(r2_test))

df = pd.DataFrame({'số năm kinh nghiệm': X_test.flatten(), 'Lương Thực tế': y_test.flatten(), 'Lương Dự báo': y_pred.flatten()})
print("\n") # xuống dòng
print("Đánh giá năng lực dự báo trung bình trên tập test")
print('Sai số dự báo trung bình:', metrics.mean_absolute_error(y_test, y_pred))
plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

# lưu trữ mô hình vào máy tính
import pickle # thư viện  giúp lưu trữ mô hình
filename = 'model.sav'
pickle.dump(regressor, open(filename, 'wb'))

# sử dụng mô hình
loaded_model = pickle.load(open(filename, 'rb'))
x = [[1],[2],[4]]
y_pred = loaded_model.predict(x)
print(y_pred)