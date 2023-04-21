from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)
username = None


@app.route('/')
@app.route('/home/<username>')
def home(username=None):
    return 'Это должна быть домашняя страница'

@app.route('/entrance')
def entrance():
    return 'Выйди и зайди нормально'

@app.route('/post/<username>')
def post_work(username):
    pass

@app.route('/reg', methods=['POST', 'GET'])
def registration():
    if request.method == 'GET':
        f = open('registration.html', 'rb')
        result = f.read()
        return result
    elif request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        photo = request.form.get('file')
        password = request.form.get('password')
        about = request.form.get('about')
        
        con = sqlite3.connect("fintiflyushka_db.sqlite")
        cur = con.cursor()
        cur.execute('''INSERT INTO Users(Username,Password,Email,Extra,Photo,Photos_amount) VALUES (username, password, email, about, photo, 0)''')
        
        return "Форма отправлена"
        
    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')