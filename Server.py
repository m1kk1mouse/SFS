import signal
import sys
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

ADDRESS = '127.0.0.1'
PORT = 5454
USER = "q"
PASS = "qwerty"
DIRECTORY = "/home/q/ftp"

print (" _____ _____ ____ ")
print ("|  ___|_   _|  _ \ ")
print ("| |_    | | | |_) |")
print ("|  _|   | | |  __/ ")
print ("|_|     |_| |_|  ")
print ("")
print('The server is running on {host} use port {port} ...'.format(host=ADDRESS,port=PORT))
print("To stop the server, press Ctrl+C")

def signal_handler(signal, frame):
    print("")
    print("You press Ctrl+C, server is stopped. Bye <3 ")
    sys.exit(0)

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
    signal.signal(signal.SIGINT, signal_handler)
    server.serve_forever()  #Prevents the server from shutting down automatically

if __name__ == '__main__':
    main()
