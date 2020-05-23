from .models import User
from flask import (
    Flask,
    request,
    session,
    redirect,
    url_for,
    render_template,
    flash,
    jsonify,
)

app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.get_json()["username"]
        password = request.get_json()["password"]
        first_name = request.get_json()["first_name"]
        last_name = request.get_json()["last_name"]
        email = request.get_json()["email"]

    if not User(username).register(password, first_name, last_name, email):
        return jsonify(response="fail")
    else:
        session["username"] = username
        return jsonify(response="success")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.get_json()["username"]
        password = request.get_json()["password"]

    if not User(username).verify_password(password):
        return jsonify(response="fail")
    else:
        session["username"] = username
        return jsonify(response="success")


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out.")
    return "success"


@app.route("/profile/<username>")
def profile(username):
    logged_in_user = session.get("username")

    if logged_in_user:
        return "Ovo je profil hehe"
    else:
        return "Please login"
