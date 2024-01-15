from flask import Blueprint, render_template, session, redirect, request

from userClass import User

auth = Blueprint('auth', __name__)

@auth.route("/signup", methods=["POST", "GET"])
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


@auth.route("/login", methods=["POST", "GET"])
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

@auth.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/signup')
    