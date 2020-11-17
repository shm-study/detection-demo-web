from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def get_started():
    return 'SHM project 시작!'

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method =='POST':
        value1 = int(request.form['val1'])
        value2 = int(request.form['val2'])
        return '{} + {} = {}'.format(value1, value2, value1+ value2)
    
    elif request.method =='GET':
        return render_template('add.html')


@app.route('/<username>')
def hello_user(username): 
    return f"Hello, {username}"

if __name__ == "__main__" :
    app.run(debug=True)