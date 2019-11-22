import socket
import select
import cv2
import numpy as np

Port = 1234
IP = "127.0.0.1"
HeadLength = 10
textHeight = 30
image = np.zeros((515, 515, 3))

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
S.bind((IP, Port))
S.listen()
socketsList = [S]
Clients = {}
print("Started server")


def getMessage(clientSocket):
    try:
        messageHead = clientSocket.recv(HeadLength)
        if not len(messageHead):
            return False
        messageLength = int(messageHead.decode('utf-8').strip())
        return {'header': messageHead, 'data': clientSocket.recv(messageLength)}
    except:
        return False


while True:
    readSockets, _, exceptionsSockets = select.select(socketsList, [], socketsList)
    for notifySockets in readSockets:
        if notifySockets == S:
            clientSocket, clientAddress = S.accept()
            socketsList.append(clientSocket)
            print("New connection")
        else:
            Message = getMessage(notifySockets)
            print("Recieved message: " + Message["data"].decode("utf-8"))

            if textHeight >= 530:
                textHeight = 30
                image = np.zeros((515, 515, 3))
            cv2.putText(image, Message["data"].decode("utf-8"), (5, textHeight), 0, 1, 255)
            textHeight += 30
            cv2.imshow("Chat", image)
            cv2.waitKey(1)
