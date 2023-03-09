import pymongo

client = pymongo.MongoClient("mongodb+srv://rachamalla:rachamalla143.@rachamalla.eurulow.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Nagaraju",
    "surname":"Rachamalla",
    "mail_id":"rachamalla.mf@gmail.com"
}

db1 = client['mongotest']
coll = db1["test"]
coll.insert_one(d)
