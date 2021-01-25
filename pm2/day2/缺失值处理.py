# -*- coding: utf-8 -*-
# python 数据清洗-缺失值处理
import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer     #导入Imputer库

#生成缺失数据
df =pd.DataFrame(np.random.randn(6, 4), columns=['col1','col2','col3','col4'])
df.iloc[1:2, 1] =np.nan
df.iloc[4, 3] =np.nan
print (df)

#查看哪些值缺失
nan_all = df.isnull()
print (nan_all)

#查看那些列缺失
nan_col1 = df.isnull().any()
nan_col2 = df.isnull().all()
print (nan_col1)
print (nan_col2)

#丢弃缺失值
df2 = df.dropna()  # 直接丢弃含有NA的记录
print (df2)

#sklearn将缺失值换为特定值
nan_model = Imputer(missing_values='NaN',strategy='mean',axis=0)     #建立替换规则：将值为NaN的值用均值做替换
nan_result = nan_model.fit_transform(df)    #应用模型规则
print nan_result
print ('---------------')
print (df)

#使用Pandas将缺失值替换为特定值
nan_result_pd1 = df.fillna(method='backfill')            #用后面行的值替换缺失值
nan_result_pd2 = df.fillna(method='bfill', limit=1)      #用后面的值替换缺失值，限制每列只能替换一个缺失值
nan_result_pd3 = df.fillna(method='pad')                 #用前面的值替换缺失值
nan_result_pd4 = df.fillna(0)                            #用0替换缺失值
nan_result_pd5 = df.fillna({'col2': 1.1, 'col4':1.2})    #用不同值替换不同列额的缺失值
nan_result_pd6 = df.fillna(df.mean()['col2':'col4'])     #用平均数代替，选择各自列的均值替换缺失值

print ('用后面的值替换缺失值')
print nan_result_pd1
print ('用后面的值替换缺失值，限制每列只能替换一个缺失值')
print nan_result_pd2
print ('用前面的值替换缺失值')

print nan_result_pd3
print ('用0替换缺失值')

print nan_result_pd4
print ('用不同值替换不同列额的缺失值')

print nan_result_pd5
print ('用平均数代替，选择各自列的均值替换缺失值')

print nan_result_pd6











