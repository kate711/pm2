# -*- coding: utf-8 -*-
import pandas as pd
# 使用 read_csv 方法读取
csv_data = pd.read_csv('D:/pythonfile/pythonbooksamples/chapter2/csv_data.csv',names=['col1','col2','col3','col4','col5'])
# print csv_data

# 使用 read_fwf 方法读取   基于固定宽度
fwf_data = pd.read_fwf('D:/pythonfile/pythonbooksamples/chapter2/fwf_data',widths=[5,5,5,5],names=['col1','col2','col3','col4'])
# print fwf_data

#使用 read_table 方法读取   基于分隔符号
table_data = pd.read_table('D:/pythonfile/pythonbooksamples/chapter2/table_data.txt',sep=';',names=['col1','col2','col3','col4','col5'])
print table_data


