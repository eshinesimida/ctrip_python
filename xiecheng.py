# -*- coding: utf-8 -*-
import MySQLdb
import uuid
import random

class xiechengDAO(object):
    def __init__(self,host="*********",user="******",password="123443", db="ctrip_info"
                         ):
        self.host = host
        self.db = db
        self.user = user
        self.password = password



    def savehotellink(self,listPageInfo):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,use_unicode=1,charset='utf8')
        cursor = db.cursor()
        for hotel in listPageInfo:
            try:
                    id = uuid.uuid1()
                    cursor.execute("insert IGNORE into A_ctrip(jingqu,province,href,author,ID,jingse,quwei,xingjiabi,comment,time,class)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,
                                   (hotel["jingqu"],hotel["province"],hotel["url"],hotel["author"],hotel["ID"],hotel["jingse"],hotel["quwei"],hotel["xingjiabi"],hotel["comment"],hotel["time"],hotel["class"]))
            except Exception,e:
                print hotel["url"]
        db.commit()
        cursor.close()
        db.close()

    