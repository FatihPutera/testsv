from flask import Blueprint, jsonify,request
import repository

table = Blueprint('table', __name__, url_prefix='/user')

@table.route('/<int:limit>/<int:offset>', methods=['GET'])
def list(limit,offset):
    list = repository.user(limit,offset)
    return jsonify(list)

@table.route('/<int:id>', methods=['GET'])
def getid(id):
    getid = repository.getUser(id)
    return jsonify(getid)

@table.route('delete/<int:id>', methods=['DELETE'])
def delete(id):
    delete = repository.deleteUser(id)
    return jsonify({"status":True})

@table.route('update/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if len(data["username"])<3 or len(data["password"])<7 or len(data["name"])<3:
        return jsonify({"Status":"Gagal","Pesan":"Usename Minimal 3 Karakter, Password Minimal 7 Karakter,Name Minimal 3 Karakter"}),411
    update = repository.updateUser(id,data)
    return jsonify({"status":True})


@table.route('insert', methods=['POST'])
def insert():
    data = request.get_json()
    if len(data["username"])<3 or len(data["password"])<7 or len(data["name"])<3:
        return jsonify({"Status":"Gagal","Pesan":"Usename Minimal 3 Karakter, Password Minimal 7 Karakter,Name Minimal 3 Karakter"}),411
    insert = repository.insertUser(data)
    return jsonify({"status":True})