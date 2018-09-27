from pymongo import MongoClient
from random import randint

conn = MongoClient('localhost',27017)

db = conn.grade

myset = db.class1

cursor = myset.find()
for i in cursor:
    myset.update({'_id':i['_id']},
        {'$set':{'score':{'chinese':randint(60,100),
        'math':randint(60,100),
        'english':randint(60,100)}}})

l1=[{'$group':{"_id":'$sex','num':{'$sum':1}}}]
l2 = [{'$match':{'sex':'m'}},
       {'$project':{'_id':0,'name':1,'score.chinese':1}}]
l3 = [{'$match':{'sex':'w'}},
      {'$sort':{'score.english':-1}},
      {'$project':{'_id':0,'name':1}}]
cursor = myset.aggregate(l3)
for i in cursor:
    print(i)

conn.close()