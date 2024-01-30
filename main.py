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


        return render_template('html/home.html', name='home', result = username)
    return redirect("/signup")


from proj.search import finder
app.register_blueprint(finder, url_prefix='/')

from proj.profile import pfile 
app.register_blueprint(pfile, url_prefix='/profile')  

from proj.auth import auth 
app.register_blueprint(auth, url_prefix='/')  

if __name__ == '__main__':
    app.run(debug=True)