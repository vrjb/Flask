#4. Create a Flask app with a form that accepts user input and displays it.

from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def details():
    if request.method =="POST":
        data = {'First_Name':request.form.get('First_Name'),
        'Last_Name':request.form.get('Last_Name'),
        'Date_of_Birth' :request.form.get('Date_of_Birth'),
        'Sex':request.form.get('Sex'),
        'Address':request.form.get('Address'),
        'Email' : request.form.get('EmailId'),
        'Mobile' :request.form.get('Mobile')}
        # print(data)
        return render_template('user_data.html', data=data)
    return render_template('user.html')


if __name__ == "__main__":
    app.run(debug=True, port='5002')

