import pymongo

client = pymongo.MongoClient("mongodb+srv://vigneshramperumal:<password>@cluster0.uukk3p9.mongodb.net/test")

db = client["test_learning"]

col = db["test_collection"]

insertData = [
                {"name":"Vignesh","job_role":"Developer","office_name":"XYZ","Salary":"6.2 LPA"},
                {"name":"Saravanan","job_role":"Tester","office_name":"XYZ","Salary":"8.2 LPA"}
                
             ]
# INSERT SINGLE DATA
col.insert_one({"name":"Deepak","job_role":"Manager","office_name":"XYZ","Salary":"18 LPA"})

# INSERT MULTIPLE DATA
col.insert_many(insertData)