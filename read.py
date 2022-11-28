import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb+srv://vigneshramperumal:<password>@cluster0.uukk3p9.mongodb.net/test")

db = client["test_learning"]

col = db["test_collection"]

# READ ALL DATA IN COLLECTIONS
read_data = col.find()

for data in read_data:
    pprint(data)

# READ DATA USING WHERE CONDITION

condition_data = col.find({"job_role":"Manager"})

pprint(condition_data)

# READ ALL DATA WITH LIMIT 

read_limit =  col.find().limit(2)
for data in read_limit:
    pprint(data)

# SORTING THE DATA
sorting_data = col.find().sort("name",1) # 1 ASC -1 DESC
for data in sorting_data:
    pprint(sorting_data)

# SKIP Values
skip_data = col.find().skip(1)
for data in skip_data:
    pprint(data)