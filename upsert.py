import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["test_learning"]

col = db["test_collection"]

# UPSERT is UPDATE + INSERT 

update_query = {"$set":{"Salary":"15 LPA","MailID":"vickeyram2@gmail.com"}}

condition_query = {"name":"Vigneshram"}

col.update(condition_query,update_query,upsert=True)