from flask import Blueprint, render_template, request, flash, redirect, url_for, session

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("contact", __name__)


@bp.route("/contact", methods=("GET", "POST"))
@login_required
def contact():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        problem = request.form["problem"]
        db = get_db()
        error = None

        if not username:
            error = "Username required."

        if not email:
            error = "Email required."

        if not problem:
            error = "You can't send an empty form."

        if error is None:
            db.execute(
                "INSERT INTO tickets(username, email, problem) VALUES (?, ?, ?)",
                (username, email, problem),
            )
            db.commit()
            return redirect(url_for("index"))

        flash(error)

    return render_template("contact.html")
