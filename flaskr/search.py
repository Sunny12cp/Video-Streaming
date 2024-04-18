from flask import Blueprint, request, redirect, url_for, render_template

from flaskr.auth import login_required, admin_required
from flaskr.db import get_db

bp = Blueprint("search", __name__)


@bp.route("/search/movie", methods=["POST"])
@login_required
def searchMovie():
    movieName = request.form["movie"]
    db = get_db()

    moviesToDisplay = list()
    movies = db.execute("SELECT * from rooms").fetchall()

    for i in movies:
        if movieName in i["title"]:
            moviesToDisplay.append(i)

    return render_template(
        "search.html", movies=moviesToDisplay, term=movieName, type="movie"
    )


@bp.route("/search/user", methods=["POST"])
@login_required
@admin_required
def searchUser():
    userName = request.form["user"]
    db = get_db()

    usersToDisplay = list()
    users = db.execute("SELECT * from users").fetchall()

    for i in users:
        if userName in i["username"]:
            usersToDisplay.append(i)

    return render_template(
        "search.html", users=usersToDisplay, term=userName, type="user"
    )
