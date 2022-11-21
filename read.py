import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["test_learning"]

col = db["test_collection"]

# READ ALL DATA IN COLLECTIONS
read_data = col.find()

for data in read_data:
    print(data)

# READ DATA USING WHERE CONDITION

condition_data = col.find({"job_role":"Manager"})

print(condition_data)

# READ ALL DATA WITH LIMIT 

read_limit =  col.find().limit(2)
for data in read_limit:
    print(data)

# SORTING THE DATA
sorting_data = col.find().sort("name",1) # 1 ASC -1 DESC
for data in sorting_data:
    print(sorting_data)