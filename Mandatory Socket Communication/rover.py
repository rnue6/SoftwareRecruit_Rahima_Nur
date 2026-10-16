import os
import socket

# set path to bitmap file
path = os.getcwd()
folder = path + "/Mandatory Socket Communication"
fileName = folder + "/Utah.bmp"

# dunction for reading bitmap file
def read_bmp_file(file):
    readFile = open(file, "rb")

    # read the bitmap file header and DIB header
    bmpHeader = readFile.read(14)
    DIBHeader = readFile.read(40)
    print("BMP Header: ", bmpHeader, "\nDIB Header: ", DIBHeader)
    
    # read the pixel data
    pixelData = readFile.read()

    readFile.close()

read_bmp_file(fileName)