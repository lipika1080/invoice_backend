from pymongo import MongoClient

COSMOS_CONNECTION_STRING = "mongodb://invoice143:yH9UB7hlTfoVvcZzKTWxMNMrP5Ut0soDgSFoS5q3oyg2aDrDt4oqqvERpN70Rn2wAC14GWwewGt4ACDbYSp6yw==@invoice143.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@invoice143@"

client = MongoClient(COSMOS_CONNECTION_STRING)
db = client.get_database("InvoiceDB")
collection = db["Invoices"]
