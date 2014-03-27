__author__ = 'tian'
__status__ = 'In Progress'
__date__ = '3/10/14'


from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

server_ip = 'localhost'
server_port = 18000


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class MyXMLServer():
#    def __init__(self):
           
    def lookup(self):
            return 'dns lookup'

    def adder_function(self, x, y):
        return x + y


def substract(x,y):
        return x - y 

def hello(name):
        return "hello %s" % name

server = SimpleXMLRPCServer((server_ip, server_port), requestHandler=RequestHandler)
server.register_introspection_functions()
                                                                                                   
#server.register_function(self.lookup(), 'lookup')
server.register_instance(MyXMLServer())
server.register_function(substract, 'sub')
server.register_function(hello, 'hello')
server.serve_forever()
