# coding=utf-8

'''
使用 flask 框架

使用前需要导入支持库
pip install flask
'''

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/login', methods=['GET'])
def loginUI():
    return '''  <form action='/login' method='post'>
                    <p>用户名:<input type='text' name='userName'></p>
                    <p>密码:<input type='text' name='pwd'></p>
                    <p><input type='submit' value='登录'></p>
                </form>
            '''


@app.route('/login', methods=['POST'])
def login():
    if request.form['userName'] == 'admin' and request.form['pwd'] == '123':
        return '<h3>hello admin</h3>'
    else:
        return 'Bad userName or pwd'


if __name__ == '__main__':
    app.run()
