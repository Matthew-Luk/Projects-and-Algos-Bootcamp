from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.book import Book
from flask_app import app

@app.route("/add_book", methods=["POST"])
def add_book():
    data = {
        "title":request.form["title"],
        "description":request.form["description"]
    }
    if Book.validate_book(request.form):
        Book.save(data)
    return redirect("/dashboard")

@app.route("/books/<int:id>")
def view_book(id):
    data = {
        "id":id
    }
    data2 = {
        "id":session["user_id"]
    }
    book_id = Book.get_by_id(data)
    print(session["user_id"])
    if session["user_id"] == book_id.user_id:
        return render_template("creator.html", user=User.get_by_id(data2), book=Book.get_by_id(data))
    return render_template("viewer.html", user=User.get_by_id(data2), book=Book.get_by_id(data))