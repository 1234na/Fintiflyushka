from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)
username = None


@app.route('/')
@app.route('/home/<username>')
def home(username=None):
    f = open('homepage.html', 'rb')
    result = f.read()
    return result

@app.route('/enter')
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
        username = request.form.get('username')
        password = request.form.get('password')
        about = request.form.get('about')
        
        con = sqlite3.connect("fintiflyushka_db.sqlite")
        cur = con.cursor()
        cur.execute(f'''INSERT INTO Users(Username,Password,Extra,Photos_amount) VALUES ("{username}", "{password}", "{about}", 0)''')
        
        return "Форма отправлена"
        
    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')