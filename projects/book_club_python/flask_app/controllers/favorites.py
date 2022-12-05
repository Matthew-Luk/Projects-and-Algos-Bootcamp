from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite
from flask_app import app

@app.route("/add_to_favorites", methods=["POST"])
def add_to_favorites():
    data = {
        "user_id":session["user_id"],
        "book_id":request.form["book_id"]
    }
    Favorite.save(request.form)
    return redirect("/dashboard")