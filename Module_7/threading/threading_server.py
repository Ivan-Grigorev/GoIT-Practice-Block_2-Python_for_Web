import socket
import threading

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(('127.0.0.1', 1235))
soc.listen(5)

users = []


def send_all(data):
    for user in users:
        user.send(data)


def listen_user(user):
    while True:
        data = user.recv(2048)
        print(f'User sent {data}')

        send_all(data)


def start_server():
    while True:
        user_socket, address = soc.accept()
        print(f'User {address[0]} connected')

        users.append(user_socket)
        listen_concurrently = threading.Thread(
            target=listen_user,
            args=(user_socket,))
        listen_concurrently.start()


if __name__ == '__main__':
    start_server()
