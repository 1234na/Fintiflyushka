from flask import Flask
from flask import request
from flask import render_template
import sqlite3

app = Flask(__name__)
username = None


@app.route('/')
def mainpage():
    f = open('mainpage.html', 'rb')
    result = f.read()
    return result

@app.route('/user/<name>')
def userpage(name):
    con = sqlite3.connect("fintiflyushka.sqlite")
    cur = con.cursor()
    about = cur.execute(f'''SELECT Extra FROM Users WHERE Username == "{username}"''').fetchall()
    return render_template('user_cab.html', username=name, about=about)

@app.route('/home/<name>')
def home(name):
    return render_template('homepage.html', username=name)

@app.route('/enter', methods=['GET', 'POST'])
def entrance():
    if request.method == 'GET':
        f = open('entrance.html', 'rb')
        result = f.read()
        return result
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        con = sqlite3.connect("fintiflyushka.sqlite")
        cur = con.cursor()
        password_right = cur.execute(f'''SELECT Password FROM Users WHERE Username == "{username}"''').fetchall()
        try:
            if password_right[0][0] == password:
                return render_template('homepage.html', username=username)
            else:
                return 'Пользователь с таким именем не найден.'
        except BaseException:
            return 'Ошибка входа. Попробуйте перезайти на сайт.'


@app.route('/post/<username>', methods=['POST', 'GET'])
def post_work(username):
    if request.method == 'GET':
        return render_template('post_foto.html', username=username)
    elif request.method == 'POST':
        text = request.form.get('about')
        filename = request.form.get('filename')
        con = sqlite3.connect("fintiflyushka.sqlite")
        cur = con.cursor()

        cur.execute(f'''INSERT INTO Pictures(filename,author,text) VALUES ("{filename}", "{username}", "{text}")''')

        num = 1
        print(cur.execute(f'''UPDATE Users SET Photos_amount = "{num}" WHERE Username = "{username}"''').fetchall())

        con.commit()
        return render_template('successful_posted.html', username=username)


@app.route('/reg', methods=['POST', 'GET'])
def registration():
    if request.method == 'GET':
        f = open('registration.html', 'rb')
        result = f.read()
        return result
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        about = request.form.get('about')
        
        con = sqlite3.connect("fintiflyushka.sqlite")
        cur = con.cursor()
        password_right = cur.execute(f'''SELECT Password FROM Users WHERE Username == "{username}"''').fetchall()
        if password_right == []:
            cur.execute(f'''INSERT INTO Users(Username,Password,Extra,Photos_amount) VALUES ("{username}", "{password}", "{about}", 0)''')
            con.commit()
            return render_template('successful_reg.html', username=username)
        else:
            return 'Данный ник уже был зарегистрирован. Попробуйте войти в аккаунт, либо придумайте другой никнейм.'

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')