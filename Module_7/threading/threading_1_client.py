import socket
import threading

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(("127.0.0.1", 1235))


def listen_server():
    while True:
        data = soc.recv(4096)
        print(data.decode("UTF-8"))


def send_server():
    listen_thread = threading.Thread(target=listen_server)
    listen_thread.start()
    while True:
        soc.send(input().encode("UTF-8"))


if __name__ == '__main__':
    send_server()
