from flask import Blueprint, render_template, session, redirect, request, flash

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

        if " " in username:
            flash('There should be no spaces in username')
        if(username == "" or name == "" or email == "" or password == "" or Cpassword == ""):
            flash("Empty fields!")
        else:
            if(password == Cpassword and " " not in username):
                username = username.strip()
                user = User(username=username, name=name, email=email, password=password)
                if(not user.Authenticate()):
                    user.CreateUser()
                    return redirect('/')  
                else:
                    flash("User already exists!")
                    user.Authenticate()
                    if(user.password != password):
                        session.pop('username', None)
            else:
                flash("Passwords Don't match!")
        session.pop('username', None)
        return redirect('/signup')
    return render_template('html/signup.html', name='signup')   


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        username = request.form['username']
        password = request.form['pass1']

        if(username != "" and password != ""):
            username = username.strip()

            user = User(username=username, name="", email="", password="")
            
            if(user.AuthenticateByUsername(username) and user.password == password):
                return redirect('/')
            else:
                flash('User does not exists!.')
                session.pop('username', None)

        else:
            flash("Empty Fields!.")

        session.pop('username', None)
        return redirect("/login")
            
    return render_template('html/login.html', name='login')  

@auth.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')
    