from pymongo import MongoClient

connection = "mongodb://localhost:27017"
client = MongoClient(connection)
db = client.guihelper
collection = db.inputs

class database:

    def connect(coll):
        global collection
        collection = db[coll]

    def drop(coll):
        db[coll].drop()
        
    def write(id, device, key, state, x, y, time):
        input = {"_id":id, "device":device, "key":key, "state":state, "x":x, "y":y, "time":time}
        collection.insert_one(input)

    def read():
        return collection.find({})
    
    def read_row(id):
        return collection.find({'_id':id})

    def update_collections():
        collections = db.list_collection_names()
        collections.sort()
        return collections
    
#input = {"device":'keyboard', "key":"enter", "state":"pressed", "time":"00:00"}