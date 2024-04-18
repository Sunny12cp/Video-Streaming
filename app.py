from flaskr import create_app
from flask import session, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = create_app()
socketio = SocketIO(app)


@socketio.on("join")
def join(room):
    if session.get("room"):
        leave_room(room)
    join_room(room)
    session["room"] = room


@socketio.on("check")
def handle_check(data):
    emit("check", data, room=data["room"])


@socketio.on("addMsg")
def addMsg(msg):
    username = session.get("username")
    text = f"{username}: {msg}"
    emit("displayMsg", text, room=session.get("room"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    socketio.run(app=app, host="0.0.0.0", port=5000, debug=True)
