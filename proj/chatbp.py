from flask import Blueprint, session, request, render_template, redirect
from userClass import User
import pymysql

chatting = Blueprint('chatting', __name__)

db = pymysql.connect(host = "localhost", user = "root", password = "1234", db = "twitter_clone", autocommit=True)
cursor = db.cursor()


@chatting.route("/")
def chatpage():
    if 'username' in session:
        username = session['username']
        user = User()
        user.AuthenticateByUsername(username)

        sql = f'''select * from chatbox where cbid like '{user.id}-%' or cbid like '%-{user.id}' order by lastupdated;'''
        cursor.execute(sql)
        result = cursor.fetchall()

        cblist = []

        for index, chatbox in enumerate(result):
            print(chatbox[0])
            idstr = chatbox[0]
            #getting other usernames
            ids = idstr.split('-')
            ids.remove(f'{user.id}')
            other = ''
            
            oid = int(ids[0])
            ouser = User()
            ouser.AuthenticateById(oid)
            other = ouser.name
                
            
            cblist.append({'idlink':idstr, 'name':other})
        
        print(cblist)

        return render_template("html/chatpage.html", chatboxes = cblist[::-1])
    return redirect("/login")


@chatting.route("/chatbox/<string:idlink>", methods=['GET', 'POST'])
def chatbox(idlink):
    if 'username' in session:
        username = session['username']
        user = User()
        user.AuthenticateByUsername(username)
        if request.method == 'POST':
            text = request.form["cbtext"]
            if text != "":
                sql = f'''insert into chats values(NULL, {user.id}, '{idlink}', '{text}', default);'''
                cursor.execute(sql)
                sql = f'''update chatbox set lastupdated=current_timestamp() where cbid = '{idlink}';'''
                cursor.execute(sql)

        sql = f'''select * from chats where chatboxid = '{idlink}' order by datetime;'''
        cursor.execute(sql)
        texts = cursor.fetchall()

        return render_template("html/chatbox.html", idlink = idlink, texts = texts, currentuser = user)

    return redirect("/login")


@chatting.route("/chatwith/<int:otheruid>")
def chatwith(otheruid):
    if 'username' in session:
        username = session['username']
        user = User()
        user.AuthenticateByUsername(username)
        uid = user.id
        ouid = otheruid

        chaturl = ""

        if uid > ouid:
            chaturl = f"{ouid}-{uid}"
        else:
            chaturl = f"{uid}-{ouid}"
        
        print(chaturl)
        
        sql = f'''select * from chatbox where cbid='{chaturl}';'''
        cursor.execute(sql)
        result = cursor.fetchone()
        if result == None:
            sql = f'''insert into chatbox values('{chaturl}', current_timestamp());'''
            cursor.execute(sql)
        
        sql = f'''select * from chatbox where cbid='{chaturl}';'''
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        return redirect("/chat/chatbox/" + result[0])

    return redirect("/login")