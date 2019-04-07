import pymongo
from bson.json_util import dumps
from flask import Flask,render_template

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


@app.route('/insert/<int:id>/<string:name>/<string:adresse>', methods=['GET'])
def insert(name, adresse, id):
    data = {"_id": id, "name": name, "address": adresse}

    x = mycol.insert_one(data)
    if (x.inserted_id > 0):
        return dumps({'status': 'OK'})
    else:
        return dumps({'status': 'ERROR'})


@app.route('/delete_all', methods=['GET'])
def delete_all():
    x = mycol.delete_many({})
    if (x.deleted_count == 0 or x.deleted_count > 1):
        return dumps({'status': 'OK'})
    else:
        return dumps({'status': 'ERROR'})


@app.route('/select_all', methods=['GET'])
def get_all():
    x = mycol.find()
    return dumps(x)


@app.route('/select_first', methods=['GET'])
def get_one():
    x = mycol.find_one()
    if x is []:
        return dumps({'status': 'EMPTY'})
    else:
        return dumps({'data':x, 'status': 'OK'})


@app.route('/find_by_adr/<string:adresse>', methods=['GET'])
def find_by_adr(adresse):
    x = mycol.find({"address": adresse})
    if x is []:
        return dumps({'status': 'EMPTY'})
    else:
        return dumps(x, {'status': 'OK'})


@app.route('/find_by_name/<string:name>', methods=['GET'])
def find_by_name(name):
    x = mycol.find({"name": name})
    if x is []:
        return dumps({'status': 'EMPTY'})
    else:
        return dumps({'status': 'OK'})


@app.route('/sort_by_adr', methods=['GET'])
def sort_by_adr():
    x = mycol.find().sort("address")

    return dumps(x, {'status': 'OK'})


@app.route('/sort_by_name/', methods=['GET'])
def sort_by_name():
    x = mycol.find().sort("name")

    if x is []:
        return dumps({'status': 'EMPTY'})
    else:
        return dumps(x, {'status': 'OK'})


@app.route('/sort_by_id/', methods=['GET'])
def sort_by_id():
    x = mycol.find().sort("_id")

    if x is []:
        return dumps({'status': 'EMPTY'})
    else:
        return dumps(x, {'status': 'OK'})


@app.route('/update_name/<int:id>/<old_name>/<new_name>')
def update_name(id, old_name, new_name):
    old = {'_id': id, 'name': old_name}
    new = {'$set': {'_id': id, 'name': new_name}}
    if (mycol.update_one(old, new)):
        return dumps({'status': 'OK'})
    else:
        return dumps({'status': 'ERROR'})


@app.route('/update_adr/<int:id>/<old_adr>/<new_adr>')
def update_adr(id, old_adr, new_adr):
    old = {'_id': id, 'address': old_adr}
    new = {'$set': {'_id': id, 'address': new_adr}}
    x = mycol.update_one(old, new)
    if (mycol.update_one(old, new)):
        return dumps({'status': 'OK'})
    else:
        return dumps({'status': 'ERROR'})


@app.route('/')
def help():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2000', debug=True)
