from pysimplesoap.client import SoapClient, SoapFault
client = SoapClient(
    location = "http://localhost:8000/",
    action = 'http://localhost:8000/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", 
    soap_ns='soap',
    ns = False)
# call the remote method
response = client.HelloWorld(a=2)
# extract and convert the returned value
result = response.Result
print result
