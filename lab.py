from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        name = q.get('name', ['BLUH'])[0]
        # ABSICHTLICH unsicher - nur für eigenes Lab!
        html = f"<h1>Hello {name}</h1><p>Try: ?name=&lt;script&gt;alert(1)&lt;/script&gt;</p>"
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    def log_message(self, *a): pass

HTTPServer(('127.0.0.1', 8000), H).serve_forever()
