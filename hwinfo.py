# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:39:57 2021

@author: KIT

"""
import pandas as pd
import json
x=[]
f= open(r'/etc/ansible/ansible-code/final1.json','r')
j=open(r'/etc/ansible/ansible-code/final7.json','w')
data=f.read()
jsonObj=json.loads(data,strict=False)
j.write("{")
for element in jsonObj:
    for i in range(30):
        try:
            
            if str(i) in element:
                ac=element[str(i)]['backing_filename'].split('/')
                ac=str(ac[0]).split(']')[1]
                a="{\"summary\":\""+element[str(i)]['summary']+"\""
                
                b=",\"hdcount\":\""+element[str(i)]['label']+"\"}"
                
                j.write("\""+str(ac)+"\":"+str(a)+str(b)+",")
        except:
            pass

j.write("---")
j.close()
f.close()
j=open(r'/etc/ansible/ansible-code/final7.json','rt')
h=j.read()
h=h.replace(",---","}")
j.close() 
m=open(r'/etc/ansible/ansible-code/final7.json','wt')
m.write(h)
m.close()
writer = pd.ExcelWriter('/etc/ansible/ansible-code/DATAdisk.xlsx', engine='xlsxwriter')
#pd.read_json('etc\\ansible\\ansible-code\\final6.json',typ='series').to_excel('etc\\ansible\\ansible-code\\DATAdisk.xlsx')
pd.read_json('/etc/ansible/ansible-code/final7.json',typ='series').to_excel(writer,sheet_name="storage_info")

pd.read_csv('/etc/ansible/ansible-code/final1.csv').to_excel(writer,sheet_name="hwsummary")
writer.save()
"""
with open('c://1/data1.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame({'count': data})

df.to_excel('c:\\1\DATAFILE1.xlsx')

"""