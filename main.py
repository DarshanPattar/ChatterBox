from flask import Flask, render_template, session, redirect, request
import pymysql

from userClass import User



db = pymysql.connect(host = "localhost", user = "root", password = "1234", db = "twitter_clone", autocommit = True)
cursor = db.cursor()

app = Flask(__name__)

app.secret_key = "hello"

@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        sql = f"select name from users where username='{username}';"
        cursor.execute(sql)
        result = cursor.fetchone()

        return render_template('html/index.html', name='index', result = result)
    return redirect("/signup")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        session['username'] = request.form['username']
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        password = request.form['pass1']
        Cpassword = request.form['pass2']

        # sql = f'''insert into users values(id, '{username}', '{name}', '{email}', '{password}', '', 0);'''
        # cursor.execute(sql)

        if(password == Cpassword and username != ""):
            username = username.strip()
            user = User(username=username, name=name, email=email, password=password)
            if(not user.Authenticate()):
                user.CreateUser()  
            else:
                print("User already exists!")
                user.Authenticate()
                if(user.password != password):
                    session.pop('username', None)
                    return redirect('/signup')

        return redirect('/')
    return render_template('html/signup.html', name='signup')   


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        username = request.form['username']
        password = request.form['pass1']

        if(username != ""):
            username = username.strip()

            user = User(username=username, name="", email="", password="")
            
            if(user.AuthenticateByUsername(username) and user.password == password):
                return redirect('/')
            else:
                print('User does not exists!.')
                session.pop('username', None)
                return redirect('/login')
            
    return render_template('html/login.html', name='login')  

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/signup')
    

if __name__ == '__main__':
    app.run(debug=True)