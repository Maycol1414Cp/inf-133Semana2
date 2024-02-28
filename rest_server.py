from http.server import BaseHTTPRequestHandler, HTTPServer
import json
estudiantes =[{
    "id":1,
    "nombre":"Pedrito",
    "apellido":"Garcia ",
    "edad":20
}]
class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/estudiantes":
            self.get_estudiantes()
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
def run_server (port=8000):
    try:
        server_address = ('',port)
        httpd = HTTPServer(server_address,RESTRequestHandler)
        print(f"Servidor corriendo en el puerto {port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Servidor detenido")
        httpd.server.close()