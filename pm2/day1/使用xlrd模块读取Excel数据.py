#  -*- coding: utf-8 -*-
import xlrd
# 打开文件
xlsx = xlrd.open_workbook('D:/pythonfile/pythonbooksamples/chapter2/demo.xlsx')

# 查看所有 sheet列表
print ('All sheets: %s' % xlsx.sheet_names())
print ('-------------------------------------')

# 查看 sheet1 的数据概况
sheet1 = xlsx.sheets()[0]     # 获得第一张sheet，索引从0开始
sheet1_name = sheet1.name     # 获得名称
sheet1_cols = sheet1.ncols    # 获得列数
sheet1_nrows = sheet1.nrows   # 获得行数
print (('sheet1 name: %s\nsheet1 cols: %s\nsheet1 rows: %s') % (sheet1_name,sheet1_cols,sheet1_nrows))

print ('------------------------------------')

sheet1_nrows4 = sheet1.row_values(4)   # 获得第4行数据
sheet1_cols2 = sheet1.col_values(2)    # 获得第2列数据
cell23 = sheet1.row(2)[3].value        # 查看第3行第4列数据

print (('Row 4 : %s\nCol 2 : %s\nCell 1 : %s\n') % (sheet1_nrows4,sheet1_cols2,cell23))

print ('-------------------------------------')

for i in range(sheet1_nrows):          # 逐行打印sheet1数据
    print (sheet1.row_values(i))




