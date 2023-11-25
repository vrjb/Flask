# 7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.

from flask import Flask,request, render_template, flash,redirect, url_for
import sqlite3 as s
import os

app = Flask(__name__)

def get_db():
        conn = s.connect("database.db")
        conn.row_factory = s.Row
        return conn
    
@app.route('/')
def view_list():
    with get_db() as db1:
        cursor = db1.cursor()
        cursor.execute("SELECT * FROM to_do")
        tasks=cursor.fetchall()
    return render_template('home1.html',tasks = tasks)

@app.route('/add', methods= ["POST"])
def add():
    Task = request.form.get('Task')
    Assignee = request.form.get('Assignee')
    Notes = request.form.get('Notes')
    Status = request.form.get('Status')
    with get_db() as db1:
        cursor = db1.cursor()
        cursor.execute('INSERT INTO to_do (Task, Assignee, Notes, Status) VALUES (?,?,?,?)',(Task, Assignee, Notes, Status))
        db1.commit()
    # db.close()
    return redirect(url_for('view_list'))

@app.route('/update/<int:id>', methods = ["POST"])
def update(id):
    new_Task = request.form.get('new_Task')
    new_Assignee = request.form.get('new_Assignee')
    new_Note = request.form.get('new_Note')
    new_Status = request.form.get('new_Status')
    with get_db() as db1:
        cursor = db1.cursor()
        cursor.execute('UPDATE to_do SET Task = ?, Assignee = ?, Notes = ?, Status=? WHERE id =?', (new_Task, new_Assignee, new_Note, new_Status, id))
        db1.commit()
    # db.close()
    return redirect(url_for('view_list'))

@app.route("/delete/<int:id>")
def delete(id):
     with get_db() as db1:
        cursor = db1.cursor()
        cursor.execute('DELETE FROM to_do WHERE id =?', (id,))
        db1.commit()
    #  db.close()
     return redirect(url_for('view_list'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5013', debug= True)




