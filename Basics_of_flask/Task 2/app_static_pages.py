#2. Build a Flask app with static HTML pages and navigate between them.
from flask import Flask, request,render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/Details")
def details():
    return render_template("detail.html")

@app.route("/contact us")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host ="0.0.0.0", port="5001")