from flask import Flask, flash, redirect, render_template, request


# Configure application
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_object(__name__)

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
arms = {'nose': 25, '1': 135, '2': 165, '3': 195,
        '4': 225, '5': 254, '6': 281, '7': 320}


def get_index(weight, arm):
    index_mod = weight * (arm - 210) / 4536
    return index_mod


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        actmass = dom
        index = doi
        actmass += int(request.form.get("nose-hold"))
        index += get_index(int(request.form.get("nose-hold")), arms['nose'])
        for i in range(1, 8):
            for j in ["A", "B", "C"]:
                seatweight = int(request.form.get("seat-" + str(i) + "-" + j))
                actmass += seatweight
                index += get_index(seatweight, arms[str(i)])
        return render_template("index.html", actualmass=actmass, index=index)
    else:
        return render_template("index.html", actualmass=dom, index=doi)
