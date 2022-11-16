from sqlite3.dbapi2 import Cursor
from typing import SupportsRound
from flask import Flask, render_template, flash, wrappers
from flask import redirect
from flask import request
from hashlib import sha256
from flask import session
from flask.helpers import url_for
import os
import sqlite3
import os.path
import requests

app = Flask(__name__)
app.secret_key = b'asdasjosdfusyhgydrtyuerdyl'


@app.route('/')
def index():
    response = requests.get('http://127.0.0.1:5000/')
    return response.text


@app.route('/nature')
def nature():
    response = requests.get('http://127.0.0.1:5000/nature')
    return response.text


@app.route('/anime')
def anime():
    response = requests.get('http://127.0.0.1:5000/anime')
    return response.text


@app.route('/animals')
def animals():
    response = requests.get('http://127.0.0.1:5000/animals')
    return response.text


@app.route('/auto')
def auto():
    response = requests.get('http://127.0.0.1:5000/auto')
    return response.text


@app.route('/game')
def game():
    response = requests.get('http://127.0.0.1:5000/game')
    return response.text


@app.route('/future')
def future():
    response = requests.get('http://127.0.0.1:5000/future')
    return response.text


@app.route('/pixel')
def pixel():
    response = requests.get('http://127.0.0.1:5000/pixel')
    return response.text


@app.route('/minimalism')
def minimalism():
    response = requests.get('http://127.0.0.1:5000/minimalism')
    return response.text


@app.route('/space')
def space():
    response = requests.get('http://127.0.0.1:5000/space')
    return response.text


@app.route('/meme')
def meme():
    response = requests.get('http://127.0.0.1:5000/meme')
    return response.text


@app.route('/search', methods=["GET", "POST"])
def search():
    response = requests.get('http://127.0.0.1:5000/search')
    return response.text


@app.route("/reg")
def reg():
    response = requests.get('http://127.0.0.1:5000/reg')
    return response.text


@app.route("/logout")
def logout():
    response = requests.get('http://127.0.0.1:5000/logout')
    return response.text


@app.route("/fun/reg", methods=["POST"])
def fun_reg():
    username = request.form["login"].encode(encoding=" utf-8", errors=" strict")
    password = sha256(request.form["password"].encode("utf-8")).hexdigest().encode(encoding=" utf-8", errors=" strict")
    email = request.form["email"].encode(encoding=" utf-8", errors=" strict")
    response = requests.post('http://127.0.0.1:5000/fun/reg', data={username, password, email})
    return response.text


@app.route("/login")
def login():
    response = requests.get('http://127.0.0.1:5000/login')
    return response.text


@app.route("/fun/login", methods=["POST"])
def fun_login():
    login = request.form['login']
    # password = sha256(request.form['password'].encode("utf-8")).hexdigest().encode(encoding=" utf-8", errors=" strict")
    password = request.form['password']
    response = requests.post('http://127.0.0.1:5000/fun/login', json={"login": login, "password": password})
    print(login, password)
    print(response)
    return response.text


@app.route("/create")
def create():
    response = requests.get('http://127.0.0.1:5000/create')
    return response.text


@app.route("/fun/create", methods=["POST"])
def fun_create():
    response = requests.post('http://127.0.0.1:5000/fun/create')
    return response.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
