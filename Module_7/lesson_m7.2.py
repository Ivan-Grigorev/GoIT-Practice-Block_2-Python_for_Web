from jinja2 import Template


class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def getAge(self):
        return self.age

    def getName(self):
        return self.name


person = Person('Peter', 34, "Kiev")

tm = Template("My name is {{ per.getName() }} and I am {{ per.getAge() }}. I live at {{per.address}}")
msg = tm.render(per=person)

print(msg)


###############################
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from io import BytesIO


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Server working, and its simple"

        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


if __name__ == '__main__':
    run(handler_class=Handler)
