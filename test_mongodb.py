from pymongo import MongoClient

client = MongoClient('mongodb+srv://root:1234@mydb.vqrlsdn.mongodb.net/?retryWrites=true&w=majority')


#create schema 
db = client.test

#create document
list = db.mydata

list.insert_one({
    "name":"UB",
    "hello" : "goodmorning!!"
})

