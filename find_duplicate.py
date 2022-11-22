import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["test_learning"]

col = db["test_collection"]

# Find Duplicate

# db['collection_name'].aggregate([{'$group': {'_id':'$name', 'count': {'$sum': 1}}}, {'$match': {'count': {'$gt': 1}}}])

x = col.aggregate([{'$group': {'_id':'$name', 'count': {'$sum': 1}}}, {'$match': {'count': {'$gt': 1}}}])

for i in x:
    print(i)