from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)
#创建数据库对象
db = conn.stu

#创建集合对象
myset = db.class4

#数据操作
# print(dir(myset))
#插入一条数据
# myset.insert({'name':'张铁林','king':'乾隆'})
#插入多条数据
# myset.insert([{'name':'张国立','king':'康熙'},\
#     {'name':'陈道明','king':'康熙'}])
# myset.insert_many([{'name':'唐国强','king':'雍正'},{'name':'陈建斌','king':'雍正'}])
# myset.insert_one({'name':'郑少秋','king':'乾隆'})
# myset.save({'_id':1,'name':'聂远','king':'乾隆'})
# myset.save({'_id':1,'name':'吴奇隆','king':'四爷'})

#查找
# cursor = myset.find({},{'_id':0})
# for i in cursor:
#     print(i['name'],'----',i['king'])

# dic = myset.find_one({},{'_id':0})
# print(dic)
#操作符使用
myset1 = db.class0

# cursor = myset1.find({'$or':[{'gender':'w'},{"age":{'$lt':18}}]},{'_id':0})
# for i in cursor:
#     print(i)

#获取下一条记录
# print(cursor.next())
# print(cursor.next())
#跳过前1条显示后三条
# for i in cursor.skip(1).limit(3):
#     print(i)

# for i in cursor.sort([('age',1),('name',-1)]):
#     print(i)


#修改
# myset1.update({'name':'idom'},{'$unset':{'tel':''}})
# myset1.update({'name':'Tom'},{'$set':{'age':18}},multi= True)
# myset.update({'name':'梁家辉'},{'$set':{'king':'咸丰'}},upsert =True)
# myset.update_many({'name':'张家辉'},{'$set':{'king':'咸丰'}},upsert =True)

#删除
# myset.remove({'king':'四爷'})
# #只删除一个符合条件的文档
# myset.remove({'king':'咸丰'},multi =False)

# myset1.remove({'gender':{'$exists':False}})
#复合操作
#查找ｋｉｎｇ＝咸丰并删除
# print(myset.find_one_and_delete({'king':'咸丰'},multi =False))

#关闭连接
conn.close()