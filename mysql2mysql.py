import pymysql
# d={1:'Michael',2:'Bob',3:'Tracy'}
# print(d[1])
brand={}
brandid=1
typeid=1
db = pymysql.connect(host   = 'localhost',
                     user   = 'root',
                     passwd = 'root',
                     db     = 'car')
db.set_charset('utf8')
cursor2=db.cursor()                                             #第二个标记
cursor = db.cursor()
cursor3=db.cursor()# 获得数据库游标
#获取所有brandname
sql ="SELECT * from carbrand1"
sql_inserttype="INSERT INTO cartype(id,type,brandId)VALUES(%s,%s,%s)"
sql_insertbrand="INSERT INTO carbrand(id,brand,pinyin)VALUES(%s,%s,%s)"
res=cursor.execute(sql)
res = cursor.fetchall()
#插入Brand表
i=0#遍历标记
while(i<len(list(res))):
    #转化格式brand[brandname:brandid]
    brandName = res[i][0]
    if(brand.get(brandName)==None):
        pinyin=res[i][1]
        brand[format(brandName).replace("('","").replace("',)","")]=brandid
        value2 = (brandid,brandName,pinyin)
        brandid = brandid + 1
        cursor3.execute(sql_insertbrand,value2)
        print(value2)
        db.commit()
    i = i + 1


#插入cartype表
res=cursor.execute(sql)
res = cursor.fetchall()
# 生成type表
i=0#遍历标记
while(i<len(list(res))):
    type=res[i][2]
    brandName=res[i][0]
    brandid=brand.get(brandName)
    value1 = (typeid, type, brandid)
    cursor2.execute(sql_inserttype, value1)
    #循环条件
    typeid=typeid+1
    i=i+1
    db.commit()
    print(value1)


