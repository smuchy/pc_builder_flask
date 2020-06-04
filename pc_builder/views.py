from __future__ import print_function
from .models import User
from .models import (
    serve_cpus,
    serve_motherboards,
    serve_rams,
    serve_storages,
    serve_video_cards,
    serve_cpu_coolers,
    serve_cases,
    serve_power_supplies,
    serve_operating_systems,
    graph,
)
from flask import (
    Flask,
    request,
    session,
    redirect,
    url_for,
    render_template,
    flash,
    jsonify,
    json,
)
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_raw_jwt,
)
from .commands import import_database
import click
from flask.cli import with_appcontext


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret"
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access"]

jwt = JWTManager(app)
blacklist = set()
CORS(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token["jti"]
    return jti in blacklist


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
        # session["username"] = username
        return jsonify(response="success")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.get_json()["username"]
        password = request.get_json()["password"]
        response = ""

    user = User(username).verify_password(password)
    if user == False:
        return jsonify({"error": "Invalid username or password"})
    else:
        access_token = create_access_token(
            identity={"username": user["username"], "email": user["email"],}
        )
        result = jsonify({"token": access_token})
    return result


@app.route("/logout")
@jwt_required
def logout():
    jti = get_raw_jwt()["jti"]
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out."})


@app.route("/protected", methods=["GET"])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)


# @app.route("/authenticate/<username>")
# def authenticate(username):

#     print(session["username"])
#     if "username" in session:
#         return username
#         if username == session["username"]:
#             return jsonify(response="true")
#         else:
#             return jsonify(response="false")
#     else:
#         return jsonify(response="false")


@app.route("/update_user_data/", methods=["GET", "POST"])
def update_user_data():
    username = session.get("username")
    if request.method == "POST":
        first_name = None
        last_name = None
        email = None
        requestData = request.get_json()
        if "first_name" in requestData:
            first_name = requestData["first_name"]
        if "last_name" in requestData:
            last_name = requestData["last_name"]
        if "email" in requestData:
            email = requestData["email"]

    return User(username).update_user_data(first_name, last_name, email)


@app.route("/add_favourite/<component>/<name>")
def add_favourite(component, name):
    username = session.get("username")
    return User(username).add_to_favourite(component, name)


@app.route("/remove_favourite/<component>/<name>")
def remove_favourite(component, name):
    username = session.get("username")
    return User(username).remove_favourite(component, name)


@app.route("/profile/<username>")
def profile(username):
    logged_in_user = session.get("username")

    if logged_in_user == username:
        return jsonify(response=User(username).find())
    else:
        return jsonify(response="fail")


@app.route("/add_pcbuild", methods=["GET", "POST"])
def add_pcbuild():
    if request.method == "POST":
        cpu = request.get_json()["cpu"]
        motherboard = request.get_json()["motherboard"]
        ram = request.get_json()["ram"]
        storage = request.get_json()["storage"]
        video_card = request.get_json()["video_card"]
        cpu_cooler = request.get_json()["cpu_cooler"]
        case = request.get_json()["case"]
        power_supply = request.get_json()["power_supply"]
        operating_system = request.get_json()["operating_system"]

    return User(session["username"]).add_pcbuild(
        cpu,
        motherboard,
        ram,
        storage,
        video_card,
        cpu_cooler,
        case,
        power_supply,
        operating_system,
    )


@app.route("/delete_pcbuild/<id>")
def delete_pcbuild(id):
    return User(session["username"]).delete_pcbuild(id)


@app.route("/cpus")
def cpus():
    cpuList = serve_cpus()
    cpuList = jsonify(componentList=cpuList)
    return cpuList


@app.route("/motherboards/<cpu>")
def motherboards(cpu):
    motherboardList = serve_motherboards(cpu)
    motherboardList = jsonify(motherboardList=motherboardList)
    return motherboardList


@app.route("/rams")
def rams():
    ramList = serve_rams()
    ramList = jsonify(componentList=ramList)
    return ramList


@app.route("/storages")
def storages():
    storageList = serve_storages()
    storageList = jsonify(componentList=storageList)
    return storageList


@app.route("/video_cards")
def video_cards():
    video_cardList = serve_video_cards()
    video_cardList = jsonify(componentList=video_cardList)
    return video_cardList


@app.route("/cpu_coolers")
def cpu_coolers():
    cpu_coolerList = serve_cpu_coolers()
    cpu_coolerList = jsonify(componentList=cpu_coolerList)
    return cpu_coolerList


@app.route("/cases")
def cases():
    caseList = serve_cases()
    caseList = jsonify(componentList=caseList)
    return caseList


@app.route("/power_supplies")
def power_supplies():
    power_suppliesList = serve_power_supplies()
    power_suppliesList = jsonify(componentList=power_suppliesList)
    return power_suppliesList


@app.route("/operating_systems")
def operating_systems():
    operating_systemList = serve_operating_systems()
    operating_systemList = jsonify(componentList=operating_systemList)
    return operating_systemList


# @click.command()
# @with_appcontext
@app.cli.command("import_db")
def import_db():
    print("Importing database...")
    import_database()
    print("Database imported.")


app.cli.add_command(import_db)
