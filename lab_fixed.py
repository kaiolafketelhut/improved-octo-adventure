import html
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        name = q.get('name', ['BLUH'])[0]
        safe = html.escape(name)  # FIX: XSS weg!
        html_out = f"<h1>Hello {safe}</h1>"
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(html_out.encode())
    def log_message(self, *a): pass

HTTPServer(('127.0.0.1', 8001), H).serve_forever()
