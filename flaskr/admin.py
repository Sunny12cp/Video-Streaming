from flask import Blueprint, render_template, request, flash, redirect, url_for, session

from flaskr.auth import login_required, admin_required
from flaskr.db import get_db

bp = Blueprint("admin", __name__)


@bp.route("/admin/users", methods=("GET", "POST"))
@login_required
@admin_required
def users():
    db = get_db()

    if request.method == "POST":
        user = request.form["userDelete"]
        db.execute("DELETE FROM users WHERE id = ?", user)
        db.commit()

    users = db.execute("SELECT * FROM users").fetchall()
    return render_template("users.html", users=users)


@bp.route("/admin/tickets", methods=("GET", "POST"))
@login_required
@admin_required
def tickets():
    db = get_db()

    if request.method == "POST":
        ticket = request.form["ticketDelete"]
        db.execute("DELETE FROM tickets WHERE id = ?", ticket)
        db.commit()

    tickets = db.execute("SELECT username, email, problem, id FROM tickets").fetchall()
    return render_template("tickets.html", tickets=tickets)
