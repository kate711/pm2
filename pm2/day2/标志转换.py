# —*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import OneHotEncoder   #导入OneHotEncoder

#生成数据
df = pd.DataFrame({'id': [3566841,6541227,3512441],
                   'sex': ['male','Female','Female'],
                   'level': ['high','low','middle']})

print df

print ('----------------------------1')

# 自定义转换过程
# 复制一份新的数据框用来存储转换结果
df_new = df.copy()

# 循环读出每个列的索引值和列名
for col_num,col_name in enumerate(df) :

    col_data = df[col_name]           # 获得每列数据
    col_dtype = col_data.dtype        # 获得每列dtype类型
    if col_dtype == 'object':         # 如果dtype类型是object(非数值型)，执行条件
        df_new = df_new.drop(col_name,1)   # 删除数据框中要进行标志转换的列
        value_sets = col_data.unique()     # 获取分类和顺序变量唯一的值域
        print value_sets
        print ('---------------------2')
        for value_unique in value_sets:    # 获取分类和顺序变量中的每一个值

            col_name_new = col_name + '_' + value_unique   # 创建新的列名，使用‘原标题 + 值’ 的方式命名
            col_tmp = df.iloc[:, col_num]   #  获取原始数据列
            new_col = (col_tmp == value_unique)   # 将原始数据列与每个值进行比较，相同为true，不同为false
            df_new[col_name_new] = new_col     # 为最终结果集增加新列值
print df_new                               #打印输出转换后的数据框


print ('-----------------------3')

df2 = pd.DataFrame({'id':[3566841, 6541227, 3512441],
                    'sex': [1,2,2],
                    'level': [3,1,2]})
id_data = df2.values[:, :1]                    # 获得 id 列
transform_data = df2.values[:, 1:]             # 指定要转换的列
enc = OneHotEncoder()                         # 建立模型对象
df2_new = enc.fit_transform(transform_data).toarray()       #标志转换
df2_all = pd.concat((pd.DataFrame(id_data), pd.DataFrame(df2_new)),axis=1)     # 组合为数据框
print df2_all                                                          # 打印输出转换后的数据框

print ('----------------------4')
print df_new

