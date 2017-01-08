# coding=utf-8

'''
    使用模板  jinjia2 库
    使用 web库 flask

'''
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def loginUI():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    userName = request.form['userName']
    if userName == 'admin' and request.form['pwd'] == '123':
        return render_template('success.html', userName=userName)
    else:
        return render_template('login.html', message='Bad userName or pwd', userName=userName)


if __name__ == '__main__':
    app.run()
