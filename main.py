from flask import Flask, render_template, session, redirect, request
import pymysql
from userClass import User
from postClass import Post

db = pymysql.connect(host = "localhost", user = "root", password = "1234", db = "twitter_clone", autocommit = True)
cursor = db.cursor()

app = Flask(__name__)

app.secret_key = "hello"



@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        user = User()
        user.AuthenticateByUsername(username)
        result = Post.fetchAllPost()
        return render_template('html/home.html', name='home', posts = result, cuser = user)
    return redirect("/signup")


from proj.chatbp import chatting
app.register_blueprint(chatting, url_prefix='/chat')

from proj.posts import posting
app.register_blueprint(posting, url_prefix='/post')

from proj.search import finder
app.register_blueprint(finder, url_prefix='/')

from proj.profile import pfile 
app.register_blueprint(pfile, url_prefix='/profile')  

from proj.auth import auth 
app.register_blueprint(auth, url_prefix='/')  

if __name__ == '__main__':
    app.run(debug=True)