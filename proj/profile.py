from flask import Blueprint, session, request, render_template, redirect
from userClass import User

pfile = Blueprint('pfile', __name__)



@pfile.route("/")
def profile():
    if 'username' in session:
        username = session['username']
        user = User("", "", "", "")
        user.AuthenticateByUsername(username)
        return render_template('html/profile.html', user = user)
    return redirect('/login')


@pfile.route("/edit", methods=['GET', 'POST'])
def editProfile():
    if 'username' in session:
        if request.method == "POST":
            username = session['username']
            user = User('', '', '', '')
            name = request.form['name']
            bio = request.form['bio']
            if(user.AuthenticateByUsername(username)):
                user.UpdateUser(name, bio)
                return redirect('/profile')
            else:
                print('Failed to Update')

        return render_template("html/editprofileForm.html")
    return redirect('/login')

@pfile.route("/delete")
def deleteProfile():
    if 'username' in session:
        username = session['username']
        user = User('', '', '', '')
        if(user.AuthenticateByUsername(username)):
            user.deleteUser()
            return redirect('/login')
    return redirect('/login')