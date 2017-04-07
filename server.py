from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route("/orange", methods=["POST"])
def orange():
        return render_template("/orange.html")


@app.route("/bule", methods=["POST"])
def bule():
    return render_template("bule.html")

@app.route("/red", methods=["POST"])
def red():
        return render_template("/red.html")


@app.route("/purple", methods=["POST"])
def purple():
    return render_template("purple.html")

@app.route("/ninjas", methods=["POST"])
def ninjas():
    return render_template("ninjas.html")
app.run(debug=True)
