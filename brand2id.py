# -*- coding: cp936 -*-
import os
import pymysql
db = pymysql.connect(host   = 'localhost',
                     user   = 'root',
                     passwd = 'root',
                     db     = 'car')
db.set_charset('utf8')
cursor=db.cursor()
brandid=0
sql="SELECT brand from carbrand ORDER BY id ASC"
res=cursor.execute(sql)
res=cursor.fetchall()
path = 'D:\scrapy_project\logo'
#print(format(res[0]).replace("('", '').replace("',)", ''))
for file in os.listdir(path):
    if file.find(format(res[brandid]).replace("('", '').replace("',)", '')):
        oldname=format(res[brandid]).replace("('", '').replace("',)", '')+".jpg"
        brandid = brandid + 1
        newname=format(brandid)+".jpg"
        print(oldname+"      "+newname)
        os.rename(os.path.join(path,oldname),os.path.join(path,newname))
        #     newname=file+'rsfdjndk.jpg'
        #     os.rename(os.path.join(path,file),os.path.join(path,newname))
        #     print (file,'ok')
#        print file.split('.')[-1]
#123