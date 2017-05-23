#!/usr/bin/python3
# coding=utf-8
'''
下载头像
'''

import os
import requests
import requests.packages.urllib3.util.ssl_
import db

def storeImg(user_name,signature,imgUrl,targetPath,userId,flower_count):
    isExist=os.path.exists(targetPath)
    if isExist !=True :
        #文件夹不存在创建文件夹
        #makedirs是多层目录创建函数 和mkdir的区别是父目录不存在时 mkdir会抛出异常，而makedirs会创建父目录
        os.makedirs(targetPath)
        print("创建文件夹:%s" % targetPath)
    #获取文件保存本地
    targetImg = targetPath  + userId+".jpg"
    #创建文件
    req=requests.Session()
    req.headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res=req.get(imgUrl)
    with open(targetImg,"wb") as f:
        f.write(res.content)
        print("用户:%s头像下载完毕！" % userId)
    db.inserUser(user_name,signature,userId,userId+".jpg",flower_count)


