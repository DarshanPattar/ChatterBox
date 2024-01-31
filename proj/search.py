from flask import Blueprint, session, request, render_template, redirect
from userClass import User

finder = Blueprint('finder', __name__)


@finder.route("/search", methods=['GET', 'POST'])
def search():
    if 'username' in session:
        username = session['username']
        user = User()

        if(request.method == 'GET'):
            usern = request.args["searchtxt"]

            if(usern !=  "" and user.AuthenticateByUsername(username)):
                print("text : " , usern)
                others = user.searchUser(usern)
                
            else:
                user.AuthenticateByUsername(username)    
                others = user.getAllOtherUsers()
            return render_template('html/search.html', users = others)
        else:
            return redirect("/signup")
    return redirect("/signup")

@finder.route("/search/<string:usn>")
def usrProfile(usn):
    if 'username' in session:
        username = session['username']
        user = User()
        if(user.AuthenticateByUsername(username)):
            
            otheruser = User()
            otheruser.AuthenticateByUsername(usn)
            following = user.getFollowing()
            print(following)
            isfollowing = False
            if (otheruser.id, otheruser.username, otheruser.name) in following:
                isfollowing = True
            return render_template("html/otherprofile.html", otheruser = otheruser, isfollowing = isfollowing)
        else:
            return redirect("/signup")
    return redirect("/signup")

@finder.route("/search/follow/<string:usr>")
def followUser(usr):
    if 'username' in session:
        username = session['username']
        user = User()
        if(user.AuthenticateByUsername(username)):
            otheruser = User()
            otheruser.AuthenticateByUsername(usr)
            if(not user.isfollowing(otheruser)):
                user.follow(otheruser)
            return redirect("/search/" + usr)
        return redirect("/signup")
    return redirect("/signup")

@finder.route("/search/unfollow/<string:usr>")
def unFollowUser(usr):
    if 'username' in session:
        username = session['username']
        user = User()
        if(user.AuthenticateByUsername(username)):
            otheruser = User()
            otheruser.AuthenticateByUsername(usr)
            user.unFollow(otheruser.id)
            return redirect("/search/" + usr)
    return redirect("/signup")
