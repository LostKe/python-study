#!/usr/bin/python3
# coding=utf-8
'''
爬取吾志用户的头像
url: https://wuzhi.me/u/xxx  需要爬取数据的地址
'''
import asyncio
import requests
import re
import requests.packages.urllib3.util.ssl_
import downloadImg


requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
from bs4 import BeautifulSoup

IMG_STORE_PATH="/wuzhi/img/"
URL_HEAD = "https://wuzhi.me/u/"
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
MAX_USER_ID=272690

def getRes(url_head,user_id):
    url=url_head+str(user_id)
    res=requests.get(url)
    status_code = res.status_code
    if status_code==requests.codes.ok:
        return res
    else:
        print("用户：%s无法访问" % user_id)
        return -1

@asyncio.coroutine
def spider(url_head,user_id):
    res=getRes(url_head,user_id)
    if -1!=res:
        html = res.text.encode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        head = soup.find("head")
        title = soup.find("title")
        print("作者:%s" % title.get_text())
        siderbar_left_div = soup.find("div", {"class", "siderbar_left"})
        #检查图片是否存在
        img=siderbar_left_div.has_attr("src")
        if img!=True:
            print("用户：%s头像不存在" % user_id)
            img_url=None
        else:
            img_url = siderbar_left_div.find("img").attrs["src"]
        print("头像地址:%s" % img_url)
        array_temp = img_url.split("/")
        user_id = array_temp[len(array_temp) - 1].split(".")[0]

        print("用户ID:%s" % user_id)

        flower_count = soup.find(text=re.compile("×")).replace("×", "")
        flower_count = flower_count.strip()
        print("小花数量:%s" % flower_count)
        if img_url!=None:
            downloadImg.storeImg(img_url, IMG_STORE_PATH, user_id)

@asyncio.coroutine
def index_spider():
    for index in range(1,MAX_USER_ID):
        r=yield from asyncio.spider(URL_HEAD,index)



if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(index_spider())
    loop.close()

