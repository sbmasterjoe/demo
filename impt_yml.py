# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 07:05:55 2021

@author: KIT
"""


#import numpy as np
import xlrd
#import openpyxl
#import pandas
data = xlrd.open_workbook('./DATAFILE1.xls')
#data=pandas.read_excel('./DATAFILE1.xlsx',engine='openpyxl')
#sheet_names = data.sheet_names()


sheet1_object = data.sheet_by_name(sheet_name="Sheet1")

sheet1_is_load = data.sheet_loaded(sheet_name_or_index="Sheet1")
#print(sheet1_is_load) 
a=[1,2,3,4,5,6]
cell_info = sheet1_object.cell(rowx=2, colx=1)
#print(cell_info)   



all_row_values = sheet1_object.row_values(rowx=2)
#print(all_row_values) 

all_col_values = sheet1_object.col_values(colx=1)
#print(all_col_values)

        # 结果: text:'m'
f=open(r'/etc/ansible/ansible-code/abc.yml','w')
f.write('---\n')
f.write("data:"+str(all_col_values)+'\n')
f.close() 
