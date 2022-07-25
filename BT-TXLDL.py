import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
df=pd.read_csv('Credit_Scoring.csv')
print(df.info())
print(df.describe())
df1=df.isna()
print(df1)
df=df.fillna(0)
print(df.info())
sns.boxplot(x=df['SeriousDlqin2yrs'])
plt.show()
sns.boxplot(x=df['RevolvingUtilizationOfUnsecuredLines'])
plt.show()
# sns.boxplot(x=df['age'])
# plt.show()
# sns.boxplot(x=df['NumberOfTime30-59DaysPastDueNotWorse'])
# plt.show()
# sns.boxplot(x=df['DebtRatio'])
# plt.show()
# sns.boxplot(x=df['MonthlyIncome'])
# plt.show()
# sns.boxplot(x=df['NumberOfOpenCreditLinesAndLoans'])
# plt.show()
# sns.boxplot(x=df['NumberOfTimes90DaysLate'])
# plt.show()
# sns.boxplot(x=df['NumberRealEstateLoansOrLines'])
# plt.show()
# sns.boxplot(x=df['NumberOfTime60-89DaysPastDueNotWorse'])
# plt.show()
# sns.boxplot(x=df['NumberOfDependents'])
# plt.show()
Q1 = df['RevolvingUtilizationOfUnsecuredLines'].quantile(0.25)
Q3 = df['RevolvingUtilizationOfUnsecuredLines'].quantile(0.75)
IQR = Q3 - Q1
df1 = df
df1['outlier'] = ~((df['RevolvingUtilizationOfUnsecuredLines'] < (Q1 - 1.5*IQR)) | (df['RevolvingUtilizationOfUnsecuredLines'] > (Q3 + 1.5*IQR)))
# xóa phần tử ngoại lai
df1 = df1[df1['outlier'] == True]
sns.boxplot(x=df1['RevolvingUtilizationOfUnsecuredLines'])
plt.show()
# chia thành 4 khoảng giá trị có độ dài bằng nhau
cats = pd.cut(df1['RevolvingUtilizationOfUnsecuredLines'], 4)
print(cats)
a=pd.value_counts(cats)
print(a)
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
df2 = df
df2['outlier'] = ~((df['age'] < (Q1 - 1.5*IQR)) | (df['age'] > (Q3 + 1.5*IQR)))
df2 = df2[df2['outlier'] == True]
cats = pd.cut(df2['age'], [0, 30, 40, 50, 80, 150])
print(cats)
b=pd.value_counts(cats)
print(b)