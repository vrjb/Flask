# 3. Develop a Flask app that uses URL parameters to display dynamic content.
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return 'Welcome!'

@app.route('/user')
def page():
    data=request.args.get('name')
    return render_template('result.html',data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5010')