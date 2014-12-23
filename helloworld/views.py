from django.shortcuts import render

# Create your views here.
# A simple views.py file sample for dispatcher
from pysimplesoap.server import SoapDispatcher
from django.http import HttpResponse

# just a remote function ;)

def HelloWorld(a):
    "Add two values"
    return "helloworld\n"*a
dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8000/",
    action = 'http://localhost:8000/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    ns = True)
dispatcher.register_function('HelloWorld', HelloWorld,
    returns={'Result': str},
    args={'a': int})

def dispatcher_handler(request):
    if request.method == "POST":
        response = HttpResponse(mimetype="application/xml")
        response.write(dispatcher.dispatch(request.body))
    else:
        response = HttpResponse(mimetype="application/xml")
        response.write(dispatcher.wsdl())
    response['Content-length'] = str(len(response.content))
    return response