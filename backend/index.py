from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://username:password@localhost/lostnfound'
db = SQLAlchemy(app)

@app.route('/')
def start():
    return "LOST & FOUND"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rno = db.Column(db.String(10))
    name = db.Column(db.String(50))
    item = db.Column(db.String(50))
    time = db.Column(db.DateTime, default=datetime.now())
    place = db.Column(db.String(50))
    desc = db.Column(db.String(100))
    numb = db.Column(db.String(12))

class Found(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rno = db.Column(db.String(10))
    name = db.Column(db.String(50))
    item = db.Column(db.String(50))
    time = db.Column(db.DateTime, default=datetime.now())
    place = db.Column(db.String(50))
    desc = db.Column(db.String(100))
    numb = db.Column(db.String(12))
    status = db.Column(db.String(10))

@app.route('/lost', methods=['POST'])
def index():
    data = request.get_json()
    lostItem = User(rno = data["rno"], name= data["name"], item=data["item"], place=data["place"], desc=data["desc"], numb=data["numb"], time=datetime.now())
    db.session.add(lostItem)
    db.session.commit()
    return "Post request issa set"

@app.route('/find', methods=['POST'])
def index2():
    data = request.get_json()
    lostItem = Found(rno = data["rno"], name= data["name"], item=data["item"], place=data["place"], desc=data["desc"], numb=data["numb"], time=datetime.now())
    db.session.add(lostItem)
    db.session.commit()
    return "FIND request issa set"

@app.route('/viewalllost', methods=['GET'])
def index3():
    data=User.query.all()
    retVal = []
    for dataEach in data:
        temp = {}
        temp["id"] = dataEach.id
        temp["rno"] = dataEach.rno
        temp["name"] = dataEach.name
        temp["item"] = dataEach.item
        temp["time"] = dataEach.time
        temp["place"] = dataEach.place
        temp["desc"] = dataEach.desc
        temp["numb"] = dataEach.numb
        retVal.append(temp)
    return jsonify(retVal)


@app.route('/viewallfound', methods=['GET'])
def index4():
    data=Found.query.all()
    retVal = []
    for dataEach in data:
        temp = {}
        temp["id"] = dataEach.id
        temp["rno"] = dataEach.rno
        temp["name"] = dataEach.name
        temp["item"] = dataEach.item
        temp["time"] = dataEach.time
        temp["place"] = dataEach.place
        temp["desc"] = dataEach.desc
        temp["numb"] = dataEach.numb
        temp["status"] = dataEach.status
        retVal.append(temp)
    return jsonify(retVal)

# @app.route('/update/<id>', methods=['PUT'])
# def index5():
#     update(db).where(db.User.id=='id').\
#         value(status='check')

# @app.route('/update/<id>', methods=['PUT'])
# def index6():
#     update(db).where(db.Found.id=='id').\
#         value(status='check')


# stmt = update(users).where(users.c.id==5).\
#         values(name='user #5')


if __name__ == '__main__':
    app.run(host = "0.0.0.0")