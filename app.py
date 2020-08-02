from flask import Flask
# Import necessary modules
from flask import Flask,render_template,request,make_response,jsonify,redirect


app = Flask(__name__)
@app.route("/")
def hello():
    print("##################")
    
    print(request.remote_addr)
    print("##################")   
    from pymongo import MongoClient
    from flask import render_template
    from bson.objectid import ObjectId
    cluster = MongoClient("mongodb://cdevairakkam:Amplitude20DEC!@minilinkcluster-shard-00-00-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-01-ja0tk.azure.mongodb.net:27017,minilinkcluster-shard-00-02-ja0tk.azure.mongodb.net:27017/test?ssl=true&replicaSet=minilinkcluster-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = cluster["links"]
    # collection = counters
    collection = db["link_performance"]
    my_dict={"ip":request.remote_addr}
    collection.insert_one(my_dict)
    return 'Hello'
  
    



if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1')
