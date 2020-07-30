def inject(ip_address,user_agent,short_url,original_url):
    import requests
    url = "http://api.ipstack.com/"+ip_address+"?access_key=55a1adfd4020c63a6080af8759e88e3b"
    payload = {'': ''}
    files = []
    headers = {}
    response = requests.request("GET", url, headers=headers, data = payload, files = files)
    ip_adress_based_response=response.text.encode('utf8')
    import time
    seconds = time.time()

    my_dict = {
    "ip": ip_adress_based_response['ip'],
    "type": ip_adress_based_response['type'],
    "continent_code": ip_adress_based_response['continent_code'],
    "continent_name": ip_adress_based_response['continent_name'],
    "country_code": ip_adress_based_response['country_code'],
    "country_name": ip_adress_based_response['country_name'],
    "region_code": ip_adress_based_response['region_code'],
    "region_name": ip_adress_based_response['region_name'],
    "city": ip_adress_based_response['city'],
    "zip": ip_adress_based_response['zip'],
    "latitude": ip_adress_based_response['latitude'],
    "longitude": ip_adress_based_response['longitude'],
    "capital": ip_adress_based_response['capital'],
    "calling_code": ip_adress_based_response['calling_code'],
    "is_eu": ip_adress_based_response['is_eu'],
    "user_agent":ip_adress_based_response['user_agent'],
    "short_url":short_url,
    "long_url":original_url,
    time_stamp:seconds
    }

    from pymongo import MongoClient
    from flask import render_template
    from bson.objectid import ObjectId
    cluster = MongoClient("mongodb://cdevairakkam:Amplitude20DEC!@minilinkcluster-shard-00-00-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-01-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-02-ja0tk.azure.mongodb.net:27017/test?ssl=true&replicaSet=minilinkcluster-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = cluster["links"]
    # collection = counters
    collection = db["link_performance"]
    collection.insert_one(my_dict)

inject(ip_address,user_agent,short_url,original_url)
