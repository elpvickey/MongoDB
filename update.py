import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["test_learning"]

col = db["test_collection"]


# Update SINGLE DATA
col.update_one({"job_role":"Manager"},{"$set":{"Salary":"25 LPA"}})

# Want to ADD new KEY VALUE
col.update_one({"job_role":"Manager"},{"$set":{"Experience":10}})

# ADD BOOLEAN FIELD
col.update_one({"job_role":"Manager"},{"$set":{"Eligible":True}})
col.update_many({},{"$set":{"Eligible":True}})

# Update MULTIPLE DATA
col.update_many({"job_role":"Developer"},{"$set":{"Salary":"12 LPA"}})