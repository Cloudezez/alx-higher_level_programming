from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/route_1':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, world!")
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")

    def do_PUT(self):
        if self.path == '/catch_me':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b"You got me!")
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")

    def do_POST(self):
        if self.path == '/route_json':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            try:
                import json
                json.loads(post_data)
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Valid JSON")
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Not a valid JSON")
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
