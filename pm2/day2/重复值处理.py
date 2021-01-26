# -*- coding: utf-8 -*-
import pandas as pd

# 生成重复数据
data1 = ['a', 3]
data2 = ['b', 2]
data3 = ['a', 3]
data4 = ['c', 2]

df = pd.DataFrame([data1,data2,data3,data4], columns=['col1', 'col2'])
print df

# 判断重复数据
isDuplicated = df.duplicated() # 判断重复记录数据
print isDuplicated

# 删除重复值
new_df1 = df.drop_duplicates()  # 删除数据记录中所有列值相同的记录
print ('------------------------------')
new_df2 = df.drop_duplicates(['col1'])   # 删除数据记录中列col1值相同的记录
new_df3 = df.drop_duplicates(['col2'])   # 删除数据记录中列col2值相同的记录
new_df4 = df.drop_duplicates(['col1','col2'])  #删除数据记录中指定列（col1,col2）值相同的记录

print new_df1
print new_df2
print new_df3
print new_df4
