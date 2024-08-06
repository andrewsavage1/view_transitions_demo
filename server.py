import http.server
import socketserver

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set custom headers here
        self.send_header('X-Frame-Options', 'ALLOW-FROM https://www.youtube.com')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        # Call the superclass's end_headers method to ensure headers are sent
        super().end_headers()

with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
