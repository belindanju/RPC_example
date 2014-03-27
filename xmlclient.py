__author__ = 'tian'
__status__ = 'In Progress'
__date__ = '3/10/14'


import xmlrpclib

# make the server_ip and server_port known to client 
server_ip = 'localhost'
server_port = 18000

rpc_server = xmlrpclib.ServerProxy("http://%s:%d"%(server_ip, server_port))  # address is a tuple

print rpc_server.system.listMethods()  # list all the available funcs

print rpc_server.add(2,3)
print rpc_server.lookup()
print rpc_server.sub(3,2)
print rpc_server.hello('your name')
