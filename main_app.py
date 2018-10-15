from flask import Flask, render_template, url_for

app = Flask(__name__)

#==============================================================================
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/business")
def business():
    return render_template("business.html")

@app.route("/personal")
def personal():
    return render_template("personal.html")

#==============================================================
if __name__ == '__main__':
    app.run(debug = True)
