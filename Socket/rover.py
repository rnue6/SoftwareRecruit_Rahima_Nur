import os
import socket

# set path to bitmap file
path = os.getcwd()
folder = path + "/Socket"
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

def broadcastImage():
    # creates an endpoint for communication with socket type TCP, connected to the 5 different IP servers
    servers = ["192.168.16.2", "192.168.16.4", "192.168.16.5", "192.168.16.9", "192.168.16.10"]
    endpoints = [] # array to store the endpoints for each server for later sending of the bitmap file
    for ip in servers:
        endpoint = socket.create_connection((ip, 5555))
        endpoints.append(endpoint)

    # send the bitmap file to all servers
    readFile = open(fileName, "rb")
    while True:
        bitInfo = readFile.read(1024)
        if not bitInfo:
            break
        # iterate through endpoints array and send file to every connection
        for endpoint in endpoints:
            endpoint.send(bitInfo)

    readFile.close()

    # close all endpoints after sending the file
    for endpoint in endpoints:
        endpoint.close()

# uncomment to run broadcastImage() function with no receiver
# broadcastImage() 
