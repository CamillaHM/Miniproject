import socket
import cv2
import sys

Port = 1234
IP = "127.0.0.1"
HeadLength = 10

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, Port))
clientSocket.setblocking(False)

while True:
    Message = input(f'')
    if Message:
        Message = Message.encode('utf-8')
        messageHeader = f"{len(Message):<{HeadLength}}".encode('utf-8')
        clientSocket.send(messageHeader + Message)

    try:
        while True:
            usernameHeader = clientSocket.recv(HeadLength)

            if not len(usernameHeader):
                print("closed by server")
                sys.exit()
            messageHeader = clientSocket.recv(HeadLength)
            messageLength = int(messageHeader.decode('utf-8').strip())
            message = clientSocket.recv(messageLength).decode('utf-8')

    except Exception as IOError:
        sys.exit()