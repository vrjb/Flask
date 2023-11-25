# 6. Build a Flask app that allows users to upload files and display them on the website.

import os
from flask import Flask,session, request, render_template, flash,url_for,redirect
from werkzeug.utils import secure_filename

Upload_folder = r'C:\Users\49179\Flask-Assignment\Intermediate Flask\Task 6\uploads'
Extentions = {'txt', 'docx', 'pdf', 'jpg', 'jpeg'}

app= Flask(__name__)
app.secret_key= "Hello"
app.config['Upload_folder'] = Upload_folder



@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        session['Email'] = request.form.get("Email")
        session['Password'] = request.form.get("password")
        flash("Logged in Successfully!")
        return redirect(url_for('uploads'))
    return render_template('login.html')

@app.route("/upload",methods = ["GET","POST"])
def uploads():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        
        if file:
            file_path= os.path.join(app.config["Upload_folder"],secure_filename(file.filename))
            print("file_path:", file_path)
            file.save(file_path)
            return redirect(url_for("display"))
    return render_template('storage.html')  

@app.route("/diplay", methods= ["GET","POST"])
def display():
        folder=app.config['Upload_folder']
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        return render_template('file.html',files = files)
    
@app.route("/logout",methods=["GET","POST"])
def logout():
    session.pop('Email',None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port= 5007, debug= True)



