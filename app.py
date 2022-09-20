from flask import Flask
from flask_crontab import Crontab

app = Flask(__name__)
crontab = Crontab(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"