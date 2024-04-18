from flask import Blueprint, render_template

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("video", __name__)


@bp.route("/video/<invite>")
@login_required
def video(invite):
    db = get_db()
    room = db.execute("SELECT * FROM rooms WHERE invite = ?", (invite,)).fetchone()
    return render_template("video.html", room=room)
