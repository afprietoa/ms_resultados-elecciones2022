import pymongo
import certifi
ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://afprietoa:aO73ir9fa648@misiontic.rrhvypu.mongodb.net/results_db?retryWrites=true&w=majority",
    tlsCAFILE=ca
)
db = client.test
print(db)

data_base = client['results_db']
collection = data_base.get_collection('table')
print(collection.find())