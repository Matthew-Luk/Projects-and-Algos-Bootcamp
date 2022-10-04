from flask import redirect, render_template, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "password":pw_hash
    }
    user_id = User.save(data)
    session["user_id"] = user_id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", session_id=session["user_id"])

@app.route("/login", methods=["POST"])
def login():
    if not User.validate_login(request.form):
        return redirect("/")
    user = User.get_by_email(request.form)
    if user:
        if not bcrypt.check_password_hash(user.password, request.form["password"]):
            flash("The password you've entered is incorrect.")
            return redirect("/")
        session["user_id"] = user.id
        return redirect("/dashboard")
    flash("The email you entered isn't connected to an account. Find your account and log in.")
    return redirect("/")

@app.route("/edit_profile/<int:id>")
def edit_profile(id):
    data = {
        "id":session["user_id"]
    }
    user = User.get_by_id(data)
    return render_template("edit_profile.html", user = User.get_by_id(data))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")