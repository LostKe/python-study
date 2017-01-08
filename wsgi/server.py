# coding=utf-8

from wsgiref.simple_server import make_server

from wsgi.Demo1 import application

httpd = make_server('', 8000, application)
print('Service HTTP on port 8000.....')
httpd.serve_forever()
