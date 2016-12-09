import pymongo
import json


## importing the pymongo for the connections
##
client = pymongo.MongoClient("localhost", 27017)
db = client.test

datas=db.grades.find_one()
# for data in datas:
print(datas)
print(datas['_id'])
print(json.dumps(datas['scores']))
