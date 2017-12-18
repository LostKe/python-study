#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 16:10
# @Author  : zsaq
# @Site    : 
# @File    : read_file.py
# @Software: PyCharm
# @desc    : 读取文件发送

# -*-encoding:utf-8-*-
import socket

import os
import sys
import math
import time


def progressbar(cur, total):
    percent = '{:.2%}'.format(float(cur) / float(total))
    sys.stdout.write('\r')
    sys.stdout.write("[%-50s] %s" % ('=' * int(math.floor(cur * 50 / total)), percent))
    sys.stdout.flush()


def getFileSize(file):
    file.seek(0, os.SEEK_END)
    fileLength = file.tell()
    file.seek(0, 0)
    return fileLength


def byteToStr(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_byte(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


def getFileName(fileFullPath):
    index = fileFullPath.rindex('\\')
    if index == -1:
        return fileFullPath
    else:
        return fileFullPath[index + 1:]


def transferFile():
    fileFullPath = r"%s" % input("File path: ").strip("\"")
    if os.path.exists(fileFullPath):
        time_start = time.clock()
        file = open(fileFullPath, 'rb')
        file_size = getFileSize(file)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((targetHost, targetPort))
        # send file size
        client.send(str(file_size).encode())
        response = client.recv(1024)
        # send file name
        client.send(getFileName(fileFullPath))
        response = client.recv(1024)
        # send file content
        sentLength = 0
        while sentLength < file_size:
            bufLen = 1024
            buf = file.read(bufLen)
            client.send(buf)
            sentLength += len(buf)
            process = int(float(sentLength) / float(file_size) * 100)
            progressbar(process, 100)
        client.recv(1024)
        file.close()
        timeEnd = time.clock()
        print("\r\nFinished, spent %d seconds" % (timeEnd - time_start))

    else:
        print("File doesn't exist")


targetHost = input("Server IP Address: ")

targetPort = int(input("Server port: "))

while True:
    transferFile()
