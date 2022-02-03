from flask import Flask, flash, redirect, render_template, request
import secrets

secret = secrets.token_urlsafe(32)


# Configure application
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_object(__name__)
app.secret_key = secret

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


dom = 3683
doi = 6.45
arms = {
    'nose-hold': 25, '1': 135, '2': 165, 'FWD-tank': 191,
    '3': 195, 'AFT-tank': 210, '4': 225, '5': 254,
    '6': 281, '7': 320, 'tail-hold': 354
}


def get_index(weight, arm):
    return weight * (arm - 210) / 4536

def calculateCg_and_GenerateMessage(dom, doi):
    #set parameters
    actmass = int(dom)
    index = float(doi)
    weights = {}
    items = ["nose-hold", "tail-hold", "FWD-tank", "AFT-tank"]
    #calculate cg
    for item in items:
        item_value = int(request.form.get(item) or '0')
        if "tank" in item:
            weights[item] = item_value / 2.2
        else:
            weights[item] = item_value
        actmass += weights[item]
        index += get_index(weights[item], arms[item])

    for i in range(1, 8):
        for j in ["A", "B", "C"]:
            seatweight = int(request.form.get("seat-" + str(i) + "-" + j)) / 2.2
            actmass += seatweight
            index += get_index(seatweight, arms[str(i)])
    #generate message
    if not 3.6 < index < 16.7 or actmass > 5760:
            category = "danger"
    else:
        category = "success"

    variables = {
        "message": "Takeoff mass is " + str(round(actmass)) + " Kg and\
            the index is " + str(round(index, 2)),
        "category": category,
        "aircraft": ""
    }
    return variables

def calculateMantaCg_and_GenerateMessage(dom, doi):
    #set parameters
    actmass = int(dom)
    index = float(doi)
    weights = {}
    items = ["nose-hold", "tail-hold", "FWD-tank", "AFT-tank"]
    #calculate cg
    for item in items:
        item_value = int(request.form.get(item) or '0')
        weights[item] = item_value
        actmass += weights[item]
        index += get_index(weights[item]/2.2, arms[item])

    for i in range(1, 6):
        for j in ["A", "B", "C"]:
            seatweight = int(request.form.get("seat-" + str(i) + "-" + j))
            actmass += seatweight
            index += get_index(seatweight/2.2, arms[str(i)])
    baggage = int(request.form.get("baggage-area") or '0')
    actmass += baggage
    index += get_index(baggage/2.2, 300)
    #generate message
    if not 3.6 < index < 16.7 or actmass > 12500:
            category = "danger"
    else:
        category = "success"

    variables = {
        "message": "Takeoff mass is " + str(round(actmass)) + " Lbs and\
            the index is " + str(round(index, 2)),
        "category": category,
        "aircraft": ""
    }
    return variables

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/custom", methods=["GET", "POST"])
def custom():
    plate = 'manta custom'
    if request.method == "POST":
        aps = request.form.get("APS")
        index = request.form.get("index")
        variables = calculateMantaCg_and_GenerateMessage(aps, index)
        variables['aircraft'] = '/custom'
        
        return render_template("manta.html", variables = variables, plate = plate)
    else:
        variables = {'aircraft': '/custom'}
        return render_template("manta.html", variables = variables, plate = plate)

@app.route("/ghial", methods=["GET", "POST"])
def ghial():
    plate = 'for G-HIAL'
    if request.method == "POST":
        
        variables = calculateCg_and_GenerateMessage(3686, 6.45)
        variables['aircraft'] = '/ghial'
        
        return render_template("aircraft.html", variables = variables, plate = plate)
    else:
        variables = {'aircraft': '/ghial'}
        return render_template("aircraft.html", variables = variables, plate = plate)

@app.route("/gsgts", methods=["GET", "POST"])
def gsgts():
    plate = 'for G-SGTS'
    if request.method == "POST":
        
        variables = calculateCg_and_GenerateMessage(3666, 6.89)
        variables['aircraft'] = '/gsgts'
        
        return render_template("aircraft.html", variables = variables, plate = plate)
    else:
        variables = {'aircraft': '/gsgts'}
        return render_template("aircraft.html", variables = variables, plate = plate)

@app.route("/gbvvk", methods=["GET", "POST"])
def gbvvk():
    plate = 'for G-BVVK'
    if request.method == "POST":
        
        variables = calculateCg_and_GenerateMessage(3576, 6.37)
        variables['aircraft'] = '/gbvvk'
        
        return render_template("aircraft.html", variables = variables, plate = plate)
    else:
        variables = {'aircraft': '/gbvvk'}
        return render_template("aircraft.html", variables = variables, plate = plate)

@app.route("/info", methods=["GET"])
def index_info():
    variables = {
            "message": "Accepted index range is between 3.6 and 16.7",
            "category": "info",
            "aircraft": ""
        }
    
    return render_template("aircraft.html", variables = variables)