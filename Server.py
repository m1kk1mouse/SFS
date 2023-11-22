#pyftpdlib docs https://pyftpdlib.readthedocs.io/en/latest/index.html

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

print (" _____ _____ ____ ")
print ("|  ___|_   _|  _ \ ")
print ("| |_    | | | |_) |")
print ("|  _|   | | |  __/ ")
print ("|_|     |_| |_|  ")
print ("")

ADDRESS = '127.0.0.1'
PORT = 5454
USER = "q"
PASS = "qwerty"
DIRECTORY = "/home/q/ftp"

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(USER, PASS, DIRECTORY, perm='w')    #Perm set permission, w - only write

    handler = FTPHandler
    handler.log_prefix = 'XXX [%(username)s]@%(remote_ip)s' #Adds extended logs
    handler.authorizer = authorizer

    address = (ADDRESS, PORT)
    server = FTPServer(address, handler)

    server.max_cons = 100   #Maximum number of server connections
    server.max_cons_per_ip = 1  #Maximum number of server connections from a single IP
    handler.max_login_attempts = 2  #Maximum number of sign-in attempts

    server.serve_forever()  #Prevents the server from shutting down automatically

if __name__ == '__main__':
    main()