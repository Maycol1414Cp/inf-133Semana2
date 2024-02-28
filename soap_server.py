from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "!Hola {}!".format(nombre)
dispatcher=SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8008/",
    action="http://localhost:8008/",
    namespace="http://localhost:8008/",
    trace=True,
    ns=True,
)
dispatcher.register_function(
    "saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str}
)
try:
    server=HTTPServer(("localhost",8008),SOAPHandler)
    server.dispatcher=dispatcher
    print("Servidor corriendo en el puerto 8008")
    server.serve_forever()
except KeyboardInterrupt:
    print("Servidor detenido")
    server.server_close()