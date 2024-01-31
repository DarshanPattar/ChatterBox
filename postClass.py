import pymysql

db = pymysql.connect(host = "localhost", user = "root", password = "1234", db = "twitter_clone", autocommit=True)
cursor = db.cursor()

class Post:
    def __init__(self, pid = None, uid = None, username = "", content="", datetime=""):
        self.pid = pid
        self.uid = uid
        self.username = username
        self.content = content
        self.datetime = datetime

    def fetchpost(self, pid):
        sql=f'''select * from posts where pid={pid}'''
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            self.pid = result[0]
            self.uid = result[1]
            self.content = result[2]
            self.datetime = result[3]
            return True
        return False
    
    def fetchAllPost():
        sql = f'''select pid, id, username, content, datetime from posts, users where id = uid order by datetime;'''
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def createPost(self):
        sql = f'''insert into posts values(NULL, {self.uid}, '{self.content}', default);'''
        cursor.execute(sql)
        return
    
    def deletePost(self, pid):
        sql = f'''delete from posts where pid = {pid}'''
        cursor.execute(sql)
        return