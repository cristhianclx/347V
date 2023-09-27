from flask import Flask, render_template
from pypdf import PdfReader


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
