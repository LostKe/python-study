# coding=utf-8
# 接收文件
import socket
import threading
import os
import sys
import math

bindIp = "0.0.0.0"
bindPort = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bindIp, bindPort))
server.listen(1)
print("Listening on %s:%d" % (bindIp, bindPort))


def progressbar(cur, total):
    percent = '{:.2%}'.format(float(cur) / float(total))
    sys.stdout.write('\r')
    sys.stdout.write("[%-50s] %s" % ( '=' * int(math.floor(cur * 50 / total)), percent))
    sys.stdout.flush()

def checkFileName(originalFileName):
    extensionIndex = originalFileName.rindex(".")
    name = originalFileName[:extensionIndex]
    extension = originalFileName[extensionIndex + 1:]
    index = 1
    newNameSuffix = "(" + str(index) + ")"
    finalFileName = originalFileName
    if os.path.exists(finalFileName):
        finalFileName = name + " " + newNameSuffix + "." + extension
    while os.path.exists(finalFileName):
        index += 1
        oldSuffix = newNameSuffix
        newNameSuffix = "(" + str(index) + ")"
        finalFileName = finalFileName.replace(oldSuffix, newNameSuffix)
    return finalFileName


def handleClient(clientSocket):
    # receive file size
    fileSize = int(clientSocket.recv(1024).decode())
    # print "[<==] File size received from client: %d" % fileSize
    clientSocket.send("Received".encode())
    # receive file name
    fileName = clientSocket.recv(1024)
    # print "[<==] File name received from client: %s" % fileName
    clientSocket.send("Received".encode())
    fileName = checkFileName(fileName)
    file = open(fileName, 'wb')
    # receive file content
    print("[==>] Saving file to %s" % fileName)
    receivedLength = 0
    while receivedLength < fileSize:
        bufLen = 1024
        if fileSize - receivedLength < bufLen:
            bufLen = fileSize - receivedLength
        buf = clientSocket.recv(bufLen)
        file.write(buf)
        receivedLength += len(buf)
        process = int(float(receivedLength) / float(fileSize) * 100)
        progressbar(process, 100)
    file.close()
    print("\r\n[==>] File %s saved." % fileName)
    clientSocket.send("Received".encode())

while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    clientHandler = threading.Thread(target=handleClient, args=(client,))
    clientHandler.start()