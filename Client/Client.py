import socket
import cv2
import sys

# Defines the Port and IP
Port = 1234
IP = "127.0.0.1"
HeadLength = 10

C = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C.connect((IP, Port))

while True:
    # Client can write messages and send them
    Message = input("")
    try:
        if Message:
            Message = Message.encode('utf-8')
            messageHeader = f"{len(Message):<{HeadLength}}".encode('utf-8')
            C.send(messageHeader + Message)
    except Exception as ex:
        sys.exit()
