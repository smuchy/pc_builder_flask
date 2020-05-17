from .models import User
from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify

app = Flask(__name__)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.get_json()['username']
        password = request.get_json()['password']

    if not User(username).register(password):
        return jsonify(response = "fail")
    else:
        session['username'] = username
        return jsonify(response = "success")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.get_json()['username']
        password = request.get_json()['password']

    if not User(username).verify_password(password):
        return jsonify(response = "fail")
    else:
        session['username'] = username
        return jsonify(response = "success")
    