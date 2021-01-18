# -*- coding: utf-8 -*-
import re
import numpy
from sklearn import linear_model
from matplotlib import pyplot as plt
fn = open('D:/pythonfile/pythonbooksamples/chapter1/data.txt','r')
all_data = fn.readlines()
# print all_data
fn.close()
#创建两个空列表，用来存放自变量和因变量
x = []
y = []
for single_data in all_data:
     tmp_data = re.split('\t|\n',single_data)
     #获取每行第一个值，追加到列表x
     x.append(float(tmp_data[0]))
     y.append(float(tmp_data[1]))

#列表转为数组
x =numpy.array(x).reshape([100,1])
y =numpy.array(y).reshape([100,1])

#先通过散点图，观察数据分布
# plt.scatter(x,y)
# plt.show()

# 使用sklearn中的线性模块建模
model = linear_model.LinearRegression()
model.fit(x,y)

#获取模型的自变量系数
model_coef = model.coef_
#获取模型的截距
model_intercept = model.intercept_
r2 = model.score(x,y)
# print model_coef
# print model_intercept
# print r2

#得到线性回归方程
print ("y =" + str(model_coef) +" *x + " + str(model_intercept))

#预测，当 x = 84610

new_x = 84610
pre_y = model.predict(new_x)
print round(pre_y)


#导入库，获取数据，数据预处理，数据展示分析，数据建模，模型评估，数据预测