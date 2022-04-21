import json

from flask import Flask, request, jsonify
import pymysql.cursors
import pymongo

# sql connections
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='assignment',
                             cursorclass=pymysql.cursors.DictCursor)

#Mongo connections
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.ppsmc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.INEURON

app = Flask(__name__)

@app.route("/getsql",methods = ["POST"])
def getdatausingsql():
    result = ''
    with connection.cursor as cursor:
        # read a single record
        sql = "select * from assignment.sample limit 5"
        cursor.execute()
        result = cursor.fetchall()
        result = str(result)
    return result

@app.route("/getmongodata",methods=["POST"])
def getdatausingmongo():
    col1 = db.INEURON
    data = {"result":str(list(col1.find().limit(10)))}
    return data

if __name__ == "__main__":
    app.run()
