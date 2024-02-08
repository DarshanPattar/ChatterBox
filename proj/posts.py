from flask import Blueprint, session, request, render_template, redirect
from userClass import User
from postClass import Post

posting = Blueprint('posting', __name__)

@posting.route("/create", methods = ['GET', 'POST'])
def createPost():
    if 'username' in session:
        if request.method == 'POST':
            username = session['username']
            user = User()
            user.AuthenticateByUsername(username)

            content = request.form["postcontent"]
            print(request)
            post = Post()
            post.content = content
            post.uid = user.id
            post.createPost()
            return redirect("/")

        return render_template("html/createpost.html")

    return redirect("/signup")

@posting.route("/delete/<int:pid>")
def deletePost(pid):
    if 'username' in session:
        username = session['username']
        user = User()
        user.AuthenticateByUsername(username)
        post = Post()
        post.fetchpost(pid)
        if post.uid == user.id or user.isSuper:
            post.deletePost(pid)
        return redirect("/")

    return redirect("/signup")