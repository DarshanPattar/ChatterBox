from flask import Flask, render_template, session, redirect, request
import pymysql

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


from proj.auth import auth 
app.register_blueprint(auth, url_prefix='/')  

if __name__ == '__main__':
    app.run(debug=True)