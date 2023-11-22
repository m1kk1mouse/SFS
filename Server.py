# pyftpdlib docs https://pyftpdlib.readthedocs.io/en/latest/index.html

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
    authorizer.add_user(USER, PASS, DIRECTORY, perm='emwlr')    
        # perm - set permission:
        # "e" = change directory (CWD, CDUP commands)
        # "m" = create directory (MKD command)
        # "w" = store a file to the server (STOR, STOU commands)
        # "l" = list files (LIST, NLST, STAT, MLSD, MLST, SIZE commands)
        # "r" = retrieve file from the server (RETR command)

    handler = FTPHandler
    handler.log_prefix = 'XXX [%(username)s]@%(remote_ip)s' #Adds extended logs
    handler.authorizer = authorizer
    handler.banner = "Welcome to my FTP server"

    address = (ADDRESS, PORT)
    server = FTPServer(address, handler)

    server.max_cons = 100   #Maximum number of server connections
    server.max_cons_per_ip = 5  #Maximum number of server connections from a single IP
    handler.max_login_attempts = 2  #Maximum number of sign-in attempts

    server.serve_forever()  #Prevents the server from shutting down automatically

if __name__ == '__main__':
    main()