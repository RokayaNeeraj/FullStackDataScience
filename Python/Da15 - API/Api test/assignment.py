import mysql.connector as conn

conn.connect(host='localhost', user='root', password='password', port='3306', database='assignment')

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/assign', methods=['GET', 'POST'])
def assign():
    i = int(request.json['i'])
    if i < 30:
        output = 'select * from assignment.sample where Game_Length < 30'
    if i <= 60:
        output = 'select * from assignment.sample where Game_Length <= 60'
    if i > 60:
        output = 'select * from assignment.sample where Game_length > 60'
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=8000)
