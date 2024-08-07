#!/usr/bin/python3
"""
A simple HTTP server that serves files from the current directory and handles custom routes.
"""

import http.server
import socketserver
from urllib.parse import parse_qs

PORT = 5000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom request handler to manage specific routes and methods.
    """
    def do_GET(self):
        if self.path == '/route_json':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = '{"message": "Hello, JSON!"}'
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/catch_me':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = '{"message": "You caught me!"}'
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/status_401':
            self.send_response(401)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = "<html><body><h1>401 Unauthorized</h1></body></html>"
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/status_500':
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = "<html><body><h1>500 Internal Server Error</h1></body></html>"
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = "<html><body><h1>404 Not Found</h1></body></html>"
            self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        if self.path == '/post_email':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)
            email = params.get('email', [''])[0]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = f"Your email is: {email}"
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = "<html><body><h1>404 Not Found</h1></body></html>"
            self.wfile.write(response.encode('utf-8'))

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

