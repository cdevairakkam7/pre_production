# Look up long url based on short url 
# if no long url present then re route to omelet.xyz

def long_url(short_url):
    from pymongo import MongoClient
    from flask import render_template
    from bson.objectid import ObjectId
    cluster = MongoClient("mongodb://cdevairakkam:Amplitude20DEC!@minilinkcluster-shard-00-00-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-01-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-02-ja0tk.azure.mongodb.net:27017/test?ssl=true&replicaSet=minilinkcluster-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = cluster["links"]
    # collection = counters
    collection = db["counters"]
    # collection = short
    kollection =db["short"]
    from urllib.parse import urlparse
    short_url_path=urlparse(short_url)
    print(short_url_path[0:4])
    if(short_url[0:4]=='www.' ):
        netloc=short_url_path.netloc
        netloc=netloc.replace('www.','')
        short_url_path= short_url_path.path.split('/')
        short_url_path[0]=short_url_path[0].replace('www.','')
        myquery = { "_key": short_url_path[1],"brand_domain":short_url_path[0]}
        print(myquery)
        mydoc = kollection.find(myquery)
        print(kollection.count_documents(myquery))
        if(kollection.count_documents(myquery)>0):
        
            for i in mydoc:
                original_url =i['long_url']
                return original_url 
    elif (short_url[0:4]=='http'):
        netloc=short_url_path.netloc
        netloc=netloc.replace('www.','')
        short_url_path= short_url_path.path
        short_url_path=short_url_path.replace('/','')
        myquery = { "_key":short_url_path,"brand_domain":netloc}
        mydoc = kollection.find(myquery)
        print(kollection.count_documents(myquery))
        if(kollection.count_documents(myquery)>0):
        
            for i in mydoc:
                original_url =i['long_url']
                return original_url 
        
    else:
        print('code was in else')
        short_url_path= short_url_path.path.split('/')
        myquery = { "_key": short_url_path[1],"brand_domain":short_url_path[0]}
        print(myquery)
        mydoc = kollection.find(myquery)
        print(kollection.count_documents(myquery))
        if(kollection.count_documents(myquery)>0):
        
            for i in mydoc:
                original_url =i['long_url']
                return original_url 
                                                                                                          
  
    return 'https://omelet.xyz/'
