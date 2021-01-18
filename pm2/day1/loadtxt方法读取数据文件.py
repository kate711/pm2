# -*- coding: utf-8 -*-
import numpy as np
# 使用 loadtxt 方法读取文件
file_name = 'D:/pythonfile/pythonbooksamples/chapter2/numpy_data.txt'   #定义数据文件
data = np.loadtxt(file_name,dtype='float32',delimiter=' ')              #获取数据
# print data

# 使用load 方法读取数据文件
write_data = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
np.save('load_data.txt',write_data)  #保存为.npy的数据文件
read_data = np.load('load_data.txt.npy')
print read_data

# 使用fromfile方法读取文件
tofile_name = 'binary'     #定义导出二进制文件名
data.tofile(tofile_name)   #导出二进制文件，通过tofile方法创建1个二进制文件
fromfile_data = np.fromfile(tofile_name,dtype='float32')   #读取二进制文件
print fromfile_data

