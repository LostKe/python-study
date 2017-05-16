# coding=utf-8
'''
爬取吾志用户的头像
url: https://wuzhi.me/u/xxx  需要爬取数据的地址
'''
import urllib
from urllib import request

URL_HEAD = "http://www.douban.com/"
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
req = request.Request(URL_HEAD)
req.add_header("User-Agent", USER_AGENT)

with request.urlopen(req) as f:
    print("status", f.status, f.reason)
    for key, value in f.getheaders():
        print("%s:%s" % (key, value))
    print("Data:", f.read().decode("utf-8"))
