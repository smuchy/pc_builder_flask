from .models import User
from .models import serve_cpus
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
        # session["username"] = username
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
    return jsonify(response="success")


@app.route("/authenticate/<username>")
def authenticate(username):

    if username == session["username"]:
        return jsonify(response="true")
    else:
        return jsonify(response="false")


@app.route("/profile/<username>")
def profile(username):
    logged_in_user = session.get("username")

    if logged_in_user:
        return "Ovo je profil hehe"
    else:
        return "Please login"


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


@app.route("/cpus")
def cpus():
    cpuList = serve_cpus()
    cpuList = jsonify(cpuList=cpuList)
    return cpuList


@app.route("/motherboards/<cpu>")
def serve_motherboards(cpu):
    motherboardList = User(session["username"]).serve_motherboards(cpu)
    motherboardList = jsonify(motherboardList=motherboardList)
    return motherboardList


@app.route("/rams")
def serve_rams():
    ramList = User(session["username"]).serve_rams()
    ramList = jsonify(ramList=ramList)
    return ramList


@app.route("/storages")
def serve_storages():
    storageList = User(session["username"]).serve_storages()
    storageList = jsonify(storageList=storageList)
    return storageList


@app.route("/video_cards")
def serve_video_cards():
    video_cardList = User(session["username"]).serve_video_cards()
    video_cardList = jsonify(video_cardList=video_cardList)
    return video_cardList


@app.route("/cpu_coolers")
def serve_cpu_coolers():
    cpu_coolerList = User(session["username"]).serve_cpu_coolers()
    cpu_coolerList = jsonify(cpu_coolerList=cpu_coolerList)
    return cpu_coolerList


@app.route("/cases")
def serve_cases():
    caseList = User(session["username"]).serve_cases()
    caseList = jsonify(caseList=caseList)
    return caseList


@app.route("/power_supplies")
def serve_power_supplies():
    power_suppliesList = User(session["username"]).serve_power_supplies()
    power_suppliesList = jsonify(power_suppliesList=power_suppliesList)
    return power_suppliesList


@app.route("/opearating_systems")
def serve_operating_systems():
    operating_systemList = User(session["username"]).serve_operating_systems()
    operating_systemList = jsonify(operating_systemList=operating_systemList)
    return operating_systemList
