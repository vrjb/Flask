# 5. Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask, render_template, request, session, redirect, url_for


# Create the Flask application
app = Flask(__name__)
app.secret_key='hello'

@app.route("/login", methods= ["GET","POST"])
def email():
   if request.method =="POST":
    session['email'] = request.form.get('email')
    return redirect(url_for('details'))
   return render_template('email.html')

@app.route("/user_details",methods=["GET","POST"])
def details():
    if request.method =="POST":
            data = {'First_Name':request.form.get('First_Name'),
            'Last_Name':request.form.get('Last_Name'),
            'Date_of_Birth' :request.form.get('Date_of_Birth'),
            'Sex':request.form.get('Sex'),
            'Address':request.form.get('Address'),
            'Email' : session['email'],
            'Mobile' :request.form.get('Mobile')}
            # print(data)
            return render_template('user_data.html', data=data)
    return render_template('user.html')

@app.route("/logout")
def log_out():
    session.pop('email', default=None)
    return redirect(url_for('login'))


if __name__ =="__main__":
   app.run(host='0.0.0.0',debug=True, port='5015')