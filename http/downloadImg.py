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
        os.mkdir(targetPath)
        print("创建文件夹:%s" % targetPath)
    #获取文件保存本地
    targetImg = targetPath + "/" + userId+".jpg"
    #创建文件

    with request.urlopen(imgUrl) as _data:
        with open(targetPath,'wb') as outfile:
            outfile.write(_data.read())
    print("用户:%s头像下载完毕！" % userId)

