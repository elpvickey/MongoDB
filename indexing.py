import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["test_learning"]

col = db["test_collection"]

# Create a new indexing of any key in the document. indexing easy to scan the particular document in the collection.
x = col.create_index([("name",-1)],unique=True)
print(x)

# drop INDEX 
x = col.drop_index("name_-1")
print(x)