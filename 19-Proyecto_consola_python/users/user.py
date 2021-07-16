from datetime import datetime
import hashlib
import users.conn as connection

conn = connection.doConnect()
db = conn[0]
cursor = conn[1]

class User:

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def __str__ (self):
        return self.email + ' ' + self.name

    def register(self):
        curDate = datetime.now()
        
        # encrypt password
        encrypt = hashlib.sha256()
        encrypt.update(self.password.encode('utf8'))
        
        sql = 'INSERT INTO users VALUES (null, %s, %s, %s, %s, %s)'
        user = (self.name, self.surname, self.email, encrypt.hexdigest(), curDate)

        try:
            cursor.execute(sql, user)
            db.commit()
            result = [cursor.rowcount, self]
        except: 
            result = [0, self]   
        
        return result

    def identify(self):
        sql = 'SELECT * FROM users WHERE email = %s and password = %s'

        encrypt = hashlib.sha256()
        encrypt.update(self.password.encode('utf8'))

        user = (self.email, encrypt.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result

