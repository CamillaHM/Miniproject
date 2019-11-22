import socket
import select
import cv2



Port=1234
IP="127.0.0.1"
HeadLength=10

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serverSocket.bind((IP, Port))
serverSocket.listen()
socketsList = [serverSocket]
Clients = {}

def getMessage(clientSocket):
    try:
        messageHead=clientSocket.recv(HeadLength)
        if not len(messageHead):
            return False
        messageLength=int(messageHead.decode('utf-8').strip())
        return
    except:
        return False

while True:
    readSockets,_,exceptionsSockets=select.select(socketsList,[],socketsList)
    for notifySockets in readSockets:
        if notifySockets==serverSocket:
            clientSocket,clientAddress=serverSocket.accept()