# Import necessary modules
from flask import Flask,render_template,request,make_response,jsonify,redirect
from python_files import inject_mongo
from python_files import long_url
#,link_performance

app = Flask(__name__)

#Landing Page
@app.route('/')
def main():
    import os
    return render_template('index.html')

#Handle Errors
@app.errorhandler(404)
def not_found(e):
    return render_template('index.html')


#Receive Post from Index.html
@app.route('/',methods=["POST"])
def create_entry():

    req = request.get_json()
    if not str(req['usr_input']) :
   
        long_url=req['long_url']
        brand_url=req['brand_domain']
        short_url=inject_mongo.execute_the_input(long_url,brand_url)
        result= make_response(jsonify({"short_url": short_url}),200)
    else:
        short_url=inject_mongo.inject_custom_mongo(req['long_url'],req['usr_input'],req['brand_domain'])
        if short_url== False:
            short_url=req['usr_input']+" has been stolen from " + req['brand_domain']
            result= make_response(jsonify({"short_url": short_url}),200)
        else:

            result= make_response(jsonify({"short_url": short_url}),200)

    
    return result
    

    
# Rerouting to Original URL
@app.route("/<path:path>")
def lookup(path=None):

    short_url=request.url
    ip_address = request.remote_addr
    user_agent = request.user_agent
    original_url=long_url.long_url(short_url)
    if len(original_url) > 1 :
        
       # link_performance.inject(ip_address,user_agent,short_url,original_url)
        return redirect(original_url,302)
    return render_template('index.html')










if __name__ =="__main__":

    app.secret_key = '@i9E6asdasdasdaddasxasxsaUce5UG7c1&Xa#a2IsP=sTo4of!AS$DL37dRe_#&BUSw2$h@'
    app.run(debug=True,host='127.0.0.1')
