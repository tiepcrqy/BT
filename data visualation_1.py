#Thực hành tạo biểu đồ đơn giản
# import matplotlib.pyplot as plt
#
# x = [2, 4, 6, 8, 10]
# y = [12.2, 16.3, 20.5, 25.4, 31.2]
# plt.plot(x, y)
# plt.title('This is Title')
# plt.xlabel('X attribute')
# plt.ylabel('Y attribute')
# plt.title('This is Title')
# plt.title('This is Title', fontdict={'fontsize': 12,
#                                      'fontweight': 8,
#                                      'verticalalignment': 'baseline',
#                                      'horizontalalignment': 'left'})
# plt.xlabel('X attribute')
# plt.ylabel('Y attribute')
# plt.xlabel('X attribute', fontsize=14, color='red')
# plt.ylabel('Y attribute', fontsize=18, color='blue')
# plt.plot(x, y, color='red', linewidth=2, linestyle='dashed', marker = 'o')
# plt.show()

##Biểu đồ Histogram
import matplotlib.pyplot as plt
import numpy as np
gaussian_numbers = np.random.normal(size=10000)
plt.hist(gaussian_numbers, bins = 35)
plt.title('Histogram Example', fontsize = 14)
plt.show()

##Biểu đồ cột
import matplotlib.pyplot as plt
x = ['2017', '2018', '2019', '2020', '2021']
y = [234, 389, 333, 402, 451]
plt.bar(x, y)
plt.title('Sản Lượng Vải Xuất Khẩu', fontsize = 14)
plt.xlabel('Năm', fontsize = 12)
plt.ylabel('Sản lượng (tấn)', fontsize = 12)
plt.show()


##Biểu đồ tròn
import matplotlib.pyplot as plt
labels = ['Gạo', 'Gas', 'Thịt', 'Trứng', 'Sữa']
sizes = [443, 292, 231, 110, 20]
plt.pie(sizes, labels = labels)
plt.title('Sản lượng xuất khẩu năm 2021', fontsize = 14)
plt.show()