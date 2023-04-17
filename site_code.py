from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)
username = None


@app.route('/')
@app.route('/home/<username>')
def home(username):
    pass

@app.route('/entrance')
def entrance():
    return 'Выйди и зайди нормально'

@app.route('/post/<username>')
def post_work(username):
    pass

@app.route('/reg', methods=['POST', 'GET'])
def registration():
    if flask.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            
                            <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                            
                            <title>Регистрация</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации</h1>
                            <div>
                              <form class="login_form" method="post">
                                <p>
                                  <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                </p>
                                <p>
                                  <input type="password" class="form-control" id="password" aria-describedby="passwordHelp" placeholder="Введите пароль" name="password">
                                </p>
                                <p>
                                  <input type="text" class="form-control" id="username" placeholder="Придумайте никнейм" name="username">
                                </p>
                                <div class="form-group">
                                  <p><label for="about">Немного о себе</label></p>
                                  <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                  <label for="photo">Приложите фотографию</label>
                                  <input type="file" class="form-control-file" id="photo" enctype="multipart/form-data" name="file">
                                </div>
                                <p>
                                  <button type="submit" class="btn btn-primary">Подтвердить регистрацию</button>
                                </p>
                              </form>
                            </div>
                          </body>
                      </html>'''
    elif flask.method == 'POST':
        email = flask.form.get('email')
        username = flask.form.get('username')
        photo = flask.form.get('file')
        password = flask.form.get('password')
        about = flask.form.get('about')
        
        con = sqlite3.connect("Fintiflyushka")
        cur = con.cursor()
        #cur.execute('''INSERT INTO Users VALUES (username, password, email, about, photo, 0)''')
        print(cur.execute('SELECT * FROM Users'))
        
        return "Форма отправлена"
        
    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')