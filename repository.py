import database
import pymysql.cursors
import pymysql
import json
import hashlib
import base64

def user(limit,offset):
    offsets = (limit * offset) - limit
    conn = database.connect_db()
    cr = conn.cursor(pymysql.cursors.DictCursor)
    query = "SELECT * FROM users limit {} offset {}".format(limit, offsets)
    
    cr.execute(query)
    data = []
    for r in cr.fetchall():
        data.append(r)
    query_count = "SELECT count(*) as c FROM users"
    cr.execute(query_count)
    total = cr.fetchone()
    conn.close()
    return {"data":data, "total":total["c"]}

def getUser(id):
    conn = database.connect_db()
    cr = conn.cursor(pymysql.cursors.DictCursor)
    query = "SELECT * FROM users where id = {}".format(id)    
    cr.execute(query)
    data=[]
    for r in cr.fetchall():
        data.append(r)
    conn.close()
    return {"data":data}

def deleteUser(id):
    conn = database.connect_db()
    cr = conn.cursor(pymysql.cursors.DictCursor)
    query = "Delete FROM users where id = {}".format(id)    
    cr.execute(query)
    conn.commit()
    conn.close()

def updateUser(id,data):
    conn = database.connect_db()
    password=hashing(data["password"])
    cr = conn.cursor(pymysql.cursors.DictCursor)
    query = "UPDATE users SET username = %s,password = %s,name = %s  WHERE id = {}".format(id)
    val=(data["username"],password,data["name"])    
    cr.execute(query,val)
    conn.commit()
    conn.close()


def insertUser(data):
    conn = database.connect_db()
    password=hashing(data["password"])
    cr = conn.cursor(pymysql.cursors.DictCursor)
    query = "INSERT INTO users (username ,password ,name) VALUES (%s,%s,%s)"
    val=(data["username"],password,data["name"])    
    cr.execute(query,val)
    conn.commit()
    conn.close()

def hashing(password):
    hash_object = hashlib.sha256(password.encode())
    digest = hash_object.digest()
    encoded = base64.b64encode(digest)
    return encoded.decode('utf-8')