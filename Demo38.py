# coding=utf-8

'''
https://www.python.org/events/python-events/
输出Python官网发布的会议时间、名称和地点。
'''

from html.parser import HTMLParser
from html.entities import name2codepoint
from contextlib import closing
from urllib.request import urlopen


class MyHtmlParse(HTMLParser):
    is_time = False
    is_topic = False
    is_address = False
    is_miss = True
    current_index = 0

    def __init__(self):
        self.msg = []
        HTMLParser.__init__(self)

    # 开始标签
    def handle_starttag(self, tag, attrs):
        if len(attrs) > 0:
            if tag == 'h3' and attrs[0][1] == 'event-title':
                self.is_topic = True
            elif tag == 'time' and attrs[0][0] == 'datetime':
                self.is_time = True
            elif tag == 'span' and attrs[0][1] == 'event-location':

                self.is_address = True
            elif tag == "h3" and attrs[0][1] == 'widget-title just-missed':
                self.is_miss = False

    # 标签中数据
    def handle_data(self, data):
        if self.is_topic and self.is_miss:
            self.msg.append({})
            self.msg[self.current_index]['topic'] = data
            self.is_topic = False
        elif self.is_time and self.is_miss:
            self.msg[self.current_index]['time'] = data
            self.is_time = False
        elif self.is_address and self.is_miss:
            self.msg[self.current_index]['address'] = data
            self.is_address = False
            self.current_index += 1


def parseInfo():
    parser = MyHtmlParse()
    html_context = ""
    with closing(urlopen('https://www.python.org/events/python-events/')) as f:
        html_context = f.read().decode('utf-8')
    parser.feed(html_context)

    for val in parser.msg:
        print("--" * 10)
        print("topic:%s,time:%s,address:%s" % (val['topic'], val['time'], val['address']))


parseInfo()
