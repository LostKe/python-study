# coding=utf-8
'''
爬取吾志用户的头像
url: https://wuzhi.me/u/xxx  需要爬取数据的地址
'''
import requests
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

URL_HEAD = "https://wuzhi.me/u/148189"
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
response = requests.get(URL_HEAD)
print(response.text)
