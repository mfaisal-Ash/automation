import pymongo

url=pymongo.MongoClient("mongodb+srv://Sal:admin123@sal.94xhv.mongodb.net/")
db = url["automation_config"]
col = db["test_config"]

execute_query=collection.find({})
print("concert value....>"+str(list(execute_query)))

# EXPLORER 