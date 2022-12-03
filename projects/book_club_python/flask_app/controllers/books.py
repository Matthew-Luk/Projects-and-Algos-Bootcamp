from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite
from flask_app import app

@app.route("/add_book", methods=["POST"])
def add_book():
    if Book.validate_book(request.form):
        book_id = Book.save(request.form)
        data = {
            "user_id":session["user_id"],
            "book_id":book_id
        }
        Favorite.save(data)
    return redirect("/dashboard")

@app.route("/books/<int:id>")
def view_book(id):
    data = {
        "id":id
    }
    data2 = {
        "id":session["user_id"]
    }
    book = Book.get_by_id(data)
    print(session["user_id"])
    if session["user_id"] == book.users.id:
        return render_template("creator.html", user=User.get_by_id(data2), book=Book.get_by_id(data), all_users=Favorite.get_users_who_favorited(data))
    return render_template("viewer.html", user=User.get_by_id(data2), book=Book.get_by_id(data))

@app.route("/update_description", methods=["POST"])
def update_description():
    print(request.form)
    if Book.validate_book(request.form):
        Book.update(request.form)
    return redirect("/dashboard")