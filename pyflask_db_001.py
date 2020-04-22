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

@app.route('/')
def  index():
    return "<h1> Flask DB 001 - Connecting !!! </h1>"

@app.route('/login', methods=['GET', 'POST'])
def  login():
    return render_template("login.html")

@app.route('/profile')
def  profile():
    return render_template("profile.html")

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

class Parameters(Resource):
    def get(self, firstParam):
        return "Day la tam so " + firstParam
    
@app.route('/giaiptb2', methods=['GET'])
import math
def giaiptb2():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")
    c = query_parameters.get("a")

    a = int(a)
    b = int(b)
    c = int(c)
    str = "khong co nghiem"
    kq = { "tt" : str }
    
    if (a == 0):
        if (b == 0):
            kq = { "tt" : str };
        else:
            x =  -b/a
            str = "co 1 nghiem"
            kq = { "tt" : str , "x" : x}
        return;
    delta = b * b - 4 * a * c;
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        str = "co 2 nghiem"
        kq = { "tt" : str , "x1" : x1,"x2" : x2}
    elif (delta == 0):
        x1 = (-b / (2 * a));
        str = "co nghiem kep"
        kq = { "tt" : str , "x1 = x2 = " : x1}
    else:
        str = "khong co nghiem"
        kq = { "tt" : str }
    return jsonify(kq)

class Parameters(Resource):
    def get(self, firstParam):
        return "Day la tam so " + firstParam


api = Api(app)
api.add_resource(Parameters, '/parameters/<firstParam>') # Route_1
