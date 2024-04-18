from flask import Blueprint, render_template, session, request, url_for, redirect, flash
import uuid
import os

from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr.thumbnail import make_thumbnail

bp = Blueprint("create", __name__)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        movie = request.files["movie"]
        error = None

        if not title:
            error = "The title can't be empty."
        elif not movie:
            error = "You need to submit a mp4 file."
        elif not movie.filename.endswith(".mp4"):
            error = "You can only submit mp4 files."
        else:
            path = os.getcwd() + "/flaskr/static/videos/" + str(session.get("userId"))

            if not os.path.isdir(path):
                os.mkdir(path)

            filename = str(uuid.uuid4())
            invite = str(uuid.uuid4())

            movie.save(f"{path}/{filename}.mp4")
            make_thumbnail(f"{path}/{filename}.mp4", f"{path}/{filename}.png")

            db = get_db()
            db.execute(
                "INSERT INTO rooms (userId, invite, title, filename) VALUES (?, ?, ?, ?)",
                (session.get("userId"), invite, title, filename),
            )
            db.commit()

            return redirect(url_for("index"))

        flash(error)

        return render_template("create.html")

    return render_template("create.html")
