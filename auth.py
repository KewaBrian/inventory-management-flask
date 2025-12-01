from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from extensions import db
from models import User
from forms import LoginForm, RegisterForm
from datetime import datetime

bp = Blueprint("auth", __name__, template_folder="templates")


# ===========================
# LOGIN
# ===========================
@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password.", "danger")
            return redirect(url_for("auth.login"))

        # Update last login AFTER successful login
        user.last_login = datetime.utcnow()
        db.session.commit()

        login_user(user)

        flash("Logged in successfully!", "success")

        next_page = request.args.get("next")
        return redirect(next_page or url_for("main.index"))

    return render_template("login.html", form=form)


# ===========================
# REGISTER
# ===========================
@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Check if username exists
        existing_username = User.query.filter_by(username=form.username.data).first()
        if existing_username:
            flash("Username already taken.", "warning")
            return redirect(url_for("auth.register"))

        # Check email duplicate
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash("Email already in use.", "danger")
            return redirect(url_for("auth.register"))

        # Create user
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            created_at=datetime.utcnow()
        )
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash("Account created! Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


# ===========================
# LOGOUT
# ===========================
@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "info")
    return redirect(url_for("auth.login"))
