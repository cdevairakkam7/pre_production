# This function is used to inject 
# long url 
#  mini link
#  key
# Seq

def inject_custom_mongo(long_url,usr_input):
    from pymongo import MongoClient
    from flask import render_template
    from bson.objectid import ObjectId

    cluster = MongoClient("mongodb://cdevairakkam:Amplitude20DEC!@minilinkcluster-shard-00-00-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-01-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-02-ja0tk.azure.mongodb.net:27017/test?ssl=true&replicaSet=minilinkcluster-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = cluster["links"]
    # collection = counters
    collection = db["counters"]
    # collection = short
    kollection =db["short"]


    # search for a given value 
    result = kollection.find({"_key":usr_input})
    resultant=result.explain()




    if resultant['executionStats']['nReturned'] ==0:
         # Query the counters 
        results = collection.find({"_id": ObjectId('5e87ff521c9d440000487720')})
        for i in results:
            seq= i["seq"]

        seq=int(seq)

        myquery = { "_id": ObjectId('5e87ff521c9d440000487720') }
        newvalues = { "$set": { "seq": seq+1 } }
        collection.update_one(myquery, newvalues)


        mini_link="omelet.xyz/"+usr_input
        mydict = { "long_url": long_url, "_key": usr_input,"mini_link":mini_link,"seq":seq }

        kollection.insert_one(mydict)
        
        return mini_link
    else:
        
        return False