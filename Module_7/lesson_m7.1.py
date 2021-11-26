import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888))
sock.send(b'Some message')
sock.close()


########################
# An example script to connect to Google using socket
# programming in Python
import socket  # for socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")


port = 80

host_ip = socket.gethostbyname('www.google.com')

# connecting to the server
s.connect((host_ip, port))

print(f"the socket has successfully connected to google on {host_ip}, {port}")


###########################
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(3)

while True:
    try:
        client, address = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print("message: ", result.decode('utf-8') )


##############################
import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(("127.0.0.1", 1235))


def start_client():
    while True:
        soc.send(input("print something").encode('utf-8'))

        data = soc.recv(4096)
        print(data.decode("utf-8"))


if __name__ == '__main__':
    start_client()


#################################
import socket

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
        print(f'user {address[0]} connected')

        users.append(user_socket)
        listen_user(user_socket)


if __name__ == '__main__':
    start_server()


############################
import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(("127.0.0.1", 1235))


def start_client():
    while True:
        soc.send(input("print something").encode('utf-8'))

        data = soc.recv(4096)
        print(data.decode("utf-8"))


if __name__ == '__main__':
    start_client()


############################
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
