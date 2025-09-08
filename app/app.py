from flask import Flask,request,jsonify
import random

app = Flask(__name__)

#get_ip
@app.route('/my-ip',methods=['GET'])
def myip():
    ip_add=request.remote_addr
    return ip_add
    #return jsonify({"ip":ip_add})

if __name__ == '__main__':
    app.run(debug=True)
