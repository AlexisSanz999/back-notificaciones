from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app, origins=['http://localhost:3000', 'http://192.168.100.2:3000'])

@app.route('/message', methods=['POST'])
def handle_json_message():
    data = request.json
    message = data['message']
    socketio.emit('response', message, include_self=True)
    return {'status': 'success'}


if __name__ == '__main__':
    # Iniciar el servidor de desarrollo Flask
    socketio.run(app, host='0.0.0.0', port=5000)
