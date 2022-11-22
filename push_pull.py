import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["test_learning"]

col = db["test_collection"]

# PUSH - Append the data 

push_query = {"$push":{"Skill_Set":"JavaScript"}}

condition_query = {"name":"Saravanan"}

x = col.update_many(condition_query,push_query,upsert=True)

print(x.modified_count,"documents Updated")

# PULL - DELETE the data

pull_query = {"$pull":{"Skill_Set":"Angular"}}

y = col.update_many(condition_query,pull_query,upsert=True)

print(y.modified_count,"documents Updated")