#!/usr/bin/python3

# https://pythonbasics.org/webserver/

from http.server import BaseHTTPRequestHandler, HTTPServer
import time


myhost = ''
myport = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes('<p></p>', 'utf-8'))
        self.wfile.write(bytes('<div>', 'utf-8'))
        self.wfile.write(bytes('<object type="text/html" data="http://validator.w3.org/" width="800px" height="600px" style="overflow:auto;border:5px ridge blue">', 'utf-8'))
        self.wfile.write(bytes('</object>', 'utf-8'))
        self.wfile.write(bytes('</div>', 'utf-8'))
        self.wfile.write(bytes('<iframe src="http://192.168.68.109:8081/index.html" width="1920" height="1080"></iframe>', 'utf-8'))
        self.wfile.write(bytes('<iframe src="http://192.168.68.105:8000/index.html" width="1920" height="1080"></iframe>', 'utf-8'))
        self.wfile.write(bytes('<iframe src="http://192.168.68.110:8000/index.html" width="1920" height="1080"></iframe>', 'utf-8'))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webserver = HTTPServer((myhost, myport), MyServer)
    print("Server started http://%s:%s" % (myhost, myport))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")






