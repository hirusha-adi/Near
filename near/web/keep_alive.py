import os
from threading import Thread

from flask import Flask, render_template

app = Flask(__name__, template_folder=f"{os.getcwd()}/near/web/templates")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/help')
def help():
    return render_template("help.html")


def run():
    app.run(host='0.0.0.0', port=8090)


def keep_alive():
    t = Thread(target=run)
    t.start()
