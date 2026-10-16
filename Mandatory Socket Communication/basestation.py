import socket

# function for reading bitmap file
def read_bmp_file():
    # listen for incoming connections on port 5555
    serverConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverConnection.bind(("127.0.0.1", 5555))
    print("Waiting for connection...")
    serverConnection.listen(1)

    # accept the incoming connection
    connection, address = serverConnection.accept()
    print(f"Connection established with {address}")

    outputFile = open("output.bmp", "wb")
    while True:
        # recieve data in chunks of 1024 bytes, break loop if no bytes remaining
        chunkRecv = connection.recv(1024)
        if not chunkRecv:
            break
        outputFile.write(chunkRecv)

    outputFile.close()
    connection.close()
    serverConnection.close()

read_bmp_file()