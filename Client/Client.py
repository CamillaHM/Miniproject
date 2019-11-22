import socket
import sys

# Defines the Port and IP
Port = 1234
IP = "127.0.0.1"
HeadLength = 10
# Create client socket as C
C = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C.connect((IP, Port))

# Client can write messages and send them
while True:
    # wait for user input
    Message = input("")
    try:
        # send message
        if Message:
            # encode to bytes
            Message = Message.encode('utf-8')
            messageHeader = f"{len(Message):<{HeadLength}}".encode('utf-8')
            # send
            C.send(messageHeader + Message)
    # exit on exception
    except Exception as ex:
        sys.exit()
