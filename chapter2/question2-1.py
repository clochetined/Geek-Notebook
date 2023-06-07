import numpy as np
import pandas as pd
 
col_1 = np.array([23, 20, 15, 30, 25, 23, 19, 25, 40, 18, 34, 28])
col_2 = np.array(['男', '女', '男', '男', '女', '男', '女', '男', '女', '女', '男', '女'])
col_3 = np.array(['東京', '京都', '不明', '奈良', '新潟', '広島', '熊本', '北海道', '群馬', '不明', '神奈川', '宮城'])
col_4 = np.array([50, 75, 99, 46, 70, 68, 55, 50, 90, 87, 80, 65])

df = pd.DataFrame({'年齢':col_1,'性別':col_2,'出身':col_3,'得点':col_4})
# print(df)

# print(df[df['出身'] == '奈良'])

df = df.replace('不明', np.nan)
# df = df.dropna()
# df.fillna('東京')
df = df.replace(np.nan, '東京')
print(df)

print(df['年齢'].mean())

print(df[df['性別'] == '男'])
print(df[df['性別'] == '女'])


df_male = df[df['性別'] == '男']
df_female = df[df['性別'] == '女']

df_male_sorted = df_male.sort_values('得点', ascending=False)
df_female_sorted = df_female.sort_values('得点', ascending=False)

print(df_male_sorted.head(5))
print(df_female_sorted.head(5))


