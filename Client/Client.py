import socket
import cv2



Port=1234
IP="127.0.0.1"

# create the socket
client.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# set socket options
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# bind port and ip to socket
server_socket.bind((IP, Port))






