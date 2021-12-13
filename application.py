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


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        actmass = dom
        index = doi
        weights = {}
        items = ["nose-hold", "tail-hold", "FWD-tank", "AFT-tank"]
        for item in items:
            if "tank" in item:
                weights[item] = int(request.form.get(item)) / 2.2
            else:
                weights[item] = int(request.form.get(item))
            actmass += weights[item]
            index += get_index(weights[item], arms[item])
        for i in range(1, 8):
            for j in ["A", "B", "C"]:
                seatweight = int(request.form.get("seat-" + str(i) + "-" + j))
                actmass += seatweight
                index += get_index(seatweight, arms[str(i)])
        if not 3.6 < index < 16.7 or actmass > 5760:
            category = "danger"
        else:
            category = "success"
        flash("Takeoff mass is " + str(round(actmass)) + "Kg and\
             the index is " + str(round(index, 2)), category)
        return redirect("/")
    else:
        return render_template("index.html")

@app.route("/info", methods=["GET"])
def index_info():
    category = "info"
    flash("Accepted index range is between 3.6 and 16.7", category)
    return redirect("/")