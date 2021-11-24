from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.ext import declarative

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


def addToDo(title, desc):
    todo = Todo(title=title, description=desc)
    db.session.add(todo)
    db.session.commit()


def updateToDo(id, title, desc):
    todo = Todo.query.filter_by(id=id).first()
    todo.title = title
    todo.description = desc
    db.session.add(todo)
    db.session.commit()


def deleteToDo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()


def loadAndRedirectToList():
    allTodos = Todo.query.all()
    return render_template("todolist.html", allTodos=allTodos)


@app.route("/", methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['description']

        addToDo(title, desc)

        return loadAndRedirectToList()

    return render_template("index.html")


@app.route("/todo")
def todo():
    return render_template("index.html")


@app.route("/todo/list")
def todolist():
    return loadAndRedirectToList()


@app.route("/todo/delete/<int:id>")
def delete(id):
    deleteToDo(id)
    return loadAndRedirectToList()


@app.route("/todo/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['description']

        updateToDo(id, title, desc)

        return loadAndRedirectToList()

    todo = Todo.query.filter_by(id=id).first()
    return render_template("update.html", todo=todo)
    
if __name__ == "__main__":
    app.run(debug=True)
