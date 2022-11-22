import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["test_learning"]

col = db["test_collection"]

# REPLACE ONE IS AVAILABLE IN MONGO DB BUT REPLACEMANY IS NOT AVAILALE ALTERNATIVLY USE UPDATE_MANY WITH UPSERT TRUE

update_query = {"name":"Ram Perumal","Experience":5,"Salary":"15 LPA","MailID":"vickeyram2@gmail.com"}

condition_query = {"name":"Ram Perumal"}

x = col.replace_one(condition_query,update_query,upsert=True)
print(x.modified_count, "documents updated.")