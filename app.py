from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from flask import Flask, request

app = Flask(__name__)

class HelloWorldService(ServiceBase):
    @rpc(_returns=str)
    def say_hello(ctx):
        return "Hola, Mundo!"

soap_application = Application(
    [HelloWorldService],
    tns='urn:spyne.examples.hello',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_application)

@app.route('/')
def hello():
    return "Servicio SOAP corriendo. Accede a /soap para usar el servicio."

@app.route('/soap', methods=['GET', 'POST'])
def soap():
    if request.method == 'POST':
        return wsgi_app()  # Procesa la solicitud SOAP
    else:
        return "Accede a esta URL usando el método POST para consumir el servicio SOAP."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
