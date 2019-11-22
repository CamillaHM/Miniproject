import socket
import select
import cv2
import numpy as np

# Defines the Port and IP
Port = 1234
IP = "127.0.0.1"
HeadLength = 10
textHeight = 30
# Create a black image
image = np.zeros((515, 515, 3))
# Create socket as S
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set options of socket
S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind it to IP and Port
S.bind((IP, Port))
# Listen for connections
S.listen()
socketsList = [S]
Clients = {}
print("Started server")


def getMessage(clientSocket):
    try:
        # Get message length
        messageHead = clientSocket.recv(HeadLength)
        if not len(messageHead):
            return False
        # Convert it to int
        messageLength = int(messageHead.decode('utf-8').strip())
        return {'header': messageHead, 'data': clientSocket.recv(messageLength)}
    except:
        return False


while True:
    # Gets the list sockets which are ready to be read through select
    readSockets, _, exceptionsSockets = select.select(socketsList, [], socketsList)
    for notifySockets in readSockets:
        # If a new connection request is received
        if notifySockets == S:
            # The new connection is accepted
            clientSocket, clientAddress = S.accept()
            socketsList.append(clientSocket)
            print("New connection")
            # If a message from a client is received
        else:
            # Get that message
            Message = getMessage(notifySockets)
            print("Received message: " + Message["data"].decode("utf-8"))
            # If the text is going out of bounds of image, reset height
            if textHeight >= 530:
                textHeight = 30
                image = np.zeros((515, 515, 3))
            # Put the received text in image
            cv2.putText(image, Message["data"].decode("utf-8"), (5, textHeight), 0, 1, 255)
            # Add height for new line
            textHeight += 30
            # Show chat
            cv2.imshow("Chat", image)
            cv2.waitKey(1)
