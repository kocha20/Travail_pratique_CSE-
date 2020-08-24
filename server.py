from http.server import HTTPServer, BaseHTTPRequestHandler

class Server (BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = '/Equador.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open("File Not Found")
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
    
    def do_POST(self):
        if self.path == "/":
            self.path = '/Equador.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open("File Not Found")
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_PUT(self):
        if self.path == "/":
            self.path = '/Equador.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open("File Not Found")
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
    
    def do_DELETE(self):
        if self.path == "/":
            self.path = '/Equador.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open("File Not Found")
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 80), Server)
httpd.serve_forever()