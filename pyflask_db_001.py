from math import *
import pymongo 
from pymongo import MongoClient 
from flask import  (
    Flask,
    render_template,
    request
)
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify

MONGO_URI = 'mongodb+srv://rong:rong@cluster0-f5qr6.mongodb.net/test?retryWrites=true&w=majority'
cluster = MongoClient(MONGO_URI)
db = cluster["ShopOnline"]

app = Flask(__name__)
#db_connect = create_engine('sqlite:///dsNhanVien.db')

@app.route('/')
def  index():
    return "<h1> Flask DB 001 - Connecting !!! </h1>"

@app.route('/login', methods=['GET', 'POST'])
def  login():
    query_parameters = request.args
    vusername = query_parameters.get("username")
    vpassword = query_parameters.get("password")
    collection = db["NhanVien"]
    results = collection.find({"username":vusername, "password":vpassword})

    if len(list(results)) == 1:
        return render_template("profile.html")
    else:
        return render_template("login.html")

@app.route('/profile')
def  profile():
    return render_template("profile.html")

@app.route('/services')
def  call_services():
    return render_template("call_api.html")

@app.route('/params', methods=['GET'])
def api_filter():
    query_parameters = request.args
    return jsonify(query_parameters)

@app.route('/giaiptb1', methods=['GET'])
def giaiptb1():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")

    a = int(a)
    b = int(b)

    str = "khong co nghiem"
    
    kq = { "tt" : str }

    if a == 0 and b == 0:
        str = "VSN"
        kq = { "tt" : str }
    elif a != 0:
        x =  -b/a
        str = "co 1 nghiem"
        kq = { "tt" : str , "x" : x}
    else:
        str = "KoCoN"
        kq = { "tt" : str }
    return jsonify(kq)


@app.route('/giaib2', methods=['GET'])
def giaib2():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")
    c = query_parameters.get("c")

    a = float(a)
    b = float(b)
    c = float(c)

    str = "chưa biết có nghiệm hay không ! "
    
    kq = { "Trạng thái" : str , "Hệ số" : (a, b, c) }
    ### 
    
    return jsonify(kq)


class Parameters(Resource):
    def get(self, firstParam):
        return "Day la tam so " + firstParam

api = Api(app)
api.add_resource(Parameters, '/parameters/<firstParam>') # Route_1
