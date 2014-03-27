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
    def __init__(self, name):
        self.name = name 
           
    def lookup(self):  # an instance function takes no args, but return a string
        return "my name is %s" % self.name

    def add(self, x, y):  # an instance function takes args, returns integer
        return x + y


# module level function
def substract(x,y):
        return x - y 

def hello(name):
        return "hello %s" % name

if __name__ == '__main__':
    # start a XMLRPCServer that could handle RPC requests
    server = SimpleXMLRPCServer((server_ip, server_port), requestHandler=RequestHandler)
    server.register_introspection_functions()  # important! 
                      
    # register instances, all the functions inside is available
    server.register_instance(MyXMLServer('simple server'))
    
    # register functions
    server.register_function(substract, 'sub')  # expose substract as function sub
    server.register_function(hello, 'hello')
    
    server.serve_forever()  # start the server 
