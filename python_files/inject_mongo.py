
# When No Custom domain is given funtion execute_the_input is invoked.
# This function is used to inject 
# long url 
#  mini link
#  key
# Seq
def execute_the_input(long_url,brand_url):
    long_url=long_url.strip()
   
    
    # Retrieving Millisecond From Current Time
    import time
    millis = int(round(time.time() * 1000))
    str_millis=str(millis)
    str_millis=(str_millis[-6:])
    str_millis=hex(int(str_millis))
    millis=str_millis[2:]

    # Lookup Key based on Day of year
    from python_files import key_year_lookup
    import datetime
    day_of_year_key=key_year_lookup.key_year_lookup(datetime.datetime.now().strftime('%j'))

    short_url_key=''.join(sorted(millis+day_of_year_key))

    from pymongo import MongoClient
    from flask import render_template
    from bson.objectid import ObjectId
    cluster = MongoClient("mongodb://cdevairakkam:Amplitude20DEC!@minilinkcluster-shard-00-00-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-01-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-02-ja0tk.azure.mongodb.net:27017/test?ssl=true&replicaSet=minilinkcluster-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = cluster["links"]
    # collection = counters
    collection = db["counters"]
    # collection = short
    kollection =db["short"]

    # Query the counters 
    results = collection.find({"_id": ObjectId('5e87ff521c9d440000487720')})
    for i in results:
        seq= i["seq"]

        seq=int(seq)

    # increment the count

    myquery = { "_id": ObjectId('5e87ff521c9d440000487720') }
    newvalues = { "$set": { "seq": seq+1 } }
    collection.update_one(myquery, newvalues)

    mini_link= brand_url+"/"+short_url_key

    mydict = { "long_url": long_url, "_key": short_url_key,"mini_link":mini_link,"seq":seq ,"brand_domain":brand_url}

    kollection.insert_one(mydict)

    return mini_link


# When custom domain input is given function inject_custom_mongo is invoked.
def inject_custom_mongo(long_url,usr_input,brand_domain):
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
    result = kollection.find({"_key":usr_input,"brand_domain":brand_domain})
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
        mini_link=brand_domain+"/"+usr_input
        mydict = { "long_url": long_url, "_key": usr_input,"mini_link":mini_link,"seq":seq,"brand_domain":brand_domain }
        kollection.insert_one(mydict)
        return mini_link
    else:

        return False

