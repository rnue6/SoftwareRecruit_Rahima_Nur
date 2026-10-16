import os
import socket

# set path to bitmap file
path = os.getcwd()
folder = path + "/Mandatory Socket Communication"
fileName = folder + "/Utah.bmp"

# function for sending bitmap file
def send_bmp (file):
    readFile = open(file, "rb")
    
    # creates an endpoint for communication with socket type TCP, connected to the server at 127.0.0.1 on port 5555
    commEndpoint = socket.create_connection(("127.0.0.1", 5555))
    
    while True:
        # send bitinfo in chunks until there is nothing to send
        bitInfo = readFile.read(1024)
        if not bitInfo:
            break
        commEndpoint.send(bitInfo)

    readFile.close()
    commEndpoint.close()


send_bmp(fileName)
