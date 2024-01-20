import pymysql

db = pymysql.connect(host = "localhost", user = "root", password = "1234", db = "twitter_clone", autocommit=True)
cursor = db.cursor()


class User:
    def __init__(self, username, name, email, password, bio = ""):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        self.bio = bio
    
    def Authenticate(self):
        sql = f'''select * from users where username='{self.username}';'''
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            print(f"Connected, User exist, user {result}")
            self.id = result[0]
            return self.id
        else:
            print("User does not exists!")
            return False
    
    def AuthenticateByUsername(self, username):
        sql = f'''select * from users where username='{username}';'''
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            print(f"Connected, User exist, user {result}")
            self.id = result[0]
            self.username = result[1]
            self.name = result[2]
            self.email = result[3]
            self.password = result[4]
            self.bio = result[5]
            return self.id
        else:
            print("User does not exists!")
            return False
        
    def AuthenticateById(self, id):
        sql = f'''select * from users where id={id};'''
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            print(f"Connected, User exist, user {result}")
            self.id = result[0]
            self.username = result[1]
            self.name = result[2]
            self.email = result[3]
            self.password = result[4]
            self.bio = result[5]
            return self.id
        else:
            print("User does not exists!")
            return False



    def CreateUser(self):
        # insert into users values(id, 'dbpattar', 'Darshan B Pattar', 'darshanbpattar@gmail.com', 'qwerty123', 'This is super user!', 1);
        if(self.Authenticate() == False):
            sql = f'''insert into users values(id, '{self.username}', '{self.name}', '{self.email}', '{self.password}', '{self.bio}', 0);'''
            cursor.execute(sql)
            if self.Authenticate():
                print(f"Successfully created User, user id = {self.Authenticate()}")
                return self.id
            else:
                print("Failed to create User")
                return False
        else:
            return False

    # update users set bio = 'This is updated Bio' where id = 24;
    def UpdateUser(self, name, bio):
        if bio != "":
            sql = f'''update users set bio = '{bio}' where id = {self.id};'''
            result = cursor.execute(sql)
            if result:
                print("Successfully Updated.")
            else:
                print("Failed to Update")

        if name != "":
            sql = f'''update users set name = '{name}' where id = {self.id};'''
            result = cursor.execute(sql)
            if result:
                print("Successfully Updated.")
            else:
                print("Failed to Update")

    
    def deleteUser(self):
        sql = f'''delete from users where id={self.id}'''
        result = cursor.execute(sql)
        if result:
            print("Successfully Deleted.")
        else:
            print("Failed to Delete")



