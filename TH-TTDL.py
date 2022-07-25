import pandas as pd
df=pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
df

# Để đơn giản ta thực hiện lọc tập dữ liệu ban đầu theo các thuộc tính sau
df = df[['join_month', 'join_day','join_year','shop_location','rating_bad','rating_good','rating_normal']]
df

# Tạo cột 'rating' tính điểm cho mỗi cửa hàng dựa vào thông tin các cột rating_bad, rating_good, rating_normal
# theo công thức sau: rating = rating_good *2 + rating_normal - rating_bad*3

df['rating'] = df['rating_good'] * 2 + df['rating_normal'] - df['rating_bad'] * 3
df

# ghép 3 cột join_month, join_day, join_year thành cột mới có tên 'date' nhận giá trị có dạng: "join_month join_day,join_year"

df['date'] = df['join_month'] + " " + df['join_day'].astype(str) + "," + df['join_year'].astype(str)
df

# Thêm cột new có giá trị True nếu join_year = 2021 và False trong trường hợp còn lại.
df['new'] = df['join_year'] == 2021
df

# Nếu có 2 lựa chọn ta sử dụng np.where
# Thêm cột rate có giá trị good nếu rating_good >= 50000,  bad trong trường hợp còn lại

import numpy as np
df['rate'] = np.where(df['rating_good'] >= 50000,'good','bad' )
df

# Nếu có nhiều hơn 2 lựa chọn ta sử dụng np.select
# Thêm cột flag tặng cờ cho các cửa hàng, flag nhận các giá trị như sau:
# blue khi rating_good >= 30000 và rating_bad <= 100
# yellow khi 10000 <= rating_good < 30000 và 100 < rating_bad <= 1000
# red khi rating_good < 10000
# black đối với các trường hợp còn lại

conditions = [(df['rating_good'] >= 30000) & (df['rating_bad'] <= 100),
              (df['rating_good'] >= 10000) & (df['rating_good'] < 30000) & (df['rating_bad'] <= 1000) & (df['rating_bad'] > 100),
              (df['rating_good'] < 10000)]
choices = ['blue', 'yellow','red']
df['flag'] = np.select(conditions, choices, default='black')
df

