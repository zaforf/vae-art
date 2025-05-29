from http.server import SimpleHTTPRequestHandler, HTTPServer

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    port = 8000
    server = HTTPServer(('0.0.0.0', port), NoCacheHandler)
    print(f"Serving at http://localhost:{port} with no cache")
    server.serve_forever()
