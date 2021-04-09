import flask 
from flask import request


'''
Code Reference 
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://wings2pc.tistory.com/entry/%EC%9B%B9-%EC%95%B1%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%8C%EB%9D%BC%EC%8A%A4%ED%81%ACPython-Flask-Request-get-parameterHTTP-method-GET-POST

'''
app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return "<h1>Arithmetic is Fun!!</h1><p>You can do plus, minus, multiply, divide.</p>"


@app.route('/plus', methods=['GET'])
def plus():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return {"ans" : a + b}

@app.route('/minus', methods=['GET'])
def minus():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return {"ans" : a - b}

@app.route('/multiply', methods=['GET'])
def multiply():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return {"ans" : a * b}

@app.route('/divide', methods=['GET'])
def divide():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return {"ans" : a / b}

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
