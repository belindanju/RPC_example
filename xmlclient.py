__author__ = 'tian'
__status__ = 'In Progress'
__date__ = '3/10/14'


import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:18000')

print s.system.listMethods()

print s.adder_function(2,3)

#print s.add(2,3)

print s.lookup()

print s.sub(3,2)
print s.hello('your name')
