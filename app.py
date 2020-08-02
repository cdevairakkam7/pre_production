from flask import Flask
# Import necessary modules
from flask import Flask,render_template,request,make_response,jsonify,redirect
from flask_cloudflare_remote import CloudflareRemote


app = Flask(__name__)
@app.route("/")
def hello():
    from flask import Flask
# Import necessary modules
from flask import Flask,render_template,request,make_response,jsonify,redirect,request


app = Flask(__name__)
@app.route("/")
def hello():
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

  
    from pymongo import MongoClient
    from flask import render_template
    from bson.objectid import ObjectId
    cluster = MongoClient("mongodb://cdevairakkam:Amplitude20DEC!@minilinkcluster-shard-00-00-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-01-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-02-ja0tk.azure.mongodb.net:27017/test?ssl=true&replicaSet=minilinkcluster-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = cluster["links"]
    # collection = counters
    collection = db["link_performance"]
    ip_address=request.remote_addr
    ip_address=ip_address.split(':')[0]

    import requests
    import json
    url = "http://api.ipstack.com/"+ip_address+"?access_key=55a1adfd4020c63a6080af8759e88e3b"
    payload = {'': ''}
    files = []
    headers = {}
    response = requests.request("GET", url, headers=headers, data = payload, files = files)
    ip_adress_based_response=json.loads(response.text.encode('utf8'))
    print(ip_adress_based_response)
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
    "longitude": ip_adress_based_response['longitude']   
    }

    from pymongo import MongoClient
    from flask import render_template
    from bson.objectid import ObjectId
    cluster = MongoClient("mongodb://cdevairakkam:Amplitude20DEC!@minilinkcluster-shard-00-00-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-01-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-02-ja0tk.azure.mongodb.net:27017/test?ssl=true&replicaSet=minilinkcluster-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = cluster["links"]
    # collection = counters
    collection = db["link_performance"]
    collection.insert_one(my_dict)
   
    return 'Hello'
  
    



if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1')


        
            

        
            
            



