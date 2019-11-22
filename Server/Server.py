import socket
import select
import cv2
import numpy as np

Port=1234
IP="127.0.0.1"
HeadLength=10

S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
S.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
S.bind((IP, Port))
S.listen()
socketsList = [S]
Clients = {}
print("Started server")
def getMessage(clientSocket):
    try:
        messageHead=clientSocket.recv(HeadLength)
        if not len(messageHead):
            return False
        messageLength=int(messageHead.decode('utf-8').strip())
        return {'header': messageHead, 'data': clientSocket.recv(messageLength)}
    except:
        return False
while True:
    readSockets,_,exceptionsSockets=select.select(socketsList,[],socketsList)
    for notifySockets in readSockets:
        if notifySockets==S:
            clientSocket,clientAddress=S.accept()
            socketsList.append(clientSocket)
            print("New connection")
        else:
            Message=getMessage(notifySockets)
            print("Recieved message: " + Message["data"].decode("utf-8"))
            image = np.zeros((512, 512, 3))
            cv2.putText(image, Message["data"].decode("utf-8"), (200, 200), 0, 1, 255)
            cv2.imshow('Image', image)
            cv2.waitKey(1)