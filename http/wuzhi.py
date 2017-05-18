#!/usr/bin/python3
# coding=utf-8
'''
爬取吾志用户的头像
url: https://wuzhi.me/u/xxx  需要爬取数据的地址
'''
import requests
import re
import requests.packages.urllib3.util.ssl_
import downloadImg


requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
from bs4 import BeautifulSoup

IMG_STORE_PATH="/wuzhi/img/"
URL_HEAD = "https://wuzhi.me/u/43013"
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
response = requests.get(URL_HEAD)
html = response.text.encode("utf-8")

soup = BeautifulSoup(html, "html.parser")
head = soup.find("head")
title = soup.find("title")
# print(head)
print("作者:%s" % title.get_text())

siderbar_left_div = soup.find("div", {"class", "siderbar_left"})
img_url = siderbar_left_div.find("img").attrs["src"]
print("头像地址:%s" % img_url)


array_temp=img_url.split("/")
user_id=array_temp[len(array_temp)-1].split(".")[0]

print("用户ID:%s" % user_id)

flower_count=soup.find(text=re.compile("×")).replace("×","")
flower_count=flower_count.strip()
print("小花数量:%s" % flower_count)

downloadImg.storeImg(img_url,IMG_STORE_PATH,user_id)