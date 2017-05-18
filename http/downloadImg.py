#!/usr/bin/python3
# coding=utf-8
'''
下载头像
'''

import os
from os import path
from urllib import request
def storeImg(imgUrl,targetPath,userId):
    isExist=os.path.exists(targetPath)
    if isExist !=True :
        #文件夹不存在创建文件夹
        #makedirs是多层目录创建函数 和mkdir的区别是父目录不存在时 mkdir会抛出异常，而makedirs会创建父目录
        os.makedirs(targetPath)
        print("创建文件夹:%s" % targetPath)
    #获取文件保存本地
    targetImg = targetPath + "/" + userId+".jpg"
    #创建文件
    request.urlretrieve(imgUrl,targetImg)
    print("用户:%s头像下载完毕！" % userId)

