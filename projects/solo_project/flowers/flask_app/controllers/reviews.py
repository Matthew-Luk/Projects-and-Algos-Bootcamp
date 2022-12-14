from crypt import methods
from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.review import Review
from flask_app.models.user import User

@app.route("/reviews")
def reviews():
    return render_template("reviews.html", all_reviews=Review.get_all_with_user(), session_id=session["user_id"])

@app.route("/submit_review", methods=["POST"])
def submit_review():
    data = {
        "user_id":session["user_id"],
        "description":request.form["description"]
    }
    if Review.validate_review(request.form):
        Review.save(data)
    return redirect("/reviews")

@app.route("/edit/review/<int:id>")
def edit_review(id):
    data = {
        "id":id
    }
    review = Review.get_by_id(data)
    return render_template("edit_review.html", review = review, session_id=session["user_id"])

@app.route("/update/review", methods=["POST"])
def update_review():
    review = Review.get_by_id({"id":request.form["id"]})
    if not Review.validate_review(request.form):
        return redirect(f"/edit/review/{review.id}")
    Review.update_review(request.form)
    return redirect("/reviews")

@app.route("/delete/review/<int:id>")
def delete_review(id):
    data = {
        "id":id
    }
    Review.delete(data)
    return redirect("/reviews")