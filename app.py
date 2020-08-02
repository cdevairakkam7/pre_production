from flask import Flask
# Import necessary modules
from flask import Flask,render_template,request,make_response,jsonify,redirect
from python_files import inject_mongo
app = Flask(__name__)

@app.route("/")
def hello():
    def inject(ip_address,user_agent,short_url,original_url,referrer_url):
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
        "longitude": ip_adress_based_response['longitude'],
        "short_url":short_url,
        "long_url":original_url,
        "time_stamp":seconds,
        "referrer_url":referrer_url,
        "user_agent":user_agent    
        }

        from pymongo import MongoClient
        from flask import render_template
        from bson.objectid import ObjectId
        cluster = MongoClient("mongodb://cdevairakkam:Amplitude20DEC!@minilinkcluster-shard-00-00-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-01-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-02-ja0tk.azure.mongodb.net:27017/test?ssl=true&replicaSet=minilinkcluster-shard-0&authSource=admin&retryWrites=true&w=majority")

        db = cluster["links"]
        # collection = counters
        collection = db["link_performance"]
        collection.insert_one(my_dict)
        return True
    inject(request.environ.get('HTTP_X_REAL_IP', request.remote_addr),request.headers.get('User-Agent'),'short_url','original_url','referrer_url')

    return "Hello World!"
    



if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1')