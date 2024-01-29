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

@pfile.route("/followers")
def followers():
    if 'username' in session:
        username = session['username']
        user = User('', '', '', '')
        if(user.AuthenticateByUsername(username)):
            followers = user.getFollowers()
            return render_template("html/followers.html", followers = followers)
    return redirect('/login')

#following to be created
@pfile.route("/following")
def following():
    if 'username' in session:
        username = session['username']
        user = User('', '', '', '')
        if(user.AuthenticateByUsername(username)):
            following = user.getFollowing()
            return render_template("html/following.html", following = following)
    return redirect('/login')


@pfile.route("/unfollow/<int:id>")
def unfollow(id):
    if 'username' in session:
        username = session['username']
        user = User('', '', '', '')
        if(user.AuthenticateByUsername(username)):
            user.unFollow(id)
            return redirect("/profile/following")
    return redirect('/login')