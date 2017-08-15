# -*- coding: cp936 -*-
import os
import pymysql
db = pymysql.connect(host   = 'localhost',
                     user   = 'root',
                     passwd = 'root',
                     db     = 'car')
db.set_charset('utf8')
cursor=db.cursor()
sql="SELECT brand from carbrand ORDER BY id ASC"
res=cursor.execute(sql)
res=cursor.fetchall()
path = 'D:\scrapy_project\image\full'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find(res[0]):
            print(res[0])
        #     newname=file+'rsfdjndk.jpg'
        #     os.rename(os.path.join(path,file),os.path.join(path,newname))
        #     print (file,'ok')
#        print file.split('.')[-1]