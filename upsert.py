import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["test_learning"]

col = db["test_collection"]

# UPSERT is UPDATE + INSERT (IF CONDITION QUERY DATA IS AVAILABLE IT WILL BE UPDATED OR ITS NOT AVAILABLE INSERT THE VALUE)

update_query = {"$set":{"Salary":"15 LPA","MailID":"vickeyram2@gmail.com"}}

condition_query = {"name":"Vigneshram Perumal"}

x = col.update_many(condition_query,update_query,upsert=True)
print(x.modified_count, "documents updated.")