from threading import Thread
from flask import Flask, render_template

app = Flask('')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/help')
def help():
    return render_template("help.html")


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


keep_alive()
