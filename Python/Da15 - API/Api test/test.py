from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/xyz', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':  # sending data in a secure way
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))


@app.route('/test1', methods = ['POST'])
def test1():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify(str(result))


@app.route('/test2', methods = ['POST'])
def test2():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify(str(result))


@app.route('/test3', methods = ['POST'])
def test3():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        result = a%b
        return jsonify(str(result))

if __name__ == '__main__':
    app.run(port=8000)

# write a function to fetch data from sql via api
# write a function to fetch data from mongodb via api