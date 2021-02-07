import os

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
arms = [0, 135, 165, 195, 225, 254, 281, 320]

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    actualmass = dom
    index = doi
    for i in range (1,8):
      for j in ["a", "b", "c"]:
        form_seat_val = request.form.get("seat-"+ str(i) +"-"+ j)
        if form_seat_val:
          seatweight = int( form_seat_val )
          if seatweight > 0:
            actualmass += seatweight
            index += seatweight * (arms[i] - 210)/4536
    return render_template("index.html", actualmass=actualmass, index=index)
  else:
    return render_template("index.html", actualmass=dom, index=doi)
