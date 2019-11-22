import socket
import select
import cv2



Port=1234
IP="127.0.0.1"
HeadLength=10
# create the socket
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# set socket options
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# bind port and ip to socket
serverSocket.bind((IP, Port))

# turn on listen
serverSocket.listen()

# list sockets
socketsList = [serverSocket]

# list clinets
Clients = {}

def getMessage(clientSocket):

    try:
        # get head
        messageHead=clientSocket.recv(HeadLength)
        if not len(messageHead):
            return False
        # make into int
        messageLength=int(messageHead.decode('utf-8').strip())

        return
    except:
        return False


while True:
    readSockets,_,exceptionsSockets=select.select(socketsList,[],socketsList)