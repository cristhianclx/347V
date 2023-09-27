from flask import Flask, render_template
from pypdf import PdfReader


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")


users_data = [{
    "name": "cristhian",
    "age": 34,
    "language": "python",
}, {
    "name": "genaro",
    "age": 34,
    "language": "nodejs",
}]
    

@app.route('/users')
def users():
    return render_template("users.html", users=users_data)

@app.route('/users/<name>')
def users_by_name(name):
    user = {}
    for user_data in users_data:
        if user_data.get("name") == name:
            user = user_data
    return render_template("user.html", user=user)