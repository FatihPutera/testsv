import flask
import pymysql.cursors
import pymysql

def connect_db():
    conn= pymysql.connect(host='localhost',
                        user='root',
                        password='',                             
                        db='db_dummy')
    return conn