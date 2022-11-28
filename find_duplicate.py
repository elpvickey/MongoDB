import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb+srv://vigneshramperumal:<password>@cluster0.uukk3p9.mongodb.net/test")

db = client["test_learning"]

col = db["test_collection"]

# Find Duplicate

# db['collection_name'].aggregate([{'$group': {'_id':'$name', 'count': {'$sum': 1}}}, {'$match': {'count': {'$gt': 1}}}])

x = col.aggregate([{'$group': {'_id':'$name', 'count': {'$sum': 1}}}, {'$match': {'count': {'$gt': 1}}}])

for i in x:
    pprint(i['_id'])