from flask import Blueprint, render_template

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("home", __name__)


@bp.route("/")
@login_required
def index():
    db = get_db()
    rooms = db.execute("SELECT * FROM rooms").fetchall()
    return render_template("home.html", rooms=rooms)
