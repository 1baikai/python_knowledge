#直接转换为二进制插入到数据库
from pymongo import MongoClient
import bson

conn = MongoClient('localhost',27017)
db = conn.image

myset = db.MM

#存储图片
# f = open('mm.jpg','rb')

#将图片内容转换成可存储的二进制格式
# content = bson.binary.Binary(f.read())

# myset.insert({'filename':'mm.jpg','data':content})


# #提取图片
img= myset.find_one({'filename':'mm.jpg'})
#将内容写入到本地
with open('mm.jpg','wb') as f:
    f.write(img['data'])









# f.close()
conn.close()