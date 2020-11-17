from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/add', methods = ["POST", "GET"])
def add():
    return render_template()

# @app.route('/<display>', methods = ["POST", "GET"])
# def display(display):
#     return f"<h1>{display}</h1>"

@app.route('/<username>')
def hello_user(username): 
    return f"Hello, {username}"

if __name__ == "__main__" :
    app.run()