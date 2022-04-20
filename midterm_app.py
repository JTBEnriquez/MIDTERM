from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")
    
@app.route("/r")
def register():
    return render_template("registration.html")
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port= 5000)
