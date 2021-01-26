# -*- coding: utf-8 -*-
import pandas as pd
#生成异常数据
df = pd.DataFrame({'col1': [1, 120, 3, 5, 2,12, 13],'col2': [12, 17, 31, 53, 22, 32, 43]})
print df

#通过 Z-Score方法判断异常值
#复制一个用来存储Z-score得分的数据框
df_zscore = df.copy()
#获得数据框的列名
cols = df.columns
#循环读取每列
for col in cols:
    df_col = df[col]   #得到每列的值
    z_score = (df_col - df_col.mean()) / df_col.std()  #计算每列的Z-score的得分
    df_zscore[col] = z_score.abs() > 2.2               #判断Z-score的得分是否大于2.2，如果是为TRUE，否则为false

print df_zscore


