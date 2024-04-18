from flask import Blueprint, render_template, session, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("settings", __name__)


@bp.route("/settings", methods=("GET", "POST"))
@login_required
def settings():
    userId = session.get("userId")

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        old_pass = request.form["oldpass"]
        new_pass = request.form["newpass"]
        db = get_db()
        error = None

        user = db.execute("SELECT * FROM users WHERE id = ?", (userId,)).fetchone()

        # empty strings in python evaluate to False, so if the strings are not "" or None the if statement will work
        if username and username != user["username"]:
            db.execute("UPDATE users SET username = ? WHERE id = ?", (username, userId))
            session["username"] = username
            db.commit()
        if email and email != user["email"]:
            db.execute("UPDATE users SET email = ? WHERE id = ?", (email, userId))
            db.commit()
        if old_pass:
            if check_password_hash(user["password"], old_pass):
                if new_pass:
                    db.execute(
                        "UPDATE users SET password = ? WHERE id = ?",
                        (generate_password_hash(new_pass), userId),
                    )
                    db.commit()
                else:
                    error = "The new password cannot be empty."
            else:
                error = "The password is incorrect."

        if error:
            flash(error)
        else:
            return redirect(url_for("index"))

        return redirect(url_for("settings"))

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE id = ?", (userId,)).fetchone()
    return render_template("settings.html", user=user)
