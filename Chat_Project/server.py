import socket
import threading
import time

HOST = 'localhost'
PORT = 8000

clients = []
aliases = []


def broadcast(message):
    for client in clients:
        try:
            client.sendall((message + '\n').encode('utf-8'))
        except:
            pass


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            message = message.decode('utf-8').strip()

            if not message:
                break

            alias = aliases[clients.index(client)]

            now = time.strftime('%H:%M:%S')
            final_message = f'[{now}] [{alias}] {message}'

            print(final_message)

            print(f'BROADCASTING: {final_message}')

            broadcast(final_message)

        except:
            if client in clients:
                index = clients.index(client)

                alias = aliases[index]

                clients.remove(client)
                aliases.remove(alias)

                broadcast(f'{alias} left the chat.')

                client.close()

            break


def receive():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen()

    print(f'\nServer running on {HOST}:{PORT}\n')

    while True:
        client, address = server.accept()

        print(f'Connected with {str(address)}')

        client.send('alias'.encode('utf-8'))

        alias = client.recv(1024).decode('utf-8')

        aliases.append(alias)
        clients.append(client)

        print(f'Alias: {alias}')

        broadcast(f'{alias} joined the chat.')

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()


receive() 
