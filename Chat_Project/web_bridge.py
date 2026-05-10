from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import socket
import threading
import webbrowser


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app, cors_allowed_origins='*')

TCP_HOST = 'localhost'
TCP_PORT = 8000

browser_clients = {}


@app.route('/')
def home():
    return render_template('index.html') 

@socketio.on('join')
def join(data):
    alias = data['alias']

    try:
        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_client.connect((TCP_HOST, TCP_PORT))

        first = tcp_client.recv(1024).decode('utf-8')

        if first == 'alias':
            tcp_client.send(alias.encode('utf-8'))

        browser_clients[alias] = tcp_client

        emit('system', {
            'message': f'Connected as {alias}'
        })

        thread = threading.Thread(
            target=receive_messages,
            args=(tcp_client,),
            daemon=True
        )
        thread.start()

    except Exception as e:
        emit('system', {
            'message': str(e)
        }) 

@socketio.on('send_message')
def send_message(data):
    alias = data.get('alias')
    message = data.get('message')

    if not alias or not message:
        return

    try:
        tcp_client = browser_clients.get(alias)

        if tcp_client:
            tcp_client.sendall(message.encode('utf-8'))

            print(f'Sent from {alias}: {message}')

        else:
            emit('system', {
                'message': 'Client connection not found.'
            })

    except Exception as e:
        print(e)

        emit('system', {
            'message': f'Error: {e}'
        })

def receive_messages(tcp_client):
    while True:
        try:
            message = tcp_client.recv(1024)

            if not message:
                break

            decoded_message = message.decode('utf-8').strip()

            print(f'RECEIVED FROM TCP SERVER: {decoded_message}')
            socketio.emit(
                'message',
                {
                    'message': decoded_message
                },
                namespace='/'
            )

        except Exception as e:
            print(f'Receive Error: {e}')
            break

if __name__ == '__main__':
    print('\nOpening browser...\n')

    threading.Timer(
        1.5,
        lambda: webbrowser.open('http://127.0.0.1:5000')
    ).start()

    socketio.run(app, host='0.0.0.0', port=5000) 
