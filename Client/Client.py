import socket
import select
import cv2



Port=1234
IP="127.0.0.1"
HeadLength=10
# create the socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# set socket options
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# bind port and ip to socket
server_socket.bind((IP, Port))

# turn on listen
server_socket.listen()

# list sockets
sockets_list = [server_socket]

# list clinets
clients = {}

def getMessage(client_socket):

    try:
        # get head
        messageHead=client_socket.recv(HeadLength)
    except
        return False
