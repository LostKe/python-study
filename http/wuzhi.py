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

IMG_STORE_PATH = "/Users/zhangshuqing/wuzhi/img/"
URL_HEAD = "https://wuzhi.me/u/"
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
MAX_USER_ID = 272690


def getRes(url_head, user_id):
    url = url_head + str(user_id)
    res = requests.get(url, allow_redirects=False)
    status_code = res.status_code
    if status_code != 302:
        return res
    else:
        print("用户：%s无法访问" % user_id)
        return -1


@asyncio.coroutine
def spider(url_head, user_id):
    try:
        res = getRes(url_head, user_id)
        if -1 != res:

            html = res.text.encode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            isprivacy = soup.find("div", {"class": "privacy_tip"})
            if isprivacy:
                print("用户：%s设置隐私不可见" % user_id)
                return

            iscancel = soup.find("div", {"class", "span-13 last"})

            head = soup.find("head")
            title = soup.find("title")
            user_name=title.get_text()
            print("作者:%s" % user_name)

            #检查个人签名是否存在
            signature=""
            quote=soup.find("div",{"class","quote"})
            if not quote:
                print("用户：%s没有设置签名" % user_id)
            else:
                signature=quote.contents[0].string
                print("用户：%s 签名:%s" % (user_id,signature))

            siderbar_left_div = soup.find("div", {"class", "siderbar_left"})
            # 检查图片是否存在
            img = siderbar_left_div.find("div", {"class", "default_avatar"})
            img_url=""
            if img:
                print("用户：%s头像不存在" % user_id)
                return
            else:
                img_url = siderbar_left_div.find("img").attrs["src"]
                array_temp = img_url.split("/")
                #user_id = array_temp[len(array_temp) - 1].split(".")[0]
                #print("用户ID:%s" % user_id)
                print("头像地址:%s" % img_url)
            #查找小花的数量

            flower_img=soup.find_all(src="/img/flower-16.png")[0]
            flower_count=flower_img.parent.contents[1].replace("×", "").strip()
            print("小花数量%s" % flower_count)
            # 没有头像的也得存入db中统计
            downloadImg.storeImg(user_name,signature,img_url, IMG_STORE_PATH, str(user_id),flower_count)
    except Exception as e:
        print("ERROR:",e)
    finally:
        pass


def index_spider():
    task_arry = []
    for index in range(1, MAX_USER_ID):
        task_arry.append(spider(URL_HEAD, index))
    return task_arry


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task_arry = index_spider()
    loop.run_until_complete(asyncio.wait(task_arry))
    loop.close()
