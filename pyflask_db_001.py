from math import *

from flask import  (
    Flask,
    render_template,
    request
)
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify


app = Flask(__name__)
#db_connect = create_engine('sqlite:///dsNhanVien.db')

import pymongo 
from pymongo import MongoClient 

app = Flask(__name__)
#db_connect = create_engine('sqlite:///dsNhanVien.db')

MONGO_URI = 'mongodb+srv://rong:rong@cluster0-f5qr6.mongodb.net/test?retryWrites=true&w=majority'
cluster = MongoClient(MONGO_URI)

db = cluster["ShopOnline"]

@app.route('/')
def  index():
    return "<h1> Flask DB 001 - Connecting !!! </h1>"

@app.route('/login', methods=['GET', 'POST'])
def  login():
    query_parameters = request.args
    vusername = query_parameters.get("Id")
    vpassword = query_parameters.get("HoTen")

    ### ch-eck Account / Tài khoản USER
    collection = db["NhanVien"]
    results = collection.find({"Id":1001, "HoTen": "NguyenVanA"}) 

    if len(results) == 1:
        logined_flag = True
        return render_template("home.html")
    else:
        return render_template("login.html"))

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


api = Api(app)
api.add_resource(Parameters, '/parameters/<firstParam>') # Route_1
