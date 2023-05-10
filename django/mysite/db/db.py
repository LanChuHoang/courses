from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://admin:zE33vhM48sDQd35e@nasacluster.as9mx.mongodb.net/"
)
db = client["nasa"]

te = "te"
