from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'cibertec123'

socketio = SocketIO(app)


# modelo Message
# flask-migrate


@app.route("/")
def home():
    # todos los mensajes pasados
    return render_template('home.html')


def messagesReceived(methods=["GET", "POST"]):
    print("message was received")


@socketio.on('messages')
def handle_messages(json, methods=["GET", "POST"]):
    # guarde en base de datos
    print('received json: ' + str(json))
    socketio.emit("responses-messages", json, callback=messagesReceived)


@socketio.on('welcome')
def handle_welcome(json, methods=["GET", "POST"]):
    print('received json: ' + str(json))
    socketio.emit("responses-welcome", json, callback=messagesReceived)


if __name__ == '__main__':
    socketio.run(app)